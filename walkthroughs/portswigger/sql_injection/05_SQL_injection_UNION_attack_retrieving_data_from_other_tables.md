# URL
https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables
# Concept
* using UNION select SQL injection to retrieve columns from other tables in the database
# Method of solve
* select the filter in the search page
* tack the UNION select payload onto the end of the URL:
```
' UNION SELECT null,null -- - 
```
* this returns data, which means we have two columns to work with for UNION select attack:
* this lab lets us know that there are two columns, `username` and `password` in another table called `users`
* this means we craft a payload like the following:
```
' UNION SELECT username,password from users -- -
```
* in the data returned, there are usernames and passwords
* copy the `administrator` users's password and login in to finish the lab

