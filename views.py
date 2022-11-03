from platform import java_ver
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.forms import ModelForm
from cart.models import Hotels,Userdetails1, MenuItem, Category, OrderModel

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
class Order(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        roti = MenuItem.objects.filter(
                category__name__contains='Roti')
        sabji = MenuItem.objects.filter(category__name__contains='Sabji')
        dal = MenuItem.objects.filter(category__name__contains='Dal')


            # pass into context
        context = {
                'roti': roti,
                'sabji': sabji,
                'dal': dal,

            }


            # render the template
        return render(request, 'order.html', context)
    def post(self, request, *args, **kwargs):
        order_items = {
            'items': [],

        }

        items = request.POST.getlist('items[]')



        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,
                #'quantity':menu_item.quantity


            }
            #item_data1 = {

                #'quantity':menu_item.quantity,


            #}

            order_items['items'].append(item_data)
        #    order_items['items1'].append(item_data1)

            price=0
            #quantity=0
            item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])



            item_ids.append(item['id'])


        order = OrderModel.objects.create(price=price)

        order.items.add(*item_ids)

        context = {
            'items': order_items['items'],
            'price': price,
            #'quantity':quantity
        }

        return render(request, 'confirmation.html', context)



def userdetails1(request):

        return render(request,"userdetails.html")
