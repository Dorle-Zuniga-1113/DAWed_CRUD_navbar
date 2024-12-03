from django.shortcuts import render,redirect
from .models import Catalogo
# Create your views here.
#cambiar variables 
def inicio_catalogo(request):
    loscata=Catalogo.objects.all()
    
#cambiar los htmls
    return render(request,"gestionarCatalogo.html",{"loscata":loscata})
    
def registrarCatalogo(request):
    codigo=request.POST["txtcod"]
    nombre = request.POST["txtnombre"]
    fecha_inicio = request.POST["numfechai"]
    fecha_fin  = request.POST["numfechaf"]
    promocion = request.POST["numprom"]
    coleccion = request.POST["txtcole"]
    novedad = request.POST["txtnew"]
    
#cambiar los redirect por variable de inicio
    guardarcatalogo=Catalogo.objects.create(codigo=codigo,nombre=nombre,fecha_inicio=fecha_inicio,fecha_fin=fecha_fin,promocion=promocion,coleccion=coleccion,novedad=novedad)
    return redirect("catalogo")

def SeleccionarCatalogo(request,codigo):
    loscata=Catalogo.objects.get(codigo=codigo)
    return render(request,"editarcata.html",{"loscata":loscata})
    
def editarCatalogo(request):
    codigo = request.POST["txtcod"]
    try:
        loscata = Catalogo.objects.get(codigo=codigo)
        loscata.nombre = request.POST["txtnombre"]
        loscata.fecha_inicio = request.POST["numfechai"]
        loscata.fecha_fin  = request.POST["numfechaf"]
        loscata.promocion = request.POST["numprom"]
        loscata.coleccion = request.POST["txtcole"]
        loscata.novedad = request.POST["txtnew"]
        loscata.save()
    except Catalogo.DoesNotExist:
        # Manejar el caso de un código no válido
        pass
    return redirect("catalogo")


def Borrarcatalogo(request, codigo):
    try:
        loscata = Catalogo.objects.get(codigo=codigo)
        loscata.delete()
    except Catalogo.DoesNotExist:
        # Manejar el caso de un código no válido
        pass
    return redirect("catalogo")
