from django.shortcuts import render,redirect
from .models import Productos
# Create your views here.
#cambiar variables 
def inicio_producto(request):
    losprodu=Productos.objects.all()
    
#cambiar los htmls
    return render(request,"gestionarProductos.html",{"losprodu":losprodu})
    
def registrarProducto(request):
    id_producto = request.POST["txtcod"]
    nombre = request.POST["txtnombre"]
    costo = request.POST["numcosto"]
    descripcion = request.POST["txtdescri"]
    instrucciones = request.POST["txtinstru"]
    ingredientes = request.POST["txtingre"]
    caducidad = request.POST["numcadu"]
    id_proveedor = request.POST["txtprov"]

    
#cambiar los redirect por variable de inicio
    guardarproductos=Productos.objects.create(id_producto=id_producto,nombre=nombre,costo=costo,descripcion=descripcion,ingredientes=ingredientes,instrucciones=instrucciones,caducidad=caducidad,id_proveedor=id_proveedor)
    return redirect("productos")

def SeleccionarProducto(request,id_producto):
    losprodu=Productos.objects.get(id_producto=id_producto)
    return render(request,"editarprodu.html",{"losprodu":losprodu})
    
def editarProducto(request):
    id_producto = request.POST["txtcod"]
    try:
        losprodu = Productos.objects.get(id_producto=id_producto)
        losprodu.nombre = request.POST["txtnombre"]
        losprodu.costo = request.POST["numcosto"]
        losprodu.descripcion = request.POST["txtdescri"]
        losprodu.instrucciones = request.POST["txtinstru"]
        losprodu.ingredientes = request.POST["txtingre"]
        losprodu.caducidad = request.POST["numcadu"]
        losprodu.id_proveedor=request.POST["txtprov"]

        losprodu.save()
    except Productos.DoesNotExist:
        # Manejar el caso de un código no válido
        pass
    return redirect("productos")


def BorrarProducto(request, id_producto):
    try:
        losprodu = Productos.objects.get(id_producto=id_producto)
        losprodu.delete()
    except Productos.DoesNotExist:
        # Manejar el caso de un código no válido
        pass
    return redirect("productos")