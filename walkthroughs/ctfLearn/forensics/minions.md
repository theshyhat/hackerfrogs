# URL
https://ctflearn.com/challenge/955
# Concept
* embedded files
* base64-encoded strings
# Method of solve
* download the image from the link
* use `strings` to inspect the file
```
strings Hey_You.png
```
* we see another link near the end of the `strings` output
```
https://mega.nz/file/wZw2nAhS#i3Q0r-R8psiB8zwUrqHTr661d8FiAS1Ott8badDnZkoH
```
* after downloading this file, we can look at `strings` again, and we see reference to a jpg file..
```
strings Only_Few_Steps.jpg
```
* if we use `xxd`, we can identify where this file is referenced in the bytes of the file:
```
xxd Only_Few_Steps.jpg | grep YouWon -C 3
```
* this lets us know that the file could be a Rar file:
```
unrar e Only_Few_Steps.jpg
```
* and then we look at the `strings` of the file again
```
strings -8 'YouWon(Almost).jpg'
```
* this points us to a base64-encoded string
* we have to decode it about 4 times before we get the flag:
```
echo -n 'VmtaU1IxUXhUbFZSYXpsV1RWUnNRMVpYZEZkYWJFWTJVVmhrVlZGVU1Eaz0=' | base64 -d | base64 -d | base64 -d | base64 -d
```



