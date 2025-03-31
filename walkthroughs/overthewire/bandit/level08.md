# Username
bandit8
# Password
dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
# Method of solve
Locate the line in the file that occurs only once. Use the sort command to organize the data in the groups, then the uniq command with the -c flag to output the number of times each line appears in the file, then the sort command again to return the least occuring lines at the end of the list.
```
sort data.txt | uniq -c | sort
```
