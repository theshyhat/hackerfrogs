# URL
https://play.picoctf.org/practice/challenge/530
# Concept
* hidden strings in metadata
# Method of solve
* download the file
* examine the file with `exiftool`
* note that there is a weird string listed as the `author`
* decode the string from base64
```
echo -n 'cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jOTk5ZTJhNH0\075' | base64 -d
```
