# URL
https://training.olicyber.it/challenges#challenge-78
# Concept
* RSA cryptosystem - flawed implementation
* close p / q values - Fermat factorization attack
# Method of solve
* we're given the following information with the challenge:
* this is `ct.txt`
```
n= 146652948863107767915515696389262268647958080423363432809510595078682568112085519929016552006340132750260244391442650419716209388476887752518821948643355769332931080957723170703642823372471212059667069985712741031890734368079274545006791082030796999444978356751235369237849185209094420930556569139123564127723
e= 65537
ct= 29866550050067643692473619455049192140190479758069897252295829267390344690107747214634468574079853475351608563312052986143110232253489826549882185837122231695139253296376749571108533659993018491393797757794110130200246559684585596096579385116077972392131805016636133672522654864012092864459984453971252224283
```
* how this is generated, the `challenge.py` script, looks like this:
```Python
from sympy import *
from Crypto.Util.number import getStrongPrime


def getPrime():
    p=getStrongPrime(512)
    q=nextprime(p)
    return p,q


f=open("flag.txt","r")
flag=f.readline()
f.close()
flag=int(flag.encode().hex(),16)

e=65537

p,q=getPrime()
n=p*q 
fi=(p-1)*(q-1)
d=pow(e,-1,fi)
ct=pow(flag,e,n)

print("n=", n)
print("e=",e)
print("ct=",ct)
```
* the unsafe implentation of RSA is demonstrated in these lines of code:
```Python
def getPrime():
    p=getStrongPrime(512)
    q=nextprime(p)
    return p,q
```
* the security of RSA hinges on the fact that the `p` and `q` values (and therefore the `n` value) are hard to determine through factorization
* the fact that this script creates `p` and `q` values that are close to one another exposes it to an attack called the Fermat Factorization attack:
  * which is possible if the difference between the two numbers `p` and `q` is relatively small (Fermat can be used in other circumstances, but this is one of them)
* we can use this script to factorize the `N` value and break the RSA encryption:
```Python
import math
from sympy import mod_inverse
from Crypto.Util.number import long_to_bytes

N= 146652948863107767915515696389262268647958080423363432809510595078682568112085519929016552006340132750260244391442650419716209388476887752518821948643355769332931080957723170703642823372471212059667069985712741031890734368079274545006791082030796999444978356751235369237849185209094420930556569139123564127723
e= 65537
ct= 29866550050067643692473619455049192140190479758069897252295829267390344690107747214634468574079853475351608563312052986143110232253489826549882185837122231695139253296376749571108533659993018491393797757794110130200246559684585596096579385116077972392131805016636133672522654864012092864459984453971252224283

def fermat_factor(N):
    # Step 1: Start just above the square root of N
    a = math.isqrt(N) + 1
    
    while True:
        # Step 2: Calculate b^2
        b2 = a**2 - N
        b = math.isqrt(b2)
        
        # Step 3: Check if it's a perfect square
        if b*b == b2:
            p = a - b
            q = a + b
            return p, q
        a += 1
            
# If an attacker has N and the public exponent e, they get the private key:
p, q = fermat_factor(N)
phi = (p - 1) * (q - 1)
d = mod_inverse(e, phi)

# Decrypt the ciphertext
m = pow(ct,d,N)
b = long_to_bytes(m)

# Print the plaintext
print(f"The plaintext is: {b}")
```
