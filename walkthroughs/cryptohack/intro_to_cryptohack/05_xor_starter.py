# We might want to create a Python virtual environment to
# install the Python pwn package
# python -m venv myenv
# cd myenv
# source bin/activate
# pip install pwn

from pwn import xor

# Define our variables for XOR operation
encrypted_bytes = b"label"
key_integer = 13

# perform the XOR operation, then decode to ASCII characters
xor_result = xor(encrypted_bytes, key_integer).decode()

print(f"{encrypted_bytes} XOR {key_integer} equals {xor_result}")

