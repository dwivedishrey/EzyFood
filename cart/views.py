from django.shortcuts import render

from cart.models import Hotels

# Create your views here.


def cart(request):
    hotels=Hotels.objects.all()
    context={'hotels':hotels}
    print(context)
    return render(request, 'cart.html',context)

def hotels(request,pk):
    hotels=Hotels.objects.get(name=pk)
    context={"hotels":hotels}
    return render(request,'hotels.html',context)