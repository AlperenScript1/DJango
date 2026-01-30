from django.shortcuts import render


# Create your views here.

def homePage(request):
    return render(request,'homePage.html')

def lastPage(request):
    return render(request, 'lastPage.html')