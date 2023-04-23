from django.urls import path
from .views import CourseListView, CourseDetailView, VideoDetailView
from content import views
from django.utils.translation import gettext_lazy as _


app_name = "content"  

urlpatterns = [
    path(_('saved-product/'), views.SavedProductView.as_view(), name='saved-product'),
    path(_('remove-from-saved/<pk>/'),
         views.RemoveFromSavedView.as_view(), name='remove-from-saved'),
    # path('contact/', views.ContactView.as_view(), name='contact'),
    # path("", CourseListView.as_view(), name='course-list'),
    path('', CourseListView, name='course-list'),
    path("<slug>/", CourseDetailView.as_view(), name='course-detail'),
    path("<slug>/<video_slug>/", VideoDetailView.as_view(), name='video-detail'),
    
]