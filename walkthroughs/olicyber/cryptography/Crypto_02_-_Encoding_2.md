# URL
https://training.olicyber.it/challenges#challenge-327
# Concept
* hexadecimal to ASCII encoding
# Method of solve
* we're asked to convert a hexadecimal string to bytes / ASCII characters
## CyberChef
* In the `Input` window, paste the hexadecimal string
* Apply the `From Hex` operation, by searching it in the `Operations` search bar, then drag it into the `Recipe` window
* the flag for the challenge can be found in the `Output` window
## Linux
```
echo '666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d' | xxd -r -p
```
## Python
```Python
hex_string = '666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d'

flag_bytes = bytes.fromhex(hex_string)

print(flag_bytes)
```
