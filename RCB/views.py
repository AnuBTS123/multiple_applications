from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse

def kohli(request):
    return render(request,'kohli.html')

def ABD(request):
    return HttpResponse('<h1>Mr 360 is best batsman and fielder of RCB</h1>')


