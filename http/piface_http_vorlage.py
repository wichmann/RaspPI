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
           <h1>PiFace-Ausgänge</h1>
           <form action="/ausgang" method="GET">
             Ausgang: <input type="text" name="ausgang" value="{ausgang}"><br>
             <input type="radio" name="zustand" value="ein" {checked_ein}> Ein<br></input>
             <input type="radio" name="zustand" value="aus" {checked_aus}> Aus<br></input>
             <input type="submit" value="Absenden" />
           </form>
           </body>
           </html>
           """

@app.route('/')
def info():
    return 'Informationsseite'

@app.route('/ausgang', methods=['GET', 'POST'])
def ausgang():
    if request.method == 'GET':
        # lese Argumente aus dem GET-Request aus
        ausgang = request.args.get('ausgang')
        print('Gewählter Ausgang: {}'.format(ausgang))
        if ausgang:
            ausgang = int(ausgang)
        if request.args.get('zustand') == 'ein':
            return formular.format(checked_ein='checked', checked_aus='', ausgang=request.args.get('ausgang'))
        elif request.args.get('zustand') == 'aus':
            return formular.format(checked_ein='', checked_aus='checked', ausgang=request.args.get('ausgang'))
        else:
            return formular.format(checked_ein='checked', checked_aus='', ausgang='1')
    elif request.method == 'POST':
        # lese Parameter aus dem übergebenen Formular aus
        ausgang = request.form.get('ausgang')
        print('Gewählter Ausgang: {}'.format(ausgang))
        if ausgang:
            ausgang = int(ausgang)
        if request.form.get('zustand') == 'ein':
            return formular.format(checked_ein='checked', checked_aus='', ausgang=request.form.get('ausgang'))
        elif request.form.get('zustand') == 'aus':
            return formular.format(checked_ein='', checked_aus='checked', ausgang=request.form.get('ausgang'))
        else:
            return formular.format(checked_ein='checked', checked_aus='', ausgang='1')

if __name__ == '__main__':
    app.debug = True
    app.run(host= '0.0.0.0')
