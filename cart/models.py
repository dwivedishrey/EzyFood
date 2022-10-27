from operator import truediv
from pickle import TRUE
from pydoc import describe
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from tkinter import CASCADE
from django.contrib.auth.models import User

# Create your models here.

class Roti(models.Model):
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)

        
class Dal(models.Model):
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)

class Sabji(models.Model):
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)
     
    
    
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
    


class Customize(models.Model):
    host=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    food=models.ForeignKey(Food, on_delete=models.SET_NULL,null=True,blank=TRUE)
    roti=models.ForeignKey(Roti,on_delete=models.SET_NULL,null=True,blank=TRUE)
    dal=models.ForeignKey(Dal,on_delete=models.SET_NULL,null=True,blank=TRUE)
    sabji=models.ForeignKey(Sabji,on_delete=models.SET_NULL,null=True,blank=TRUE)
    description=models.TextField(null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

class Userdetails1(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    fname=User.first_name
    email=User.email
    address=models.CharField(max_length=220)
    