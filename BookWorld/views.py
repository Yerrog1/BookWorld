from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from django.core.paginator import Paginator
from .models import *


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



def cartView(request):
    return render(request, 'cart.html')


def products(request):
    books_list = Book.objects.all().order_by('title')
    paginator = Paginator(books_list, 9)
    page = request.GET.get('page') or 1
    books = paginator.get_page(page)
    current_page = int(page)
    pages = range(1, books.paginator.num_pages + 1)
    return render(request, 'products.html', {'books': books, 'pages': pages, 'current_page': current_page})
def product(request, product_isbn):
    book = Book.objects.get(isbn=product_isbn)
    return render(request, 'product.html', {'book': book})

def add_to_cart(request, product_isbn):
    cart = Cart(request)
    product = Book.objects.get(isbn=product_isbn)
    cart.add(product)
    return redirect("index")

def remove_from_cart(request, product_isbn):
    cart = Cart(request)
    product = Book.objects.get(isbn=product_isbn)
    cart.remove(product)
    return redirect("index")
def subtract_from_cart(request, product_isbn):
    cart = Cart(request)
    product = Book.objects.get(isbn=product_isbn)
    cart.subtract(product)
    return redirect("index")

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("index")