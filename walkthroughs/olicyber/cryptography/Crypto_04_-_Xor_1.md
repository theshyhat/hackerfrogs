# URL
https://training.olicyber.it/challenges#challenge-329
# Concept
* XOR
# Method of solve
* the challenge tasks us with doing a XOR string operator between two hexadecimal strings
* we can use the following Python script to get that done:
```
# Creating the XOR function for bytes
def xor(a, b):
    # List to be populated by XORed bytes
    result = []
    # Loop to XOR the bytes together and add them to the result list
    for x, y in zip(a, b):
        result.append(x ^ y)
    return bytes(result)

# Hex strings
m1 = "158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf"
m2 = "73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2"

# Hex bytes
m1bytes = bytes.fromhex(m1)
m2bytes = bytes.fromhex(m2)

# Create the bytes to be printed
result_bytes = xor(m1bytes, m2bytes)

# Print the result
print(f"The result of a XOR operation between the string:\n{m1}\nand the string:\n{m2}\nis the following:\n{result_bytes}")
```
