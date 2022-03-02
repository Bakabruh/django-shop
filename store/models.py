from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    desc = models.TextField(blank=True)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self) -> str:
        return self.title
