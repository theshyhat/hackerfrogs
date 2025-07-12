import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx18" to choose the level
    s.send(b'levelx18')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes to a string
    string = data2.decode('ASCII')
    print(f"This is the bytes converted to string:\n{string}")

    # Convert the string to binary value
#   binary_number = ''.join([bin(ord(x)).replace('0b','') for x in string])
    binary = ''.join(format(ord(x), '08b') for x in string)
    print(f"This is the string converted to binary:\n{binary}\n")


    # Convert the string to bytes
    bytes = binary.encode('ASCII')
    print(f"This is the string converted to bytes:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
