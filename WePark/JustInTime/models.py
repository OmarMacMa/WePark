from django.db import models
from django.utils import timezone

# Create your models here.
class DeviceState(models.Model):
    id_device = models.IntegerField(primary_key=True)
    slot_state = models.BooleanField(default=False)
    parking_segment = models.CharField(max_length=1)

    def __str__(self):
        s = "Device ID: " + str(self.id_device) + \
            " Slot State: " + str(self.slot_state) + \
            " Parking Segment: " + str(self.parking_segment)
        return s


class DeviceHistoric(models.Model):
    id_device = models.ForeignKey(DeviceState, related_name="state_historic", on_delete=models.CASCADE)
    arrive_leave = models.BooleanField(default=False)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        s = "Device ID: " + str(self.id_device) + \
            " Arrive/Leave: " + str(self.arrive_leave) + \
            " Fecha: " + str(self.fecha)
        return s
    

class SegmentState(models.Model):
    # parking_segment of DeviceState
    parking_segment = models.ForeignKey(DeviceState, related_name="state_segment", on_delete=models.CASCADE)
    occupied = models.FloatField(default=0.0)   # Percentage of occupied slots

    def __str__(self):
        s = "Parking Segment: " + str(self.parking_segment) + \
            " Occupied: " + str(self.occupied) + "%"
        return s
