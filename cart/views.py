from platform import java_ver
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

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
        
def bill(request):
    fprice=0
    if request.method=="post":
        p1=(Roti.objects.filter(name=request.id).first()).price
        p2=(Dal.objects.filter(name=request.id).first()).price
        p3=(Sabji.objects.filter(name=request.id).first()).price
        fprice=fprice+p1+p2+p3
        print(fprice)
    context={"price":fprice}
    return render(request,"bill.html",context)