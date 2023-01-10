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
    all_dogs = dogs.objects.all()
    context = {"dogs":all_dogs}
    return render(request, "Pets/dogs.html",context= context)

def list_cats(request):
    all_cats = cats.objects.all()
    context = {"cats" : all_cats}
    return render(request, "Pets/cats.html",context=context)

def list_more_pets(request):
    all_more_pets = more_pets.objects.all()
    context = {"others" : all_more_pets}
    return render(request, "Pets/others.html",context=context)

