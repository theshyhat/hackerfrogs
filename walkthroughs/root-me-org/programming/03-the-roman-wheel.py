import socket

HOST = "challenge01.root-me.org"
PORT = 52021

# Define the string extraction function
def extract_between_single_quotes(input_string):
    start = input_string.find("'")
    if start == -1:
        return ""

    end = input_string.find("'", start + 1)
    if end == -1:
        return ""

    return input_string[start + 1:end]

# Define the ROT13 function
def rot13(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            # Shift within lowercase letters
            offset = ord('a')
            result.append(chr((ord(char) - offset + 13) % 26 + offset))
        elif 'A' <= char <= 'Z':
            # Shift within uppercase letters
            offset = ord('A')
            result.append(chr((ord(char) - offset + 13) % 26 + offset))
        else:
            # Non-alphabetic characters are unchanged
            result.append(char)
    return ''.join(result)

# Connection code

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and the output the challenge
    print('Receiving challenge...')
    data = s.recv(1024)
    print(data)

    # Convert data to a string
    data_string = data.decode('utf-8')

    # Extract the string between single quotes in the response string
    extracted_string = extract_between_single_quotes(data_string)
    print(f"This is the ROT13 encoded string {extracted_string}")

    # Run the extraction function
    rot13_string = rot13(extracted_string + "\n")
    print(f"This is the decoded string {rot13_string}")

    # Convert the string to bytes
    answer_bytes = rot13_string.encode('utf-8')

    # Send the challenge solved
    print('Sending answer...')
    s.sendall(answer_bytes)

    # Receive the flag
    print('Receiving response...')
    data2 = s.recv(1024)
    print(data2)
