from django.urls import path
from empleado_app import views

urlpatterns = [
    path("empleado",views.inicio_empleado,name="empleado"),
    path("registrarCoordi/",views.registrarCoordi,name="registrarCoordi" ), 
    path("SeleccionarCoordi/<id_empleado>",views.SeleccionarCoordi,name="SeleccionarCoordi"),
    path("editarCoordi/",views.editarCoordi,name="editarCoordi"),
    path("BorrarCoordi/<id_empleado>",views.BorrarCoordi,name="BorrarCoordi")
    
]
