#! /usr/bin/env python3

# Notwendige Bibliothek installieren:
#     pip3 install paho-mqtt


import time
import random

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

# erzeuge Objekt für die Verbindung zum MQTT-Broker
mqttc = mqtt.Client()
# setze Funktionen für verschiedene Ereignisse
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# baue Verbindung zum Broker auf
mqttc.connect("192.168.24.129", port=1883, keepalive=120)

# abboniere ein Thema beim Broker
mqttc.subscribe(TOPIC, 0)

# starte einen Hintergrundprozess, der Daten vom Broker entgegen nimmt
mqttc.loop_start()

while True:
    print("Publishing data...")
    # veröffentliche eine neue Nachricht alle zwei Sekunden
    mqttc.publish(TOPIC, "Current number: {}".format(random.randint(0, 100)))
    time.sleep(2)

mqttc.loop_stop()
