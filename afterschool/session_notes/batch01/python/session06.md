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
