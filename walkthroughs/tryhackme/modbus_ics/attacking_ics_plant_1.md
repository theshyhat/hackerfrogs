# URL
https://tryhackme.com/room/attackingics1
# Concept
* interacting with the modbus protocol
* attacking ICS systems
# Method of solve
* we are given a number of Python scripts that are compatible with the `Pymodbus` module
* we can use this script, named `discovery.py`, can be used to return all of the values held in the systems registers in realtime:
```
#!/usr/bin/env python3

import sys
import time
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.exceptions import ConnectionException

ip = sys.argv[1]
client = ModbusClient(ip, port=502)
client.connect()
while True:
    rr = client.read_holding_registers(1, 16)
    print(rr.registers)
    time.sleep(1)
```
* the first thing we should do for any modbus service is determine which registers are associated with each of the sensors, actuators, and counters in the system
* 
## Q1 - Which is the function used to read holding registers in pymodbus library?
read_holding_registers
## Q2 - Which is the function used to write holding registers in pymodbus library?
write_register
## Q3 - How many phases can we observe?
3
## Q4 - How many sensors can we observe?
2
## Q5 - How many actuators can we observe?
3
## Q6 - Using the script discovery.py, how many registers can we count?
16
## Q7 - After the plant is started and a bottle is loaded, how many registers are continuously changing their values?
4
## Q8 - Which is the minimum observed value?
0
## Q9
1
## Q10 - Which registry is holding its value?
16
## Q11 - Which registries are set to 1 while the nozzle is filling a bottle?
16
## Q12 - Which registries are set to 1 while the roller is moving the bottles?
2 4
## Q13 - Which is the color of the water level sensor?
1 3
## Q14 - Which is the color of the bottle sensor?
red
## Q15 - If you observe the plant at the very beginning, which is the registry associated with the roller?
green
## Q16 - Based on the previous answer, which is the registry associated with the water level sensor?
3
## Q17 - Which is the registry associated with the nozzle?
1
