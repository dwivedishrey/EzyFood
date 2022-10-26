from platform import java_ver
from django.shortcuts import render
from django.http import JsonResponse

from django.forms import ModelForm
from cart.models import Hotels,Customize,Roti,Sabji,Dal,Userdetails1

# Create your views here.


def cart(request):
    hotels=Hotels.objects.all()
    context={'hotels':hotels}
    print(context)
    return render(request,'cart.html',context) 

def hotels(request,pk):
    hotels=Hotels.objects.get(name=pk)
    context={"hotels":hotels}
    return render(request,'hotels.html',context)

def customize(request):
    roti=Roti.objects.all()
    sabji=Sabji.objects.all()
    dal=Dal.objects.all()
    context={"roti":roti,"sabji":sabji,"dal":dal,}
    return render(request,"customize.html",context)

def userdetails1(request):
    
        return render(request,"userdetails.html")
        
