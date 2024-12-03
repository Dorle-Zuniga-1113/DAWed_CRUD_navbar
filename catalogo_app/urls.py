from django.urls import path
from catalogo_app import views

urlpatterns = [
    path("catalogo",views.inicio_catalogo,name="catalogo"),
    path("registrarcatalogo/",views.registrarCatalogo,name="registrarcatalogo" ), 
    path("seleccionarcatalogo/<id_catalogo>",views.SeleccionarCatalogo,name="seleccionarcatalogo"),
    path("editarcatalogo/",views.editarCatalogo,name="editarcatalogo"),
    path("borrarcatalogo/<id_catalogo>",views.Borrarcatalogo,name="borrarcatalogo")
    
]
