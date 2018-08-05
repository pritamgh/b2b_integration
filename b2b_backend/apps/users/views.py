from .models import CustomUser
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from django.http import (
    HttpResponse,
    HttpResponseRedirect
)
from django.shortcuts import render

from django.urls import reverse
# from django.core.exceptions import ValidationError
# from django.db.models import Q


def index(request):
    """ Initially User haveto login to enter the dashboard """
    if not request.user.is_authenticated:
        """users = CustomUser.objects.all()
        context = {
            "users": users
        }
        return render(request, 'users/login.html', context)"""
        return render(request, 'users/login.html', {"message": None})
    context = {
        "user": request.user
    }
    return render(request, 'users/dashboard.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        return HttpResponse(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'users/login.html',
                          {"message": "Invalid Credentials"})
    """user_obj = None
    email = request.POST['email']
    password = request.POST['password']
    return HttpResponse(email)

    if not email:
        raise ValidationError("Email is Required")

    user = CustomUser.objects.filter(Q(email=email)).distinct()
    if user.exists() == 1:
        user_obj = user.first()
    else:
        raise ValidationError("Email is not Valid")

    if user_obj:
        if not user_obj.check_password(password):
            raise ValidationError("Creadentials incorrect")

    if user_obj is not None:
        login(request, user_obj)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'users/login.html',
                      {"message": "Invalid Credentials"})"""


def logout_view(request):
    logout(request)
    return render(request, 'users/login.html',
                  {"message": "Logged out."})
