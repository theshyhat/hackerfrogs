import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx12" to choose the level
    s.send(b'levelx12')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes into a string
    data_string = data2.decode('utf-8')
    print(f"These are the bytes converted into a string:\n{data_string}")

    # Separate the string from the number by turning the pair into a list
    list_from_string = data_string.split()
    print(f"This is the string separated into a list:\n{list_from_string}")

    # Turn the elements of the list into variables
    target_string = list_from_string[0]
    target_number = int(list_from_string[1])
    print(f"This is the string:\n{target_string}")
    print(f"This is the number:\n{target_number}")

    # Create the multiplied string to send back to the server
    mult_string = target_string * target_number
    print(f"This is the multiplied string:\n{mult_string}")

    # Convert the string to bytes
    bytes = mult_string.encode('utf-8')
    print(f"This is the string converted to bytes:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
