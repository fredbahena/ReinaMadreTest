from django.db import models

class empleados(models.Model):
    nombre = models.CharField(max_length=200)
    id_departamento = models.IntegerField()
    fecha_nacimiento = models.DateField()
    correo_electronico = models.EmailField()
    genero = models.CharField(max_length=1)
    telefono = models.CharField(max_length=10)
    celular = models.CharField(max_length=10)
    fecha_ingreso = models.DateTimeField(auto_now=True) 


class empresas(models.Model):
    id_empresa = models.IntegerField()
    nombre = models.CharField(max_length=250)
    

class departamentos(models.Model):
    id_departamento = models.IntegerField()
    nombre = models.CharField(max_length=250)
    id_empresa = models.IntegerField()

class view_empleados(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    departamento = models.CharField(max_length=250)
    empresa = models.CharField(max_length=250)
   
    class Meta:
            managed = False
            db_table = 'view_empleados'
