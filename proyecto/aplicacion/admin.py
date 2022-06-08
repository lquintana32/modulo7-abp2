from multiprocessing.connection import Client
from django.contrib import admin
from .models import Ticket
from .models import Ticket
from django.contrib.auth.models import Group
# Register your models here.

#admin.site.register(Cliente)

admin.site.unregister(Group)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_id','user','content')
admin.site.register(Ticket,TicketAdmin)