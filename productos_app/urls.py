from django.urls import path
from productos_app import views
#cambiar variables a productos
urlpatterns = [
    path("productos",views.inicio_producto,name="productos"),
    path("registrarproducto/",views.registrarProducto,name="registrarproducto" ), 
    path("seleccionarproducto/<id_producto>",views.SeleccionarProducto,name="seleccionarproducto"),
    path("editarproducto/",views.editarProducto,name="editarproducto"),
    path("borrarproducto/<id_producto>",views.BorrarProducto,name="borrarproducto")
    
]
