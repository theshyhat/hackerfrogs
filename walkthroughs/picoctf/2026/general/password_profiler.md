# URL
https://learn.cylabacademy.org/library/712
# Concept
* building a custom user password list using CUPP
* password hash cracking
# Method of solve
* we're given a sha1 hash
* we need to crack it using a custom password list
* we can use cupp.py

`https://github.com/Mebus/cupp`

* run the script and insert the following details
```
First Name: Alice
Surname: Johnson
Nickname: AJ
Birthdate: 15-07-1990
Partner's Name: Bob
Child's Name: Charlie
```
* after creating the password list, we can crack the password using John the Ripper
```
john --wordlist=./passwords.txt --format=raw-sha1 ./hash.txt
```
* to confirm the password, we can confirm the hash by hashing the password
```
printf '%s' 'Aj_15901990' | sha1sum
968c2349040273dd57dc4be7e238c5ac200ceac5  -
```
* and compare it to the hash we have
```
cat hash.txt   
968c2349040273dd57dc4be7e238c5ac200ceac5
```
* lastly, we write the password into a file and run the password checker script on it to get the flag
```
echo -n 'Aj_15901990' > passwords.txt
python check_password.py
```

