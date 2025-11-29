# URL
https://play.picoctf.org/practice/challenge/400
# Concept
* the Python eval() function
# Method of solve
* the script used in the challenge uses the eval() function to run other functions in the script
```
while(True):
  try:
    print('Try entering "getRandomNumber" without the double quotes...')
    user_input = input('==> ')
    eval(user_input + '()')
```
* because we have user input that is passed to the eval() function, we can force the script to run the win() function, which will output the flag
* unfortunately, the flag is not returned in plaintext, but rather a series of hexadecimal strings that represent ASCII characters
* this script will decode the flag
```
str_o_hex = "0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x62 0x35 0x32 0x33 0x62 0x32 0x61 0x31 0x7d"

list_o_hex = str_o_hex.split()

plaintext = ""

for i in list_o_hex:
  decoded_chr = chr(int(i, 16))
  plaintext += decoded_chr

print(plaintext)
```


