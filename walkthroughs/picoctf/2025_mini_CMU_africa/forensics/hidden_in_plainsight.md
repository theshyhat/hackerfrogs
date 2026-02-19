# URL
https://play.picoctf.org/practice/challenge/524
# Concept
* image forensics
* steganography
* steghide tool
# Method of solve
* download the file
* if we look at the metadata, there's some base64-encoded info in the comment field
```
exiftool img.jpg
```
* if we decode this base64 string, it gives us an important clue as to how to solve the challenge:
```
echo 'c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9' | base64 -d
```
* this lets us know that steganography is involved, because it points to a common steganography tool called `steghide`
* we also need to decode the password for the steghide program:
```
echo 'cEF6endvcmQ=' | base64 -d
```
* the last step is to extract information from the jpg file using the `steghide` program:
```
steghide extract -sf img.jpg -p pAzzword
```

