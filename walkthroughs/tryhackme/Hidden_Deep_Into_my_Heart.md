# URL
https://tryhackme.com/room/lafb2026e9
# Concept
* robots.txt
# Method of solve
* look at the `robots.txt` file in the webroot of the app
* we see there is a directory indicated as well as a string in the comments that could be a password
* when we directory bust into that directory, we find an `/administrator` endpoint
* on that endpoint there is a login page
* we use the password captured from the `robots.txt` file and the username `admin` to gain access
* finished!
