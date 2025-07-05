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

    # Send "levelx17" to choose the level
    s.send(b'levelx17')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the base64 bytes back into its original form
    png_bytes = base64.b64decode(data2)
    print(f"This is the PNG decoded from base64:\n{png_bytes}")

    # Open the image, convert the image to RBBA, then get its dimensions
    png_image = Image.open(io.BytesIO(png_bytes))
    png_image = png_image.convert("RGBA")
    width, height = png_image.size
    print(f"These are the dimensions of the PNG image:\n{width}, {height}")

    # Get the RGBA value of the last pixel
    rgba_value = png_image.getpixel((width - 1, height - 1))
    last_value = rgba_value[-1]
    print(f"This is the RGBA value of the last pixel: {rgba_value}")
    print(f"This is the last value: {last_value}")

    # Conver the integer to a string, and then to bytes
    last_value_string = str(last_value)
    print(f"The is the integer convert to string: {last_value_string}")

    # Convert the string to bytes
    bytes = last_value_string.encode('utf-8')
    print(f"This is the string converted to bytes:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
