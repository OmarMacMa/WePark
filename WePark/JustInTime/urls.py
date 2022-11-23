from django.urls import path
from . import views


app_name = 'JustInTime'

urlpatterns = [
    path('', views.index, name='index'),
    path('Iframe/', views.Iframe, name='Iframe'),
]

"""Generar una url que reciba "id_device/estado/segment" con eso se hace un
datetime.now() y se actualiza en la tabla DeviceState y se crea un
registro en la tabla DeviceHistoric
En dichas tablas se debe escribir todas las variables en ambas tablas,
mediante python con un script de SQL o mediante Django de la siguiente manera
DeviceState.objects.create(id_device=1, slot_state=inp, parking_segment=inp)"""

