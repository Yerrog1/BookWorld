from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Q
from django.shortcuts import redirect
from django.shortcuts import render
from .models import *
import BookWorld.models.user as user
from .forms import *


def index(request):
    books = Book.objects.all().order_by('title')[:9]

    return render(request, 'index.html', {'books': books})


def registerUser(request):
    if Cart(request).cart:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                usuario = form.save(commit=False)
                change = False
                usuario.save()
                userOrder = UserOrder(request, usuario, Cart(request))
                created = userOrder.saveInvoice()
                books = Book.objects.all().order_by('title')[:9]
                userOrder.sendMail()
                Cart(request).clear()
                return render(request, 'index.html', {'books': books, 'created': created, 'change': change})
            else:
                change = False
                if (user.validateDni(form.data.get('dni'))
                        and user.validateEmail(form.data.get('email'))
                        and len(str(form.data.get('phone'))) == 9):
                    usuario = User.objects.get(dni=form.data.get('dni'))
                    if usuario.email != form.data.get('email'):
                        usuario.email = form.data.get('email')
                        change = True
                        usuario.save()
                    if usuario.phone != form.data.get('phone'):
                        usuario.phone = form.data.get('phone')
                        usuario.save()
                        change = True
                    if usuario.address != form.data.get('address'):
                        usuario.address = form.data.get('address')
                        usuario.save()
                        change = True
                    if usuario.name != form.data.get('name'):
                        usuario.name = form.data.get('name')
                        usuario.save()
                        change = True
                else:
                    form = UserForm()
                    error = True
                    return render(request, 'registerUser.html', {'form': form, 'error': error})
                userOrder = UserOrder(request, usuario, Cart(request))
                created = userOrder.saveInvoice()
                books = Book.objects.all().order_by('title')[:9]
                userOrder.sendMail()
                Cart(request).clear()
                return render(request, 'index.html', {'books': books, 'created': created, 'change': change})

        else:
            form = UserForm()
            return render(request, 'registerUser.html', {'form': form})
    else:
        return redirect('index')


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
    return redirect("cart")


def add_to_cart_in_products(request, product_isbn):
    cart = Cart(request)
    product = Book.objects.get(isbn=product_isbn)
    cart.add(product)
    return redirect("search_books")


def remove_from_cart(request, product_isbn):
    cart = Cart(request)
    product = Book.objects.get(isbn=product_isbn)
    cart.remove(product)
    return redirect("cart")


def subtract_from_cart(request, product_isbn):
    cart = Cart(request)
    product = Book.objects.get(isbn=product_isbn)
    cart.subtract(product)
    return redirect("cart")


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


def search_books(request):
    query = request.GET.get('q')
    if query:
        books_list = Book.objects.filter(
            Q(title__icontains=query) | Q(author__name__icontains=query) | Q(genre__icontains=query))
    else:
        books_list = Book.objects.all()
    paginator = Paginator(books_list, 9)
    page = request.GET.get('page') or 1
    books = paginator.get_page(page)
    current_page = int(page)
    pages = range(1, books.paginator.num_pages + 1)
    if query:
        return render(request, 'products.html',
                      {'books': books, 'pages': pages, 'current_page': current_page, 'query': query})

    return render(request, 'products.html', {'books': books, 'pages': pages, 'current_page': current_page})
