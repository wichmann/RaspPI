#! /usr/bin/env python3

# Notwendige Bibliothek installieren:
#     sudo apt install python3-flask
# oder
#     pip3 install flask

import time
import threading

from flask import Flask
from flask import request


# TODO: Bibliothek zur Ansteuerung des PiFace importieren und PiFace initialisieren

# initialisiere Flask server
app = Flask(__name__)

# globale Variable zur Speicherung der aktuellen Lauflicht-Geschwindigkeit
aktuelle_geschwindigkeit = 100

# HTML-Formular
formular = """
           <html>
           <body>
           <h1>Lauflicht mit dem PiFace</h1>
           <form action="/lauflicht" method="POST">
             <p><input type="number" name="geschwindigkeit" value="{geschwindigkeit}" /> Geschwindigkeit </p>
             <p><input type="submit" value="Absenden" /></p>
           </form>
           </body>
           </html>
           """

@app.route('/lauflicht', methods=['GET', 'POST'])
def lauflicht_html():
    global aktuelle_geschwindigkeit
    if request.method == 'POST':
        aktuelle_geschwindigkeit = int(request.form['geschwindigkeit'])
        print('Geschwindigkeit geändert zu: {}'.format(aktuelle_geschwindigkeit))
        return formular.format(geschwindigkeit=aktuelle_geschwindigkeit)
    else:
        return formular.format(geschwindigkeit=aktuelle_geschwindigkeit)

def lauflicht_steuerung():
    global aktuelle_geschwindigkeit
    aktuelle_Ausgabe = 0x01
    while True:
        # TODO: Schreibe aktuellen Wert auf Ausgang
        print('laufe mit Geschwindigkeit {}'.format(aktuelle_geschwindigkeit))
        time.sleep(aktuelle_geschwindigkeit / 100.)

if __name__ == '__main__':
    # starte Hintergrund-Thread für das Lauflicht
    thread = threading.Thread(target=lauflicht_steuerung, args=())
    thread.daemon = True
    thread.start()
    # starte Web-Server zur Steuerung des Lauflichts
    app.run(host= '0.0.0.0', port=5000, debug=True, use_reloader=False)
