import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

# Write decimal list to ASCII function
def decimals_to_ascii(decimal_list):
    ascii_string = ''
    for num in decimal_list:
        try:
            ascii_string += chr(num)
        except ValueError:
            print(f"Skipping invalid ASCII value: {num}")
    return ascii_string

# Connection code

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message / Conecta al host y recibes la intro general.
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx22" to choose the level / Envia levelx00 para elegir el nivel.
    s.send(b'levelx22')

    # Receive the challenge / Recibe el challenge.
    print('Receiving challenge...')
    data2 = s.recv(1024)
    print(data2)

    # Convert data2 to a string
    ascii_decimal_string = data2.decode('utf-8')

    # Convert the string to a list 
    ascii_decimal_list = [int(num) for num in ascii_decimal_string.split()]

    # Create an empty string to be populated in the next step
    ascii_string = decimals_to_ascii(ascii_decimal_list)
    print(f"This is the ASCII string {ascii_string}")

    # Convert the string to bytes
    ascii_bytes = ascii_string.encode('utf-8')

    # Send the challenge solved / Envia el resultado del challenge.
    print('Sending response...')
    s.send(ascii_bytes)

    # Receive the flag / Recibe la flag.
    print('Receiving flag...')
    data3 = s.recv(1024)
    print(data3)
