import socket
import base64

HOST = "challenge01.root-me.org"
PORT = 52023

# Define the extraction function
def extract_between_single_quotes(input_string):
    start = input_string.find("'")
    if start == -1:
        return ""

    end = input_string.find("'", start + 1)
    if end == -1:
        return ""

    return input_string[start + 1:end]

# Connection code

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and the output the challenge
    print('Receiving challenge...')
    data = s.recv(1024)
    print(data)

    # Convert data to a string
    data_string = data.decode('utf-8')

    # Run the extraction function
    base64_string = extract_between_single_quotes(data_string)
    print(f"This is the base64 encoded string {base64_string}")

    # Decode the base64 string
    decoded_bytes = base64.b64decode(base64_string)

    # Convert the bytes to string
    decoded_string = decoded_bytes.decode('utf-8') + "\n"
    print(f"Decoded value: {decoded_string}")

    # Convert the string to bytes
    answer_bytes = decoded_string.encode('utf-8')

    # Send the challenge solved
    print('Sending answer...')
    s.send(answer_bytes)

    # Receive the flag
    print('Receiving response...')
    data2 = s.recv(1024)
    print(data2)
