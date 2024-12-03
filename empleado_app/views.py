from django.shortcuts import render,redirect
from .models import Empleado
# Create your views here.

def inicio_empleado(request):
    loscoordis=Empleado.objects.all()

    return render(request,"gestionarCoordinador.html",{"loscoordis":loscoordis})
    
def registrarCoordi(request):
    codigo=request.POST["txtcod"]
    nombre=request.POST["txtnombre"]
    numero=request.POST["numnumero"]
    puesto=request.POST["txtpuesto"]
    direccion=request.POST["txtdire"]
    email=request.POST["txtemail"]
    sueldo=request.POST["numsueldo"]
    fecha_ing=request.POST["numfecha"]


    guardarcoordi=Empleado.objects.create(codigo=codigo,nombre=nombre,numero=numero,puesto=puesto,direccion=direccion,email=email,sueldo=sueldo,fecha_ing=fecha_ing)
    return redirect("empleado")

def SeleccionarCoordi(request,codigo):
    infcoor=Empleado.objects.get(codigo=codigo)
    return render(request,"editarcoordi.html",{"loscoordis":infcoor})
    
def editarCoordi(request):
    codigo = request.POST["txtcod"]
    try:
        infcoor = Empleado.objects.get(codigo=codigo)
        infcoor.nombre = request.POST["txtnombre"]
        infcoor.numero = request.POST["numnumero"]
        infcoor.puesto = request.POST["txtpuesto"]
        infcoor.direccion = request.POST["txtdire"]
        infcoor.email = request.POST["txtemail"]
        infcoor.sueldo = request.POST["numsueldo"]
        infcoor.fecha_ing = request.POST["numfecha"]
        infcoor.save()
    except Empleado.DoesNotExist:
        # Manejar el caso de un código no válido
        pass
    return redirect("empleado")


def BorrarCoordi(request, codigo):
    try:
        infcoor = Empleado.objects.get(codigo=codigo)
        infcoor.delete()
    except Empleado.DoesNotExist:
        # Manejar el caso de un código no válido
        pass
    return redirect("empleado")
