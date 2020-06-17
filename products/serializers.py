from rest_framework import serializers
from .models import *

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Brand
        fields = ('name', 'image')

    def get_image_url(self, obj):
        return obj.image.url


class ProductSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Product
        depth = 1
        fields = '__all__'

    def get_image_url(self, obj):
        return obj.image.url
     