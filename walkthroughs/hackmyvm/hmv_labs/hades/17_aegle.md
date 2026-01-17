# username
aegle
# password
YRturIymmHSdBmEClEGe
# mission contents
User calliope likes to have her things looked at.
# method of solve
* in this level we have `sudo` permissions with the `cat` command as the `calliope` user
* because this is a `privileged file read` vulnerability we're taking advantage of, we can leverage an common technique for `local file inclusion`
* try to read the `calliope` user's `ssh` private key...
```
sudo -u /pwned/calliope/.ssh/id_rsa
```
