from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm;
from .models import User
from .forms import *


def index(request):
    return render(request, 'index.html')


def registerUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()
    else:
        form = UserForm()
    return render(request, 'registerUser.html', {'form': form})


def cart(request):
    return render(request, 'cart.html')


def search(request):
    return render(request, 'search.html')