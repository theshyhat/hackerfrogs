import socket
import re
import math

HOST = "challenge01.root-me.org"
PORT = 52002

# Write the math function
def square_root_then_multiply(num1, num2):
    result = math.sqrt(num1) * num2
    return round(result, 2)

# Write the number extraction function
def extract_numbers(input_string):
    numbers = re.findall(r'\d+', input_string)
    return [int(num) for num in numbers]

# Connection code

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and the output the challenge
    print('Receiving challenge...')
    data = s.recv(1024)
    print(data)

    # Convert data to a string
    data_string = data.decode('utf-8')

    # Extract the numbers using a function
    numbers_list = extract_numbers(data_string)
    print(f"Extracted numbers: {numbers_list}")

    # Isolate the numbers for calculation
    number1 = numbers_list[1]
    number2 = numbers_list[2]

    # Perform the calculation with the function
    answer_int = square_root_then_multiply(number1, number2)
    print(f"The answer is {answer_int}!")

    # Convert the integer to string
    answer_string = str(answer_int) + "\n"

    # Conver the string to bytes
    answer_bytes = answer_string.encode('utf-8')

    # Send the challenge solved / Envia el resultado del challenge.
    print('Sending answer...')
    s.send(answer_bytes)

    # Receive the flag / Recibe la flag.
    print('Receiving response...')
    data3 = s.recv(1024)
    print(data3)
