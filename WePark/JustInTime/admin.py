from django.contrib import admin
from .models import DeviceState, SegmentState, DeviceHistoric

# Register your models here.
admin.site.register(DeviceState)
admin.site.register(SegmentState)
admin.site.register(DeviceHistoric)