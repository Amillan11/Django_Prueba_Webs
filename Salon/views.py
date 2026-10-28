from django.shortcuts import render
from django.http import HttpResponse
from Salon.models import Dato 

# Create your views here.


def Temperatura(request):
    temperatura = Dato.objects.filter(nombre="Temp ambiente").first()
    return render(request, "temperatura.html", {"temperatura": temperatura})

def Luz(request):
    luz = Dato.objects.filter(nombre="Luz").first()
    return render(request, "salon.html", {"luz": luz})