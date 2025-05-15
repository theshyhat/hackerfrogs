import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the initial message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx01" to choose the level
    current_level = '01'
    level_string = "levelx" + current_level
    level_bytes = level_string.encode("utf-8")
    s.send(level_bytes)
    print(f"Selecting level {current_level}")
  
    # Receive the challenge
    print('Receiving challenge 1')
    data2 = s.recv(1024)
    print(data2)

    # Send challenge 1 back
    s.send(data2)
    print(f"Sending challenge 1 back: {data2}")
    
    # Receive the second challenge
    print('Receiving challenge 2')
    data3 = s.recv(1024)
    print(data3)
  
    # Send challenge 2 back
    s.send(data3)
    print(f"Sending challenge 2 back: {data3}")
  
    # Receive the flag
    print('Receiving flag...')
    data4 = s.recv(1024)
    print(data4)
