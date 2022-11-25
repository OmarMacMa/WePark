from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'JustInTime'

urlpatterns = [
    path('index', views.index, name='index'),
    path("datosProyecto", views.datosProyecto, name="datosProyecto"),
    path("estadistic", views.estadistic, name="estadistic"),
    path("Iframe_prueba", TemplateView.as_view(template_name="JustInTime/Iframe_prueba.html"), name="Iframe_prueba"),
    #path(r"^Iframe_prueba/", TemplateView.as_view(template_name="JustInTime/Iframe_prueba.html"), name="Iframe_prueba"),
]

"""Generar una url que reciba "id_device/estado/segment" con eso se hace un
datetime.now() y se actualiza en la tabla DeviceState y se crea un
registro en la tabla DeviceHistoric
En dichas tablas se debe escribir todas las variables en ambas tablas,
mediante python con un script de SQL o mediante Django de la siguiente 
manera siempre y cuando ya esten creaos los devices y los segmentos
DeviceState.objects.get(id_device=id_device).update(slot_state=estado)
DeviceHistoric.objects.create(id_device=id_device, arrive_leave=estado, fecha=datetime.now())
SegmentState.objects.get(parking_segment=segment).update(occupied=sum(estado)/count(estado)*100))"""

