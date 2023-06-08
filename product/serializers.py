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
    products = ProductSerializer(many=True)
    counter = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = 'counter products name'.split()
    def get_counter(self, object):
        return object.products.count()
class CategoryRetrievSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = 'id text stars'.split()


class ReviewRetrievSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Product
        fields = 'id title reviews rating reviews'.split()