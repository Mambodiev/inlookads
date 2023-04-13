from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('', views.StaffView.as_view(), name='staff'),
    path('button/', views.ButtonCreateView.as_view(), name='button-create'),
    path('language/', views.LanguageCreateView.as_view(), name='language-create'),
    path('country/', views.CountryCreateView.as_view(), name='country-create'),
    path('technology/', views.TechnologyCreateView.as_view(), name='technology-create'),
    path('category/', views.CategoryCreateView.as_view(), name='category-create'),
    path('create/', views.ProductCreateView.as_view(), name='product-create'),
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<pk>/update/',
         views.ProductUpdateView.as_view(), name='product-update'),
    path('products/<pk>/delete/',
         views.ProductDeleteView.as_view(), name='product-delete'),
]
