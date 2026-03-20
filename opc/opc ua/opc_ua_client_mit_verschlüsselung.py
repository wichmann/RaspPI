
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


from opcua import Client


client = Client("opc.tcp://192.168.24.190:4840")
client.set_security_string("Basic256Sha256,SignAndEncrypt,certificate.der,privatekey.pem")
client.application_uri = 'urn:r324-01:foobar:myselfsignedclient' # kommt aus dem Zertifikat 'certificate.der'
client.set_user('admin')
client.set_password('wago')

try:
    client.connect()

    # greife auf Elemente im Baum zu
    root = client.get_root_node()
    objects = client.get_objects_node()
    ausgang = client.get_node('ns=4;s=|var|CODESYS Control for Raspberry Pi 64 SL.Application.PLC_PRG.ausgang')

    # OPC-Variablen besitzen vier Attribute: Datentyp, Wert, Status, Zeitstempel
    data = ausgang.get_data_value()
    print('************ Variable: Ausgang ************')
    print('Datentyp:    ', data.Value.VariantType)
    print('Wert:        ', data.Value.Value)
    print('Status:      ', data.StatusCode)
    print('Zeitstempel: ', data.SourceTimestamp)
    print('*******************************************')

finally:
    client.disconnect()
