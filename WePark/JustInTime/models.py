from django.db import models
from django.utils import timezone

# Create your models here.
class DeviceState(models.Model):
    id_device = models.IntegerField(primary_key=True)
    slot_active = models.BooleanField(default=False)
    LED_state = models.BooleanField(default=False)
    id_slot = models.IntegerField()
    parking_segment = models.CharField(max_length=1)

    def __str__(self):
        s = str(self.id_device) + ", " + \
            str(self.slot_active) + ", " + \
            str(self.LED_state) + ", " + \
            str(self.id_slot)
        return s


class DeviceHistoric(models.Model):
    id_device = models.ForeignKey(DeviceState, on_delete=models.CASCADE, related_name="state_historic")
    fecha = models.DateTimeField(default=timezone.now)
    id_slot = models.IntegerField()
    parking_segment = models.CharField(max_length=1)
    busy = models.BooleanField(default=False)

    def __str__(self):
        s = str(self.id_device) + ", " + \
            str(self.fecha) + ", " + \
            str(self.id_slot) + ", " + \
            str(self.parking_segment) + ", " + \
            str(self.busy)
        return s