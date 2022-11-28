from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'JustInTime'

urlpatterns = [
    path('index', views.index, name='index'),
    path("datosProyecto", views.datosProyecto, name="datosProyecto"),
    path("estadistic", views.estadistic, name="estadistic"),
    path("record/<int:id_device>/<int:slot_state>", views.record, name="record"),
    # path("record/<int:id_device>/<int:slot_state>/<str:parking_segment>", views.record, name="record"),
]

