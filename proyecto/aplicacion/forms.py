from django import forms
from django.db.models import fields
from .models import Ticket
from django.contrib.auth.models import User


class UsuariosForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    

class LoginForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

class TicketForm(forms.ModelForm):
    CATEGORIAS = [
        ('Incidente','Incidente'),
        ('Requerimiento','Requerimiento'),
        ('Logistica','Logistica')
    ]
    content = forms.CharField(widget=forms.Textarea)
    category = forms.ChoiceField(choices = CATEGORIAS)

    class Meta:
        model = Ticket
        fields = ['content','category']

class CierreTicket(forms.Form):
    solution =forms.CharField(widget=forms.Textarea)



