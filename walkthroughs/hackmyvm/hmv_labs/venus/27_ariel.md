# Target user
lola
# Method of solve:
Access a temporary file created by the VIM text editor, and extract a list of potential passwords, then brute force the login of the next user using that list of passwords
# Key commands:
hydra -s 5000 -l lola -P passwords.txt venus.hackmyvm.eu ssh
