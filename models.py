from operator import truediv
from pickle import TRUE
from pydoc import describe
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from tkinter import CASCADE
from django.contrib.auth.models import User

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')
    quantity = models.IntegerField(max_length=5,null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)



class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField(max_length=5,null=True)
    items = models.ManyToManyField(
        'MenuItem', related_name='order', blank=True)


    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'




class Food(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)


class Hotels(models.Model):
    host=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    topic=models.ForeignKey(Food, on_delete=models.SET_NULL,null=True,blank=TRUE)
    name=models.CharField(max_length=220)
    description=models.TextField(null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    hotel_img=models.ImageField(null=TRUE,blank=TRUE, upload_to='images/')

    def __str__(self):
        return str(self.name)

class message(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    room=models.ForeignKey(Hotels, on_delete=models.CASCADE)
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.body[0:50])




class Userdetails1(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    fname=User.first_name
    email=User.email
    address=models.CharField(max_length=220)
