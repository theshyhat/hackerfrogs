import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

# Add numbers function code
def add_2_numbers(num1, num2):
    return num1 + num2

# Connection code

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message / Conecta al host y recibes la intro general.
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx08" to choose the level / Envia levelx00 para elegir el nivel.
    s.send(b'levelx08')

    # Receive the challenge / Recibe el challenge.
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes to a string
    challenge_string = data2.decode("utf-8")

    # Convert the string into a list
    challenge_list = [int(num) for num in challenge_string.split()]

    # Define the numbers to be added
    num1 = challenge_list[0]
    num2 = challenge_list[1]
    print(f"First number to be added: {num1}")
    print(f"Second number to be added: {num2}")

    # Run the add 2 numbers function
    result_integer = add_2_numbers(num1,num2)
    print(f"Result: {result_integer}")

    # Convert the integer to a string
    result_string = str(result_integer)

    # Convert the string to bytes
    answer_bytes = result_string.encode("utf-8")

    # Send the challenge solved / Envia el resultado del challenge.
    print('Sending answer...')
    s.send(answer_bytes)

    # Receive the flag / Recibe la flag.
    print('Receiving flag...')
    data3 = s.recv(1024)
    print(data3)
