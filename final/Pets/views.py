from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from Pets.models import dogs, cats,more_pets
from Pets.forms import petsform 


def create_dog(request):
    if request.method == "GET":
        context = {"form" : petsform(),"title": "Agregar perro"}
        return render(request,"Pets/new_dog.html",context=context)
    elif request.method == "POST":
        form = petsform(request.POST)
        if form.is_valid():
            dogs.objects.create(
            name = form.cleaned_data["name"],
            vaccine = form.cleaned_data["vaccine"],
            castrated = form.cleaned_data["castrated"]
            )
            return render(request,"Pets/new_dog.html",context={})
        else:
            context = {
                "form_errors": form.errors,
                "form":petsform()
            }
            return render(request,"Pets/new_dog.html",context={})
            
def create_cat(request):
    if request.method == "GET":
        context = {"form" : petsform(), "title": "Agregar gato"}
        return render(request,"Pets/new_cat.html",context=context)
    elif request.method == "POST":
        form = petsform(request.POST)
        if form.is_valid():
            cats.objects.create(
            name = form.cleaned_data["name"],
            vaccine = form.cleaned_data["vaccine"],
            castrated = form.cleaned_data["castrated"]
            )
            return render(request,"Pets/new_cat.html",context={})
        else:
            context = {
                "form_errors": form.errors,
                "form":petsform()
            }
            return render(request,"Pets/new_cat.html",context={})

def create_other(request):
    if request.method == "GET":
        context = {"form" : petsform(),"title": "Agregar otro animal"}
        return render(request,"Pets/new_others.html",context=context)
    elif request.method == "POST":
        form = petsform(request.POST)
        if form.is_valid():
            more_pets.objects.create(
            name = form.cleaned_data["name"],
            vaccine = form.cleaned_data["vaccine"],
            castrated = form.cleaned_data["castrated"]
            )
            return render(request,"Pets/new_others.html",context={})
        else:
            context = {
                "form_errors": form.errors,
                "form":petsform()
            }
            return render(request,"Pets/new_others.html",context={})

def list_dogs(request):
    if "search" in request.GET:
        search = request.GET["search"]
        all_dogs = dogs.objects.filter(name__icontains=search)
    else:
        all_dogs = dogs.objects.all()
    context = {"dogs":all_dogs}
    return render(request, "Pets/dogs.html",context= context)

def list_cats(request):
    if "search" in request.GET:
        search = request.GET["search"]
        all_cats = cats.objects.filter(name__icontains=search)
    else:
        all_cats = cats.objects.all()
    context = {"cats" : all_cats}
    return render(request, "Pets/cats.html",context=context)

def list_more_pets(request):
    if "search" in request.GET:
        search = request.GET["search"]
        all_more_pets = dogs.objects.filter(name__icontains=search)
    else:
        all_more_pets = more_pets.objects.all()
    context = {"others" : all_more_pets}
    return render(request, "Pets/others.html",context=context)

