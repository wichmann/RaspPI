
"""
Einfacher OPC UA-Client

Notwendige Bibliothek installieren:

    pip3 install opcua 

"""

from opcua import Client


client = Client("opc.tcp://opcua.demo-this.com:51210/UA/SampleServer")

try:
    client.connect()
    
    # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
    root = client.get_root_node()
    print("Objects node is: ", root)
    
    # Node objects have methods to read and write node attributes as well as browse or populate address space
    print("Children of root are: ", root.get_children())

    # get a specific node knowing its node id
    #var = client.get_node(ua.NodeId(1002, 2))
    #var = client.get_node("ns=3;i=2002")
    #print(var)
    #var.get_data_value() # get value of node as a DataValue object
    #var.get_value() # get value of node as a python builtin
    #var.set_value(ua.Variant([23], ua.VariantType.Int64)) #set node value using explicit data type
    #var.set_value(3.9) # set node value using implicit data type

    # Now getting a variable node using its browse path
    #myvar = root.get_child(["0:Objects", "2:MyObject", "2:MyVariable"])
    #obj = root.get_child(["0:Objects", "2:MyObject"])
    #print("myvar is: ", myvar)
finally:
    client.disconnect()
