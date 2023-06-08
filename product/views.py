from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Category, Review
from product.serializers import (ProductSerializer, CategorySerializer, ReviewSerializer,
                                 ProductRetrievSerializer, CategoryRetrievSerializer, ReviewRetrievSerializer,
                                 ProductReviewSerializer)


@api_view(['GET', 'POST'])
def products_list_api_view(request):
    if request.method == 'GET':
        product = Product.objects.all()

        data = ProductSerializer(product, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)

    # if request.method == 'POST':
    #     data = request.data
    #     product = Product.objects.create(
    #         director_id=data.get('director_id'),
    #         title=data.get('title'),
    #         description=data.get('description'),
    #         price=data.get('price')
    #     )
    #     movie.genres.set(data.get('genres'))
    #
    #     return Response(data=ProductSerializer(product, many=False).data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def product_retrieve_api_view(request, **kwargs):
    if request.method == 'GET':
        product = Product.objects.get(id=kwargs['id'])

        data = ProductRetrievSerializer(product, many=False).data

        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def categoris_list_api_view(request):
    if request.method == 'GET':
        categoris = Category.objects.all()

        data = CategorySerializer(categoris, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def category_retrieve_api_view(request, **kwargs):
    if request.method == 'GET':
        category = Category.objects.get(id=kwargs['id'])

        data = CategoryRetrievSerializer(category, many=False).data

        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def reviews_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()

        data = ReviewSerializer(reviews, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_retrieve_api_view(request, **kwargs):
    if request.method == 'GET':
        review = Review.objects.get(id=kwargs['id'])

        data = ReviewRetrievSerializer(review, many=False).data

        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def products_reviews_api_view(request):
    if request.method == 'GET':
        products_reviews = Product.objects.all()
        data = ProductReviewSerializer(products_reviews, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
