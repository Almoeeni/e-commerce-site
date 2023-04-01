from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.FloatField()
    decription = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.title

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    total = models.IntegerField()

    def __str__(self) -> str:
        return self.name