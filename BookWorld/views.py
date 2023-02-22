from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm;
from .models import *
from .forms import *
from django.core.paginator import Paginator


def index(request):
    books = Book.objects.all().order_by('title')[:9]
    return render(request, 'index.html',{'books': books})


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


def products(request):
    books_list = Book.objects.all().order_by('title')
    paginator = Paginator(books_list, 9)
    page = request.GET.get('page') or 1
    books = paginator.get_page(page)
    current_page = int(page)
    pages = range(1, books.paginator.num_pages + 1)
    return render(request, 'products.html', {'books': books, 'pages': pages, 'current_page': current_page})
