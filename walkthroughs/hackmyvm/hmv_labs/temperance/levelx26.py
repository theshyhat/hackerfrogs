import socket
import base64
import pytesseract
from PIL import Image 
import io

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx26" to choose the level
    s.send(b'levelx26')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes from base64 to its original form
    original_png = base64.b64decode(data2)
    print(f"This is the data from the original png file:\n{original_png}")

    # Open the image with the PIL module
    pil_image = Image.open(io.BytesIO(original_png))

    # Get the extracted text
    extracted_text = pytesseract.image_to_string(pil_image)
    print(f"This is the extracted text:\n{extracted_text}")

    # Convert the string into bytes
    bytes = extracted_text.encode('utf-8')
    print(f"This is the string converted to bytes:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
