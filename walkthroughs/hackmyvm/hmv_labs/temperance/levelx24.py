import socket
import requests

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx24" to choose the level
    s.send(b'levelx24')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes into string
    url_string = data2.decode("utf-8")
    print(f"This is the URL encoded into a string:\n{url_string}")

    # Get the webpage contents
    web_content = requests.get(url_string)
    web_text = web_content.text
    print(f"This is the webpage content:\n{web_text}")

    # Convert the string into bytes
    bytes = web_text.encode('utf-8')
    print(f"This is the string converted to bytes:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
