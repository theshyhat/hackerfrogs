# WORK IN PROGRESS
# URL
https://cryptohack.org/courses/public-key/modulus_inutilis/
# Concept
* RSA cube root attack
# Method of solve
* this implementation of RSA is vulnerable to a cube root attack, which would let us decrypt the message without calculating the `d` value (from the private key)
* in order for this attack to work, we require the following:
  * a small `e` value (e.g., 3)
  * a small `m` message / `ct` ciphertext (such that `m` < (N / 3))
  * an absence of padding (which would increase the length of the message) (e.g, OAEP or PKCS#1 v1.5)
```Python
from Crypto.Util.number import long_to_bytes

def integer_cube_root(c):
    """Finds the exact integer cube root of a massive integer using binary search."""
    low = 0
    high = c
    
    while low <= high:
        mid = (low + high) // 2
        cube = mid ** 3
        
        if cube == c:
            return mid  # Exact root found
        elif cube < c:
            low = mid + 1
        else:
            high = mid - 1
            
    return None  # Not a perfect cube (the attack failed because m^3 > N)

# --- Simulation of the Attack ---

# 1. Vulnerable RSA Setup (e=3, large N)
e = 3
n = 17258212916191948536348548470938004244269544560039009244721959293554822498047075403658429865201816363311805874117705688359853941515579440852166618074161313773416434156467811969628473425365608002907061241714688204565170146117869742910273064909154666642642308154422770994836108669814632309362483307560217924183202838588431342622551598499747369771295105890359290073146330677383341121242366368309126850094371525078749496850520075015636716490087482193603562501577348571256210991732071282478547626856068209192987351212490642903450263288650415552403935705444809043563866466823492258216747445926536608548665086042098252335883

# 3. Standard RSA Encryption: c = (m^e) % N
# Because secret_message^3 is smaller than N, the % N does nothing.
ct = 243251053617903760309941844835411292373350655973075480264001352919865180151222189820473358411037759381328642957324889519192337152355302808400638052620580409813222660643570085177957
print(f"Intercepted Ciphertext: {ct}")

# 4. The Cube Root Attack
# We ignore N entirely and take the integer cube root of the ciphertext
decrypted_message = integer_cube_root(ct)
decrypted_bytes = long_to_bytes(decrypted_message)
if decrypted_message:
    print(f"\n[SUCCESS] Attack completed!")
    print(f"Recovered Plaintext: {decrypted_bytes}")
else:
    print("\n[FAILED] The ciphertext wrapped around the modulus. Message was too large.")
```
