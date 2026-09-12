# URL
https://training.olicyber.it/challenges#challenge-79
# Concept
* RSA cryptosystem - flawed implementation
  * small e value
  * lack of padding on the ciphertext
* cube root attack
# Method of solve
* we're given the following values:
```
n= 121188535871798118811428322495136173485838157702837603009744079502828661170574654643712519826693731103670617468427120197687519224611728159372629028899279680740201176466228593180097000630667826923128885153190352359299571456927587933797154384731664367396394374086703053646510220882981791309024543386831488440013
e= 3
ct=56274920108133183710879347789095782313165243853788407193317419375243717146801757114129876005705242550492379484281774120724787040219649340446091878053221949541
```
* the `e` value is very small, and the `ct` value also seems very small, so this setup might be vulnerable to a cube-root attack
* the cube-root attack is a cryptographic attack that can be performed under the following cirumstances:
  * the `e` value is 3
  * the `n` value is at least 3-times larger than the (`m` ** `e`) or (`ct` ** `e`) values
    * the `n` value has to be large enough so that the the modulo operation between the `c^e` value does nothing
  * if this applies, we can calculate the cube-root of the `ct` value to arrive at the original `m` value:
* this Python script performs the attack
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
n = 121188535871798118811428322495136173485838157702837603009744079502828661170574654643712519826693731103670617468427120197687519224611728159372629028899279680740201176466228593180097000630667826923128885153190352359299571456927587933797154384731664367396394374086703053646510220882981791309024543386831488440013

# 3. Standard RSA Encryption: c = (m^e) % N
# Because secret_message^3 is smaller than N, the % N does nothing.
ct = 56274920108133183710879347789095782313165243853788407193317419375243717146801757114129876005705242550492379484281774120724787040219649340446091878053221949541
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



