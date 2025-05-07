import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

def recv_data(sock, buffer_size=1024, encoding="utf-8"):
  # function for receiving server responses
  data = sock.recv(buffer_size)
  if not data:
    return None
  try:
    decoded_data = data.decode(encoding)
    print(f"Received: {decoded_data}")
    return decoded_data
  except UnicodeDecodeError:
    print(f"Received (raw bytes): {data}")
    return data

def level_select(sock, level):
  # function for sending the level select to the server
  level_bytes = f"levelx{level}".encode("utf-8")
  print(f"Seleting level: {level_bytes}")
  sock.send(level_bytes)
  
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))

  # Connect to the host and receive the message
  data = recv_data(s)
  print(data)

  # select the level of the game
  level_select(s, 00)

  # Receive the challenge
  data = recv_data(s)
  print(data)

  # level 00, send the challenge back
  s.send(data)

  # Receive the flag
  data = recv_data(s)
  print(data)
