# Target user
leona
# Method of solve
We needed to identify a password hash type, and then crack the hash using a password cracking program
# Key commands
john --format=md5crypt --wordlist=/usr/share/wordlists/rockyou.txt leona.hash
