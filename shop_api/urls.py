"""
URL configuration for shop_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from . import swagger
from shop_api import settings

from product import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', views.CategoryAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/categories/<int:id>/', views.CategoryAPIView.as_view({'get': 'retrieve',
                                                                       'put': 'update',
                                                                       'delete': 'destroy'})),
    path('api/v1/products/', views.ProductAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/products/<int:id>/', views.ProductAPIView.as_view({'get': 'retrieve',
                                                                     'put': 'update',
                                                                     'delete': 'destroy'})),
    path('api/v1/reviews/', views.ReviewAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/reviews/<int:id>/', views.ReviewAPIView.as_view({'get': 'retrieve',
                                                                   'put': 'update',
                                                                   'delete': 'destroy'})),
    path('api/v1/products/reviews/', views.ProductReviewAPIView.as_view()),
    # path('api/v1/users/', include('users.urls'))
]

urlpatterns += swagger.urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
