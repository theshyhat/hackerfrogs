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

    # Removing the left and right square bracket from the string
    mod_string = data_string[1:-1]
    print(f"This is the modified string, without the brackets:\n{mod_string}")

    # Convert the string in a list
    string_list = mod_string.split()
    print(f"This is the string converted to a list:\n{string_list}")

    # Sorting the list alphabetically
    string_list.sort()
    print(f"This is the sorted list:\n{string_list}")

    # Retrieve the last item in the list
    last_item = string_list[-1]
    print(f"This is the last item in the list:\n{last_item}")

    # Convert the string to bytes
    bytes = last_item.encode('utf-8')
    print(f"This is the string converted to bytes:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
