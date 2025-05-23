import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx05" to choose the level
    s.send(b'levelx05')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes into a string
    data_string = data2.decode('utf-8')
    print(f"This is the string:\n{data_string}")
    
    # Grab only the last 5 characters of the string
    last5_string = data_string[-5:]
    print(f"These are the last 5 characters:\n{last5_string}")

    # Convert the string into bytes
    last5_bytes = last5_string.encode("utf-8")
    print(f"These are the last 5 bytes:\n{last5_bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(last5_bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
