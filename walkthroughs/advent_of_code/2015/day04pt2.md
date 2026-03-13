# URL
https://adventofcode.com/2015/day/4
# Concept
* searching for specific strings in datasets
* MD5 hashing
# Instructions
--- Part Two ---

Now find one that starts with six zeroes.

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

for i in range(100000000):
  combined_string = key_value + str(i)
  hashed_string = generate_md5_hash(combined_string)
  if hashed_string.startswith("000000"):
    the_answer = i
    print(f"The answer is {the_answer}")
    print(f"This is the hash value:\n{hashed_string}")
    break

if the_answer == "":
  print("No match found in range")
```






