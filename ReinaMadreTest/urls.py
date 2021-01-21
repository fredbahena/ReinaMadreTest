"""ReinaMadreTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from ReinaMadreTest.views import saludo, continuamos, saludo_html, muestra_fecha, calcula_edad
from app_empleados.views import home, muestra_empleados, busqueda_comodin, guardar_empleado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home/', home),
    path('saludo/', saludo),
    path('seguimos/', continuamos),
    path('saludohtml/', saludo_html),
    path('fecha/', muestra_fecha),
    path('edad/<int:edad_actual>/<int:anio>/', calcula_edad),
    path('busqueda/', muestra_empleados),
    path('buscar/', busqueda_comodin),
    path('registrausuario/', guardar_empleado),
]
