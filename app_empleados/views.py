from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth import login, authenticate

from app_empleados.models import view_empleados, empresas, departamentos
from app_empleados.forms import formulario_empleado, CustomUserForm
##----------------------------------------------------
# 
def isNum(data):
    try:
        int(data)
        return True
    except ValueError:
        return False

##----------------------------------------------------
# 
def home(request):

    return render(request, "home.html")


##----------------------------------------------------
# 
def muestra_empleados(request):

    emp = empresas.objects.all() 
    deptos = departamentos.objects.values("nombre").distinct() 

    return render(request, "busqueda_empleados.html",{"empresas":emp, "departamentos":deptos})

##----------------------------------------------------
# 
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
# 
def guardar_usuario(request):
        data = {
            "form":CustomUserForm
        }
        if request.method == "POST":
            formulario = CustomUserForm(request.POST)
            if formulario.is_valid():
                formulario.save()

                username = formulario.cleaned_data("username")
                password = formulario.cleaned_data("password1")
                user = authenticate(username, password)
                login(request, user)
                return redirect(to=home)

        return render(request,"registra_usuario.html",data)    
##----------------------------------------------------
# 
def guardar_empleado(request):
        data = {
            "form":formulario_empleado
        }
        if request.method == "POST":
            formulario = formulario_empleado(request.POST)
            if formulario.is_valid():
                formulario.save()



        return render(request,"alta_empleado.html",data)  

