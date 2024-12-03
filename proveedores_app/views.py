from django.shortcuts import render,redirect
from .models import Proveedor
# Create your views here.
#cambiar variables a proveedor
def inicio_proveedores(request):
    losprove=Proveedor.objects.all()
    
#cambiar los htmls
    return render(request,"gestionarProveedores.html",{"losprove":losprove})
    
def registrarProveedor(request):
    codigo=request.POST["txtcod"]
    nombre = request.POST["txtnombre"]
    productos = request.POST["txtprodu"]
    ciudad = request.POST["txtciudad"]
    distribucion= request.POST["txtdest"]
    p_mayoreo = request.POST["nummayor"]
    certificado= request.POST["txtcerti"]
    
#cambiar los redirect por variable de inicio
    guardarproveedor=Proveedor.objects.create(codigo=codigo,nombre=nombre,productos=productos,ciudad=ciudad,distribucion=distribucion,p_mayoreo=p_mayoreo,certificado=certificado)
    return redirect("proveedor")

def SeleccionarProveedor(request,codigo):
    losprove=Proveedor.objects.get(codigo=codigo)
    return render(request,"editarprov.html",{"losprove":losprove})
    
def editarProveedor(request):
    codigo = request.POST["txtcod"]
    try:
        losprove = Proveedor.objects.get(codigo=codigo)
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


def BorrarProveedor(request, codigo):
    try:
        losprove = Proveedor.objects.get(codigo=codigo)
        losprove.delete()
    except Proveedor.DoesNotExist:
        # Manejar el caso de un código no válido
        pass
    return redirect("proveedor")
