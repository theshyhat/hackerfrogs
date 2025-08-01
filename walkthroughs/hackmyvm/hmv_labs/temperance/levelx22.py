import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx22" to choose the level
    s.send(b'levelx22')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Save the data2 variable as an string
    data_string = data2.decode('utf-8')
    print(f"These are the bytes converted to a string:\n{data_string}")

    # Convert the string into a list
    data_list = data_string.split()
    print(f"These is the string converted to a list:\n{data_list}")

    # Do a for loop which converts the elements in the list into ASCII characters
    def convert_dec_to_ascii(target_list):
        ascii_string = ''
        for i in target_list:
            ascii_string += chr(int(i))
        return ascii_string

    # Call the function
    converted_string = convert_dec_to_ascii(data_list)
    print(f"These are the decimal numbers converted to ASCII:\n{converted_string}")

    # Convert the string into bytes
    bytes = converted_string.encode('utf-8')
    print(f"This is the string converted to bytes:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
