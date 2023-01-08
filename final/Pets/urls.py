from django.urls import path
from Pets.views import list_dogs,list_cats,list_more_pets,create_dog



urlpatterns = [
    path('perros/', list_dogs),
    path("gatos/", list_cats), 
    path("gatos/",list_more_pets),
    path("nuevo-perro/",create_dog)
]