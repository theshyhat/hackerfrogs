# URL
https://hack.arrrg.de/challenge/75
# Category
General
# Concept
* search for specific strings inside of files
* grep is your friend
# Method of solve
* use the following Linux commands to download the file, unzip it, and search for the "answer"
```
wget https://hack.arrrg.de/chals/raffle.zip
unzip raffle.zip
cd raffle
grep -r . -e "answer"
```
