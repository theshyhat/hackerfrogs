# URL
https://ringzer0ctf.com/challenges/56
# Concept
* compare hash values to known data
* hash cracking
# Method of solve
* we are given a webpage and asked to crack a hash in the webpage's text
* we have send back the original value of the data before the hashing
* the hashing method used is SHA1, and the value of the data is four-digit numbers
* we confirm this by cracking a few of the hashes using the `crackstation` web app
* this script will compare the hash against a dictionary of known hashes that we create within the script:
```
#!/usr/bin/env/ python3
import requests
import hashlib

url = "http://challenges.ringzer0ctf.com:10056/"
send_url = "http://challenges.ringzer0team.com:10056/?r="

begin_string = "----- BEGIN HASH -----"
end_string = "----- END HASH -----"

start_num = 0
stop_num = 9999
width = 4

def get_key_from_value(dictionary, target_string):
    for key, value in dictionary.items():
        if value == target_string:
            return key
    return None

# Create the number list
num_list = []

for number in range(start_num, stop_num + 1):
    formatted_string = f"{number:0{width}d}"
    num_list.append(formatted_string)

# Create the dictionary of numbers / sha1 hashes
num_hash_dict = {}

for number in num_list:
    # Convert the string to bytes
    bytes_data = number.encode('utf-8')

    # Run the hash function on the data and match it with the numbers
    hash_object = hashlib.sha1(bytes_data)
    hex_digest = hash_object.hexdigest()
    # Add the entry to the dictionary
    num_hash_dict[number] = hex_digest

def extract_between(text, start_str, end_str):
    start_index = text.find(start_str)
    if start_index == -1:
        return None  # Start string not found
    end_index = text.find(end_str, start_index + len(start_str))
    if end_index == -1:
        return None  # End string not found after start string
    return text[start_index + len(start_str):end_index]

# Get the server response
response = requests.get(url)

# Isolate the data we want to transform
text = response.text
extracted_chunk = extract_between(text, begin_string, end_string)
formatted_hash = extracted_chunk.replace(" ", "").replace("<br/>", "").strip()

# Compare the string to the entries in the dictionary
correct_hash = get_key_from_value(num_hash_dict, formatted_hash)

# Send the response back to the webpage
full_url = send_url + correct_hash
flag_response = requests.get(full_url)
print(flag_response.text)
```
