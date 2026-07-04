# URL
https://learn.cylabacademy.org/library/772
# Concept
* enumerating 2D perceptron input / output relationship
# Method of solve
* this is the same as the previous challenge, except that we supply a pair of numbers instead of a single number
* first, we enumerate for the value `1` (firing)
  * the following ranges result in the the value `1`:
  * all ranges from `5,0` to `10,0`
  * all ranges from `0,3` to `0,10`
* then we need to enumerate coordinates that result in value `0` (not firing)
  * all negative numbers in the x range `-1,0` to `-10,0`
* the goal of the exercise is to have the perceptron fire and not in a pattern that matches:
```
01110000
```
* in this system, we can use the following series of numbers to achieve this end:
```
(-1,0),(5,0),(6,0),(7,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0)
```



