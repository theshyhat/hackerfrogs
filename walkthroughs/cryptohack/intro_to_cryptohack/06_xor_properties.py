# We might want to create a Python virtual environment to
# install the Python pwn package
# python -m venv myenv
# cd myenv
# source bin/activate
# pip install pwn

from pwn import xor

# Hex values (from challenge description)
key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key2_xor_key1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
key2_xor_key3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
flag_xor_keys = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

# Compute key2
key2 = xor(key1, key2_xor_key1)

# Compute key3
key3 = xor(key2, key2_xor_key3)

# Compute flag
key1_xor_key2 = xor(key1, key2)
key1_xor_key2_xor_key3 = xor(key1_xor_key2, key3)
flag = xor(key1_xor_key2_xor_key3, flag_xor_keys)

# Output flag as an ASCII string
print(flag.decode())
