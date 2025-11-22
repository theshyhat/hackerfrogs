# URL
https://ringzer0ctf.com/challenges/32
# Concept
* contacting webpages
* extracting strings from data
* converting numbers from different bases
# Method of solve
* we presented with three numbers on the webpage, one in decimal, one in hexadecimal, and one in binary
* we need to perform a math operation between all three numbers and send back the result
* this script will get the job done
```
#!/usr/bin/env/ python3
import requests

url = "http://challenges.ringzer0ctf.com:10032/"
send_url = "http://challenges.ringzer0team.com:10032/?r="

begin_string = "----- BEGIN MESSAGE -----"
end_string = "----- END MESSAGE -----"

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
extracted = extract_between(text, begin_string, end_string)
extract_list = extracted.split()

# Define our numbers
dec_num = extract_list[2]
hex_num = extract_list[4]
bin_num = extract_list[6]

# Convert the numbers to decimal
hex_to_dec = int(hex_num, 16)
bin_to_dec = int(bin_num, 2)

print(f"This is the decimal number: {dec_num}\nthis is the hexadecimal number: {hex_num}\nThis is the binary number: {bin_num}")
print(f"This is the hex number converted to decimal: {hex_to_dec}\nThis is the binary number converted to decimal: {bin_to_dec}")

# Do the math
math_op = int(dec_num) + hex_to_dec - bin_to_dec
print(f"{dec_num} + {hex_to_dec} - {bin_to_dec} = {math_op}")

# Send the response back to the webpage
full_url = send_url + str(math_op)
flag_response = requests.get(full_url)
print(flag_response.text)
```
