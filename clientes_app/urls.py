from django.urls import path
from clientes_app import views
#cambiar variables a productos
urlpatterns = [
    path("clientes",views.inicio_cliente,name="clientes"),
    path("registrarcliente/",views.registrarCliente,name="registrarcliente" ), 
    path("seleccionarcliente/<id_cliente>",views.SeleccionarCliente,name="seleccionarcliente"),
    path("editarcliente/",views.editarCliente,name="editarcliente"),
    path("borrarcliente/<id_cliente>",views.BorrarClientes,name="borrarcliente")
    
]
