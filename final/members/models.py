from django.db import models


class Members(models.Model):
    name = models.CharField(max_length=30,verbose_name="Nombre")
    job = models.CharField(max_length=30,verbose_name="Que hace?")
    is_active = models.BooleanField(default=False,verbose_name="Activo")
    since = models.DateField(null="01/01/2000",verbose_name="Desde")

    def __str__(self):
        return(self.name)    
    class Meta:
        verbose_name = "Miembro"
        verbose_name_plural = "Miembros"