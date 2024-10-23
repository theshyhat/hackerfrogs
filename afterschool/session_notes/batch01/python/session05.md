# HackerFrogs AfterSchool - Python Programming Basics
## Session 05 - Programming Loops
# This Session's Exercises
## Serpentine
https://play.picoctf.org/practice/challenge/251?originalEvent=69&page=1&search=
#### YouTube walkthrough:
https://www.youtube.com/watch?v=7j5_Sj9Ftpg
# learnpython dot org links
## Loops
https://learnpython.org/en/Loops
# End of Session Exercise Code
```
print("This program will take a series of integers, then tell us if each integer is an even number or odd number.")
numbers_string = input("Enter a series of integers, separated by spaces. E.g., 1 92 35")
number_list = numbers_string.split(" ")
for i in number_list:
  if int(i) % 2 == 0:
    print(f"{i} is an even number")
  else:
    print(f"{i} is an odd number")
```
