#! /usr/bin/env python3

import time
import asyncio
import threading

from autobahn.asyncio.websocket import WebSocketServerProtocol, WebSocketServerFactory

import pifacedigitalio

# initialisiere PiFace
pfd = pifacedigitalio.PiFaceDigital()

# globale Variable zur Speicherung der aktuellen Lauflicht-Geschwindigkeit
aktuelle_geschwindigkeit = 100


class MyServerProtocol(WebSocketServerProtocol):
    verbindungen = [] # weakref.WeakSet() aus import weakref
    
    def onConnect(self, request):
        print("Client verbunden: {0}".format(request.peer))

    def onOpen(self):
        print("WebSocket-Verbindung geöffnet.")
        self.verbindungen.append(self)

    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Binary-Nachricht empfangen: {0} Bytes".format(len(payload)))
        else:
            global aktuelle_geschwindigkeit
            message = payload.decode('utf8')
            print("Text-Nachricht empfangen: {0}".format(message))
            aktuelle_geschwindigkeit = int(message)
        # schicke Nachricht als Antwort an Alle zurück
        for verbindung in self.verbindungen:
            verbindung.sendMessage(payload, isBinary)

    def onClose(self, wasClean, code, reason):
        print("WebSocket-Verbindung geschlossen: {0}".format(reason))
        if self in self.verbindungen:
            self.verbindungen.remove(self)


def lauflicht_steuerung():
    global aktuelle_geschwindigkeit
    aktuelle_Ausgabe = 0x01
    while True:
        # schiebe Ausgabebyte um eine Stelle nach links
        if aktuelle_Ausgabe >= 128:
            aktuelle_Ausgabe = 0x01
        else:
            aktuelle_Ausgabe = aktuelle_Ausgabe << 1
        # schreibe Ausgabebyte auf den Ausgang
        pfd.output_port.value = aktuelle_Ausgabe
        print('laufe... {}'.format(aktuelle_Ausgabe))
        time.sleep(aktuelle_geschwindigkeit / 100.)


def start_server(host='127.0.0.1', port=9000):
    address = 'ws://' + host + ':' + str(port)
    factory = WebSocketServerFactory(address)
    factory.protocol = MyServerProtocol

    loop = asyncio.get_event_loop()
    coro = loop.create_server(factory, '0.0.0.0', port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
        loop.close()


if __name__ == '__main__':
    # Starte Hintergrund-Thread für das Lauflicht
    thread = threading.Thread(target=lauflicht_steuerung, args=(), daemon=True)
    thread.start()
    # Starte Web-Server zur Steuerung des Lauflichts
    start_server(host='127.0.0.1', port=9000)

