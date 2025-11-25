# URL
https://ringzer0ctf.com/challenges/14
# Concept
* hashing binary integers
# Method of solve
```
#!/usr/bin/env/ python3
import requests
import hashlib

url = "http://challenges.ringzer0ctf.com:10014/"

send_url = "http://challenges.ringzer0team.com:10014/?r="

# Get the server response
response = requests.get(url)

# Isolate the data we want to transform
text = response.text
text_list = text.split()
longest_item = max(text_list, key=len)
formatted_item = longest_item[:-3]

# Convert binary string to integer
binary_int = int(formatted_item, 2)

# Calculate hash parameters
byte_length = len(formatted_item) // 8

# Convert the binary integer to bytes
binary_bytes = binary_int.to_bytes(byte_length, byteorder='big')

# Run the hash function on the data
hash_object = hashlib.sha512(binary_bytes)
hex_digest = hash_object.hexdigest()

# Send the response back to the webpage
full_url = send_url + hex_digest
flag_response = requests.get(full_url)
print(flag_response.text)
```
