from django.shortcuts import render,redirect
from .models import Proveedor
# Create your views here.
#cambiar variables a proveedor
def inicio_proveedores(request):
    losprove=Proveedor.objects.all()
    
#cambiar los htmls
    return render(request,"gestionarProveedores.html",{"losprove":losprove})
    
def registrarProveedor(request):
    id_proveedor=request.POST["txtcod"]
    nombre = request.POST["txtnombre"]
    productos = request.POST["txtprodu"]
    ciudad = request.POST["txtciudad"]
    distribucion= request.POST["txtdest"]
    p_mayoreo = request.POST["nummayor"]
    certificado= request.POST["txtcerti"]
    
#cambiar los redirect por variable de inicio
    guardarproveedor=Proveedor.objects.create(id_proveedor=id_proveedor,nombre=nombre,productos=productos,ciudad=ciudad,distribucion=distribucion,p_mayoreo=p_mayoreo,certificado=certificado)
    return redirect("proveedor")

def SeleccionarProveedor(request,id_proveedor):
    losprove=Proveedor.objects.get(id_proveedor=id_proveedor)
    return render(request,"editarprov.html",{"losprove":losprove})
    
def editarProveedor(request):
    id_proveedor = request.POST["txtcod"]
    try:
        losprove = Proveedor.objects.get(id_proveedor=id_proveedor)
        losprove.nombre = request.POST["txtnombre"]
        losprove.productos = request.POST["txtprodu"]
        losprove.ciudad = request.POST["txtciudad"]
        losprove.distribucion= request.POST["txtdest"]
        losprove.p_mayoreo = request.POST["nummayor"]
        losprove.certificado= request.POST["txtcerti"]
        losprove.save()
    except Proveedor.DoesNotExist:
        # Manejar el caso de un código no válido
        pass
    return redirect("proveedor")


def BorrarProveedor(request, id_proveedor):
    try:
        losprove = Proveedor.objects.get(id_proveedor=id_proveedor)
        losprove.delete()
    except Proveedor.DoesNotExist:
        # Manejar el caso de un código no válido
        pass
    return redirect("proveedor")
