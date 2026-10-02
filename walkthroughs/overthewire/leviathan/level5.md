# Password
Bub9gZ3BGU
# Concept
* understanding symbolic links
# Method of solve
* when we run the binary it shows us an error message because the `/tmp/file.log` file doesn't exist
* when we create the file in the `/tmp` directory, we re-run the binary and it reads the contents of the file
* we want to read the password for `leviathan6`, and this binary is an SUID binary, which means it should be able to read it
* we can make the `/tmp/file.log` file a symbolic link to the leviathan6 password file so we can read it with the binary:
```
ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log
```
* then run the leviathan5 binary and you're done




