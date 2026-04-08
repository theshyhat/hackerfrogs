# URL
https://training.olicyber.it/challenges#challenge-353
# Concept
* learning to parse HTML comments in webpages
# Method of solve
* the challenge tells us that we are supposed to get the flag inside of HTML comments on the following webpage: `http://web-14.challs.olicyber.it/`
## Curl Method
* we can use this `curl` command to get the webpage contents, grep out only the flag
```
curl http://web-14.challs.olicyber.it/ | grep -oP 'flag\{[^}]+\}'
```
## Python method
```
import requests
from bs4 import BeautifulSoup, Comment
import re

URL = 'http://web-14.challs.olicyber.it/'
get_req = requests.get(URL)
req_text = get_req.text

soup = BeautifulSoup(req_text, 'html.parser')

comments = soup.find_all(text=lambda text: isinstance(text, Comment))

for comment in comments:
    flag_match = re.search(r'flag\{[^}]+\}', comment)
    if flag_match:
        print(flag_match.group())
```
