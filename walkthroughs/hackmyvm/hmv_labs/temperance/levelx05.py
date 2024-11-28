import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message / Conecta al host y recibes la intro general.
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx05" to choose the level / Envia levelx00 para elegir el nivel.
    s.send(b'levelx05')

    # Receive the challenge / Recibe el challenge.
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes to a string
    challenge_string = data2.decode("utf-8")

    # Retrieve the last 5 characters of the string
    last_5_string = challenge_string[-5::]
    print(f"Last 5 characters\n{last_5_string}")

    # Convert the string to bytes
    answer_bytes = last_5_string.encode("utf-8")

    # Send the challenge solved / Envia el resultado del challenge.
    print('Sending answer...')
    s.send(answer_bytes)

    # Receive the flag / Recibe la flag.
    print('Receiving flag...')
    data3 = s.recv(1024)
    print(data3)
