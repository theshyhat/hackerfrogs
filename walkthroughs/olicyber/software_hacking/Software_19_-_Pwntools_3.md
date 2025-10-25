# URL
https://training.olicyber.it/challenges#challenge-289
# Concept
* using Pwntools to test a binary locally and remotely
# Method of solve
This Python script gets the job done:
```
#!/usr/bin/env python3
from pwn import *

elf = ELF("./sw-19")
# context.binary = binary = ELF("./sw-19")

if args.REMOTE:
        p = remote("software-19.challs.olicyber.it", 13002)
else:
        p = process("./sw-19")

def lookup_function_name():
    msg = p.recvuntil(b":")
    msg_string = msg.decode('utf-8')
    msg_list = msg_string.split(' ')
    function_name_raw = msg_list[1]
    function_name = function_name_raw[0:-1]
    return function_name

def get_function_addy(function_name):
    function_address = elf.symbols[function_name]
    hex_addy = hex(function_address)[2:]
    hex_addy_bytes = hex_addy.encode('utf-8')
    return hex_addy_bytes

def send_answer(answer_bytes):
    p.sendline(answer_bytes)
    print(f"Sent answer: {answer_bytes}")
    p.recv(1024)
'''
# Receive the initial message
init_msg = p.recvuntil(b"iniziare ...")
print(init_msg)

# Send confirm input
p.sendline(b"")

# Receive the message number 2
msg2 = p.recvuntil(b":")
print(msg2)

# Convert the bytes to string
msg2_string = msg2.decode('utf-8')
print(msg2_string)

# Convert the string to a list
msg2_list = msg2_string.split(' ')
print(msg2_list)

# Extract the function name from the output
function_name_raw = msg2_list[1]
function_name = function_name_raw[0:-1]
print(function_name)

# Lookup the function name's address
function_address = elf.symbols[function_name]
print(function_address)

# Convert the function address to hex, then the string into bytes
hex_addy = hex(function_address)[2:]
hex_addy_bytes = hex_addy.encode('utf-8')
print(hex_addy)
print(hex_addy_bytes)

# Send the hex address
print("Sending 1st answer...")
p.sendline(hex_addy_bytes)

# Receive the next function name
msg3 = p.recvuntil(b":")
print(msg3)
# msg4 = p.recv(4096)
# print(msg4)
'''

# Receive the initial message
init_msg = p.recvuntil(b"iniziare ...")
print(init_msg)

# Send confirm input
p.sendline(b"")

for x in range(1,21):
    lookup = lookup_function_name()
    addy = get_function_addy(lookup)
    send_answer(addy)

last_msg = p.recv(4096)
print(last_msg)
```
