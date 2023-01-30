from django import forms
from members.models import Members

class DateInput(forms.DateInput):
    input_type = "date"



class MembersForm(forms.ModelForm,DateInput):
    class Meta:
        model = Members
        #template_name = "Members/new_member.html"
        fields = "__all__"
        widgets= {"since":DateInput()}
