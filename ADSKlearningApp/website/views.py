from django.shortcuts import render
from django.http import HttpResponse
from items.models import Item


def index(request):
    return render(request, 'website/index.html',
                  {'items': Item.objects.all()})


def items(request):
    return HttpResponse('items from database')
