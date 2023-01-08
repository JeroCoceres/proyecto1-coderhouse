from django.db import models

class dogs(models.Model):
    name = models.CharField(max_length=30,verbose_name="Nombre")
    vaccine = models.BooleanField(verbose_name="Vacunado")
    birth = models.DateField(verbose_name="Edad")
    adoption_date = models.DateField(verbose_name="Fecha de adopción")
    castrated = models.BooleanField(verbose_name="Castrado")
    
    def __str__(self):
        return(self.name)

    class Meta:
        verbose_name = "Perro"
        verbose_name_plural = "Perros"

class cats(models.Model):
    name = models.CharField(max_length=30,verbose_name="Nombre")
    vaccine = models.BooleanField(verbose_name="Vacunado")
    birth = models.DateField(verbose_name="Edad")
    adoption_date = models.DateField(verbose_name="Fecha de adopción")
    castrated = models.BooleanField(verbose_name="Castrado")

    def __str__(self):
        return(self.name)   

    class Meta:
        verbose_name = "Gato"
        verbose_name_plural = "Gatos" 

class more_pets(models.Model):
    name = models.CharField(max_length=30,verbose_name="Nombre")
    vaccine = models.BooleanField(verbose_name="Vacunado")
    birth = models.DateField(verbose_name="Edad")
    adoption_date = models.DateField(verbose_name="Fecha de adopción")
    castrated = models.BooleanField(verbose_name="Castrado")

    def __str__(self):
        return(self.name)

    class Meta:
        verbose_name = "Otros"
        verbose_name_plural = "Otros"