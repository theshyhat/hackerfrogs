import socket
import hashlib

HOST = "temperance.hackmyvm.eu"
PORT = 9988

rockyou_list = ['123456','12345','123456789','password','iloveyou','princess','1234567','rockyou','12345678','abc123','nicole','daniel','babygirl','monkey','lovely','jessica','654321','michael','ashley','qwerty','111111','iloveu','000000','michelle','tigger','sunshine','chocolate','password1','soccer','anthony','friends','butterfly','purple','angel','jordan','liverpool','justin','loveme','fuckyou','123123','football','secret','andrea','carlos','jennifer','joshua','bubbles','1234567890','superman','hannah']

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx20" to choose the level
    s.send(b'levelx20')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Do a for loop that hashes each one of the rockyou words and compares it to the data_string
    def get_hash(data_string):
        for word in rockyou_list:
            word_bytes = word.encode('utf-8')
            current_hash = hashlib.md5(word_bytes).hexdigest()
            if current_hash.encode('utf-8') == data_string:
                return word
                break

    # Run the function
    correct_word = get_hash(data2)
    print(f"This is the matching word:\n{correct_word}")
   
    # Convert the correct word into bytes
    bytes = correct_word.encode('utf-8')
    print(f"This is the string converted to bytes:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
