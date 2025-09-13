# URL
https://training.olicyber.it/challenges#challenge-256
# Concept
* list out a binary's linked libraries
# Method of solve
* the `ldd` command can be used on a binary to list out its linked libraries
```
ldd ./sw-02 | cut -d ' ' -f 1 | awk 'length <= 2' | tr -d '\t' | tr -d '\n'
```
