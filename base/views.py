from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request, 'base/home.html')


def book(request):
    return render(request, 'base/book.html')
    

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'base/register.html', {'form': form})

def login_user(request):
    form = LoginUserForm()

    if request.method == 'POST':
        form = LoginUserForm(request,data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

    return render(request, 'base/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')

def user_profile(request):
    return render(request, 'base/user_profile.html')