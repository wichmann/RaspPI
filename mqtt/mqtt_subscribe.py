#! /usr/bin/env python3

# Notwendige Bibliothek installieren:
#     pip3 install paho-mqtt


import paho.mqtt.client as mqtt


TOPIC = "test/topic"


def on_connect(mqttc, obj, flags, rc):
    print("rc: "+str(rc))

def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)

# If you want to use a specific client id, use  mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
mqttc.connect("192.168.24.132", 1883, 60) # test.mosquitto.org
mqttc.subscribe(TOPIC, 0)

mqttc.loop_forever()
