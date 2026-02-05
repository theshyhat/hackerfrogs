# SSH Command / Password
ssh the-shadows_level1@api.wargames.batamladen.com -p 10481 Enter_The_Shadows
# Concept
* looking at bash history
# Method of solve
* if we look at the `.bash_history` file, we will see previous commands executed on the terminal that our user account did in the past
```
cat .bash_history
```
* we see that among the commands there is a command to enter the `/opt` directory, then a command to read the `flag.txt` file
```
cat /opt/flag.txt
```

