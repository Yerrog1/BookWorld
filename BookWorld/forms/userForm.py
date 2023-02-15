from django import forms
from BookWorld.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['dni','name','email','address','phone']