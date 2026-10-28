from Salon.models import Dato

from django.core.management.base import BaseCommand
from s7 import Client 
from s7 import util
from django.utils import timezone
import time

class Command(BaseCommand):
    def handle(self, *args, **options):
        client = Client()
        client.connect("192.168.0.1")

        while True:
        
            datos = client.mb_read(100, 16)
            m100_2 = float(util.get_bool(datos, 0,2))
            md112 =util.get_dword(datos, 12)


            luces,_= Dato.objects.get_or_create(nombre="Luces encendidad")
            
            luces.valor = m100_2
            luces.fecha = timezone.now()
            luces.save()

            temperatura,_=Dato.objects.get_or_create(nombre="Temp ambiente")
            
            temperatura.valor =md112
            temperatura.Fecha = timezone.now()
            temperatura.save()

            time.sleep(60)