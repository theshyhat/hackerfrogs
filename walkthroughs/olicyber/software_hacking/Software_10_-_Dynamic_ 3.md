# URL
https://training.olicyber.it/challenges#challenge-264
# Concept
* using the `ltrace` command to filter for functions run by the binary
# Method of solve
* use this `ltrace` command to filter on only the `access` functions
```
ltrace -e access ./sw-10
```


