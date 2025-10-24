# URL
https://leetcode.com/problems/convert-the-temperature/description/?envType=problem-list-v2&envId=ew2tef8s
# Instructions
You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.

You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].

Return the array ans. Answers within 10-5 of the actual answer will be accepted.

Note that:

    Kelvin = Celsius + 273.15
    Fahrenheit = Celsius * 1.80 + 32.00

# Concept
* conversion of numbers from one system to another
# Code
```
class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        ans = [kelvin, fahrenheit]
        return ans

example_temp = 36.50

solve = Solution()
run = solve.convertTemperature(celsius=example_temp)
print(run)
```
