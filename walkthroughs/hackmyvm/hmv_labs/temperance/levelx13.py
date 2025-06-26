import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx13" to choose the level
    s.send(b'levelx13')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes into a string
    data_string = data2.decode('utf-8')
    print(f"These are the bytes converted into a string:\n{data_string}")

    # Remove the brackets from the string
    string_mod = data_string[1:-1]
    print(f"This is the string without the brackets:\n{string_mod}")

    # Convert the string into a list
    list_from_string = string_mod.split() 
    print(f"This is the string separated into a list:\n{list_from_string}")

    # Sort the list
    list_from_string.sort()
    print(f"This is the sorted list:\n{list_from_string}")

    # Retrieve the last element of the list
    list_last_item = list_from_string[-1]
    print(f"This is the last item in the list:\n{list_last_item}")

    # Convert the string to bytes
    bytes = list_last_item.encode('utf-8')
    print(f"This is the string converted to bytes:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
