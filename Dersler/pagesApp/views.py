from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def settings(request):
    return render(request, 'sett.html')

def hakkimizda(request):
    return render(request, 'hakkimizda.html')