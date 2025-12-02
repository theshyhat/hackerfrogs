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
* in the `Documents` directory in this user's home directory, there is an encrypted file
* we can use this GPG command to decrypt it:
```
gpg --decrypt mcskidy_note.txt.gpg
```
* we are given instructions to replace the `/home/socmas/2025/wishlist.txt` file contents with this list:
```
Hardware security keys (YubiKey or similar)
Commercial password manager subscriptions (team seats)
Endpoint detection & response (EDR) licenses
Secure remote access appliances (jump boxes)
Cloud workload scanning credits (container/image scanning)
Threat intelligence feed subscription

Secure code review / SAST tool access
Dedicated secure test lab VM pool
Incident response runbook templates and playbooks
Electronic safe drive with encrypted backups
```
* after we've this we can access the website being hosted locally on port 8080
* once there, we see a string that we need to decrypt using OpenSSL
```
U2FsdGVkX1/7xkS74RBSFMhpR9Pv0PZrzOVsIzd38sUGzGsDJOB9FbybAWod5HMsa+WIr5HDprvK6aFNYuOGoZ60qI7axX5Qnn1E6D+BPknRgktrZTbMqfJ7wnwCExyU8ek1RxohYBehaDyUWxSNAkARJtjVJEAOA1kEOUOah11iaPGKxrKRV0kVQKpEVnuZMbf0gv1ih421QvmGucErFhnuX+xv63drOTkYy15s9BVCUfKmjMLniusI0tqs236zv4LGbgrcOfgir+P+gWHc2TVW4CYszVXlAZUg07JlLLx1jkF85TIMjQ3B91MQS+btaH2WGWFyakmqYltz6jB5DOSCA6AMQYsqLlx53ORLxy3FfJhZTl9iwlrgEZjJZjDoXBBMdlMCOjKUZfTbt3pnlHWEaGJD7NoTgywFsIw5cz7hkmAMxAIkNn/5hGd/S7mwVp9h6GmBUYDsgHWpRxvnjh0s5kVD8TYjLzVnvaNFS4FXrQCiVIcp1ETqicXRjE4T0MYdnFD8h7og3ZlAFixM3nYpUYgKnqi2o2zJg7fEZ8c=
```
* the previous encrypted txt file gave us an unlock key to use to decrypt this message `UNLOCK_KEY: 91J6X7R4FQ9TQPM9JX2Q9X2Z`
* it also gives us the command syntax that we could use to decrypt the message:
```
openssl enc -d -aes-256-cbc -pbkdf2 -iter 200000 -salt -base64 -in /tmp/website_output.txt -out /tmp/decoded_message.txt -pass pass:'91J6X7R4FQ9TQPM9JX2Q9X2Z'
cat /tmp/decoded_message.txt
```
* we got a flag after we read the decrypted file `THM{w3lcome_2_A0c_2025}`
* the decrypted file also tells us that we can decrypted the secret directory in this endpoint `/home/eddi_knapp/.secret` to get access to the side quest
* this gpg command will unlock the file
```
gpg --out dir.tar.gz --decrypt dir.tar.gz.gpg
gunzip dir.tar.gz
tar -xvf dir.tar
```
* once unzipped, there is a `dir` directory
* and inside that directory there is a png file
```
xdg-open sq1.png
```
* the image has a message `now_you_see_me`
