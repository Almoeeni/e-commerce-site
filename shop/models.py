from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.FloatField()
    decription = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.CharField(max_length=300)