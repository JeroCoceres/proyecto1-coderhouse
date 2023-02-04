from django import forms
from Pets.models import dogs

class DateInput(forms.DateInput):
    input_type = "date"


class petsform(forms.ModelForm,DateInput):
    class Meta:
        model = dogs
        fields = "__all__"
        widgets= {"birth_date":DateInput()}