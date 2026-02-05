# SSH Command / Password
ssh the-shadows_level4@api.wargames.batamladen.com -p 9306 R3gr3t
# Concept
* grep for specific strings
* base64 decoding
# Method of solve
* once logged in, we see that there are specific strings that are echoed out to our terminal
* if we grep for file that contains those lines, we see a specific file:
```
grep -r / -e "He is so delusional..." 2>/dev/null
```
* this lets us know about a file called `/opt/.whispers.txt`
* in that file, there's reference to the `/usr` directory
* in the `/usr` directory there's a file called `fog_of_words.txt`
* this file contains a long string of base64 encoded info
* when we decode it, there's a lot of different strings:
```
base64 -d /usr/fog_of_words.txt
```
* we can grep out the flag with this command
```
base64 -d /usr/fog_of_words.txt | grep -i flag
```










