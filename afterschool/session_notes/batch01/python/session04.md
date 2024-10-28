# HackerFrogs AfterSchool - Python Programming Basics
## Session 04 - Boolean Types and If Conditions
# This Session's Exercises
## fixme2.py
https://play.picoctf.org/practice/challenge/241?originalEvent=69&page=1&search=
YouTube walkthrough:
https://www.youtube.com/watch?v=V0X9yu5WnYc

## Serpentine
https://play.picoctf.org/practice/challenge/251?originalEvent=69&page=1&search=
YouTube walkthrough:
https://www.youtube.com/watch?v=7j5_Sj9Ftpg

# learnpython dot org links
## Conditions
https://learnpython.org/en/Conditions

# End of Session Exercise Code
```
print("I will tell you if a number is even or odd!")
number = input('Enter a number:')
if (number % 2) == 0:
  print(f'{number} is an even number!')
if (number % 2) == 1:
  print(f'{number} is an odd number!')
```
```
user_query = input("There's a party! Check if your name is on the list. Input name:")

party_guests = ["John", "Sue", "Ashley"]

if user_query in party_guests:
    print(f"{user_query} is invited to the party!")
else:
    print(f"{user_query} is not on the guest list.")
```
```
number = int(input("Input a number"))
if number % 2 == 0:
  print(f"{number} is an even number")
else:
  print(f"{number} is an odd number")
```

