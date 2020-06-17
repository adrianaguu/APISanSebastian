from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('brands/', BrandList.as_view()),
    path('products/', ProductList.as_view()),
    path('lines/', LineList.as_view()),
    path('products/filter_category/<int:pk>', ProductByCategory.as_view()),
    path('products/filter_brand/<int:pk>', ProductByBrand.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)