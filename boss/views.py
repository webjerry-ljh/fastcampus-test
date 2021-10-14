from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop, Menu, Order, Orderfood
from order.serializers import ShopSerializer, MenuSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def order_list(request, shop):
    if request.method == 'GET':
        order_list = Order.objects.filter(shop=shop)
        return render(request, 'boss/order_list.html', { 'order_list': order_list} )
    else:
        return HttpResponse(status=404)

@csrf_exempt
def time_input(request):
    if request.method == 'POST':
        order_item = Order.objects.get(pk=int(request.POST['order_id']))
        shop = order_item.shop.id
        order_item.estimated_time = int(request.POST['elstimated_time']) 
        order_item.save()
        #return HttpResponse(status=200)
        return render(request, 'boss/success.html',{'shop':int(shop)})
    else:
        return HttpResponse(status=404)