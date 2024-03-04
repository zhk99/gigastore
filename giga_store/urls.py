"""
URL configuration for giga_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
from main_store import views
from main_store.views import home
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('producto/', views.producto, name='producto'),
    path('listarProductos/', views.listar_productos, name='listar_productos'),
    path('login/', views.login, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('aggUser/',views.aggUser, name='aggUser'),
    path('controlpanel/',views.controlpanel, name='controlpanel'),
    path('cargar_producto/', views.cargar_producto, name='cargar_producto'),
     path('menu_producto/', views.menu_producto, name='menu_producto'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
