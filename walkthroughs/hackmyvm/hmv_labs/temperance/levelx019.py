import socket
import base64
import zipfile
import io

HOST = "temperance.hackmyvm.eu"
PORT = 9988

def extract_base64_zip(zip_data, extract_to_path="extracted_files"):
    """
    Decodes a Base64 encoded ZIP file, extracts its contents, and saves them.

    Args:
        base64_encoded_zip_data (str): The Base64 encoded string of the ZIP file.
        extract_to_path (str): The directory where extracted files will be saved.
    """
    try:
        # 1. Create an in-memory file-like object
        zip_file_in_memory = io.BytesIO(zip_data)

        # 2. Open the ZIP archive
        with zipfile.ZipFile(zip_file_in_memory, 'r') as zip_ref:
            # 3. Extract and process files
            file_list = zip_ref.namelist()
            print(f"Successfully extracted files to: {extract_to_path}")
            print(f"These are the files in the archive:\n{file_list}")
            # 4. Read the contents of the extracted file
            for file in zip_ref.namelist():
                with zip_ref.open(file) as f:
                    return f.read()

    except base64.binascii.Error as e:
        print(f"Error decoding Base64 data: {e}. Ensure it's valid Base64.")
    except zipfile.BadZipFile as e:
        print(f"Error opening ZIP file: {e}. The decoded data might not be a valid ZIP archive.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx19" to choose the level
    s.send(b'levelx19')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the base64 string back into a zip file
    zip_file = base64.b64decode(data2)
    print(f"This is the original zip file:\n{zip_file}")

    # Run the zip file function
    bytes = extract_base64_zip(zip_file)
    print(f"This is the content of the text file:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
