# URL
https://training.olicyber.it/challenges#challenge-329
# Concept
* XOR
# Method of solve
* the challenge tasks us with doing a XOR string operator between two hexadecimal strings
* we can use the following Python script to get that done:
```
def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

# Hex string
m1 = "158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf"
m2 = "73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2"

# Hex bytes
m1bytes = bytes.fromhex(m1)
m2bytes = bytes.fromhex(m2)

print(xor(m1bytes, m2bytes))
```
