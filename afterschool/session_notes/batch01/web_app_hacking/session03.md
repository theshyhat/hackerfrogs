# HackerFrogs AfterSchool - Web App Hacking Basics
## Session 3 - Source Code Analysis and Local File Inclusion

# TryHackMe.com signup (we'll be using this website this week)
https://tryhackme.com/
# JS Linux Webshell Link
https://bellard.org/jslinux/vm.html?cpu=riscv64&url=fedora33-riscv.cfg&mem=256
## Command used to create example directories
mkdir -p test/test2/test3
# Natas CTF Links and Passwords
## Natas Level 6
http://natas6.natas.labs.overthewire.org/
#### username: natas6
#### password: 0RoJwHdSKWFTYR5WuiAewauSuNaBXned
## Natas Level 7
http://natas7.natas.labs.overthewire.org/
#### username: natas7
#### password: bmg8SvU1LizuWjx3y7xkNERkHxGre0GS
## Natas Level 8
http://natas8.natas.labs.overthewire.org/
#### username: natas8
#### password: xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q
```
<?

$secret = "3d3d516343746d4d6d6c315669563362";

function decodeSecret($secret) {
    return base64_decode(strrev(hex2bin($secret)));
}

echo(decodeSecret($secret));

?>
```

# This session's challenges
## Local Authority
https://play.picoctf.org/practice/challenge/278?category=1&page=1&search=local
#### YouTube walkthrough
https://youtu.be/25fClMxe2PU

## Forbidden Paths
https://play.picoctf.org/practice/challenge/270?category=1&page=1&search=forb
#### YouTube walkthrough
https://youtu.be/TtE16u_8c2I

## dont-use-client-side
https://play.picoctf.org/practice/challenge/66?category=1&page=1&search=dont
#### YouTube walkthrough
https://youtu.be/dPdGcCnfJ44
