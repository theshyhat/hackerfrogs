import socket
from latloncalc.latlon import LatLon, Latitude, Longitude

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx29" to choose the level
    s.send(b'levelx29')

    # Receive the challenge
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Convert the bytes to a string
    coord_string = data2.decode('utf-8')
    print(f"This are the coordinates in string form:\n{coord_string}")

    # Separate the string into a list
    coord_list = coord_string.split()
    print(f"This is the string coverted to a list\n{coord_list}")

    # Extract the numbers
    lat1 = int(coord_list[1])
    lon1 = int(coord_list[3])
    lat2 = int(coord_list[-3])
    lon2 = int(coord_list[-1])
    print(f"These are the raw coordinates:\n{lat1} {lon1} {lat2} {lon2}")

    # Creating the location objects
    location1 = LatLon(Latitude(lat1), Longitude(lon1))
    location2 = LatLon(Latitude(lat2), Longitude(lon2))
    print(f"These are the two location objects:\n{location1}\n{location2}")

    # Calculating the distance
    distance = location1.distance(location2)
    print("This is the distance between location1 and location2:")
    print(distance)

    # Format the number to three decimal places
    rounded_distance = round(distance, 3)
    print(f"This the rounded distance:\n{rounded_distance}")

    # Convert the float into a string, then the string into bytes
    distance_string = str(rounded_distance)
    bytes = distance_string.encode('utf-8')
    print(f"This is the distance converted into bytes:\n{bytes}")

    # Send the challenge back
    print('Sending challenge.')
    s.send(bytes)

    # Receive the flag
    print('Receiving flag')
    data4 = s.recv(1024)
    print(data4)
