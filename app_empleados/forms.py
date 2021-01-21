from django import forms
from app_empleados.models import empleados
from django.contrib.auth.forms import UserCreationForm

class formulario_empleado(forms.ModelForm):
    class Meta:
        model= empleados
        fields='__all__'
        widgets = {"fecha_nacimiento": forms.DateInput(attrs={"type":"date"}), 
                    "fecha_ingreso": forms.DateInput(attrs={"type":"date"})
                    }

class CustomUserForm(UserCreationForm):
    pass
