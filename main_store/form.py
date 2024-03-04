from django import forms
from .models import User
from .models import Product

class userForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'is_active', 'password']
        labels = {
        'username': 'Usuario',
        'is_active':'Activo',
        'password': 'password',          
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image_url', 'price']