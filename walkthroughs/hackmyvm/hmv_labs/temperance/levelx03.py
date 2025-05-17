import socket
import base64

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx03" to choose the level
    s.send(b'levelx03')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the base64 bytes of the challenge into plaintext
    data2_decoded = base64.b64decode(data2)
    print(f"Converting base64 to plaintext:\n{data2_decoded}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(data2_decoded)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
