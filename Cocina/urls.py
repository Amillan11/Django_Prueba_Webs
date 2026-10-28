from django.urls import path
from Cocina import views

urlpatterns=[
    path('',views.ganas, name="vllvl"),
    path('atleti',views.ganas,name="kkk"),
    path('nadal',views.otra,name="nadal"),
    path('viejos',views.datos_viejos,name='datos_viejos')
    ]