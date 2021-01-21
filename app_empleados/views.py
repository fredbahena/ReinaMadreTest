from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

from app_empleados.models import empresas, departamentos, empleados, view_empleados
from app_empleados.forms import formulario_empleado, CustomUserForm
##----------------------------------------------------
# Valida si la variable es un entero
def isNum(data):
    try:
        int(data)
        return True
    except ValueError:
        return False

##----------------------------------------------------
# Página principal
def home(request):

    return render(request, "home.html")


##----------------------------------------------------
# Pantalla principal de búsqueda
def muestra_empleados(request):

    emp = empresas.objects.all() 
    deptos = departamentos.objects.values("nombre").distinct() 

    return render(request, "busqueda_empleados.html",{"empresas":emp, "departamentos":deptos})

##----------------------------------------------------
# Buscar empleados por empresa, departamento y like %nombre%
def busqueda_comodin(request):

    get_empr = request.GET["empresa"]
    get_depto = request.GET["departamento"]
    get_texto = request.GET["nombre"]
    
    obj_empresas = empresas.objects.all() 
    obj_deptos = departamentos.objects.values("nombre").distinct() 


    if get_texto:
        
        if get_empr == "" and get_depto == "":
            obj_empleados = view_empleados.objects.filter(nombre__icontains=get_texto) #icontains "like"

        if get_empr != "" and get_depto == "":    
            obj_empleados = view_empleados.objects.filter(empresa=get_empr, nombre__icontains=get_texto)
        
        if get_empr == "" and get_depto != "":    
            obj_empleados = view_empleados.objects.filter(departamento=get_depto, nombre__icontains=get_texto)
        
        if get_empr != "" and get_depto != "":    
            obj_empleados = view_empleados.objects.filter(empresa=get_empr, departamento=get_depto,nombre__icontains=get_texto)

        return render(request,"resultados_busqueda.html",
        {"empleados":obj_empleados, "get_texto":get_texto, "empresas":obj_empresas,
         "get_empr":get_empr, "departamentos":obj_deptos , "get_depto":get_depto})
        

    else:
        mensaje = """<html>
        <body>
        No se ha introducido ningún valor en el campo de Nombre,
        <a href="../busqueda/">buscar de nuevo</a>
        </body>
        </html>"""

    return HttpResponse(mensaje)

##----------------------------------------------------
# Elimina empleados por id
def elimina_empleado(request,id_empleado):

    obj_empleados = empleados.objects.get(id=id_empleado)
    obj_empleados.delete()
    
    return render(request,"busqueda_empleados.html")

##----------------------------------------------------
# Edita empleados por id
def edita_empleado(request,id_empleado):

    obj_empleados = empleados.objects.get(id=id_empleado)

    if request.method == 'GET':
        form = formulario_empleado(instance=obj_empleados)
        contexto = {
            'form':form
        }
    else:
        form= formulario_empleado(request.POST, instance = obj_empleados)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return render(request,"busqueda_empleados.html")

    return render(request,'alta_empleado.html',contexto)

##----------------------------------------------------
# Guarda nuevos registros de empleados
def guarda_empleado(request):

    if request.method == 'GET':
        form = formulario_empleado()
        contexto = {
            'form':form
        }
    else:
        form= formulario_empleado()
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return render(request,"alta_empleado.html")

    return render(request,'alta_empleado.html',contexto)
     
    
##----------------------------------------------------
# Registro de usuarios para inicio de sesión
def registra_usuario(request):
        form = CustomUserForm()
        contexto = {
            'form':form
        }
        
        if request.method == "POST":
            form = CustomUserForm(request.POST)
            if form.is_valid():
                form.save()

                username = form.cleaned_data("username")
                password = form.cleaned_data("password1")
                user = authenticate(username, password)
                login(request, user)
                return redirect(to=home)

        return render(request,"login.html",contexto)    

##----------------------------------------------------
# Inicio de sesión
def login(request):
        form = AuthenticationForm()
        contexto = {
            'form':form
        }
        
        if request.method == "POST":
                        
            form = AuthenticationForm(data = request.POST)

            if form.is_valid():
                
                username = form.cleaned_data("username")
                password = form.cleaned_data("password")

                user = authenticate(username, password)

                if user is not None:
                    do_login(request, user)
                    return render(request,"home.html")

        return render(request,"login.html",contexto) 

