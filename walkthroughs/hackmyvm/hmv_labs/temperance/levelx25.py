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

    # Send "levelx25" to choose the level
    s.send(b'levelx25')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes into string
    url_string = data2.decode("utf-8")
    print(f"This is the URL encoded into a string:\n{url_string}")

    # Get the webpage headers
    web_content = requests.get(url_string)
    print(f"This is the webpage reponse:\n{web_content}")
    web_headers = web_content.headers
    print(f"These are the webpage headers:\n{web_headers}")

    # Retrieve the value of the Hmv-code header
    hmv_value = web_content.headers['Hmv-Code']
    print(f"This is the value of the Hmv-Code header:\n{hmv_value}")

    # Convert the string into bytes
    bytes = hmv_value.encode('utf-8')
    print(f"This is the string converted to bytes:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
