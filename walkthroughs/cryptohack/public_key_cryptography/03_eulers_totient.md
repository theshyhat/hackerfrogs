# URL
https://cryptohack.org/courses/public-key/rsa_starter_3/
# Concept
* reversing the factorization of the N value in RSA
* Euler's totient
# Method of solve
* RSA relies on the difficulty of the factorisation of the modulus `N` (`N = p * q`, where `p` and `q` are co-prime)
* If the prime factors can be deduced, then we can calculate the Euler totient of `N` and thus decrypt the ciphertext
* Given `N = p * q` and two primes (`p = 857504083339712752489993810777`, and `q = 1029224947942998075080348647219`):
  * what is the Euler's totient of `N`?
* We can calculate the Euler's totient for `N` with the following formula: `ϕ(N)= ϕ(pq) = (p−1)(q−1)`
  * so if we have some simple prime numbers for `p` and `q`, `3` and `5`, respectively, then:
  * `ϕ(15) = ϕ(3 * 5) = (3−1)(5−1)` which is `8`
    * the breakdown of this equation involves creating a list of all numbers from `1` to `N` (1 to 15)
    * then removing all numbers that are multiples of the `p` and `q` values, which means
    * all numbers which are divisible by `3`, and all numbers that are divisible by `5`
    * which means from a list of numbers from `1` to `15`
      * we remove `3, 6, 9, 12, and 15` (numbers divisible by `3`)
      * and we remove `5, 10, and 15` (numbers divisible by `5`)
      * after removal of all of those numbers, we are left with `1, 2, 4, 7, 8, 11, 13, and 14`, which is `8` numbers
* the way to calculate a Euler's totient with Python is:
```Python
def phi(n):
    # Start with the assumption that all numbers from 1 to n are coprime to n.
    # We will subtract off the numbers that share a prime factor with n.
    result = n

    # Begin checking possible prime factors starting from the smallest prime, 2.
    p = 2

    # We only need to test factors up to sqrt(n), because if n has a factor larger
    # than sqrt(n), the matching factor must be smaller than sqrt(n) and would
    # already have been found.
    while p * p <= n:
        # If p divides n, then p is a prime factor of n.
        if n % p == 0:
            # Remove every copy of this prime factor from n.
            # This leaves us with the remaining part of n after eliminating p.
            while n % p == 0:
                n //= p

            # Apply Euler's totient update for this distinct prime factor:
            # result = result * (1 - 1/p)
            # Using integer arithmetic, we write it as:
            # result -= result // p
            result -= result // p

        # Move on to the next possible factor.
        p += 1

    # After the loop, if n is still greater than 1, then the remaining n itself
    # is a prime factor larger than sqrt(original_n), so we must account for it.
    if n > 1:
        result -= result // n

    # The final result is the count of numbers from 1 to original_n that are
    # coprime to original_n.
    return result
```
* but there's an even simpler Python script which we can use if we know the values of `p` and `q`:
```Python
def phi_from_pq(p, q):
    return (p - 1) * (q - 1)
```

