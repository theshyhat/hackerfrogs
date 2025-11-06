# URL
https://hack.arrrg.de/challenge/330
# Category
OSINT
# Concept
* learning about the Beatles discography
# Method of solve
* we are given a list of Beatles album abbreviations and a track number. The full list looks like this:
```
LIBN#10
PPM#5
BFS#3
RA#16
YSS#1
LATHB#7
L#18
LIB#3
RS#1
```
* the password is made of the first letters of the songs from abbreviated albums
* for example, `LIBN#10` is the 10th song from the album `Let it be Naked`, which is `Across the Universe`, which would be the letter `A`
* we repeat this with all of the song / album abbreviations, and get the answer `ABBEYROAD`

