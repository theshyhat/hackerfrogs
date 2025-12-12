# URL
https://tryhackme.com/room/azuresentinel-aoc2025-a7d3h9k0p2
# Concept
* Azure log inspection
# Method of solve
# Task 5
## Q1 - How many entities are affected by the Linux PrivEsc - Polkit Exploit Attempt alert?
* in the `Incidents` window, use the search field at the upper-right corner of the window
* type in `Polkit`
* select one of the `Linux PrivEsc - Polkit Exploit Attempt` events
* click on the `Alerts` tab, located to the right of the `Attack Story` tab
* observe the number of `Impacted assets`
## Q2 - What is the severity of the Linux PrivEsc - Sudo Shadow Access alert?
* in the `Incidents` window, use the search field at the upper-right corner of the window
* type in `Shadow`
* select one of the `Linux PrivEsc - Sudo Shadow Access` events
* note the adjective under the ID number at the top of the page
## Q3 - How many accounts were added to the sudoers group in the Linux PrivEsc - User Added to Sudo Group alert?
* in the `Incidents` window, use the search field at the upper-right corner of the window
* type in `User Added`
* select the `Linux PrivEsc - User Added to Sudo Group` event
* note the number of users in the `Incident graph` window
# Task 6
## Q1 - What is the name of the kernel module installed in websrv-01?
* in the `Logs` window, click on the `Simple Mode` dropdown box and select `KQL Mode`
* in the resulting search window, paste in the following query:
```
set query_now = datetime(2025-10-30T05:09:25.9886229Z);
Syslog_CL
| where host_s == 'websrv-01'
| project _timestamp_t, host_s, Message
| where Message contains "insert_module"
```
* click the blue `Run` button
* observe the file name on the last entry on the lowest results window
## Q2 - What is the unusual command executed within websrv-01 by the ops user?
* change the query to the following:
```
set query_now = datetime(2025-10-30T05:09:25.9886229Z);
Syslog_CL
| where host_s == 'websrv-01'
| project _timestamp_t, host_s, Message
| where Message contains "ops"
```
* click the blue `Run` button
## Q3 - What is the source IP address of the first successful SSH login to storage-01?
* change the query to the following:
```
set query_now = datetime(2025-10-30T05:09:25.9886229Z);
Syslog_CL
| where host_s == 'storage-01'
| project _timestamp_t, host_s, Message
| where Message contains "ssh"
```
* click the blue `Run` button
## Q4 - What is the external source IP that successfully logged in as root to app-01?
* change the query to the following:
```
set query_now = datetime(2025-10-30T05:09:25.9886229Z);
Syslog_CL
| where host_s == 'app-01'
| project _timestamp_t, host_s, Message
| where Message !contains "10."
| where Message !contains "198."
| where Message !contains "172."
| where Message contains "root"
| where Message contains "ssh"
```
* click the blue `Run` button
## Q5 - Aside from the backup user, what is the name of the user added to the sudoers group inside app-01?
* change the query to the following:
```
set query_now = datetime(2025-10-30T05:09:25.9886229Z);
Syslog_CL
| where host_s == 'app-01'
| project _timestamp_t, host_s, Message
| where Message contains "added to group 'sudo'"
| where Message !contains "backup"
```
* click the blue `Run` button
