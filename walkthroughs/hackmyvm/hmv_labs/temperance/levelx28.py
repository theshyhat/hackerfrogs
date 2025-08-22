import socket
import jwt

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx28" to choose the level
    s.send(b'levelx28')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes to a string
    jwt_string = data2.decode('utf-8')
    print(f"This is the JWT in string form:\n{jwt_string}")

    # Decode the JWT string
    jwt_decoded = jwt.decode(jwt_string, options={"verify_signature": False})
    print(f"This is the decoded JWT:\n{jwt_decoded}")

    # Get the extracted HMVKey value
    hmvkey_value = jwt_decoded['HMVKey']
    print(f"This is the value of the HMVKey:\n{hmvkey_value}")

    # Convert the string into bytes
    bytes = hmvkey_value.encode('utf-8')
    print(f"This is the string converted to bytes:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
