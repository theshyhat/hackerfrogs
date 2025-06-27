import socket
from collections import Counter

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx14" to choose the level
    s.send(b'levelx14')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes into a string
    data_string = data2.decode('utf-8')
    print(f"These are the bytes converted into a string:\n{data_string}")

    # Convert the string in a list
    string_list = data_string.split()
    print(f"This is the string converted to a list:\n{string_list}")

    # Separate the elements of the list
    long_string = string_list[0]
    count_char = string_list[1]
    print(f"This is the long string\n{long_string}")
    print(f"This is the character we're supposed to count\n{count_char}")

    # Count the number of characters in the list
    number_of_char = str(long_string.count(count_char))
    print(f"This is the number of times that {count_char} appears in the string:\n{number_of_char}")

    # Convert the string to bytes
    bytes = number_of_char.encode('utf-8')
    print(f"This is the string converted to bytes:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
