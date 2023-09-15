from django.db import models
from django.utils import timezone


class Device(models.Model):
    device_id = models.BigIntegerField()

class Parameter(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    param_type = models.CharField(max_length=100)
    param_value = models.JSONField()
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    
# class DeviceParameter(models.Model):
#     device_id = models.BigIntegerField()
#     param_type = models.CharField(max_length=100)
#     param_value = models.JSONField()
#     date = models.DateField(default=timezone.now)
#     time = models.TimeField(default=timezone.now)