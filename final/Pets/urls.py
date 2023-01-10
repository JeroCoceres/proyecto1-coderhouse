from django.urls import path
from Pets.views import list_dogs,list_cats,list_more_pets,create_dog,create_cat,create_other

urlpatterns = [
    path('perros/', list_dogs),
    path("gatos/", list_cats), 
    path("otros/",list_more_pets),
    path("nuevo-perro/",create_dog),
    path("nuevo-gato/",create_cat),
    path("nuevo-otro/",create_other)
]