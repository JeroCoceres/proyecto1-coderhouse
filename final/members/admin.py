from django.contrib import admin
from members.models import Members

@admin.register(Members)
class Membersadmin(admin.ModelAdmin):
    list_display = ("name","job","is_active",)
    list_filter = ("job","is_active",)
    search_fields = ("name",)