from django.urls import path , include
from . import views



urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<int:id>',views.detail,name='index'),
    path('checkout/',views.checkout,name='checkout')
]
