from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('',views.index,name='index'),
    path('crearusuario',views.crearUsuario),
    path('loginu',views.loginu),
    path('mostrarusuarios',views.mostrarUsuarios),
    path('crearticket',views.crearticket),
    path('loginusuario',LoginView.as_view(template_name = 'aplicacion/loginusuario.html'),name='loginusuario'),
    path('logoutusuario',LogoutView.as_view(template_name = 'aplicacion/logoutusuario.html'),name='logoutusuario'),
    path('tickets',views.tickets),
    path('ticketsu',views.ticketsu),
    path('cerrarticket/<int:id>',views.cerrarticket),
    path('prueba',views.prueba)

]
