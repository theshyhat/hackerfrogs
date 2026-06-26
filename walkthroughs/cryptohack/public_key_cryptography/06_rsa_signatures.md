# URL
https://cryptohack.org/courses/public-key/rsa_starter_6/
# Concept
* digitally signing a message with RSA
# Method of solve
* How can you ensure that the person receiving your message knows that you wrote it?
* You've been asked out on a date, and you want to send a message telling them that you'd love to go, however a jealous lover isn't so happy about this.
* When you send your message saying yes, your jealous lover intercepts the message and corrupts it so it now says no!
* We can protect against these attacks by cryptographically signing the message.
* Imagine you write a message `m`. You encrypt this message with your friend's public key: `c = (m ** e) % N`
* To sign this message, you calculate the hash of the message: `H(m)` and "encrypt" this with your private key: `S = (H(m) ** d) % N`​.
* Your friend can decrypt the message using their private key: `m = (c ** d) % N`​. Using your public key they calculate `s = (S ** e) % N`​.
* Now by computing `H(m)` and comparing it to `s: assert H(m) == s`, they can ensure that the message you sent them, is the message that they received! As long as your private key is safe, no one else could have signed this message!
* Sign the flag `crypto{Immut4ble_m3ssag1ng}` using your private key and the SHA256 hash function.
* This Python script will get the job done:
```Python
from hashlib import sha256
from Crypto.Util.number import bytes_to_long

values = {}

with open("private_0a1880d1fffce9403686130a1f932b10.key", "r", encoding="utf-8") as f:
  for line in f:
    line = line.strip()
    if not line or "=" not in line:
      continue

    key, value = line.split("=", 1)
    key = key.strip()
    value = value.strip()
    values[key] = int(value)

N = values["N"]
d = values["d"]

flag = b"crypto{Immut4ble_m3ssag1ng}"

h = sha256(flag).digest()
h_int = bytes_to_long(h)

signature = pow(h_int, d, N)

print(f"Flag value: {flag}\n")
print(f"Flag hash: {h}\n")
print(f"Signature hex representation:\n{hex(signature)}\n")
print(f"Signature decimal representation:\n{signature}")
```
