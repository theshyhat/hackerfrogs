import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message / Conecta al host y recibes la intro general.
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx04" to choose the level / Envia levelx00 para elegir el nivel.
    s.send(b'levelx04')

    # Receive the challenge / Recibe el challenge.
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

'''

    # Send the challenge solved / Envia el resultado del challenge.
    print('Envio reto')
    s.send(data2)

    # Receive the flag / Recibe la flag.
    print('Recibo flag')
    data3 = s.recv(1024)
    print(data3)
'''
