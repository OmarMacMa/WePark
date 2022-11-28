from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse
from .models import DeviceState, SegmentState, DeviceHistoric
from django.conf import settings


def index(request):
    percentage_A = SegmentState.objects.get(pk="A").occupied
    percentage_B = SegmentState.objects.get(pk="B").occupied
    percentage_C = SegmentState.objects.get(pk="C").occupied
    percentage_D = SegmentState.objects.get(pk="D").occupied
    percentage_E = SegmentState.objects.get(pk="E").occupied
    percentage_F = SegmentState.objects.get(pk="F").occupied
    percentage_G = SegmentState.objects.get(pk="G").occupied
    percentage_H = SegmentState.objects.get(pk="H").occupied
    percentage_I = SegmentState.objects.get(pk="I").occupied
    return render(request, 'JustInTime/index.html', {
        'percentage_A': percentage_A,
        'percentage_B': percentage_B,
        'percentage_C': percentage_C,
        'percentage_D': percentage_D,
        'percentage_E': percentage_E,
        'percentage_F': percentage_F,
        'percentage_G': percentage_G,
        'percentage_H': percentage_H,
        'percentage_I': percentage_I,
        "GOOGLE_MAPS_API_KEY": settings.GOOGLE_MAPS_API_KEY,
    })


def Iframe_prueba(request):
    return render(request, 'JustInTime/Iframe_prueba.html')


def datosProyecto(request):
    return render(request, 'JustInTime/datosProyecto.html')


def estadistic(request):
    return render(request, 'JustInTime/estadistic.html')


def record(request, id_device, slot_state):
    # Aqui se hace el guardado de los datos en la base de datos

    if slot_state == 1:
        slot_state = True
    else:
        slot_state = False
    parking_segment = DeviceState.objects.get(id_device=id_device).parking_segment
    device, created = DeviceState.objects.get_or_create(id_device=id_device)
    device.slot_state = slot_state
    device.parking_segment = parking_segment
    device.save()
    DeviceHistoric.objects.create(id_device=id_device, arrive_leave=slot_state, hour_date=timezone.now())
    total = DeviceState.objects.filter(parking_segment=parking_segment).count()
    active = DeviceState.objects.filter(
        parking_segment=parking_segment, slot_state=True).count()
    segment, created = SegmentState.objects.get_or_create(
        parking_segment=parking_segment)
    segment.occupied = active/total*100
    segment.save()

    # DeviceState.objects.get(id_device=id_device).update_(
    #     slot_state=slot_state, parking_segment=parking_segment)
    # From DeviceHistoric get the last record of the device and check if the slot_state is the same
    ##if device.slot_state != device.state_historic.last().arrive_leave:
    ##    device.state_historic.create(arrive_leave=slot_state, hour_date=timezone.now())
    # if DeviceHistoric.objects.filter(id_device=id_device).last().arrive_leave != slot_state:
    #     DeviceHistoric.objects.create(
    #         id_device=id_device, arrive_leave=slot_state, hour_date=timezone.now())
    # Update the occupied percentage of the segment
    """## total = DeviceState.objects.filter(parking_segment=parking_segment).count()
    ## active = DeviceState.objects.filter(
    ##     parking_segment=parking_segment, slot_state=True).count()
    ## SegmentState.objects.get(parking_segment=parking_segment).update(
    ##     occupied=(active/total*100).round(2))"""
    
    """device = DeviceState.objects.get_or_create(id_device=id_device)
    if slot_state == 1:
        device.update(slot_state=True, parking_segment=parking_segment)
    else:
        device.update(slot_state=False, parking_segment=parking_segment)
    # From DeviceHistoric get the last record of the device and check if the slot_state is the same
    if device.slot_state != device.state_historic.last().arrive_leave:
        device.state_historic.create(arrive_leave=slot_state, hour_date=timezone.now())
    # Update the occupied percentage of the segment
    total = device.state_historic.filter(parking_segment=parking_segment).count()
    active = device.state_historic.filter(parking_segment=parking_segment, arrive_leave=True).count()
    device.state_segment.update(occupied=(active/total*100).round(2))
    device.save()"""

    return HttpResponse("OK")
