# URL
https://training.olicyber.it/challenges#challenge-288
# Concept
* sending data to a remote server via Pwntools
# Method of solve
```Python
from pwn import *
import sys

HOST = "software-18.challs.olicyber.it"
PORT = 13001

# Connect to the server
r = remote(HOST, PORT)

first_msg = r.recvuntil("iniziare ...")

print(first_msg)

first_snd = r.sendline(b"A")

# Run the packing operation 100 times
for i in range(100):
  # Receive the challenge
  hex_str = ""
  instruct = ""
  arch = ""
  print(f"Loop {i}")
  msg = r.recvuntil("bit")
  print(msg)
  # Parse the message
  msg_list = [i.decode('utf-8') for i in msg.split(b',')]
  str_list = msg_list[0].split()
  for i in str_list:
    if i.startswith("0x"):
      hex_str = i
    if i.endswith("bit"):
      arch = i
  # Determine the payload to send in response
  print(hex_str)
  if arch == '64-bit':
    payload = p64(int(hex_str, 16))
  else:
    payload = p32(int(hex_str, 16))
  # Send the payload to the server
  r.send(payload)

final = r.recv(1024)
print(final)
r.sendline(b"A")
final_two = r.recv(1024)
print(final_two)

r.close()
```
