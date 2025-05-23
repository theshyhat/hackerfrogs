import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx04" to choose the level
    s.send(b'levelx04')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes into a string
    data_string = data2.decode('utf-8')
    print(f"This is the string:\n{data_string}")
    
    # Reverse the string
    string_reverse = data_string[::-1]
    print(f"This is the string in reverse:\n{string_reverse}")

    # Convert the reverse string into bytes
    reverse_bytes = string_reverse.encode("utf-8")
    print(f"These are the reverse bytes:\n{reverse_bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(reverse_bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
