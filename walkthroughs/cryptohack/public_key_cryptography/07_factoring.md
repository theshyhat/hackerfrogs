# URL
https://cryptohack.org/courses/public-key/rsa_factoring/
# Concept
* calculating prime factors
# Method of solve
* So far we've been using the product of small primes for the modulus, but small primes aren't much good for RSA as they can be factorised using modern methods.
* Factorise the 150-bit number `510143758735509025530880200653196460532653147` into its two constituent primes. Give the smaller one as your answer.
* the first method we could use is a website that has pre-calculated factors: `http://factordb.com`
* the other method involves using a Python script with the `sympy` module:
```Python
from sympy import primefactors

number = 510143758735509025530880200653196460532653147
print(primefactors(number))
```
* we can also use the recommended module for doing the prime factorization:
```
pip install git+https://github.com/elliptic-shiho/primefac-fork@master
python -m primefac -v 510143758735509025530880200653196460532653147
```



