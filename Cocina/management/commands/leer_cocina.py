from Cocina.models import Dato

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
        
            datos = client.mb_read(100, 4)

            m100_1 = float(util.get_bool(datos, 0,1))
            mw102 =util.get_dword(datos, 2)


            Lavadora,_= Dato.objects.get_or_create(nombre="TMarcha Lavadora")
            
            Lavadora.valor = m100_1
            Lavadora.fecha = timezone.now()
            Lavadora.save()

            temperatura,_=Dato.objects.get_or_create(nombre="Temp horno")
            
            temperatura.valor =mw102
            temperatura.Fecha = timezone.now()
            temperatura.save()

            time.sleep(20)