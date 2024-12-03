from django.urls import path
from empleado_app import views

urlpatterns = [
    path("empleado",views.inicio_empleado,name="empleado"),
    path("registrarCoordi/",views.registrarCoordi,name="registrarCoordi" ), 
    path("SeleccionarCoordi/<codigo>",views.SeleccionarCoordi,name="SeleccionarCoordi"),
    path("editarCoordi/",views.editarCoordi,name="editarCoordi"),
    path("BorrarCoordi/<codigo>",views.BorrarCoordi,name="BorrarCoordi")
    
]
