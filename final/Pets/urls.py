from django.urls import path
from Pets.views import list_dogs,list_cats,list_others,create_dog,create_cat,create_other,update_dog,dogDeleteView,update_cat,catDeleteView,update_other,otherDeleteView


urlpatterns = [
    path('list_dogs/', list_dogs),
    path("new-dog/",create_dog),
    path("update-dog/<int:pk>/",update_dog),
    path("delete-dog/<int:pk>/",dogDeleteView.as_view()),

    path("list_cats/", list_cats),     
    path("new-cat/",create_cat),
    path("update-cat/<int:pk>/",update_cat),
    path("delete-cat/<int:pk>/",catDeleteView.as_view()),


    path("list_others/",list_others),    
    path("new-other/",create_other),
    path("update-other/<int:pk>/",update_other),    
    path("delete-other/<int:pk>/",otherDeleteView.as_view()),



]