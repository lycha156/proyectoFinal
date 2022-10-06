from django import forms
from .models import Contacto

class FormContacto(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = [
            'nombre',
            'email',
            'mensaje'
        ]

    nombre = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInputGrid', 'placeholder': 'Apellido y Nombre'}))
    email = forms.EmailField( widget=forms.EmailInput( attrs={'class': 'form-control', 'type': 'email', 'id': 'floatingInputGrid', 'placeholder': 'Email'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Deje un comentario', 'id': 'floatingTextarea', 'style': 'height: 200px;'}))

