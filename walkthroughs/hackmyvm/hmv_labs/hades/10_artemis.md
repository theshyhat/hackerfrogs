# username
artemis
# password
HIiaojeORLaJBVSPDDCZ
# mission contents
We need /bin/bash so that the user asia gives us her password.
# method of solve
It seems that the `restricted` binary outputs the password for the next level if the `SHELL` environment variable is set to `/bin/bash`, and it seems like the challenge is currently bugged, and gives us the answer straight away
```
./restricted
```
