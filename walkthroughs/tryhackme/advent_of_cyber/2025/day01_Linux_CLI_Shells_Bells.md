# URL
https://tryhackme.com/room/linuxcli-aoc2025-o1fpqkvxti
# Concept
* Linux CLI Basics
# Method of solve
## Q1 - Which CLI command would you use to list a directory?
The answer is `ls`
# The LS Command
The `ls` command is used to list out a directory's contents when using the CLI (command-line interface) terminal.
## Q2 - What flag did you see inside of the McSkidy's guide?
* first use the `ls` command to see what's in the current directory
* then use the `cd` command to enter the Guides directory
```
cd Guides
```
* if we run the `ls` command inside this directory, we won't see anything
* use the following modified `ls` command to see hidden files
```
ls -a
```
* then we can read the hidden file:
```
cat .guide.txt
```
* the answer is `THM{learning-linux-cli}`
# The CD Command
The `cd` command is used to switch between different directories in the filesystem. The syntax is:
```
cd <name_of_directory_to_move_to>
```
# Hidden Files in Linux (also Unix)
In Linux filesystems, any file that begins with the `.` character is considered a hidden file, which will not be returned by the standard `ls` command
# Listing Hidden Files with LS
Hidden files can be listed out using `ls` with the `-a` parameter
# The CAT Command
The `cat` command is used to read files. The syntax is:
```
cat <name_of_file_to_be_read>
```
## Q3 - Which command helped you filter the logs for failed logins?
* the log we're looking for is in the `/var/log` directory
```
cd /var/log
```
* then we can use the `grep` on the `auth.log` file to look for `Failed password` entries in the file
```
grep "Failed password" auth.log
```
* the answer is `grep`
# The GREP Command
The `grep` command is used to return lines in a file that match certain patterns, which you supply to the command. The syntax is:
```
grep <pattern_to_search_for> <file_to_be_searched>
```
## Q4 - What flag did you see inside the Eggstrike script?
* we can find the Eggstrike script using the following find command:
```
find / -name eggstrike.sh 2>/dev/null
```
* then we can read the file:
```
cat /home/socmas/2025/eggstrike.sh
```
* the answer is `THM{sir-carrotbane-attacks}`
# The FIND Command
The `find` command is used to search the filesystem for files matching criteria that the user provides. The syntax is:
```
find <directory_to_search_in> <pattern_key> <pattern_value>
```
There are many patterns we can use with `find`, but a common one to use is `-name`, which searches by the name of the file
# 2>/dev/null Argument
We can add `2>/dev/null` to any command we suspect will output a lot of error messages to redirect any error messages the command produces to the `/dev/null` device
## Q5 - Which command would you run to switch to the root user?
* the answer is `sudo su`
# The SU Command
The `su` command is used to switch between different user accounts. The syntax is:
```
su <user_account_to_switch_to>
```
# The SUDO Command
The `sudo` command is used to run another command in the context of the `root` user, who has the highest level privileges on the system
## Q6 - Finally, what flag did Sir Carrotbane leave in the root bash history?
* to read the root user's bash history file, we can use this command
```
cat /root/.bash_history
```
* the answer is `THM{until-we-meet-again}`
# The .bash_history File
Each user in the Linux filesystem has a file named `.bash_history` in their respective home directory which contains all of the previous commands used by that user in the CLI terminal
