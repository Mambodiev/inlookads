from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from django.utils.translation import gettext_lazy as _


from core.views import (
    selectlanguage,
    )


urlpatterns = [
    path('selectlanguage/',selectlanguage,name='selectlanguage'),
    path('i18n/', include('django.conf.urls.i18n')),
]


urlpatterns += i18n_patterns (
    path(
        _("about/"), TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),

    # Core
    path("", include("core.urls", namespace="core")),


    # Content
    path(_("courses/"), include("content.urls", namespace="content")),
    # path("payment/", include("payment.urls", namespace="payment")),

    # tailwind
    path("__reload__/", include("django_browser_reload.urls")),
    
    # ckeditor 
    path('_ckeditor/', include('ckeditor_uploader.urls')),

    # translation
    path(_('rosetta/'), include('rosetta.urls')),

    # User management
    path(_("users/"), include("users.urls", namespace="users")),
    path(_("accounts/"), include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path(_('staff/'), include('staff.urls', namespace='staff')),
    prefix_default_language=False,
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns