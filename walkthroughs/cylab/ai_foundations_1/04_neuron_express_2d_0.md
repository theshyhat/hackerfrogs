# URL
https://learn.cylabacademy.org/library/770
# Concept
* enumerating and solving the possible weight and bias values for a perceptron
# Method of solve
* this is a more difficult version of the previous challenge, because we're dealing with double the number of inputs
* the formula for whether the perceptron fires or not is this:
```
w1*x + w2*y + b >= 0 -> 1, else 0
```
* in this formula:
  * `w1` is the weight for the `x` input
  * `w2` is the weight for the `y` input
  * `b` is the bias
  * `x` and `y` are both user inputs
* when testing, it seemed like any number put in the `y` coordinate didn't affect whether the perceptron fired or not
  * so we conclude that the `w2` value is `0`
* the threshold for whether the result was `1` or `0` after inputs seemed to be `x=2` (doesn't fire) and `x=3` (does fire)
* this leads us to believe that an accurate value for `w1` `w2` and `b` would be:
```
w1 = 2, w2 = 0, b = -5
```



