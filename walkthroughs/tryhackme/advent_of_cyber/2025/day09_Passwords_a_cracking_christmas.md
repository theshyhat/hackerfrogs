# URL
https://tryhackme.com/room/attacks-on-ecrypted-files-aoc2025-asdfghj123
# Concept
Password cracking
# Method of solve
## Q1 - What is the flag inside the encrypted PDF?
```
pdf2john flag.pdf > pdf.hash
```
```
john --wordlist=/usr/share/wordlists/rockyou.txt pdf.hash
```

`naughtylist`

```
xdg-open flag.pdf
```

## Q2 - What is the flag inside the encrypted zip file?

```
zip2john flag.zip > zip.hash
```
```
john --wordlist=/usr/share/wordlists/rockyou.txt zip.hash
```

`winter4ever`

```
7z x flag.zip
```

