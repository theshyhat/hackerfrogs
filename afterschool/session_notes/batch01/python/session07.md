# HackerFrogs AfterSchool - Python Programming Basics
## Session 07 - Classes / Objects and Dictionaries
# This Session's Exercises
## WebDecode
https://play.picoctf.org/practice/challenge/427?page=1&search=web
YouTube walkthrough:
https://www.youtube.com/watch?v=TdSmaAqt_jk

# Scripts for Solving the WebDecode Challenge
## 1. Downloading the webpage
https://github.com/theshyhat/ctf_documents/blob/main/scripts/web_hacking/webpage_fetch.py

## 2. Extracting links from the webpage
https://github.com/theshyhat/ctf_documents/blob/main/scripts/web_hacking/extract_links.py

## 3. Searching for Base64 encoded strings
https://github.com/theshyhat/ctf_documents/blob/main/scripts/web_hacking/base64_search.py

# Extra Credit Challenge
## PW Crack 4
https://play.picoctf.org/practice/challenge/248?page=1&search=pw

## Modified code for PW Crack 4 challenge
```
def level_4_pw_check():
    for pw in pos_pw_list:
        user_pw_hash = hash_pw(pw)
    
        if( user_pw_hash == correct_pw_hash ):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), pw)
            print(decryption)
            return
    print("That password is incorrect")
```
# More Python Education Resources
https://www.reddit.com/r/hackerfrogs/comments/1bjpxmk/python_language_education_resources_online_and/

```
class HackerFrog:
    def __init__(self, name, fave_subject):
        self.name = name
        self.fave_subject = fave_subject
    HF_motto = "Hip hop and hack!"
    
Web_frog = HackerFrog("Web Frog", "web app hacking")

print(Web_frog)
```
