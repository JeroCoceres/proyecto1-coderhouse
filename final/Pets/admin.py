from django.contrib import admin

from Pets.models import dogs,cats,more_pets


@admin.register(dogs)
class dogsadmin(admin.ModelAdmin):
    list_display = ("name","vaccine","birth","adoption_date","castrated",)
    list_filter = ("vaccine","castrated",)
    search_fields = ("name",)