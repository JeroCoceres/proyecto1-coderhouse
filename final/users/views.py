from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from users.forms import RegisterForm,UserUpdateForm,UserProfileForm
from users.models import UserProfile


def login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
        context = {"form":form}
        return render(request, "users/login.html",context=context)
    elif request.method == "POST":
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request,user)
                context = { "message":f"Bienvenido {username}!"}
                return render (request, "index.html",context=context)
        
        form = AuthenticationForm
        context = {
            "form":form,
            "errors" : "Usuario o contraseña incorrectos!"
        }
        return render(request, "index.html",context=context)

def register(request):
    if request.method == "GET":
        form = RegisterForm
        context = { "form" : form}
        return render (request,"users/register.html", context=context)
    
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            context = {
                "form" : AuthenticationForm() 
            }
            return redirect("login")
        context = {
                "errors":form.errors,
                "form": RegisterForm
            }
        return render(request,"users/register.html",context=context)

@login_required
def update_user(request):
    if request.method == "GET":
        user = request.user
        form = UserUpdateForm(initial = {
            "username":user.username,
            "first_name":user.first_name,
            "last_name":user.last_name
        } 
        )
        context = { "form" : form}
        return render (request,"users/update.html", context=context)
    
    elif request.method == "POST":
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                "form" : AuthenticationForm() 
            }
            return redirect("index.html")
        context = {
                "errors":form.errors,
                "form": UserUpdateForm
            }
        return render(request,"users/update.html",context=context)

def create_user_profile(request):
        if request.method == "GET":
            form = RegisterForm
            context = { "form" : form}
            return render (request,"users/register.html", context=context)
    
        elif request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                context = {
                "form" : AuthenticationForm() 
            }
            return redirect("login")
        context = {
                "errors":form.errors,
                "form": RegisterForm
            }
        return render(request,"users/register.html",context=context)

def update_user_profile(request):
        if request.method == "GET":
            form = UserProfileForm(initial={
            "phone":request.user.profile.phone,
            "birth_date":request.user.profile.birth_date,
            "profile_picture":request.user.profile.profile_picture 
            })
            context = { "form" : form}
            return render (request,"users/update_profile.html", context=context)
    
        elif request.method == "POST":
            form = UserProfileForm(request.POST,request.FILES, instance=request.user.profile)
            print(request.POST)
            print(request.FILES)
            if form.is_valid():
                request.user.profile.phone = form.cleaned_data.get("phone")
                request.user.profile.birth_date = form.cleaned_data.get("birth_date")
                request.user.profile.profile_picture = form.cleaned_data.get("profile_Picture")
                request.user.profile.save()
            return  render(request,"index.html")
        context = {
                "errors":form.errors,
                "form": UserProfileForm
            }
        return render(request,"users/update_profile.html",context=context)
