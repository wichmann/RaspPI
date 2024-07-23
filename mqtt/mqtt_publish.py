#! /usr/bin/env python3

"""
Einfaches Python-Skript um Nachrichten auf einem MQTT-Broker zu veröffentlichen.

Notwendige Bibliothek installieren:
 - pip3 install paho-mqtt

"""


import paho.mqtt.publish as publish


# veröffentliche eine neue Nachricht unter dem angegebenen Thema
publish.single('test/topic', 'Test-Nachricht', hostname='192.168.10.52')
