# URL
https://ringzer0ctf.com/challenges/75
# Concept
* Local File Inclusion (LFI)
# Method of solve
* this app is vulnerable to LFI through the landing page's `page` URL parameter
* we can send this payload, which is typical of LFI testing, to find out if it is vulnerable or not
```
../../../../../../../etc/passwd
```
* the flag is in the contents of the `passwd` file
