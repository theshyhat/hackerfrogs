# URL
https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-multiple-values-in-single-column
# Concept
* retrieving multi-column information from a single column in a UNION select SQL attack
# Method of solve
* set the filter category in the app landing page
* paste the UNION select payload on the end of the address:
```
' UNION SELECT null,null -- -
```
* we get data back, so we know this is the correct number of columns
* next, we need to figure out which columns can return string data
* use this payload to figure out of the first column can hold string data:
```
' UNION SELECT 'a',null -- -
```
* this results in an error, which means we should test the other column
```
' UNION SELECT null,'a' -- -
```
* this returns back, so we know we need to leak data with UNION using the second column
* because we only have one column to work with, we need to concatenate the username and password data from the UNION attack into a single column
* the way we concatenate is different, depending on the DBMS being used
* so the next payload we use will test for the version of DBMS
```
' UNION SELECT null,version() -- -
```
* the resulting data lets us know that the DBMS is PostGreSQL, and we can supply an appropriate payload to get the username / password columns into a single column
```
' UNION SELECT null,username || ':' || password FROM users -- -
```
* the resulting response lets us know the `administrator` user's password
* use it to login to the app to finish the challenge
