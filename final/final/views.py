from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render (request, "index.html" , context={})
    
def us(request):
    return render (request, "Us.html" , context={})

def donate(request):
    return render (request, "donate.html" , context={})    

def about(request):
    return render (request, "about.html",context={})