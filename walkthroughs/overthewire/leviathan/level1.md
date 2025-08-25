# username / password
leviathan1 / 3QJ3TgzHDq
# concept
* inspecting the dynamic library calls and system calls used by a process using the `ltrace` command
# method of solve
* there is a `check` SUID binary in the home directory owned by our target user, `leviathan2`
* when we run the `check` binary, it asks us for a password, but we don't know it
* we use the ltrace command to check which dynamic library calls and system calls are used when it is run
* we see that the binary is doing a `strcmp` function that checks the user input against the `sex` value
* when we provide the correct password, we get an /bin/sh shell.
