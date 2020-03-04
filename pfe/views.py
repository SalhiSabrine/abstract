# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Role

# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pfe:home')
        else:
            return redirect('pfe:notfoundpage')
    return render(request, 'login.html')

def home(request):
    roles = Role.objects.all()
    return render(request, 'index.html' , {'roles' : roles})

def notfoundpage(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'login.html')

def ajouter(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        cpassword = request.POST.get('cpassword', '')
        name = request.POST.get('name', '')
        lastname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        r = request.POST.get('role', '')
        user = User.objects.create_user(username, email, password)
        user.last_name = lastname
        user.first_name = name
        user.email = email
        user.save()
        role  = Role()
        role.user = user
        role.role = r
        role.save()
        lastuser = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, lastuser)
        return redirect('pfe:home')
    roles = Role.objects.all()
    return render(request, 'index.html', {'roles' : roles})

