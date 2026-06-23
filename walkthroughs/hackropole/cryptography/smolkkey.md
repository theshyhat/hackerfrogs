# URL
https://hackropole.fr/en/challenges/crypto/fcsc2025-crypto-smolkkey/
# Concept
* RSA with small exponent (e) values
* Cube root attack
# Method of solve
* download the two files
* when we look at the script that created the `smolkkey.txt` file, we see that this is RSA encryption:
```Python
from gmpy2 import powmod as pow
from Crypto.PublicKey import RSA

class Smolkkey:
        def __init__(self):
                k = RSA.generate(2048, e = 3)
                self.pk = (k.n, k.e)
                self.sk = (k.n, k.d)

        def encrypt(self, m):
                n, e = self.pk
                c = pow(m, e, n)
                return int(c)

        def decrypt(self, c):
                n, d = self.sk
                m = pow(c, d, n)
                return int(m)

# Generate a key
E = Smolkkey()

# Encrypt the fag
flag = open("flag.txt", "rb").read()
flag = int.from_bytes(flag, "little")
c = E.encrypt(flag)

# Test decryption
assert flag == E.decrypt(c)

# Output public values
n, e = E.pk
print(f"{n = }")
print(f"{e = }")
print(f"{c = }")
```
* the important thing to pay attention to here is that the `RSA.generate` method that is used to create the RSA keypair:
```
RSA.generate(2048, e = 3)
```
* this indicates that the modulus size of the keypair is 2048 bits, and that the public exponent of the keypair is 3
* since the exponent value is very small (3), we can conduct a cryptographic attack on the RSA keypair called the `cube root attack`
* this script can conduct the attack:
```Python
from sympy import integer_nthroot

# Given values
N = 20828609401338794038836680655046788059251524928933537772275737490132096798900518851229365799426251400151127719543434160180496659560792762761336988343332946920310984844136554433346165529108260963140451576722579583104830933409454682160084747257400706214980238995436388944310800852033141986598424966358149711167942491331040747300866718813771865768701794983365111208518863175847678947437360554933091347604616653687980177405805542214635577758515398014710929022135522835744517328114492844837858920033569071591971676487452812830920525469634367387593309067794509735740140745616085618489218115494716811261406227449967579233657
e = 3
c = 6317668510138686569655374990729607736156413707292408158720036346854309670467296052918552527575331589363290061240725095262980389263184520673983411112154423282089471021996509038472493779143273789325774414352608726252566350689111876373836913240644190951995980896093509379920452743478551321978067299216590452459233562642920123055978471365092000347562228787318105538018723376505390423730687522026043802357456368003656219942603097205774742385485995835519133581552096067468551713114231926639878045212204590071768

# Compute the cube root of c
m, is_perfect_cube = integer_nthroot(c, e)

if is_perfect_cube:
    print("Decrypted plaintext (m):", m)

    byte_length = (m.bit_length() + 7) // 8
    m_bytes = m.to_bytes(byte_length, byteorder='big')
    
    # Decode the bytes to a string (assuming UTF-8 encoding)
    try:
        plaintext = m_bytes.decode('utf-8')
        print("Decrypted text:", plaintext)
    except UnicodeDecodeError:
        print("Failed to decode the bytes as UTF-8. The plaintext may use a different encoding or contain non-text data.")
else:
    print("The ciphertext is not a perfect cube. Further analysis is needed.")
```
* this will give us the plaintext of the flag, but the flag is reversed, because of this part of the code in the encryption script:
```Python
flag = int.from_bytes(flag, "little")
```
* the `int.from_bytes` method is rendering the flag bytes in little endian order (i.e., reverse order)
* all we need to do to get the proper orientation of the flag is to do this:
```
echo -n 'flag_contents' | rev
```

