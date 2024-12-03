from django.shortcuts import render,redirect
from .models import Catalogo
# Create your views here.
#cambiar variables 
def inicio_catalogo(request):
    loscata=Catalogo.objects.all()
    
#cambiar los htmls
    return render(request,"gestionarCatalogo.html",{"loscata":loscata})
    
def registrarCatalogo(request):
    id_catalogo=request.POST["txtcod"]
    nombre = request.POST["txtnombre"]
    fecha_inicio = request.POST["numfechai"]
    fecha_fin  = request.POST["numfechaf"]
    promocion = request.POST["numprom"]
    coleccion = request.POST["txtcole"]
    novedades = request.POST["txtnew"]
    
#cambiar los redirect por variable de inicio
    guardarcatalogo=Catalogo.objects.create(id_catalogo=id_catalogo,nombre=nombre,fecha_inicio=fecha_inicio,fecha_fin=fecha_fin,promocion=promocion,coleccion=coleccion,novedades=novedades)
    return redirect("catalogo")

def SeleccionarCatalogo(request,id_catalogo):
    loscata=Catalogo.objects.get(id_catalogo=id_catalogo)
    return render(request,"editarcata.html",{"loscata":loscata})
    
def editarCatalogo(request):
    id_catalogo = request.POST["txtcod"]
    try:
        loscata = Catalogo.objects.get(id_catalogo=id_catalogo)
        loscata.nombre = request.POST["txtnombre"]
        loscata.fecha_inicio = request.POST["numfechai"]
        loscata.fecha_fin  = request.POST["numfechaf"]
        loscata.promocion = request.POST["numprom"]
        loscata.coleccion = request.POST["txtcole"]
        loscata.novedades = request.POST["txtnew"]
        loscata.save()
    except Catalogo.DoesNotExist:
        # Manejar el caso de un código no válido
        pass
    return redirect("catalogo")


def Borrarcatalogo(request, id_catalogo):
    try:
        loscata = Catalogo.objects.get(id_catalogo=id_catalogo)
        loscata.delete()
    except Catalogo.DoesNotExist:
        # Manejar el caso de un código no válido
        pass
    return redirect("catalogo")
