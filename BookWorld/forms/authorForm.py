from django import forms
from BookWorld.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name','description']
