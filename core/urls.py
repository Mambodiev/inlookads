from django.urls import path
from django.views.generic import TemplateView
from core import views

 
app_name = "core"

urlpatterns = [
    # path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path('', views.home, name='home'),
    path('privacy/', views.privacy, name='privacy'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]