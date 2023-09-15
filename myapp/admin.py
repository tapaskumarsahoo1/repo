from django.contrib import admin
from .models import Device,Parameter
# Register your models here.

@admin.register(Device)                      
class Device(admin.ModelAdmin):
    list_display = ['device_id']
    
# @admin.register(DataPoint)
# class DataPoint(admin.ModelAdmin):
#     list_display = ['timestamp']

@admin.register(Parameter)                                    
class Parameter(admin.ModelAdmin):
    list_display = ['param_type','param_value','date','time']
    
# class Mqttadmin(admin.ModelAdmin):
#     list_display = ['id','Device_id','Temprature','DO','pH','ORP','TDS','Time']

# @admin.register(DeviceParameter)
# class DeviceParameter(admin.ModelAdmin):
#     list_display = ['device_id','param_type','param_value','date','time']