from django.contrib import admin
from .models import Product, Category,Order
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["title","price","discount","decription","category"]
    search_fields = ["title"]
    fields = ["title","price"]
    list_editable = ["price","category"]




admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)