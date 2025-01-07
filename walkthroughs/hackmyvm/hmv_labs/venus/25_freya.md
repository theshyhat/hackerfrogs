Target user: alexa
Method of solve: Write a loop which constantly reads an empty directory, but read all the file contents when a file exists there
Key command:
while true; do [ -f /free/* ] && cat /free/*; sleep 1; done
