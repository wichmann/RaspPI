import pifacedigitalio as p
from flask import Flask


# initialisiere PiFace
p.init()

# initialisiere Flask server
app = Flask(__name__)


@app.route('/')
def info():
    return 'PiFace HTTP-Schnittstelle'

@app.route('/<name>')
def hello(name):
    return 'Hallo {}!'.format(name)

@app.route('/lampe1/ein')
def lampe1_ein():
    p.digital_write(0,1)
    return 'Lampe 1 ist AN.'

@app.route('/lampe1/aus')
def lampe1_aus():
    p.digital_write(0,0)
    return 'Lampe 1 ist AUS.'

@app.route('/eingang/<int:eingang>')
def eingang_auslesen(eingang):
    wert = p.digital_read(eingang)
    if wert:
       return 'Eingang ist: EIN.'
    else:
       return 'Eingang ist: AUS.'

if __name__ == '__main__':
    # starte Flask-Server im Debug-Modus
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
