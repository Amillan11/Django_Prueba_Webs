from django.urls import path
from Salon import views

urlpatterns=[
    path('Temperatura',views.Temperatura, name="Temperatura"),
    path('Luz',views.Luz,name="Temperatura"),
    ]