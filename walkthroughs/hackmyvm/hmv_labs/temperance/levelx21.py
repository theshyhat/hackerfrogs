import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx21" to choose the level
    s.send(b'levelx21')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Save the data2 variable as an integer
    data_int = int(data2)
    print(f"This is the bytes converted to integer:\n{data_int}")

    # Format the integer as kilobytes
    kilobytes_raw = data_int / 1024
    print(f"These is the integer converted to raw kilobytes:\n{kilobytes_raw}")

    # Round the result to only the first 2 decimal places
    rounded_result = round(kilobytes_raw, 2)
    print(f"This is the rounded result to 2 decimal places:\n{rounded_result}")

    # Format the number into a string that the server expects
    result_string = str(rounded_result) + 'KB'
    print(f"This is the formatted string:\n{result_string}")

    # Convert the string into bytes
    bytes = result_string.encode('utf-8')
    print(f"This is the string converted to bytes:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
