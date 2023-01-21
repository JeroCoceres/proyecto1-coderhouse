from django.db import models


class Members(models.Model):
    name = models.CharField(max_length=30,verbose_name="Nombre")
    job = models.CharField(max_length=30,verbose_name="Que hace?")
    is_active = models.BooleanField(default=False,verbose_name="Activo")
    