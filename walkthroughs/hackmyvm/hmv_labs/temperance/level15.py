import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx15" to choose the level
    s.send(b'levelx15')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes into a string
    data_string = data2.decode('utf-8')
    print(f"These are the bytes converted into a string:\n{data_string}")

    # Convert the string in a list
    string_list = data_string.split()
    print(f"This is the string converted to a list:\n{string_list}")

    # Separate the number that we're going to compare
    second_number = string_list[1]
    first_number = string_list[0]
    print(f"This is the number we're going to subtract from:\n{second_number}")
    print(f"This is the number we're going to subtract:\n{first_number}")

    # Identify the constant number
    constant_number = int(second_number) - int(first_number)
    print(f"If we subtract {first_number} from {second_number}, we get {constant_number}, the constant number.")

    # Get the last number in the list
    last_number = int(string_list[-1])
    print(f"This is the last number in the list:\n{last_number}")

    # Do the math to figure out the next number in the pattern
    predict_number = constant_number + last_number
    print(f"We predict that the next number will be {predict_number}, which is the constant number {constant_number} plus the last number {last_number}.")

    # Do the conversions from integer to string, then string to bytes
    answer_string = str(predict_number)
    bytes = answer_string.encode("utf-8")
    print(f"This is the byte version of the answer:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
