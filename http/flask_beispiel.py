#! /usr/bin/env python3

# Notwendige Bibliothek installieren:
#     sudo apt install python3-flask
# oder
#     pip3 install flask

from flask import Flask


# initialisiere Flask-Server
app = Flask(__name__)


# definiere Route für Hauptseite
@app.route('/')
def index():
    # gebe Antwort an aufrufenden Client zurück
    return 'Hallo World!'


if __name__ == '__main__':
    # starte Flask-Server im Debug-Modus
    app.debug = True
    app.run(host= '0.0.0.0')
