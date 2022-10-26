
from .views import *
from django.urls import path,include


urlpatterns = [
    
     path('cart' , cart , name="cart"),
    path("hotels/<str:pk>",hotels,name="hotels"),
    path("customize",customize,name="customize"),

    
]

   