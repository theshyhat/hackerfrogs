# Target user
anna
# Method of solve
Access the comments inside the /etc/passwd file
# Key command
cut -d: -f1,5 /etc/passwd | grep alice
