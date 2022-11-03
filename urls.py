
from .views import *
from django.urls import path,include


urlpatterns = [

     path('cart' , cart , name="cart"),
    path("hotels/<str:pk>",hotels,name="hotels"),
    path('order/', Order.as_view(), name='order'),
    path('add-to-cart/', cart.as_view(), name='addtocart'),,


]
