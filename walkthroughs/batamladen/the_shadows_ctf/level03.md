# SSH Command / Password
ssh the-shadows_level3@api.wargames.batamladen.com -p 5086 La_La_L4nd
# Concept
* looking at running processes
# Method of solve
* look at the note
* the note references processes
* when we see the running processes on the system, we see suspicious one
```
ps -aux
```
* then we take a look at the contents of the script file we saw in the processes:
```
cat /opt/rogue_process.sh
```


