import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx02" to choose the level
    s.send(b'levelx02')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes of the challenge into a string
    data2_string = data2.decode('utf-8')
    print(f"Converting bytes to string:\n{data2_string}")

    # Convert the string to all uppercase
    data2_string_upper = data2_string.upper()
    print(f"Converting string to upper-case:\n{data2_string_upper}")

    # Convert the string to bytes
    data2_upper_bytes = data2_string_upper.encode('utf-8')
    print(f"Converting upper-case string to bytes:\n{data2_upper_bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(data2_upper_bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
