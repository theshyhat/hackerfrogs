# username
anthea
# password
yWFLtSNQArEBTHtWgkKd
# objective
User aphrodite is obsessed with the number 94.
# method of solve
The SUID binary uses the MYID environment variable. But the binary isn't looking for the exact number in the MYID variable, but rather its value when converted to ASCII decimal values. The character associated with ASCII decimal is the carat character
```
export MYID=^; ./obsessed
cat aphrodite_pass.txt
```
