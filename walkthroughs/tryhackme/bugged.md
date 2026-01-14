# URL
https://tryhackme.com/room/bugged
# Concept
* MQTT enumeration and remote code execution
# Method of solve
* after scanning the server with Nmap, we see that there are ports 22 and 1883 open
* 1883 is associated with the MQTT protocol, and we can interact with it using this tool:

[Python MQTT Client Shell](https://github.com/bapowell/python-mqtt-client-shell)

