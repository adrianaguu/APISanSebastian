from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse



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


class ProductByCategory(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, pk, format=None):
    	try:
    		category = Category.objects.get(pk=pk)
    	except Category.DoesNotExist:
    		return HttpResponse(status=404)

    	products = Product.objects.filter(category=category)
    	serializer = ProductSerializer(products, many=True)
    	return Response(serializer.data)

class ProductByBrand(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, pk, format=None):
    	try:
    		brand = Brand.objects.get(pk=pk)
    	except Brand.DoesNotExist:
    		return HttpResponse(status=404)

    	products = Product.objects.filter(brand=brand)
    	serializer = ProductSerializer(products, many=True)
    	return Response(serializer.data)

