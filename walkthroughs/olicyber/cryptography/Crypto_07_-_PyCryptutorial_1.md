# URL
https://training.olicyber.it/challenges#challenge-332
# Concept
* using Python to encrypt / decrypt:
  * DES
  * AES256
  * ChaCha20
# Method of solve
```Python
from Crypto.Cipher import DES, AES, ChaCha20
from Crypto.Util.Padding import pad

file_path = "crypto07.txt"

with open(file_path, 'r') as file:
  raw_input = file.readlines()

stripped_input = []

for i in raw_input:
  stripped_input.append(i.strip())

cipher = ""
key_hex = ""
plaintext = ""
padding_style = ""
seg_size = ""
block_size = 0
nonce_hex = ""
ciphertext_hex = ""

for i in stripped_input:
  if i.startswith("Cipher"):
    cip_str = i.split("=")[1]
    cipher = cip_str.replace("'", "").strip()
  if i.startswith("Segment size"):
    seg_str = i.split("=")[1]
    seg_size = int(seg_str.replace("'", "").strip())
  if i.startswith("key.hex"):
    hex_str = i.split("=")[1]
    key_hex = hex_str.replace("'", "").strip()
  if i.startswith("plaintext"):
    plain_str = i.split("=")[1]
    plaintext = plain_str.replace("'", "").strip()
  if i.startswith("Padding scheme"):
    pad_str = i.split("=")[1]
    padding_style = pad_str.replace("'", "").strip()
  if i.startswith("ciphertext"):
    ciptxt_str = i.split("=")[1]
    ciphertext_hex = ciptxt_str.replace("'", "").strip()
  if i.startswith("Nonce"):
    nonce_str = i.split("=")[2]
    nonce_hex = nonce_str.replace("'", "").strip()

key = bytes.fromhex(key_hex)
iv = bytes.fromhex("0000000000000000")
aes_iv = bytes.fromhex("00000000000000000000000000000000")
aes_key = "000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f"

plaintext_bytes = plaintext.encode("utf-8")

def des_encrypt():
  padded_plaintext = pad(
    plaintext_bytes,
    DES.block_size,
    style=padding_style.strip()
  )

  cipher = DES.new(
    key,
    DES.MODE_CBC,
    iv=iv
  )

  ciphertext = cipher.encrypt(padded_plaintext)
  print("DES Encryption Hex:\n" + ciphertext.hex())

def aes_encrypt():
  cipher = AES.new(
    key,
    AES.MODE_CFB,
    iv=aes_iv,
    segment_size=seg_size
  )
  padded_plaintext = pad(
    plaintext_bytes,
    block_size,
    style=padding_scheme
  )
  ciphertext = cipher.encrypt(padded_plaintext)
  print("AES Encryption Hex:\n" + ciphertext.hex())

def chacha20_decrypt():
  ciphertext = bytes.fromhex(ciphertext_hex)
  nonce = bytes.fromhex(nonce_hex)
  cipher = ChaCha20.new(key=key,nonce=nonce)
  plaintext_bytes = cipher.decrypt(ciphertext)
  plaintext = plaintext_bytes.decode("ascii")
  print("ChaCha20 decryption:\n" + plaintext)

if cipher == "DES":
  des_encrypt()
elif cipher == "AES256":
  padding_scheme = "pkcs7"
  key_hex = aes_key
  key = bytes.fromhex(key_hex)
  block_size = 16
  aes_encrypt()
else:
  chacha20_decrypt()
```
