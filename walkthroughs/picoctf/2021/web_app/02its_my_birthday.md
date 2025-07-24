# URL
https://play.picoctf.org/practice/challenge/109
# Concept
* hash collisions
* PHP magic hashes
* older versions of PHP are vulnerable to "magic hashes", where hashes of different values are evaluated the same, if they begin with the value `0e`, and the rest of the hash value is entirely made up of numbers
* this means that the following two MD5 hashes are the same, when evaluated by a vulnerable version of PHP:
```
240610708 → 0e462097431906509019562988736854
QNKCDZO → 0e830400451993494058024219903391
```
# Method of solve
* we need to create two files with the `.pdf` extension
* the app only cares if the files have the extension, so we use the following commands to create our magic-hash files:
```
echo -n '240610708' > test1.pdf
echo -n 'QNKCDZO' > test2.pdf
```
