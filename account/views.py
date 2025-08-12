from django.shortcuts import render
from .forms import RegisterForm, LoginForm, EditForm, PasswordForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required

# Create your views here.
def login1(request):
    form = LoginForm()
    if request.method == "POST":
        form=LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect("main")
    context = {
        'form' : form,
        "error" : form.errors
    }
    return render(request, 'account/login.html', context=context)
def register(request):
    form = RegisterForm()
    
    if request.method == "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main")
    context = {
        "form" : form,
        "error" : form.errors
    }
       
    return render(request, 'account/register.html', context=context)
@login_required (login_url='/account/login/')
def logout1(request):
    logout(request)
    return redirect("main")
@login_required (login_url='/account/login/')
def profile(request):
    buyed_games = request.user.buyed_games.all()
    context= {
        "buyed_games" : buyed_games
    }
    return render(request, 'account/profile.html', context = context)
@login_required (login_url='/account/login/')
def edit(request):
    
    form=EditForm(instance = request.user)
    
    if request.method == "POST":
        form = EditForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            form=EditForm(instance = request.user)
        
        else:
            print(form.errors)
        
    context={
        "form" : form
    }
    return render(request, 'account/profile_edit.html', context=context)
@login_required (login_url='/account/login/')
def change_password(request):
    form=PasswordForm()
    error = ""
    
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            user=request.user
            if  check_password(form.cleaned_data["password"], request.user.password) and form.cleaned_data["password1"] == form.cleaned_data["password2"]:
        #    form.save() 
                
                request.user.set_password(form.cleaned_data["password1"])
                request.user.save()
                login(request, user)
                form=PasswordForm()
                
                return redirect("main")
            else:
                error = "Пароли не совпадают"
        
        else:
            print(form.errors)
        
    context={
        "form" : form,
        "error" : error
    }
    return render(request, 'account/change_password.html', context=context)


