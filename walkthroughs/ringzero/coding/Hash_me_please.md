# URL
https://ringzer0ctf.com/challenges/13
# Concept
* contacting webpages with code
* isolating data based on patterns
* hashing
# Method of solve
* we need to write a script which retrieves the contents of a webpage
* the webpage is asking us to sha512 hash a string of data, then send it back as a URL parameter to another webpage
* this script should do the trick
```
#!/usr/bin/env/ python3
import requests
import hashlib

url = "http://challenges.ringzer0ctf.com:10013/"

send_url = "http://challenges.ringzer0team.com:10013/?r="

# Get the server response
response = requests.get(url)

# Isolate the data we want to transform
text = response.text
text_list = text.split()
longest_item = max(text_list, key=len)
formatted_item = longest_item[:-3]

# Convert the string to bytes
bytes_data = formatted_item.encode('utf-8')

# Run the hash function on the data
hash_object = hashlib.sha512(bytes_data)
hex_digest = hash_object.hexdigest()

# Send the response back to the webpage
full_url = send_url + hex_digest
flag_response = requests.get(full_url)
print(flag_response.text)
```
