import socket
from pwn import xor

key = b"HMV"

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx30" to choose the level
    s.send(b'levelx30')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Do the XOR operation
    xor_result = xor(data2,key)
    print(f"This is the result of XOR between {data2} and {key}:\n{xor_result}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(xor_result)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
