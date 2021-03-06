from django.db import models

##----------------------------------------------------
# Modelo tabla empleados
class empleados(models.Model):
    nombre = models.CharField(max_length=200)
    id_departamento = models.IntegerField()
    fecha_nacimiento = models.DateField()
    correo_electronico = models.EmailField()
    genero = models.CharField(max_length=1)
    telefono = models.CharField(max_length=10)
    celular = models.CharField(max_length=10)
    fecha_ingreso = models.DateTimeField(auto_now=True) 

##----------------------------------------------------
# Modelo tabla empresas
class empresas(models.Model):
    id_empresa = models.IntegerField()
    nombre = models.CharField(max_length=250)
    
##----------------------------------------------------
# Modelo tabla departamentos
class departamentos(models.Model):
    id_departamento = models.IntegerField()
    nombre = models.CharField(max_length=250)
    id_empresa = models.IntegerField()

##----------------------------------------------------
# Modelo tabla vista view_empleados
class view_empleados(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_empleado = models.IntegerField() 
    nombre = models.CharField(max_length=200)
    departamento = models.CharField(max_length=250)
    empresa = models.CharField(max_length=250)
   
    class Meta:
            managed = False
            db_table = 'view_empleados'
