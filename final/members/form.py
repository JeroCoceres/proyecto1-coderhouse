from django import forms
from members.models import Members

class membersForm(forms.Form):
    name = forms.CharField(max_length=50)
    job = forms.BooleanField(required=False)
    is_active = forms.BooleanField(required=False)

class MembersForm(forms.ModelForm):
    class META:
        model = Members
        fields = "__all__"
        