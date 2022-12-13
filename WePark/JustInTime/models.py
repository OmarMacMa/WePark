from django.db import models
from django.utils import timezone


# DeviceState model a representation of the state of a parking space device.
class DeviceState(models.Model):
    """
    A model representing the state of a parking space device.
    
    Attributes:
        id_device (int): The unique ID of the device.
        slot_state (bool): The current state of the parking space (occupied or not occupied).
        parking_segment (str): The ID of the parking segment the device belongs to.
    """
    id_device = models.IntegerField(primary_key=True)
    slot_state = models.BooleanField(default=False)
    parking_segment = models.CharField(max_length=1)


# SegmentState model a representation of the state of a parking segment.
class SegmentState(models.Model):
    """
    A model representing the state of a parking segment.
    
    This class defines a model that represents the current state of a parking segment.
    Attributes:
        parking_segment (str): The ID of the parking segment.
        occupied (float): The percentage of occupied parking spaces in the segment.
    """
    parking_segment = models.CharField(max_length=1, primary_key=True)
    occupied = models.FloatField(default=0.0)


# DeviceHistoric model a representation of the historic of a parking space device.
class DeviceHistoric(models.Model):
    """
    A model representing the historic of a parking space device.

    Attributes:
        id_device (int): The unique ID of the device.
        arrive_leave (bool): The state of the parking space (occupied or not occupied).
        hour_date (datetime): The date and time of the event.
        parking_segment (str): The ID of the parking segment the device belongs to.
    """
    id = models.AutoField(primary_key=True, default=None)
    id_device = models.IntegerField(default=100)
    arrive_leave = models.BooleanField(default=False)
    hour_date = models.DateTimeField(default=timezone.now)
    parking_segment = models.CharField(max_length=1, default="A")
