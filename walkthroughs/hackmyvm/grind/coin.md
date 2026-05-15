# URL
https://hackmyvm.eu/hmvgrind/c01n.php
# Concept
* database forensics
* SQLite system interaction
# Method of solve
* we need to use SQLite commands to interact with the database file and get the answers to the questions
## Question 1: How many unique users (case sensitive) are there?
* use the sqlite3 program to interface with the database file:
```
sqlite3 c0in.db
```
* from here, we need to use sqlite syntax to find the info we're looking for
```
.tables
```
* this lets us know there is a `users` table
* the second thing we should do is figure the columns in the `users` table
```
.schema users
```
* and finally, we can get the count for the the `email` column, and use the `distinct` filter, and that should return the number of users
```
select count(distinct email) from users;
```
## Question 2: It appears the credits are corrupted, but you must find the total sum of those successfully transferred.
* we need to look at the `transactions` table
```
.schema transactions
```
* we're interested in looking at the `amount` and `status` columns
```
select amount, status from transactions;
```
* we should get the possible status values
```
select status from transactions group by status;
```
* we're only interested in the rows where the status is `completed`
```
select amount, status from transactions where status == "completed";
```
* we're looking at the correct rows, but we have to sum all of the numbers in the `amount` column, but we also need to replace all of the `€` symbols with empty strings to make all the input consistent
```
select sum(replace(amount, '€', '')) from transactions where status == "completed";
```
## Question 3: What is the ID of the user who has generated the most successful transactions?
* for this question, we need to pay attention to the `user_id` and `status` columns in the `transactions` table
* 








