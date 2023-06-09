from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Category, Review
from product.serializers import (ProductSerializer, CategorySerializer, ReviewSerializer,
                                ProductRetrievSerializer, CategoryRetrievSerializer, ReviewRetrievSerializer,
                                 ProductReviewSerializer, ProductValidateSarializer, CategoryValidateSerializer,
                                 ReviewValidateSerializer)

@api_view(['GET', 'POST'])
def products_list_api_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        data = ProductSerializer(product, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    if request.method == 'POST':

        """ Validation of data"""
        serializer = ProductValidateSarializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)

        """Step 2: Create object (Operation)"""
        data = request.data
        product = Product.objects.create(
            category_id=data.get('category_id'),
            title=data.get('title'),
            description=data.get('description'),
            price=data.get('price')
        )

        """Step 3: Return response"""
        return Response(data=ProductSerializer(product, many=False).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def product_retrieve_api_view(request, **kwargs):
    product = Product.objects.get(id=kwargs['id'])

    if request.method == 'GET':
        product = Product.objects.get(id=kwargs['id'])
        data = ProductRetrievSerializer(product, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = ProductValidateSarializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)

        data = request.data

        product.category_id = data.get('category_id')
        product.title = data.get('title')
        product.description = data.get('description')
        product.price = data.get('price')

        product.save()
        return Response(data=ProductRetrievSerializer(product, many=False).data,
                        status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        product.delete()
        return Response(f'Deleted{product.title}')

@api_view(['GET', 'POST'])
def categoris_list_api_view(request):
    if request.method == 'GET':
        categoris = Category.objects.all()
        data = CategorySerializer(categoris, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = CategoryValidateSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)

        data = request.data
        categoris = Category.objects.create(
            name=data.get('name')
        )

        return Response(data=CategorySerializer(categoris, many=False).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def category_retrieve_api_view(request, **kwargs):
    category = Category.objects.get(id=kwargs['id'])
    if request.method == 'GET':
        category = Category.objects.get(id=kwargs['id'])
        data = CategoryRetrievSerializer(category, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = CategoryValidateSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)

        data = request.data
        category.name = data.get('name')
        category.save()
        return Response(data=CategoryRetrievSerializer(category, many=False).data,
                        status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        category.delete()
        return Response(f'Deleted {category.name}!')

@api_view(['GET', 'POST'])
def reviews_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)

        data = request.data
        reviews = Review.objects.create(
            product_id=data.get('product_id'),
            text=data.get('text'),
            stars=data.get('stars')
        )

        return Response(data=ReviewSerializer(reviews, many=False).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_retrieve_api_view(request, **kwargs):
    review = Review.objects.get(id=kwargs['id'])
    if request.method == 'GET':
        review = Review.objects.get(id=kwargs['id'])
        data = ReviewRetrievSerializer(review, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        data = request.data

        review.product_id = data.get('product_id')
        review.text = data.get('text')
        review.stars = data.get('stars')

        review.save()
        return Response(data=ReviewRetrievSerializer(review, many=False).data,
                        status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        review.delete()
        return Response(f'Review was deleted!')


@api_view(['GET'])
def products_reviews_api_view(request):
    if request.method == 'GET':
        products_reviews = Product.objects.all()
        data = ProductReviewSerializer(products_reviews, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
