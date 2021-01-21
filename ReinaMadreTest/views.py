from django.http import HttpResponse
from django.shortcuts import render
import datetime
import MySQLdb

##----------------------------------------------------
# primera vista
def saludo(request): 

    return HttpResponse("Hola ReinaMadre, esta es mi primera página con Django")

##----------------------------------------------------
# segunda vista
def continuamos(request):

    return HttpResponse("Seguimos desarrollando toda la noche y más test para ReinaMadre")

##----------------------------------------------------
# primera vista + html
def saludo_html(request): 

    documento = """<html>
    <body>
    <h1>Hola ReinaMadre, esta es mi primera página con Django</h1>
    </body>
    </html>"""

    return HttpResponse(documento)

##----------------------------------------------------
# vista dinámica
def muestra_fecha(request):

    fecha_actual = datetime.datetime.now()

    documento = """<html>
    <body>
    <b>La fecha y hora actual es: %s</b>
    </body>
    </html>""" %fecha_actual    

    return HttpResponse(documento)

##----------------------------------------------------
# vista parametros
def calcula_edad(request, edad_actual, anio):

    periodo = anio - 2021
    edad_futura = edad_actual + periodo

    documento = """<html>
    <body>
    <b>En el año %s tendrás %s años</b>
    </body>
    </html>""" %(anio, edad_futura)

    return HttpResponse(documento)

