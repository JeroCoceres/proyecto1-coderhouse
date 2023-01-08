from django.shortcuts import render
from django.http import HttpResponse
from Pets.models import dogs, cats,more_pets

def create_dog(request):
    new_dog = dogs.objects.create(name = "Test name", vaccine = True, birth = "2020-01-01", adoption_date = "2020-05-01", castrated = True)
    return HttpResponse("Nuevo perro creado")

def list_dogs(request):
    all_dogs = dogs.objects.all()
    context = {"dogs":all_dogs}
    return render(request, "dogs.html",context= context)

def list_cats(request):
    all_cats = cats.objects.all()
    context = {"cats" : all_cats}
    return render(request, "cats.html",context=context)

def list_more_pets(request):
    all_more_pets = more_pets.objects.all()
    context = {"cats" : all_more_pets}
    return render(request, "more_pets.html",context=context)

