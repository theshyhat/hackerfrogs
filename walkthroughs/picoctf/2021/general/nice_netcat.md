# URL
https://learn.cylabacademy.org/library/156
# Concept
* accessing services on arbitrary port numbers with netcat
* decimal ASCII encoding
# Method of solve
* When we use `netcat` to access the service, we receive a list of numbers, separated by line-breaks
* If we save this output to a file, we can try decoding it
## With CyberChef
* In the `Input` window, click on the `Open file as input` button
* Apply the `From Decimal` operation, by searching it in the `Operations` search bar, then dra it into the `Recipe` window
* in the `Recipe` window, click on the `Delimiter` button, and select `Line feed`
## With Python
```Python
with open("output.txt", "r") as f:
    num_list = f.read().splitlines("\n")

chars = ""

for i in num_list:
    chars = chars + (chr(int(i)))

print(chars)
```
## With Bash
```
awk '{ printf "%c", $1 }' output.txt
```
