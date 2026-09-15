# URL
https://cryptohack.org/courses/public-key/dh-starter-1/
# Concept
* working with fields
* Diffie-Helman
# Instructions
```
The set of integers modulo NN, together with the operations of both addition and multiplication forms a ring Z/NZZ/NZ. Fundamentally, this means that adding or multiplying any two elements in the set returns another element in the set.

When the modulus is prime: N=pN=p, we are additionally guaranteed a multiplicative inverse of every element in the set, and so the ring is promoted to a field. In particular, we refer to this field as a finite field denoted FpFp​.

The Diffie-Hellman protocol works with elements of some finite field FpFp​, where the prime modulus is typically very large (thousands of bits), but for the following challenges we will keep numbers smaller for compactness.

Given the prime p=991p=991, and the element g=209g=209, find the inverse element d=g−1d=g−1 such that g⋅dmod  991=1g⋅dmod991=1. 
```
# New Terminology
$\mathbb{F}_p^\times$
* this is `F sub p times` or `the multiplicative group of the finite field F p`
* 
# Method of solve
* we're given a prime number `p = 991` and an element `g = 209`
* we're asked to return the inverse element `d = g ** -1`
* such that `(g * d) % 991 = 1`
* so basically, we can use the `pow` function in Python to get our answer `pow(g,-1,p)`
