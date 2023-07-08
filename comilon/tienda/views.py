from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Has iniciado sesión como {username}.")
                return redirect(to="home")
            else:
                messages.error(request, "Usuario o contraseña inválidos.")
        else:
            messages.error(request, "Usuario o contraseña inválidos.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Usuario registrado.")
            return redirect(to="home")
        messages.error(request, "Información inválida.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def menu(request):
    return render(request, "menu.html")


def pedido(request):
    return render(request, "pedido.html")


def agregar(request):
    return render(request, "agregar.html")


def salir(request):
    logout(request)
    return redirect('/')
