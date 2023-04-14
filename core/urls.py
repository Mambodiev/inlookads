from django.urls import path
from django.views.generic import TemplateView
from core import views

 
app_name = "core"

urlpatterns = [
    # path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path('', views.home, name='home'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.about, name='about'),
    path('price/', views.price, name='price'),
    path('blog/', views.blog, name='blog'),
    path('affiliate/', views.affiliate, name='affiliate'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]