# URL
https://cryptohack.org/courses/modular/gcd/
# Concept
* greatest common divisors (GCD)
# Instructions
The Greatest Common Divisor (GCD), sometimes known as the highest common factor, is the largest number which divides two positive integers (a,b)(a,b).

For a=12,b=8a=12,b=8 we can calculate the divisors of aa: {1,2,3,4,6,12}{1,2,3,4,6,12} and the divisors of bb: {1,2,4,8}{1,2,4,8}. Comparing these two, we see that gcd⁡(a,b)=4gcd(a,b)=4.

Now imagine we take a=11,b=17a=11,b=17. Both aa and bb are prime numbers. As a prime number has only itself and 11 as divisors, gcd⁡(a,b)=1gcd(a,b)=1.

We say that for any two integers a,ba,b, if gcd⁡(a,b)=1gcd(a,b)=1 then aa and bb are coprime integers.

If `a` and `b` are prime, they are also coprime. If `a` is prime and `b` < `ab` < `a` then `a` and `b` are coprime.

There are many tools to calculate the GCD of two integers, but for this task we recommend looking up Euclid's Algorithm.

Try coding it up; it's only a couple of lines. Use a=12,b=8 to test it.

Now calculate gcd⁡(a,b)gcd(a,b) for a=66528,b=52920a=66528,b=52920 and enter it below. 
# Notes
* the GCD is the largest number that divides evenly into two integers
* this is a good introduction to the modulo operation, which returns the remainder after division
  * the module operator in Python is `%`, and an example equation is `9 % 4 = 1`, since the remainder after dividing 9 by 4 is 1.
* The  
# Method of solve
* this first Python script serves to teach the concepts of the GCD function while it runs:
```Python
'''
This program defines how to determine the Greatest Common Divisor (GCD) between two numbers.
That is, the largest number that can evenly divide both numbers
'''

def gcd(a, b):
    start_a = a
    start_b = b
    round = 1
    if a == b:
        print('A and B are equal. Quitting...')
        return
    print(f"Initial values: a: {a}, b: {b}")
    if b > a:
        print('B is larger than A: Reversing values...')
        new_a = b
        new_b = a
        a = new_a
        b = new_b
        print(f"New values - a: {a} b: {b}")
    print("\nIn each round, we divide a by b, but only return the remainder of the division.")
    print("Then b becomes a in the next round, and the division remainder becomes b.")
    print("We repeat this process until the remainder from dividing a by b is zero.")
    print("When that happens, the b value in that round is the GDC of the initial a and b values.\n")
    while True:
        mod_result = a % b
        print(f"Round {round}: a={a}, b={b}, division remainder result is {mod_result}.")
        a, b = b, a % b
        if b == 0:
            print(f"The GCD of {start_a}, and {start_b} is {a}")
            return a
        round += 1
```

* there is a GCD function in Python's `Math` module:
```Python
import math

a = 66528
b = 52920

result = math.gcd(a, b)
print(result)
```
