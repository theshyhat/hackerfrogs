import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx08" to choose the level
    s.send(b'levelx08')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the hex bytes into a string
    data_string = data2.decode('utf-8')
    print(f"These are the numbers converted into a string:\n{data_string}")

    # Convert the string into list
    data_list = data_string.split()
    print(f"This is the string converted to a list:\n{data_list}")

    # Convert the list contents to integers
    int_list = [int(i) for i in data_list]
    print(f"This is the list items converted to integers:\n{int_list}")

    # Add the two numbers and save the result as a variable
    two_numbers_added = int_list[0] + int_list[1]
    print(f"The result of the two numbers added together is {two_numbers_added}")

    # Convert the result to string
    string_two_numbers = str(two_numbers_added)
    print(f"This is the result converted to string:\n {string_two_numbers}")

    # Convert the string to bytes
    bytes_two_numbers = string_two_numbers.encode('utf-8')
    print(f"This is the result converted to bytes:\n {bytes_two_numbers}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes_two_numbers)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
