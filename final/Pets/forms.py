from django import forms


class petsform(forms.Form):
    name = forms.CharField(max_length=30)
    castrated = forms.BooleanField(required=False)
    vaccine = forms.BooleanField(required=False)
    #birth = forms.DateField()
    #adoption_date = forms.DateField()
    #proximas funciones