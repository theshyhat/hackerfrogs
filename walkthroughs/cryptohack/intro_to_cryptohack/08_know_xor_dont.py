# We might want to create a Python virtual environment to
# install the Python pwn package
# python -m venv myenv
# cd myenv
# source bin/activate
# pip install pwn

from pwn import xor

encrypted_bytes = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e26345>

# We know that the flag will begin with the following string
key_bytes = b"crypto{"

print(xor(encrypted_bytes, key_bytes).decode())

# Uncomment this portion after discovering the XOR key
# xor_key_bytes = b"myXORkey"
# print(xor(encrypted_bytes, xor_key_bytes).decode())
