from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import Clientes
# Create your views here.
#cambiar variables 
def inicio_cliente(request):
    losclientes=Clientes.objects.all()
    
#cambiar los htmls
    return render(request,"gestionarClientes.html",{"losclientes":losclientes})
    
def registrarCliente(request):
    codigo=request.POST["txtcod"]
    nombre = request.POST["txtnombre"]
    numero = request.POST["numcel"]
    ciudad = request.POST["txtciudad"]
    numCuenta = request.POST["numcuenta"]
    direccion = request.POST["txtdire"]
    
#cambiar los redirect por variable de inicio CAMBIAR VARIABLES ARRIBA 
    guardarclientes=Clientes.objects.create(codigo=codigo,nombre=nombre,numero=numero,ciudad=ciudad,numCuenta=numCuenta,direccion=direccion)
    return redirect("clientes")

def SeleccionarCliente(request,codigo):
    losclientes=Clientes.objects.get(codigo=codigo)
    return render(request,"editarclientes.html",{"losclientes":losclientes})
    
def editarCliente(request):
    codigo = request.POST["txtcod"]
    try:
        losclientes = Clientes.objects.get(codigo=codigo)
        losclientes.nombre = request.POST["txtnombre"]
        losclientes.numero = request.POST["numcel"]
        losclientes.ciudad = request.POST["txtciudad"]
        losclientes.numCuenta = request.POST["numcuenta"]
        losclientes.direccion = request.POST["txtdire"]
        losclientes.save()
    except Clientes.DoesNotExist:
        # Manejar el caso de un código no válido
        pass
    return redirect("clientes")


def BorrarClientes(request, codigo):
    try:
        losclientes = Clientes.objects.get(codigo=codigo)
        losclientes.delete()
    except Clientes.DoesNotExist:
        # Manejar el caso de un código no válido
        pass
    return redirect("clientes")
