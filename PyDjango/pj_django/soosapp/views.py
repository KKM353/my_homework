from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from soosapp.models import Address
from .models import Address

#def index(request):
#    return HttpResponse("<center><h3>안녕 장고^^</h3></center>")

def index(request):
    temlate = loader.get_template('index.html')
    return HttpResponse(temlate.render())

def list(request):
    temlate = loader.get_template('list.html')
    addresses = Address.objects.all().values()
    context = {
        'addresses': addresses,
    }
    return HttpResponse(temlate.render(context, request))

def write(request):
	temlate = loader.get_template('write.html')
	return HttpResponse(temlate.render({},request))

from django.urls import reverse
from django.utils import timezone
def write_ok(request):
    x = request.POST['name']
    y = request.POST['addr']
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    address = Address(name=x, addr=y, rdate=nowDatetime)
    address.save()
    return HttpResponseRedirect(reverse('list'))

def delete(request, id):
	address = Address.objects.get(id=id)
	address.delete()
	return HttpResponseRedirect(reverse('list'))

def update(request, id):
    temlate = loader.get_template('update.html')
    address = Address.objects.get(id=id)
    context = {
        'address':address,
    }
    return HttpResponse(temlate.render(context, request))

def update_ok(request, id):
    x = request.POST['name']
    y = request.POST['addr']
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    address = Address.objects.get(id=id)
    address.name = x
    address.addr = y
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    address.rdate = nowDatetime
    address.save()
    return HttpResponseRedirect(reverse('list'))