from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    #return HttpResponse("welcome to web bsae application")
    return render(request , 'base.html')