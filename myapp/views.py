from django.shortcuts import render,HttpResponse
import paho.mqtt.client as mqtt
from datetime import time
from time import sleep
# from .models import Mqtt
# Create your views here.
def home(request):
    return HttpResponse("working..")



# def mqtt_callback(request):
#     broker_address = "16.171.160.72"
#     broker_port = 1883
#     username = "BarifloLabs"
#     password = "Bfl@123"
#     topic = "topic1"

#     def on_connect(client, userdata, flags, rc):
#         if rc == 0:
#             print("Connected to broker")
#             client.subscribe(topic)
#         else:
#             print(f"Connection failed with code {rc}")

#     def on_message(client, userdata, message):
#         # print(f"Received message: {message.payload.decode()}")
#         payload = message.payload.decode()
#         print(f"Received message: {payload}")
        
#         # try:
#         #     Mqtt.objects.create(message=payload)
#         # except Exception as e:
#         #     print("Error saving to database",e)
        
        
#         # Save the received data to the database
#         data=Mqtt.objects.create(message=payload)
#         data.save()

#     client = mqtt.Client()
#     client.on_connect = on_connect
#     client.on_message = on_message

#     client.username_pw_set(username, password)
#     client.connect(broker_address, broker_port)

#     try:
#         client.loop_forever()
#     except KeyboardInterrupt:
#         print("Disconnecting...")
#         client.disconnect()

    

#     return render(request,'mqtt_callback.html')