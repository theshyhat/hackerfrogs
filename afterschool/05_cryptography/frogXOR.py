from pwn import xor

message_bytes = b"frogCTF{XOR_some_XOR_all}"

key_bytes = b"hackfrog"

cipher_bytes = (xor(message_bytes, key_bytes))

cipher_hex = cipher_bytes.hex()

print(f"The ciphertext hex string is {cipher_hex}")

# If we know partial content of the plaintext,
# and we know the ciphertext, we can determine what the key is.

partial_plaintext = b"frogCTF{"

# We know that for this CTF, all of the flags start with frogCTF{,
# so that's the partial plaintext we'll use to determine the key, which is...

print(xor(cipher_bytes, partial_plaintext))
