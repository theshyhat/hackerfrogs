# Target user
nina, but not specified
# Method of solve
Login to MariaDB and dump the table with the usernames and passwords, then compare the users between the ones in the table and the ones in the /etc/passwd file. 
# Key commands
mysql -u celeste -p
show databases;
use XXX;
show tables;
select * from YYY;
