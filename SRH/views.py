from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def warner(request):
    return render(request,'warner.html')

def natarajan(request):
    return HttpResponse('<h1>this is natarajan</h1>')
