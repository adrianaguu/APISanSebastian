from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework import generics


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BrandList(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class LineList(generics.ListCreateAPIView):
    queryset = Line.objects.all()
    serializer_class = LineSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
