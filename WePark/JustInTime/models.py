from django.db import models

# Create your models here.
class DeviceState(models.Model):
    id_device = models.IntegerField()
    slot_active = models.BooleanField(default=False)
    LED_state = models.BooleanField(default=False)
    id_slot = models.IntegerField()

    def __str__(self):
        s = str(self.id_device) + " " + \
            str(self.slot_active) + " " + \
            str(self.LED_state) + " " + \
            str(self.id_slot)
        return s


class DeviceHistoric(models.Model):
    id_device = models.IntegerField()
    fecha = models.DateTimeField()