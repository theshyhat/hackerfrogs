# URL
https://hackropole.fr/en/challenges/misc/fcsc2022-misc-color-plant-1/
# Concept
* interacting with ICS systems with the Python Modbus module
# Method of solve
* we're given documentation for the ICS system.
  * there are four coils:
    * 0 is open/close for the R valve
    * 1 is open/close for the G valve
    * 2 is open/close for the B valve
    * 3 is open/close for the M valve
  * there are 36 holding registers
    * 0-31 are the player tokens, and are read-only
    * 32 is R flow rate
    * 32 is G flow rate
    * 32 is B flow rate
    * 32 is M to F flow rate

```Python
import time
from pymodbus.client import ModbusTcpClient as ModbusClient

client = ModbusClient(host="127.0.0.1", port=4502)

# Modbus addresses
FLOW_R = 32
FLOW_G = 33
FLOW_B = 34
FLOW_M = 35

VALVE_R = 0
VALVE_G = 1
VALVE_B = 2
VALVE_M = 3

# Each source initially contains 255 units
INITIAL = 255

def read_input(address, count=1):
    response = client.read_input_registers(
        address=address, count=count
    )
    if response.isError():
        raise RuntimeError(f"Read failed: {response}")
    return response.registers

def write_flow(address, rate):
    response = client.write_register(
        address=address, value=rate
    )
    if response.isError():
        raise RuntimeError(f"Flow write failed: {response}")

def write_valve(address, opened):
    response = client.write_coil(
        address=address, value=opened
    )
    if response.isError():
        raise RuntimeError(f"Valve write failed: {response}")

def show_status():
    source = read_input(0, 3)
    mixing = read_input(3, 4)
    final = read_input(7, 4)

    print("Source:", source)
    print("Mix:   ", mixing)
    print("Final: ", final)

def add_color(name, valve, flow, target, source_address):
    """
    Add liquid until the source tank has delivered
    the desired cumulative quantity.
    """
    print(f"Adding {name}, cumulative target: {target}")

    # Start at 5 units per second
    write_flow(flow, 5)
    write_valve(valve, True)

    slow_mode = False

    while True:
        remaining_source = read_input(source_address)[0]
        delivered = INITIAL - remaining_source
        needed = target - delivered

        if needed <= 0:
            write_valve(valve, False)

            if needed < 0:
                raise RuntimeError(
                    f"Overshot {name} target by {-needed}"
                )

            print(f"{name}: {delivered} units delivered")
            return

        # Slow down near the exact target
        if needed <= 6 and not slow_mode:
            write_flow(flow, 1)
            slow_mode = True

        time.sleep(0.05)

def drain_mixing_tank():
    print("Draining M into F...")

    mixing_total = read_input(6)[0]

    if mixing_total != 100:
        raise RuntimeError(
            f"M must contain 100 units, has {mixing_total}"
        )

    write_flow(FLOW_M, 10)
    write_valve(VALVE_M, True)

    while True:
        mixing_total = read_input(6)[0]

        if mixing_total == 0:
            break

        time.sleep(0.1)

    print("Mixing tank empty")

    # Allow the safety controller to update the valves
    time.sleep(0.2)
try:
    if not client.connect():
        raise RuntimeError("Could not connect to PLC")

    start_time = time.monotonic()

    # STEP 1: Retrieve authentication token
    response = client.read_holding_registers(
        address=0, count=32
    )
    if response.isError():
        raise RuntimeError("Could not read token")

    token = "".join(chr(v) for v in response.registers)
    print("SCADA Token:", token, flush=True)

    # STEP 2: First batch
    print("\n=== BATCH 1 ===")
    add_color("RED", VALVE_R, FLOW_R, 32, 0)
    add_color("GREEN", VALVE_G, FLOW_G, 68, 1)

    show_status()
    drain_mixing_tank()

    # STEP 3: Second batch
    print("\n=== BATCH 2 ===")
    add_color("GREEN", VALVE_G, FLOW_G, 126, 1)
    add_color("BLUE", VALVE_B, FLOW_B, 42, 2)

    show_status()
    drain_mixing_tank()

    # STEP 4: Verify final contents
    print("\n=== FINAL RESULT ===")
    show_status()

    final = read_input(7, 4)
    elapsed = time.monotonic() - start_time

    print(f"Elapsed: {elapsed:.2f} seconds")

    if final == [32, 126, 42, 200]:
        print("SUCCESS: Correct RGB mixture!")
    else:
        print("Final mixture does not match target.")

    input("Press Enter to disconnect...")

finally:
    client.close()
```
