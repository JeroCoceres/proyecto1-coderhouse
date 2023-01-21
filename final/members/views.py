from django.shortcuts import render
from members.models import  Members
from django.views.generic import ListView,CreateView,DeleteView
from members.form import membersForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class membersListView(ListView):
    model = Members
    template_name = "Members/members.html"


class membersCreateView(LoginRequiredMixin,CreateView):
    model = Members
    template_name = "Members/new_member.html"
    fields = "__all__"
    success_url = "/members/members"

class membersDeleteView(LoginRequiredMixin,DeleteView):
    model = Members
    template_name = "Members/delete_member.html"
    success_url = "/members/members"
    

@login_required
def update_member(request, pk):
    member = Members.objects.get(pk=pk)
    if request.method == "GET":
        context = {
            "form" : membersForm(
                initial={
                    "name":member.name,
                    "job":member.job,
                    "is_active":member.is_active
                }
                )
        }
        return render(request,"Members/update_member.html",context=context)
    elif request.method == "POST":
        form = membersForm(request.POST)
        if form.is_valid():
            member.name  = form.cleaned_data["name"]
            member.job = form.cleaned_data["job"]
            member.is_active = form.cleaned_data["is_active"]
            member.save()

            context = {"message" : "Integrante actualizado exitosamente"}
            return render(request,"members/update_member.html",context=context)
        else:
            context = {
                "form_errors": form.errors,
                "form":membersForm()
            }
            return render(request,"members/update_member.html",context=context)

