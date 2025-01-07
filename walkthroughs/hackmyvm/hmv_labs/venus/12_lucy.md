# Target user
elena
# Method of solve
we need to isolate a string in a file between some specific characters
# Key command
```
sed -n 's/.*fu\([^<]*\)ck.*/\1/p' file.yo
```
