# We might want to create a Python virtual environment to
# install the Python pwn package
# python -m venv myenv
# cd myenv
# source bin/activate
# pip install pwn

from pwn import xor

# Hexadecimal string
hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

# Convert the hex string to bytes
data = bytes.fromhex(hex_string)

# Brute-force single-byte XOR
for key in range(256):  # Possible values for a single byte (0x00 to 0xFF)
    result = xor(data, key)
    try:
        # Attempt to decode the result as an ASCII string
        decoded = result.decode('ascii')
        if all(32 <= ord(c) <= 126 for c in decoded):  # Check for printable characters
            print(f"Key: {key}, Message: {decoded}")
    except UnicodeDecodeError:
        # Ignore decoding errors for non-ASCII results
        continue

# print(xor(data, chr(16)).decode('ascii'))
