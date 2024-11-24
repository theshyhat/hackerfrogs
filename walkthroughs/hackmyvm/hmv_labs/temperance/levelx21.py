import socket
import hashlib

HOST = "temperance.hackmyvm.eu"
PORT = 9988

def bytes_to_kilobytes(binary_bytes):
    """
    Converts bytes to binary kilobytes (KiB) and appends 'KB'.

    Parameters:
        binary_bytes (int): The number of bytes to convert.

    Returns:
        str: The converted value in kilobytes with 'KB' appended.
    """
    if not isinstance(binary_bytes, int) or binary_bytes < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Perform the conversion (1 KiB = 1024 bytes)
    kilobytes = binary_bytes / 1024

    # Format the result to two decimal places and append 'KB'
    return f"{kilobytes:.2f}KB"

# Connection code

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message / Conecta al host y recibes la intro general.
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx21" to choose the level / Envia levelx00 para elegir el nivel.
    s.send(b'levelx21')

    # Receive the challenge / Recibe el challenge.
    print('Receiving challenge...')
    data2 = s.recv(1024)
    print(data2)

    # Convert data2 to an integer
    data_int = int(data2)

    # Run the conversion to kilobytes function
    kilo_string = bytes_to_kilobytes(data_int)
    print(f"{data_int} converts to {kilo_string}")

    # Convert the string to bytes
    kilo_bytes = kilo_string.encode('utf-8')

    # Send the challenge solved / Envia el resultado del challenge.
    print('Sending response...')
    s.send(kilo_bytes)

    # Receive the flag / Recibe la flag.
    print('Receiving flag...')
    data3 = s.recv(1024)
    print(data3)
