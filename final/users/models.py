from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    phone = models.CharField(max_length=20,null=True,blank=True,verbose_name="Número de telefono")
    birth_date = models.DateField(null=True,blank=True,verbose_name="Fecha de nacimiento")
    address = models.CharField(max_length=50,null=True,blank=True,verbose_name="Dirección")
    description = models.CharField(max_length=500,null=True,blank=True,verbose_name="Descripción")
    blog = models.URLField(max_length=500,null=True,blank=True,verbose_name="Link de mi blog")
    interested_in_adopting = models.BooleanField(default=False,verbose_name="Interesado en adoptar")
    profile_picture = models.ImageField(upload_to="profile_images",null=True,blank=True,verbose_name="Foto de perfil")

    def __str__(self):
        return(self.name)    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios" 