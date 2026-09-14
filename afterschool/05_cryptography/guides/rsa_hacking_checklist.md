# WORK IN PROGRESS
# RSA Security Flaws Checklist
## E value is small
### If E is 1
* the encryption doesn't do anything to the ciphertext if the E value is one
* the ciphertext and the plaintext will be the same
### If E is 3
* if E is 3 and:
  * the ciphertext is significantly smaller than N ((`ct` ** 3) < `n`)
  * there is no padding involved
* then the ciphertext will be vulnerable to a `cube root attack`
## If the P and Q Values are Known
## If N is Monoprime
## If N is Multiprime
## If the Square Root of N is Too Close To The Next Square Root Value (N+1)
* if this is the case, then N may be vulnerable to the Fermat Factorization Attack:
  * here are a few different methods for testing the N value:
    * "simple" method which calculates distance:
```Python
import math

N= 146652948863107767915515696389262268647958080423363432809510595078682568112085519929016552006340132750260244391442650419716209388476887752518821948643355769332931080957723170703642823372471212059667069985712741031890734368079274545006791082030796999444978356751235369237849185209094420930556569139123564127723

# Step 1: Find the floor of the square root
root = math.isqrt(N)

# Step 2: Check the "distance" to the next perfect square
next_square = (root + 1) ** 2
distance = next_square - N

print(f"The distance between N and the next square is: {distance}")
      ```
### If N is Comprised of Close Primes P and Q
```
    * checking whether the values used in creating N share too many bits:
```Python
import math

N= 146652948863107767915515696389262268647958080423363432809510595078682568112085519929016552006340132750260244391442650419716209388476887752518821948643355769332931080957723170703642823372471212059667069985712741031890734368079274545006791082030796999444978356751235369237849185209094420930556569139123564127723

def check_fermat_bit_vulnerability(N):
    """
    Checks if an RSA modulus N is vulnerable to Fermat's Factorization
    based on the Bit-Length Difference Rule (|p - q| <= N^0.25).
    """
    # 1. Determine the total bit length of the modulus
    bit_length = N.bit_length()
    
    # 2. Calculate the baseline integer square root of N
    a_start = math.isqrt(N) + 1
    
    # 3. Calculate b^2 for the first possible 'a' value
    b2 = a_start**2 - N
    
    # 4. Calculate the vulnerability threshold (N^0.25) expressed in bits
    # For a 2048-bit key, this threshold is 512 bits.
    threshold_bits = bit_length // 4
    
    # 5. Extract the effective bit length of 'b'
    # Since b2 = a^2 - N, the bit length of b is roughly half the bit length of b2.
    b_bit_length = (b2.bit_length() + 1) // 2
    
    print(f"[*] Modulus Bit Length: {bit_length}-bit")
    print(f"[*] Fermat Closeness Threshold: {threshold_bits} bits")
    print(f"[*] Calculated 'b' Bit Length: ~{b_bit_length} bits")
    
    # Evaluation based on the cryptographic rule
    if b_bit_length < threshold_bits:
        print("\n[+] VULNERABLE: The primes share too many bits.")
        print(f"    Fermat's attack will succeed within roughly 2^{2 * (threshold_bits - b_bit_length)} iterations.")
        return True
    else:
        print("\n[-] SECURE AGAINST FERMAT: Primes do not share an insecure number of upper bits.")
        return False

check_fermat_bit_vulnerability(N)
```
    * checking using the Gmpy2 module:
```Python
import gmpy2

N= 146652948863107767915515696389262268647958080423363432809510595078682568112085519929016552006340132750260244391442650419716209388476887752518821948643355769332931080957723170703642823372471212059667069985712741031890734368079274545006791082030796999444978356751235369237849185209094420930556569139123564127723

def is_fermat_target(N, max_trials=50000):
    # Start just above the square root of N
    a = gmpy2.isqrt(N) + 1
    
    for i in range(max_trials):
        b2 = a**2 - N
        if gmpy2.is_square(b2):
            print(f"✅ VALID TARGET: Factored in {i} iterations!")
            p = a - gmpy2.isqrt(b2)
            q = a + gmpy2.isqrt(b2)
            return True, (int(p), int(q))
        a += 1
        
    print(f"❌ NOT A TARGET: Primes are sufficiently far apart (checked {max_trials} values).")
    return False, None

is_fermat_target(N)
```
