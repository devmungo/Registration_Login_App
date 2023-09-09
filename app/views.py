from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'index.html')

def registration(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        print("We got here")

        if form.is_valid():

            form.save()
            print("fffff")
            return redirect("login")

    context = {'form': form}

    return render(request, 'registration.html', context=context)


def login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request.POST, data=request.POST)

        print("before checking the form was valid")

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')
            print("The form was valid")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")

    context = {'form': form}

    return render(request, 'login.html', context=context)


@login_required(login_url="login")
def dashboard(request):

    return render(request, 'dashboard.html')


def logout(request):

    auth.logout(request)

    return redirect("index")