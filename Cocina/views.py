from django.shortcuts import render
from django.http import HttpResponse
from .models import Dato
from django.utils import timezone
import datetime

# Create your views here.
def ganas(request):
    return render(request, "cocina.html")

def otra(request):
    return HttpResponse("VAMOSSSS")


def datos_viejos(request):

    ## greater than
    ## lower than
    ## lower than or equal
    ahora = datetime.datetime.now()
    ayer = ahora - datetime.timedelta(days=1)
    datos = Dato.objects.filter(Fecha__lte=ayer)
    nombre="Millan"
    return render(request, "viejo.html",{"dt":datos, "name":nombre})

def probando(request):
    return render(request, "probando.html", {"name":"Millan"})


