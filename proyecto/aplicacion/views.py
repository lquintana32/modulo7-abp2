from django.shortcuts import render, redirect, get_object_or_404
from .models import  Ticket
from .forms import CierreTicket, LoginForm, TicketForm, UsuariosForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.utils import timezone
# Create your views here.
def index(request):
    return render(request,'aplicacion/index.html')  

def crearUsuario(request):
    if request.method=='POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            clave = form.cleaned_data['password']
            user = User.objects.create_user(nombre,email,clave)
            user.save()
            messages.success(request,f'Usuario {nombre} creado exitosamente!')
        return render(request,'aplicacion/crearusuario.html')
    else:
        form = UsuariosForm()
    return render(request, 'aplicacion/crearusuario.html',{'form':form})

def loginu(request):
    if request.method=='POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            clave = form.cleaned_data['password']
            user = authenticate(request, username = nombre, password = clave)
            if user is not None:
                login(request,user)
        return render(request,'aplicacion/bienvenido.html',{'user':user})
    else:
        form = LoginForm()
        return render(request,'aplicacion/loginu.html',{'form':form})

def mostrarUsuarios(request):
    usuarios = User.objects.all()
    return render(request,'aplicacion/mostrarusuarios.html',{'usuarios':usuarios,})

def tickets(request):
    tickets=Ticket.objects.all()
    return render(request, 'aplicacion/tickets.html',{'tickets':tickets})

def crearticket(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method=='POST':
        form = TicketForm(request.POST)
        if form.is_valid():  
            ticket = form.save(commit=False)
            print(ticket.category)
            ticket.user=current_user
            print(ticket.user)
            ticket.save()
            print(ticket)
            return redirect('index')
    else:
        form = TicketForm()
    return render(request, 'aplicacion/ticket.html',{'form':form})
            
def cerrarticket(request, id):
    ticket = Ticket.objects.get(pk=id)
    form = CierreTicket(request.POST)
    if request.method=='POST':
        form=CierreTicket(data=request.POST)
        if form.is_valid():
            ticket.solution = form.cleaned_data['solution']
            print(timezone.now())
            print(ticket.solution)
            ticket.timeclosing = timezone.now()
            print(ticket.timeclosing)
            ticket.state = 'Cerrado'
            print(ticket.state)
            ticket.save()
            return redirect('/tickets')

    else:
        return render(request,'aplicacion/cerrarticket.html',{'form':form})

def prueba(request):
    return render(request,'aplicacion/prueba.html')

def ticketsu(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    usuario = current_user
    tickets=Ticket.objects.filter(user=usuario)
    return render(request, 'aplicacion/ticketsu.html',{'tickets':tickets})
