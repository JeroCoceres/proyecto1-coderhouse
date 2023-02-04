from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from users.models import UserProfile

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label="Nombre")
    last_name = forms.CharField(max_length=30,required=True, label="Apellido")

    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, label="Nombre")
    last_name = forms.CharField(max_length=30,required=True, label="Apellido")
    class Meta:
        model = User
        fields = ["first_name","last_name","email"]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["phone","birth_date","profile_picture","address","interested_in_adopting","blog","description"]
