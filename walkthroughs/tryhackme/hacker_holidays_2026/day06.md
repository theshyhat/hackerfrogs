# URL
https://tryhackme.com/room/hh-overheardatbreakfast-6f01793c
# Concept
* OSINT
  * email OSINT
* social media tool lookup
# Method of solve
* we're given an image to inspect
* in the image, we see an email address `lambobytelotushotel@gmail.com`
* there's also mention of a social media tool that's used to upload profiles and link media pages, and the tool starts with the letter `G`
* when we ask for suggestions from the AI, we might get back the tool `Gravatar`
* we can also use an email checker from Gravatar, located here:
```
https://gravatar.com/site/check
```
* if we plug in the email we found into the checker, we find the correct profile and get the flag
* done!
