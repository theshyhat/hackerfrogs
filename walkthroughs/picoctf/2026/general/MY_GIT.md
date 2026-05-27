# URL
https://learn.cylabacademy.org/library/764
# Concept
* pushing a Git commit
# Method of solve
* we need to push a Git commit to finish this challenge
* we can do so by running the following 6 commands, in order:
```Bash
echo 'give me the flag' > flag.txt
git config user.email "root@picoctf"
git config user.name "root"
git add flag.txt
git commit -a -m "added flag.txt file"
git push
```
