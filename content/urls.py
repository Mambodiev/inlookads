from django.urls import path
from .views import CourseListView, CourseDetailView, VideoDetailView
from content import views

app_name = "content"

urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='contact'),
    path("", CourseListView.as_view(), name='course-list'),
    path("<slug>/", CourseDetailView.as_view(), name='course-detail'),
    path("<slug>/<video_slug>/", VideoDetailView.as_view(), name='video-detail'),
]