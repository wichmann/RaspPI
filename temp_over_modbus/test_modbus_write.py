
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

client = ModbusClient('192.168.24.40', port=502)
#client = ModbusClient(method='ascii', port='/dev/pts/2', timeout=1)
#client = ModbusClient(method='rtu', port='/dev/pts/2', timeout=1)
client.connect()

rr = client.write_register(0, 42)

