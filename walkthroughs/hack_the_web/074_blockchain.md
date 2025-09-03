# URL
https://hack.arrrg.de/challenge/74
# Category
Programming
# Concept
* we need to identify a number which will create a specific MD5 hash when it is appended to a specific string `hacktheweb`
* this is somewhat similar to how `proof of work` is achieved for the blockchain
# Method of solve
* we can create a Python script that hashes each one of the iterations of the string + number, and prints out the number if it matches the pattern
```
import hashlib

string = "hacktheweb"
sub_string = "000000"

for i in range(1000000000):
  new_string = string + str(i)
  new_bytes = new_string.encode('utf-8')
  # Create an MD5 hash object
  md5_hash_object = hashlib.md5(new_bytes)
  # Get the hexadecimal representation of the hash
  md5_hex_digest = md5_hash_object.hexdigest()
  print(md5_hex_digest)
  if md5_hex_digest.startswith(sub_string):
    print(f"Match found!\n{i}")
    break
```
* the answer is `1688157`
