from django.db import models
from django.db.models import CASCADE


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(null=True)
    category = models.ForeignKey(Category, on_delete=CASCADE, null=True, related_name='products')

    @property
    def rating(self):
        stars = [review.stars for review in self.reviews.all() if review.stars is not None]
        if not stars:
            return 0
        else:
            return round(sum(stars) / len(stars), 2)



STAR_CHOICES = (
        (1, '*'),
        (2, 2 * '*'),
        (3, 3 * '*'),
        (4, 4 * '*'),
        (5, 5 * '*')
    )

class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=CASCADE, null=True, related_name='reviews')
    stars = models.IntegerField(default=5, choices=STAR_CHOICES)

