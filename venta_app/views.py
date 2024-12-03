from django.shortcuts import render,redirect
from .models import Ventas
# Create your views here.
#cambiar variables 
def inicio_venta(request):
    lasventas=Ventas.objects.all()
    
#cambiar los htmls
    return render(request,"gestionarVentas.html",{"lasventas":lasventas})
    
def registrarVentas(request):
    id_venta=request.POST["txtcod"]
    id_cliente = request.POST["numcliente"]
    id_empleado = request.POST["numemp"]
    id_producto = request.POST["numprodu"]
    factura = request.POST["numfact"]
    descuento = request.POST["numdesc"]
    fecha_venta = request.POST["numfecha"]
    pago = request.POST["numpago"]
    iva = request.POST["numiva"]
    
#cambiar los redirect por variable de inicio
    guardarventas=Ventas.objects.create(id_venta=id_venta,id_cliente=id_cliente,id_empleado=id_empleado,id_producto=id_producto,factura=factura,descuento=descuento,fecha_venta=fecha_venta,pago=pago,iva=iva)
    
    return redirect("venta")

def SeleccionarVentas(request,id_venta):
    lasventas=Ventas.objects.get(id_venta=id_venta)
    return render(request,"editarventa.html",{"lasventas":lasventas})
    
def editarVentas(request):
    id_venta = request.POST["txtcod"]
    try:
        lasventas = Ventas.objects.get(id_venta=id_venta)
        lasventas.id_cliente = request.POST["numcliente"]
        lasventas.id_empleado = request.POST["numemp"]
        lasventas.id_producto = request.POST["numprodu"]
        lasventas.factura = request.POST["numfact"]
        lasventas.descuento = request.POST["numdesc"]
        lasventas.fecha_venta = request.POST["numfecha"]
        lasventas.pago = request.POST["numpago"]
        lasventas.iva = request.POST["numiva"]
        lasventas.save()
    except Ventas.DoesNotExist:
        # Manejar el caso de un código no válido
        pass
    return redirect("venta")



def BorrarVentas(request, id_venta):
    try:
        lasventas = Ventas.objects.get(id_venta=id_venta)
        lasventas.delete()
    except Ventas.DoesNotExist:
        # Manejar el caso de un código no válido
        pass
    return redirect("venta")
