# URL
https://training.olicyber.it/challenges#challenge-257
# Concept
* binary sections
# Method of solve
* the first thing to do is get the names of the sections in binary:
```
objdump -h sw-03
```
* there is reference to a `.super-secret-section` in the output
* the next thing we need to do is get the contents of the `.super-secret-section`
```
objdump -s -j .super-secret-section sw-03
```
