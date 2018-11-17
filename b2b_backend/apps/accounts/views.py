from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)


def index(request):
    return render(request, 'index.html')


def login_view(request):

    email = request.get("email")
    password = request.get("password")
    user = authenticate(email=email, password=password)
    login(request, user)
    print(request.user.is_authenticated())
    return redirect("/")


def register_view(request):

    user = request.save(commit=False)
    password = request.get("password")
    user.set_password(password)
    user.save()

    new_user = authenticate(username=user.username, password=password)
    login(request, new_user)
    return redirect("/")


def logout_view(request):
    logout(request)
    return redirect("/login/")
