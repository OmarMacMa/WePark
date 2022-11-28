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


class SegmentState(models.Model):
    parking_segment = models.CharField(max_length=1, primary_key=True)
    occupied = models.FloatField(default=0.0)   # Percentage of occupied slots

    def __str__(self):
        s = "Parking Segment: " + str(self.parking_segment) + \
            " Occupied: " + str(self.occupied) + "%"
        return s


class DeviceHistoric(models.Model):
    id_device = models.IntegerField()
    arrive_leave = models.BooleanField(default=False)
    hour_date = models.DateTimeField(default=timezone.now)
    #parking_segment = models.CharField(max_length=1)

    def __str__(self):
        s = "Device ID: " + str(self.id_device) + \
            " Arrive/Leave: " + str(self.arrive_leave) + \
            " Hour/Date: " + str(self.hour_date)
        return s