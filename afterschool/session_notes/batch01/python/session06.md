# This Session's Exercises
## Inspect HTML
https://play.picoctf.org/practice/challenge/275?page=1&search=inspect
YouTube walkthrough:
https://www.youtube.com/watch?v=fm1EvGY3aow

# End of Session Exercise
```
import os

url = input("Which webpage do you want to read? ")
curl_command = f"curl {url}"

def read_webpage(curl_command):
  print(os.popen(curl_command).read())

read_webpage(curl_command)
```
# Code Snippet 1
```
def greet_user(first_name='John', last_name='Doe'):
  print(f'Hello {first_name} {last_name}!')

greet_user(last_name='Smith')
greet_user()
```
# Code Snippet 2
```
colors = ['blue', 'red', 'green', 'yellow']
fruits = ['apple', 'orange', 'grape', 'banana', 'watermelon']

def list_out(target):
  for i in target:
    print(i)

list_out(colors)
list_out(fruits)
```
