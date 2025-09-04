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

    # Send "levelx27" to choose the level
    s.send(b'levelx27')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes into a string
    url = data2.b64decode('utf-8')
    print(f"This is the URL converted to a string:\n{url}")

    # Get the URL response body
    url_request = requests.get(url)
    response_body = url_request.text
    print(f"This is the response body:\n{response_body}")

    # Extract the line
    target_user = "proxy"
    target_string = ""
    for line in response_body.splitlines():
      if target_string in response_body:
        if target_user in line:
          target_string += line
    print(f"This is the line with the proxy user:\n{target_string}")

    # Isolate the number
    target_list = target_string.split(":")
    target_num = target_list[2]
    print(f"This is the number we need to send back:\n{target_number}")
  
    # Convert the string into bytes
    bytes = target_num.encode('utf-8')
    print(f"This is the string converted to bytes:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
