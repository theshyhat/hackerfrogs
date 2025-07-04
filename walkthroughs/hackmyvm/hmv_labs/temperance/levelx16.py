import socket
import base64
import io
import PIL
from PIL import Image

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx16" to choose the level
    s.send(b'levelx16')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the base64 bytes back into its original form
    png_bytes = base64.b64decode(data2)
    print(f"This is the PNG decoded from base64:\n{png_bytes}")

    # Open the image, then get its dimensions
    png_image = Image.open(io.BytesIO(png_bytes))
    dimensions = png_image.size
    print(f"These are the dimensions of the PNG image:\n{dimensions}")
    
    # Save the width and height as variables
    png_width = dimensions[0]
    png_height = dimensions[1]
    print(f"The width of the image is {png_width}\nThe height of the image is {png_height}")

    # Get the exact string format that the server is expecting
    formatted_string = str(str(png_width) + "x" + str(png_height))
    print(f"The correct format is {formatted_string}")

    # Convert the string to bytes
    bytes = formatted_string.encode('utf-8')
    print(f"This is the string converted to bytes:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
