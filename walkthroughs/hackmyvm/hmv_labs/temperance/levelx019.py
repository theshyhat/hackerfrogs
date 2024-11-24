import socket
import base64
import zipfile
import io

HOST = "temperance.hackmyvm.eu"
PORT = 9988

# Writing the decode and extract zip function

def decode_and_extract_zip(base64_zip):
    try:
        # Decode the base64 string
        zip_data = base64.b64decode(base64_zip)

        # Create an in-memory file-like object for the zip data
        zip_file = io.BytesIO(zip_data)

        # Open the zip archive
        with zipfile.ZipFile(zip_file, 'r') as zf:
            # List the files in the zip archive
            file_name = zf.namelist()
            print("File names in the archive:", file_name)

            # Extract and display the contents of the file
            with zf.open(file_name[0]) as file:
                content = file.read().decode('utf-8') # assuming text files with utf-8 encoding
                print(f"Contents of {file_name}:\n{content}\n")
                return content

    except (base64.binascii.Error, zipfile.BadZipFile, UnicodeDecodeError) as e:
        print("Error processing the zip file:", str(e))

# Connection code

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message / Conecta al host y recibes la intro general.
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx19" to choose the level / Envia levelx00 para elegir el nivel.
    s.send(b'levelx19')

    # Receive the challenge / Recibe el challenge.
    print('Receiving challenge...')
    data2 = s.recv(1024)
    print(data2)

    # Convert data2 to a string
    b64_zip_string = data2.decode('utf-8')

    # Perform the decoding and extraction function
    contents_string = decode_and_extract_zip(b64_zip_string)
    print(f"Contents to be sent: {contents_string}")

    # Convert the string to bytes
    contents_bytes = contents_string.encode('utf-8')

    # Send the challenge solved / Envia el resultado del challenge.
    print('Sending response...')
    s.send(contents_bytes)

    # Receive the flag / Recibe la flag.
    print('Receiving flag...')
    data3 = s.recv(1024)
    print(data3)
