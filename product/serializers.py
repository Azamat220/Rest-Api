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

class ProductValidateSarializer(serializers.Serializer):
    category_id = serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=250)
    price = serializers.FloatField(max_value=1000)


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)


class ReviewValidateSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(max_value=100)
    text = serializers.CharField(max_length=220)
    stars = serializers.IntegerField(min_value=1, max_value=5)
