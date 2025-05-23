import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx06" to choose the level
    s.send(b'levelx06')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes into a string
    data_string = data2.decode('utf-8')
    print(f"This is the string:\n{data_string}")
    
    # Run the len() function to get the length of the string
    string_length = str(len(data_string))
    print(f"This is the length of the string:\n{string_length}")

    # Convert the string into bytes
    length_bytes = string_length.encode("utf-8")
    print(f"This is the length in bytes:\n{length_bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(length_bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
