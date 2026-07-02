# URL
https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text
# Concept
* figuring out which columns in a UNION select attack can return string data
# Method of solve
* click on one of the filters
* in the resulting URL, tack on the following UNION select SQL injection payload
```
' UNION SELECT null,null,null -- - 
```
* this returns data, so we know we have the right number of columns
* next, we need to figure out which column can return string data
* we test the first column
```
' UNION SELECT 'a',null,null -- - 
```
* this results in an error, which means we to test the second column
```
' UNION SELECT null,'a',null -- - 
```
* this time we return data, which means the second column can hold string data
* so we substitute the `a` in the second column with the abitrary string specified at the top of the lab webpage


