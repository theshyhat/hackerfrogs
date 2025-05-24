import socket
import binascii

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx07" to choose the level
    s.send(b'levelx07')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the hex bytes into a string
    data_string = data2.decode('utf-8')
    print(f"This is the hex converted into a string:\n{data_string}")

    # Convert the hex string into ASCII
    string_ascii = binascii.unhexlify(data_string).decode('ascii')
    print(f"This is the hex string converted to ASCII:\n{string_ascii}")

    # Convert the string into bytes
    data_bytes = string_ascii.encode("utf-8")
    print(f"This is the string converted to bytes:\n{data_bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(data_bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
