from django import forms
from BookWorld.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['isbn', 'title', 'author', 'genre', 'price', 'description']
