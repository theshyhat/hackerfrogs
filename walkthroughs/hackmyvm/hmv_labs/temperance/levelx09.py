import socket
import codecs

HOST = "temperance.hackmyvm.eu"
PORT = 9988

# Connection code

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message / Conecta al host y recibes la intro general.
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx09" to choose the level / Envia levelx00 para elegir el nivel.
    s.send(b'levelx09')

    # Receive the challenge / Recibe el challenge.
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes to a string
    challenge_string = data2.decode("ascii")

    # Run the ROT13 function on the string
    rot13_decoded_string = codecs.encode(challenge_string, 'rot-13')
    print(f"This is the ROT13 decoded string: {rot13_decoded_string}")

    # Convert the string to bytes
    answer_bytes = rot13_decoded_string.encode("ascii")

    # Send the challenge solved / Envia el resultado del challenge.
    print('Sending answer...')
    s.send(answer_bytes)

    # Receive the flag / Recibe la flag.
    print('Receiving flag...')
    data3 = s.recv(1024)
    print(data3)
