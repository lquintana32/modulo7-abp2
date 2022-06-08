from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import admin
# Create your models here.


class Ticket(models.Model):
    CATEGORIAS = [
        ('Incidente','Incidente'),
        ('Requerimiento','Requerimiento'),
        ('Logistica','Logistica')
    ]
    ESTADOS = [
        ('Abierto','Abierto'),
        ('Cerrado','Cerrado'),
    ]
    ticket_id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    timestamp = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=50,choices = CATEGORIAS)
    content = models.TextField()
    state = models.CharField(max_length=50,choices = ESTADOS,default='Abierto')
    timeclosing = models.DateTimeField(blank=True,null=True)
    solution = models.TextField(default='')  

    def __str__(self):
        num = 10000+self.ticket_id
        cadena = str(num)
        ncadena = cadena[1:]
        nuevo_id="TKT"+str(ncadena)
        self.nuevo_id=nuevo_id
        return nuevo_id

