from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<p>In Index View</p>')

def item_detail(request, id):
    return HttpResponse('<p>In Item detail view id {0}</p>'.format(id))
# Create your views here.
