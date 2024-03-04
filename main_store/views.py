from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Product
from .form import ProductForm
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
import os
# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm()
        })
    else:
        user = authenticate(
        request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
                 return render(request, 'login.html', {
                'form': AuthenticationForm(),
                'error' : "El Usuario o contrasenha es incorrecta"
            })
        else:
             login(request, user)
             return redirect('controlpanel')
def cerrar_sesion(request):
    logout(request)
    return redirect('home')
def aggUser(request):
     if request.method == 'GET':
        print('enviando datos')
        return render(request, 'aggUser.html', {
            'form': UserCreationForm
        })
     else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('task')
            except IntegrityError:
                return render(request, 'aggUser.html', {
                    'form': UserCreationForm,
                    'error': 'El Usuario ya existe'
                })
        else:
            return render(request, 'aggUser.html', {
                'form': UserCreationForm,
                'error': 'Las contraseñas no coinciden'
            })
def menu_producto(request):
    product = Product.objects.all()
    return render(request, 'modify.html',{'products':product})
def controlpanel(request):
    if login:
        return render(request, 'controlpanel.html')
    else:
        return redirect('login')
def producto(request):
    
    return render('producto.html')

def listar_productos(request):
    product = Product.objects.all()
    return render(request, 'producto.html',{'products':product})
def cargar_producto(request):
    if request.method == 'POST':
        # Obtener los datos del formulario enviado por el usuario
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image_file = request.FILES.get('image_url')  # Asegúrate de que el nombre coincida con el campo del formulario

        # Verificar si se ha proporcionado un archivo
        if image_file:
            # Guardar la imagen en la ruta especificada
            product_image_path = os.path.join('product_images', image_file.name)
            with open(os.path.join(settings.MEDIA_ROOT, product_image_path), 'wb') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)

            # Crear un nuevo objeto Product con los datos recibidos y la ruta de la imagen
            new_product = Product(name=name, description=description, image_url=product_image_path, price=price)

            # Guardar el nuevo producto en la base de datos
            new_product.save()

            print('Producto Guardado Correctamente')
            return redirect('listar_productos')

    # Renderizar el formulario vacío o con errores
    return render(request, 'aggProductos.html')