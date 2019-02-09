#! /usr/bin/env python3

# Notwendige Bibliothek installieren:
#     sudo apt install python3-flask
# oder
#     pip3 install flask

from flask import Flask
from flask import request


# initialisiere Flask server
app = Flask(__name__)

# HTML-Formular
formular = """
           <html>
           <body>
           <form action="/formular" method="GET">
             <input type="text" name="name" />
             <input type="submit" value="Absenden" />
           </form>
           <p>Hallo {wert}.</p>
           </body>
           </html>
           """

@app.route('/')
def hauptseite():
    # schicke HTML-Seite ohne einen eingefügten String zurück
    return formular.format(wert='')

@app.route('/formular', methods=['GET', 'POST'])
def verarbeite_formular():
    if request.method == 'POST':
        # hole Parameter aus POST-Request und füge Parameter in HTML-Seite ein
        parameter = request.form.get('name')
        print('Übergebener Parameter (POST): {}'.format(parameter))
        return formular.format(wert=parameter)
    elif request.method == 'GET':
        # hole Parameter aus GET-Request und füge Parameter in HTML-Seite ein
        parameter = request.args.get('name')
        print('Übergebener Parameter (GET): {}'.format(parameter))
        return formular.format(wert=parameter)

if __name__ == '__main__':
    # starte Flask-Server im Debug-Modus
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
