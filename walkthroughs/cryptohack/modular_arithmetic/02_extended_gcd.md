# URL
https://cryptohack.org/courses/modular/egcd/
# Concept
* extended GCD algorithm
# Instructions
Let `a` and `b` be positive integers.

The extended Euclidean algorithm is an efficient way to find integers `u`,`v` such that
```
a⋅u+b⋅v=gcd(a,b)
```
Using the two primes p=`26513`,q=`32321`, find the integers `u`,`v` such that
```
p⋅u+q⋅v=gcd(p,q)
```
Enter whichever of `u` and `v` is the lower number as the flag.
# Method of solve
```Python
'''
This program calculates the GCD (Greatest Common Divisor) of two numbers
as well as the GCD's Bezout coefficients. The program runs through
rounds as it runs through the calculations and prints out the values
in each round
'''

def ex_gcd(a, b):
  # keep track of the original a and b values to print later
  start_a = a
  start_b = b
  # we'll keep track of each round of calculation, starting at 1
  round = 1
  # x and y are Bezout coefficients for a
  x = 0
  y = 1
  # u and v are Bezout coefficients for b
  u = 1
  v = 0
  # these initial coefficient values are for the original values before
  # any calculations are done
  # b = (x * a) + (y * b) or (b * 1 + a * 0)
  # a = (u * a) + (v * b) or (b * 0 + a * 1)

  # Run Euclid's algorithm until a = 0
  # In each round: a will become b,
  # and b will become the remainder of a divided by b 
  # When a becomes zero, the value of b is the
  # GCD value of a and b
  while a != 0:
    # printing out our current values
    print(f"Round: {round}")
    print(f"a={a}, b={b}")
    print("Bezout coefficients:")
    print(f"y={y}, x={x}")
    print(f"u={u}, v={v}")
    print(f"{b} = ({x} x {a}) + ({y} x {b})")
    print(f"{a} = ({u} x {a}) + ({v} x {b})")
    # do the Euclid algorithm calculation
    # q is the integer division between b and a
    q = b // a
    # r is the remainder after b is divided by a
    r = b % a

    # update the Bezout coefficients
    # m is the value for the new x coefficient
    m = x - u * q
    # n is the value for the new y coefficient
    n = y - v * q

    # update all the values
    b = a
    a = r
    x = u
    y = v
    u = m
    v = n

    # increase the round so we can print all the new stuff
    round += 1

  # after all the calculations are done, b is the GCD value
  gcd = b

  # return the GCD and the Bezout coefficients
  print(f"The GCD of {start_a} and {start_b} is {gcd}")
  print(f"It's Bezout coefficients are {x} and {y}")
  return gcd, x, y

ex_gcd(26513,32321)
```
