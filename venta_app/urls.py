from django.urls import path
from venta_app import views
#cambiar variables a productos
urlpatterns = [
    path("venta",views.inicio_venta,name="venta"),
    path("registrarventa/",views.registrarVentas,name="registrarventa" ), 
    path("seleccionarventa/<codigo>",views.SeleccionarVentas,name="seleccionarventa"),
    path("editarventa/",views.editarVentas,name="editarventa"),
    path("borrarventa/<codigo>",views.BorrarVentas,name="borrarventa")
    
]
