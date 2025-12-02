# URL
from day 1
# Concept
* hunting around a Linux filesystem
# Method of solve
* we are given credentials `eddi_knapp:S0mething1Sc0ming`
* we are supposed to use this account to find the fragments for the password
* we are given this set of clues
```
There are three hidden easter eggs.
They combine to form the passcode to open my encrypted vault.

Clues (one for each egg):

1)
I ride with your session, not with your chest of files.
Open the little bag your shell carries when you arrive.

2)
The tree shows today; the rings remember yesterday.
Read the ledger’s older pages.

3)
When pixels sleep, their tails sometimes whisper plain words.
Listen to the tail.

Find the fragments, join them in order, and use the resulting passcode
to decrypt the message I left. Be careful — I had to be quick,
and I left only enough to get help.
```
* the first clue is referencing the `env` variables for a user session in Linux
* type in `env`, and we'll see the first password fragment in the variable values:
```
3ast3r
```
* the second clue is referencing `git` repositories, and we can look for a repository that this user has access to
* the directory we're supposed to look in is `/home/eddi_knapp/.secret_git`
* and we use this command to see the git logs:
```
git log -p
```
* the second fragment is:
```
-1s-
```
* the third clue is referencing pixels, which could mean digital pictures, and there's a `Pictures` directory for our user
* in that directory there is a `.easter_egg` file that we can read to get the final part of the password
```
c0M1nG
```
* the entire password is `3ast3r-1s-c0M1nG`
* in the `.secrets` directory in this user's home directory, there is an encrypted file
* 

