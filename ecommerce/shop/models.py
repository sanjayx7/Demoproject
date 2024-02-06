from django.db import models
from django.contrib.auth.models import AbstractUser
class Category(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField(default=0)
    image=models.ImageField(upload_to="category",null=True,blank=True)

    def __str__(self):
       return self.name

class Products(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField(default=0)
    image=models.ImageField(upload_to="products",null=True,blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.IntegerField(default=0)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
       return self.name


