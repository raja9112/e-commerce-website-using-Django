from django.http.response import HttpResponseRedirect
from shop.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def tickets(request):
    url = request.META.get('HTTP_REFERER')
    if request.method=="POST":
        names=request.POST.get('names')
        email= request.POST.get('emails')
        queries= request.POST.get('queries')
        saving= ticket(
            name=names,
            email=email,
            problem=queries,
            
        )
        saving.save()
        messages.success(request,"Query is posted.")
    return HttpResponseRedirect(url)