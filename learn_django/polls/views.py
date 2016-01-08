from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello frankstar! welcome to django!')
# Create your views here.
