from django.shortcuts import render
from django.http import HttpResponse # Ekledim

# Create your views here.

def index(request):
    return HttpResponse("Home page!")

def blogs(request):
    return HttpResponse("Blog page!")