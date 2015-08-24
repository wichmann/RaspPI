
import thread
import logging
import BaseHTTPServer

from pymodbus.server.async import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSparseDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer, ModbusAsciiFramer

#from multiprocessing import Queue, Process


logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)


# global variable to communicate between threads
CURRENT_TEMP = 0.0


class TempHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        global CURRENT_TEMP
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        with open('temperatur.html') as html_file: 
            s.wfile.write(html_file.read().format(temperatur=str(CURRENT_TEMP)))


def run_http_server(port=8000):
    import SocketServer
    httpd = BaseHTTPServer.HTTPServer(("", port), TempHandler)
    print "serving at port", port
    httpd.serve_forever()

thread.start_new_thread(run_http_server, ())


class OutputCallbackDataBlock(ModbusSparseDataBlock):
    '''
    Outputs incoming data...
    '''
    def __init__(self, values):
        super(OutputCallbackDataBlock, self).__init__(values)

    def setValues(self, address, value):
        global CURRENT_TEMP
        print(CURRENT_TEMP, address, value)
        super(OutputCallbackDataBlock, self).setValues(address, value)
        if address == 1:
            CURRENT_TEMP = float(value[0]) / 10
            print('Value: {value}'.format(value=value))


block   = OutputCallbackDataBlock([0] * 10)
store   = ModbusSlaveContext(di=block, co=block, hr=block, ir=block)
context = ModbusServerContext(slaves=store, single=True)

identity = ModbusDeviceIdentification()
identity.VendorName  = 'pymodbus'
identity.ProductCode = 'PM'
identity.VendorUrl   = 'http://github.com/bashwork/pymodbus/'
identity.ProductName = 'pymodbus Server'
identity.ModelName   = 'pymodbus Server'
identity.MajorMinorRevision = '1.0'

StartTcpServer(context, identity=identity) # , address=('192.168.24.40', 503))
