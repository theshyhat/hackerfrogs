# URL
https://training.olicyber.it/challenges#challenge-265
# Concept
* using the `strace` command to inspect system calls made by child processes
# Method of solve
* use the `strace` command with the `-f` flag to output system calls by child processes
```
strace -f ./sw-11
```

