# username / password
leviathan2 / NsN1HwFoyN
# concept
* more SUID binaries :D
# method of solve
* the SUID binary in this level does a privilged file read with `/bin/cat` to read a file specfied in the command arguments
* by default, it won't read any files that belong to the `leviathan3` user, which is our target user
