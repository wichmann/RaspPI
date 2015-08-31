
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

client = ModbusClient('192.168.24.40', port=502)
#client = ModbusClient(method='ascii', port='/dev/pts/2', timeout=1)
#client = ModbusClient(method='rtu', port='/dev/pts/2', timeout=1)
client.connect()

rr = client.read_holding_registers(0, 30)
for r in rr.registers:
    print(r)

#print(rr.registers[0])
#print(rr.registers[1])
#print(rr.registers[2])
#print(rr.registers[3])

