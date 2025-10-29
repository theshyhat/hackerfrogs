# URL
https://hack.arrrg.de/challenge/348
# Category
* cryptography
# Concept
* obfuscating data
* reverse engineering
# Method of solve
* we are given a Python script that decrypts a message
* when we look at the code inside the script, it appears to be a series of:
  * encoding a string into base64
  * that string decodes into a zlib compressed file
  * which is encoded in base64
  * which is a zlib compressed file
  * etc etc
