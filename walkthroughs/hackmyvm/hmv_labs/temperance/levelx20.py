import socket
import hashlib

HOST = "temperance.hackmyvm.eu"
PORT = 9988

# Creation of dictionary using rockyou.txt file
# Initialize an empty dictionary
rockyou_dict = {}

# Path to the rockyou.txt file
rockyou_file_path = "/usr/share/wordlists/rockyou.txt"

# Read the first 50 words from the file and compute their MD5 hashes
try:
    with open(rockyou_file_path, 'r', encoding='latin-1') as file:  # Encoding 'latin-1' to handle special characters
        for _ in range(50):
            word = file.readline().strip()  # Read and strip newline characters
            if word:  # Ensure the line is not empty
                # Compute the MD5 hash of the word
                md5_hash = hashlib.md5(word.encode('utf-8')).hexdigest()
                # Add the word and its hash to the dictionary
                rockyou_dict[word] = md5_hash
except FileNotFoundError:
    print(f"Error: File '{rockyou_file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Dictionary creation message
print("Rockyou.txt MD5 hash dictionary created...")

# Write md5 hash matching function

def find_matching_key(md5_hash, hash_dict):
    for key, value in hash_dict.items():
        if value == md5_hash:
            return key  # Return the plaintext word that matches the hash
    return None  # Return None if no match is found

# Connection code

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message / Conecta al host y recibes la intro general.
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx20" to choose the level / Envia levelx00 para elegir el nivel.
    s.send(b'levelx20')

    # Receive the challenge / Recibe el challenge.
    print('Receiving challenge...')
    data2 = s.recv(1024)
    print(data2)

    # Convert data2 to a string
    md5_string = data2.decode('utf-8')

    # Run the find matching key function
    matching_key_string = find_matching_key(md5_string, rockyou_dict)
    print(f"Matching key found: {matching_key_string}")

    # Convert the string to bytes
    matching_key_bytes = matching_key_string.encode('utf-8')

    # Send the challenge solved / Envia el resultado del challenge.
    print('Sending response...')
    s.send(matching_key_bytes)

    # Receive the flag / Recibe la flag.
    print('Receiving flag...')
    data3 = s.recv(1024)
    print(data3)
