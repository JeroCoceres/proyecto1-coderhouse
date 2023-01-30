from django.shortcuts import render
from members.models import  Members
from django.views.generic import ListView,CreateView,DeleteView
from members.form import MembersForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class membersListView(ListView):
    model = Members
    template_name = "Members/members.html"


def membersCreateView(request):
    if request.method == "GET":
        context = {
            "form":MembersForm
    }
        return render (request,"Members/new_member.html",context=context)
    elif request.method == "POST":
        form = MembersForm(request.POST) 
        if form.is_valid():
            Members.objects.create(
                name = form.cleaned_data["name"],
                job = form.cleaned_data["job"],
                is_active = form.cleaned_data["is_active"],
                since = form.cleaned_data["since"]
            )
            return render (request,"Members/new_member.html",context={})
        else:
            context = {
                "form_errors":form.errors,
                "form":form
            }
            return render (request,"Members/new_member.html",context=context)


class membersDeleteView(LoginRequiredMixin,DeleteView):
    model = Members
    template_name = "Members/delete_member.html"
    success_url = "/members/members"
    

@login_required
def update_member(request, pk):
    member = Members.objects.get(pk=pk)
    if request.method == "GET":
        context = {
            "form" : MembersForm(
                initial={
                    "name":member.name,
                    "job":member.job,
                    "is_active":member.is_active
                }
                )
        }
        return render(request,"Members/update_member.html",context=context)
    elif request.method == "POST":
        form = MembersForm(request.POST)
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
                "form":MembersForm()
            }
            return render(request,"members/update_member.html",context=context)

