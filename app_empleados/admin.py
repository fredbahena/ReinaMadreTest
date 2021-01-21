from django.contrib import admin

from .models import empleados, empresas, departamentos, view_empleados

admin.site.register(empleados)
admin.site.register(empresas)
admin.site.register(departamentos)
admin.site.register(view_empleados)
