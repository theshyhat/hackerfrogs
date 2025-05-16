import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx01" to choose the level
    s.send(b'levelx01')

    # Receive the first challenge
    print('Receiving first challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Send the first challenge back
    print('Sending first challenge.')
    s.send(data2)

    # Receive the second challenge
    print('Receiving second challenge.')
    data3 = s.recv(1024)
    print(data3)

    # Send the second challenge back
    print('Sending second challenge.')
    s.send(data3)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
