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

    # Send "levelx23" to choose the level
    s.send(b'levelx23')

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

    # Get the RGBA values of the pixels and save the values to a list
    def get_all_pixels_list(png_image):
        """Get all pixel RGBA values as a flat list"""
        pixel_data = list(png_image.getdata())
        # Returns list of tuples: [(R,G,B,A), (R,G,B,A), ...]
        return pixel_data

    # Call the function and get the list of tuples
    tuple_list = get_all_pixels_list(png_image)
    print(f"This is the list of all the RGBA values:\n{tuple_list}")

    # Trim the output to only the last element of each tuple
    def get_last_values(list):
        values_list = []
        for i in tuple_list:
            last_value = i[-1]
            values_list.append(last_value)
        return values_list
    
    # Call the function and get the list
    last_values_list = get_last_values(tuple_list)
    print(f"These are the last values in a list:\n{last_values_list}")

    # Do a for loop which converts the elements in the list into ASCII characters
    def convert_dec_to_ascii(target_list):
        ascii_string = ''
        for i in target_list:
            ascii_string += chr(int(i))
        return ascii_string

    # Call the function
    converted_string = convert_dec_to_ascii(last_values_list)
    print(f"These are the decimal numbers converted to ASCII:\n{converted_string}")

    # Convert the string into bytes
    bytes = converted_string.encode('utf-8')
    print(f"This is the string converted to bytes:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
