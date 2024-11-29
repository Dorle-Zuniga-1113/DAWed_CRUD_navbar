from django.urls import path
from proveedores_app import views
#cambiar variables a proveedores
urlpatterns = [
    path("proveedor",views.inicio_proveedores,name="proveedor"),
    path("registrarproveedor/",views.registrarProveedor,name="registrarproveedor" ), 
    path("seleccionarproveedor/<codigo>",views.SeleccionarProveedor,name="seleccionarproveedor"),
    path("editarproveedor/",views.editarProveedor,name="editarproducto"),
    path("borrarproveedor/<codigo>",views.BorrarProveedor,name="borrarproveedor")
    
]
