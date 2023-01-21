from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from Pets.models import dogs, cats,more_pets
from Pets.forms import petsform 
from django.views.generic import DeleteView

#Clases y funcinoes para perros
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
            

def list_dogs(request):
    if "search" in request.GET:
        search = request.GET["search"]
        all_dogs = dogs.objects.filter(name__icontains=search)
    else:
        all_dogs = dogs.objects.all()
    context = {"dogs":all_dogs}
    return render(request, "Pets/list_dogs.html",context= context)

def update_dog(request, pk):
    dog = dogs.objects.get(pk=pk)
    if request.method == "GET":
        context = {
            "form" : petsform(
                initial={
                    "name":dog.name,
                    "vaccine":dog.vaccine,
                    "castrated":dog.castrated
                }
                )
        }
        return render(request,"Pets/update_dog.html",context=context)
    elif request.method == "POST":
        form = petsform(request.POST)
        if form.is_valid():
            dog.name = form.cleaned_data["name"]
            dog.vaccine = form.cleaned_data["vaccine"]
            dog.castrated = form.cleaned_data["castrated"]
            dog.save()

            context = {"message" : "Perro actualizado exitosamente"}
            return render(request,"Pets/update_dog.html",context=context)
        else:
            context = {
                "form_errors": form.errors,
                "form":petsform()
            }
            return render(request,"Pets/update_dog.html",context=context)

class dogDeleteView(DeleteView):
    model = dogs
    template_name = "Pets/delete_dog.html"
    success_url = "/pets/list_dogs/"




#Clases y funcinoes para gatos
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

def list_cats(request):
    if "search" in request.GET:
        search = request.GET["search"]
        all_cats = cats.objects.filter(name__icontains=search)
    else:
        all_cats = cats.objects.all()
    context = {"cats" : all_cats}
    return render(request, "Pets/list_cats.html",context=context)

def update_cat(request, pk):
    cat = cats.objects.get(pk=pk)
    if request.method == "GET":
        context = {
            "form" : petsform(
                initial={
                    "name":cat.name,
                    "vaccine":cat.vaccine,
                    "castrated":cat.castrated
                }
                )
        }
        return render(request,"Pets/update_cat.html",context=context)
    elif request.method == "POST":
        form = petsform(request.POST)
        if form.is_valid():
            cat.name = form.cleaned_data["name"]
            cat.vaccine = form.cleaned_data["vaccine"]
            cat.castrated = form.cleaned_data["castrated"]
            cat.save()

            context = {"message" : "Gato actualizado exitosamente"}
            return render(request,"Pets/update_cat.html",context=context)
        else:
            context = {
                "form_errors": form.errors,
                "form":petsform()
            }
            return render(request,"Pets/update_cat.html",context=context)

class catDeleteView(DeleteView):
    model = cats
    template_name = "Pets/delete_cat.html"
    success_url = "/pets/list_cats/"




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

def list_others(request):
    if "search" in request.GET:
        search = request.GET["search"]
        all_more_pets = more_pets.objects.filter(name__icontains=search)
    else:
        all_more_pets = more_pets.objects.all()
    context = {"others" : all_more_pets}
    return render(request, "Pets/list_others.html",context=context)


def update_other(request, pk):
    other = more_pets.objects.get(pk=pk)
    if request.method == "GET":
        context = {
            "form" : petsform(
                initial={
                    "name":other.name,
                    "vaccine":other.vaccine,
                    "castrated":other.castrated
                }
                )
        }
        return render(request,"Pets/update_other.html",context=context)
    elif request.method == "POST":
        form = petsform(request.POST)
        if form.is_valid():
            other.name = form.cleaned_data["name"]
            other.vaccine = form.cleaned_data["vaccine"]
            other.castrated = form.cleaned_data["castrated"]
            other.save()

            context = {"message" : "Mascota actualizado exitosamente"}
            return render(request,"Pets/update_other.html",context=context)
        else:
            context = {
                "form_errors": form.errors,
                "form":petsform()
            }
            return render(request,"Pets/update_other.html",context=context)

class otherDeleteView(DeleteView):
    model = more_pets
    template_name = "Pets/delete_other.html"
    success_url = "/pets/list_others/"