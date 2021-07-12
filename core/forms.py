from django import forms
from .models import Contacto

class ContactoForm(forms.Form):
        model = Contacto
        fields = [
            'ID',
            'Nombre',
            'Apellidos',
            'Correo',
            'Telefono',
            'Mensaje',
            'FechaEnvio'
        ]
        labels = {
            'ID' : 'ID',
            'Nombre' : 'nombre',
            'Apellidos' : 'apellido',
            'Correo' : 'apellido',
            'Telefono' : 'apellido',
            'Mensaje' : 'mensaje',
            'FechaEnvio' : 'fechaenvio'
        }
