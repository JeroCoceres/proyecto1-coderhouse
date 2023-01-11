from django.contrib import admin

from Pets.models import dogs,cats,more_pets


@admin.register(dogs)
class dogsadmin(admin.ModelAdmin):
    list_display = ("name","vaccine","castrated",)
    list_filter = ("vaccine","castrated",)
    search_fields = ("name",)

@admin.register(cats)
class catsadmin(admin.ModelAdmin):
    list_display = ("name","vaccine","castrated",)
    list_filter = ("vaccine","castrated",)
    search_fields = ("name",)

@admin.register(more_pets)
class more_petsadmin(admin.ModelAdmin):
    list_display = ("name","vaccine","castrated",)
    list_filter = ("vaccine","castrated",)
    search_fields = ("name",)