#! /usr/bin/env python3

# Notwendige Bibliothek installieren:
#     pip3 install paho-mqtt


import paho.mqtt.publish as publish


publish.single("test/topic", "nachricht", hostname="192.168.24.132") # test.mosquitto.org

