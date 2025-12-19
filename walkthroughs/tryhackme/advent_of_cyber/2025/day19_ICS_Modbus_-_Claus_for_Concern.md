# URL
https://tryhackme.com/room/ICS-modbus-aoc2025-g3m6n9b1v4
# Concept
* industrial control systems (ICS)
* SCADA (Supervisory Control and Data Acquisition)
# Method of solve
## Q1 - What port is commonly used by Modbus TCP?
* look in the few lines above the question, and there is a port number there, which we can use as the answer
## Q2 - What's the flag?
* the materials provide us with a script to run on the system to restore the settings back to normal and receive the flag
* use the following script below, but we need to replace the IP address in the `PLC_IP` variable:
```
#!/usr/bin/env python3
from pymodbus.client import ModbusTcpClient
import time

PLC_IP = "<REPLACE_THIS>"
PORT = 502
UNIT_ID = 1

def read_coil(client, address):
    result = client.read_coils(address=address, count=1, slave=UNIT_ID)
    if not result.isError():
        return result.bits[0]
    return None

def read_register(client, address):
    result = client.read_holding_registers(address=address, count=1, slave=UNIT_ID)
    if not result.isError():
        return result.registers[0]
    return None

# Connect to PLC
client = ModbusTcpClient(PLC_IP, port=PORT)

if not client.connect():
    print("Failed to connect to PLC")
    exit(1)

print("=" * 60)
print("TBFC Drone System - Christmas Restoration")
print("=" * 60)
print()

# Step 1: Check current state
print("Step 1: Verifying current system state...")
time.sleep(1)

package_type = read_register(client, 0)
protection = read_coil(client, 11)
armed = read_coil(client, 15)

print(f"  Package Type: {package_type} (1 = Eggs)")
print(f"  Protection Active: {protection}")
print(f"  Self-Destruct Armed: {armed}")
print()

# Step 2: Disable protection
print("Step 2: Disabling protection mechanism...")
time.sleep(1)

result = client.write_coil(11, False, slave=UNIT_ID)
if not result.isError():
    print("  Protection DISABLED")
    print("  Safe to proceed with changes")
else:
    print("  FAILED to disable protection")
    client.close()
    exit(1)

print()
time.sleep(1)

# Step 3: Change package type to Christmas
print("Step 3: Setting package type to Christmas presents...")
time.sleep(1)

result = client.write_register(0, 0, slave=UNIT_ID)
if not result.isError():
    print("  Package type changed to: Christmas Presents")
else:
    print("  FAILED to change package type")

print()
time.sleep(1)

# Step 4: Enable inventory verification
print("Step 4: Enabling inventory verification...")
time.sleep(1)

result = client.write_coil(10, True, slave=UNIT_ID)
if not result.isError():
    print("  Inventory verification ENABLED")
else:
    print("  FAILED to enable verification")

print()
time.sleep(1)

# Step 5: Enable audit logging
print("Step 5: Enabling audit logging...")
time.sleep(1)

result = client.write_coil(13, True, slave=UNIT_ID)
if not result.isError():
    print("  Audit logging ENABLED")
    print("  Future changes will be logged")
else:
    print("  FAILED to enable logging")

print()
time.sleep(2)

# Step 6: Verify restoration
print("Step 6: Verifying system restoration...")
time.sleep(1)

christmas_restored = read_coil(client, 14)
new_package_type = read_register(client, 0)
emergency_dump = read_coil(client, 12)
self_destruct = read_coil(client, 15)

print(f"  Package Type: {new_package_type} (0 = Christmas)")
print(f"  Christmas Restored: {christmas_restored}")
print(f"  Emergency Dump: {emergency_dump}")
print(f"  Self-Destruct Armed: {self_destruct}")
print()

if christmas_restored and new_package_type == 0 and not emergency_dump and not self_destruct:
    print("=" * 60)
    print("SUCCESS - CHRISTMAS IS SAVED")
    print("=" * 60)
    print()
    print("Christmas deliveries have been restored")
    print("The drones will now deliver presents, not eggs")
    print("Check the CCTV feed to see the results")
    print()
    
    # Read the flag from registers
    flag_result = client.read_holding_registers(address=20, count=12, slave=UNIT_ID)
    if not flag_result.isError():
        flag_bytes = []
        for reg in flag_result.registers:
            flag_bytes.append(reg >> 8)
            flag_bytes.append(reg & 0xFF)
        flag = ''.join(chr(b) for b in flag_bytes if b != 0)
        print(f"Flag: {flag}")
    
    print()
    print("=" * 60)
else:
    print("Restoration incomplete - check system state")

client.close()
print()
print("Disconnected from PLC")
```
