# password
XIyBbRwAPt
# Concept
* binary to ASCII output
# Method of solve
* run the binary
* multiple strings of binary are output, separated by spaces
* we can convert these strings to binary using Python:
```
./bin | python3 -c "import sys; print(''.join(chr(int(x, 2)) for x in sys.stdin.read().split()))"
```
