from django.db import models
from django.db.models import CASCADE


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=CASCADE)


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=CASCADE)

