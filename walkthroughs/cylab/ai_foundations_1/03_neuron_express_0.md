# URL
https://learn.cylabacademy.org/library/769
# Concept
* enumerating possible variable values for perceptron function
# Method of solve
* in this challenge, we've given the formula for whether a perceptron fires or doesn't fire:
```
w*x + b >= 0 -> 1, else 0
```
* in this formula:
  * `w` is weight
  * `x` is the input
  * `b` is the bias
* the challenge wants us to test a perceptron and determine what it's `w` and `b` values are, given we can input specific values for `x`
* when we test the perceptron, we find that that `x=1` doesn't fire, and `x=2` does fire
* that means that some combination of `w=1` and `b=-2` is a valid answer, there are multiple combinations of `w` and `b` that also work
