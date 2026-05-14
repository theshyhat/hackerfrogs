# URL
https://hackropole.fr/en/challenges/forensics/fcsc2019-forensics-not-so-fat/
# Concept
* recovery of files from a disk image
* cracking zip file hashes
# Method of solve
* use the `mmls` tool from `Sleuthkit` to figure out if there are multiple partitions on this disk image
```
mmls not-so-fat.dd
```
* there are not, so we should list out the contents of the disk image with the `fls` tool
```
fls -r -p not-so-fat.dd
```
* there is a `flag.zip` file on the disk image, which we can extract using the `icat` tool
```
icat not-so-fat.dd 6 > flag.zip
```
* the zip file is password protected, but we can try to crack the password with `John the Ripper`
```
zip2john flag.zip > zip.hash
john --wordlist=/usr/share/wordlists/rockyou.txt zip.hash
```
* Done!



