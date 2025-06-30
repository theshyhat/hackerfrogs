# username
none
# objective
* Your goal is to connect to port 5842 on vortex.labs.overthewire.org and read in 4 unsigned integers in host byte order. Add these integers together and send back the results to get a username and password for vortex1. This information can be used to log in using SSH.
* Note: vortex is on an 32bit x86 machine (meaning, a little endian architecture)
# method of solve
This Python script will connect to the server, add up the integers, send the response back to the server, and receive the username and password:
```
import socket
import struct

HOST = 'vortex.labs.overthewire.org'
PORT = 5842

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
total = 0
for x in range(0,4,1):
        data = s.recv(4)
        total+= struct.unpack("<I", data)[0]

total = struct.pack("<I",(total & 0xFFFFFFFF))
s.send(total)
response = s.recv(1000)
print("Recieved: %s" % response)

s.close()
```
