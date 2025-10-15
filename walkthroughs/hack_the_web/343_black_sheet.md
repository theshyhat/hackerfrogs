# URL
https://hack.arrrg.de/challenge/343
# Category
General
# Concept
* identifying outlying patterns in data
# Method of solve
* most of the file in this challenge contains the 0x2d byte, which is `-` in ASCII
* we can use the `xxd` program to get a hex dump of the file
```
xxd Challenge343.txt
```
* we see most of the file has these hex contents `2d2d 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d`
* to see which lines in the file don't have this pattern, we can pipe the `xxd` output to the `grep` command
```
xxd Challenge343.txt | grep -v ": 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d"
```
* in the output, we see that the anomolous data happens on this address: `35d0`. We can convert it using another Linux command
```
echo $((0x35d0))
```
* we also need to take in account that the different bytes occur 6 characters into the line
* the answer is `13776 + 6 = 13782`
