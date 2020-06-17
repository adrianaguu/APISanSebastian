from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('brands/', BrandList.as_view()),
    path('products/', ProductList.as_view()),
    path('lines/', LineList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)