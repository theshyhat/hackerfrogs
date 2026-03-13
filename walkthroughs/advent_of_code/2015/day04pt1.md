# URL
https://adventofcode.com/2015/day/4
# Concept
* searching for specific strings in datasets
* MD5 hashing
# Instructions
--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

    If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
    If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

Your puzzle input is yzbqklnj.

# Code
```Python
import hashlib

key_value = "yzbqklnj"
the_answer = ""

def generate_md5_hash(data_string):
  # Encode the string into bytes (e.g., using UTF-8)
  encoded_string = data_string.encode('utf-8')

  # Create an MD5 hash object and update it with the encoded string
  md5_hash = hashlib.md5(encoded_string)

  # Return the hash in a human-readable hexadecimal format
  return md5_hash.hexdigest()

for i in range(10000000):
  combined_string = key_value + str(i)
  hashed_string = generate_md5_hash(combined_string)
  if hashed_string.startswith("00000"):
    the_answer = i
    print(f"The answer is {the_answer}")
    print(f"This is the hash value:\n{hashed_string}")
    break

if the_answer == "":
  print("No match found in range")
```






