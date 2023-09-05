
"""
Einfacher OPC UA-Client

Notwendige Bibliothek installieren:

    apt-get install python3-lxml
    pip3 install opcua 

Für den Zugriff auf Variablen wird die OPC UA Notation genutzt:

    ns=<namespaceIndex>;<identifiertype>=<identifier>
    
    <namespace index> -> namespace index
    <identifier type> -> flag that specifies the identifier type:
                         Flag	Identifier Type
                         i	    NUMERIC (UInteger)
                         s	    STRING (String)
                         g	    GUID (Guid)
                         b	    OPAQUE (ByteString)

Quelle: http://documentation.unified-automation.com/uasdkhp/1.0.0/html/_l2_ua_node_ids.html

"""

from time import sleep
from opcua import Client


client = Client("opc.tcp://192.168.24.190:4840")
# client.set_security_string("Basic256,SignAndEncrypt,certificate.pem,privatekey.pem")

# setze Benutzername und Passwort
client.set_user('admin')
client.set_password('wago')

try:
    client.connect()

    # greife auf Elemente im Baum zu
    root = client.get_root_node()
    objects = client.get_objects_node()
    app = objects.get_child(["2:DeviceSet", "4:WAGO 750-8102 PFC100 2ETH RS", "4:Resources", "4:Application"])

    # erzeuge Objekte für Knoten aus dem Baum über OPC UA Notation
    eingang1 = client.get_node('ns=4;s=|var|CODESYS Control for Raspberry Pi SL.Application.PLC_PRG.eingang1')
    eingang2 = client.get_node('ns=4;s=|var|CODESYS Control for Raspberry Pi SL.Application.PLC_PRG.eingang2')
    ausgang = client.get_node('ns=4;s=|var|CODESYS Control for Raspberry Pi SL.Application.PLC_PRG.ausgang')

    # OPC-Variablen besitzen vier Attribute: Datentyp, Wert, Status, Zeitstempel
    data = ausgang.get_data_value()
    print('************ Variable: Ausgang ************')
    print('Datentyp:    ', data.Value.VariantType)
    print('Wert:        ', data.Value.Value)
    print('Status:      ', data.StatusCode)
    print('Zeitstempel: ', data.SourceTimestamp)
    print('*******************************************')

    # Variable ausgang auslesen
    print('Wert der Variable "ausgang": ', ausgang.get_value())

    # Variablen eingang1 und eingang2 schreiben
    print('Setzen beider Eingänge auf True!')
    eingang1.set_value(True)
    eingang2.set_value(True)
    sleep(1.0)

    # Variable ausgang auslesen
    print('Wert der Variable "ausgang": ', ausgang.get_value())

    # Variablen eingang1 und eingang2 schreiben
    print('Setzen eines Eingangs auf False!')
    eingang2.set_value(False)
    sleep(1.0)

    # Variable ausgang auslesen
    print('Wert der Variable "ausgang": ', ausgang.get_value())

finally:
    client.disconnect()
