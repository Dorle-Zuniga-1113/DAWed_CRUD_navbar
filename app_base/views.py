from django.shortcuts import render

# Create your views here.
def inicio(request):
    #inicio de cosmeticos
    return render(request,'index.html')