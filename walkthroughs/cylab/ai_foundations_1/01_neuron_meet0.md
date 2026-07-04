# URL
https://learn.cylabacademy.org/library/771
# Concept
* enumerating perceptron input / output relationships
# Method of solve
* in this exercise, we're required to have the perceptron device output firing neurons (value 1) or not (value 0) in a specific sequence:
```
01110000
```
* so we test the perceptron to see which numbers output 1, and which ones output 0
* from testing, all negative numbers from `-10` to `-1`, all output `0`
* the numbers `0` and `1` also output `0`
* the numbers `2` to `10` output `1`
* so we can input the following sequence to create required pattern and solve the exercise
```
-10,2,3,4,1,0,-1,-2
```




