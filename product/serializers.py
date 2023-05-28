from rest_framework import serializers
from product.models import Category, Product, Review

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'description', 'category')


class ProductRetrievSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name',)


class CategoryRetrievSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('text', 'product')


class ReviewRetrievSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'