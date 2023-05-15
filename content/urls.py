from django.urls import path
from .views import CourseListView, CourseDetailView, VideoDetailView
from content import views
from django.utils.translation import gettext_lazy as _
# from mysite.core import views

app_name = "content"  

urlpatterns = [
    path('product-chart/', views.product_chart, name='product-chart'),
    path(_('remove-from-saved/<pk>/'),
         views.RemoveFromSavedView.as_view(), name='remove-from-saved'),
    path('', CourseListView, name='course-list'),
    path("<slug>/", CourseDetailView.as_view(), name='course-detail'),
    path(_('saved-product/'), views.SavedProductView.as_view(), name='saved-product'),
    path("<slug>/<video_slug>/", VideoDetailView.as_view(), name='video-detail'),
    
]