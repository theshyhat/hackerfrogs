# URL

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
