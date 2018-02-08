
"""
Einfacher OPC DA-Client

Dokumentation für OpenOPC: http://openopc.sourceforge.net/api.html

Installation:
 * Python 2.7 (Windows 32bit)
 * pywin32 (https://github.com/mhammond/pywin32/releases)
 * pyro3 (https://pypi.python.org/pypi/Pyro)
 * OpenOPC (http://sourceforge.net/projects/openopc/files/openopc/1.3.1/)

"""

import OpenOPC


opc = OpenOPC.client()

print('Liste aller OPC Server:')
for server in opc.servers():
    print(' * ' + server)

print('Verbinde mit Codesys OPC DA Server...')
opc.connect('Softing.OPCToolboxDemo_ServerDA.1')

print('Liste aller SPSen:')
for sps in opc.list():
    print(' * ' + sps)

print('Lese Wert aus SPS:')
result = opc.read('time.local.second')
print(result)
