from django.shortcuts import render, redirect
from shop.models import *


def customer_service(request):
    obj=ticket.objects.all()
    return render(request, 'customerservice.html',{'obj':obj})



