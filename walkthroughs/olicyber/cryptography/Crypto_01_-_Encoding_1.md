# URL
https://training.olicyber.it/challenges#challenge-326
# Concept
* encoding decimal numbers to ASCII
* intro to encoding
# Method of solve
## CyberChef
* In the `Input` window, paste the number list (without the square brackets)
* Apply the `From Decimal` operation, by searching it in the `Operations` search bar, then drag it into the `Recipe` window
* the flag for the challenge can be found in the `Output` window
## Linux
```
echo '102, 108, 97, 103, 123, 117, 103, 104, 95, 78, 117, 109, 66, 51, 114, 53, 95, 52, 49, 114, 51, 52, 100, 121, 125' | tr "," "\n" | awk '{ printf "%c", $1 }'
```
## Python
```Python
num_list = [102, 108, 97, 103, 123, 117, 103, 104, 95, 78, 117, 109, 66, 51, 114, 53, 95, 52,>

flag_string = ""

for i in num_list:
  flag_string = flag_string + chr(i)

print(flag_string)
```
