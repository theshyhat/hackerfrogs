# URL
https://training.olicyber.it/challenges#challenge-351
# Concept
* getting and parsing web page content
# Method of solve
* we need to visit this webpage: `http://web-12.challs.olicyber.it/`
* in the web page content, the flag will be in the second paragraph of page contents
* we can use curl to get the page contents, then parse through the content using Linux commands
```
curl -v http://web-12.challs.olicyber.it/ | awk '/<p>/{flag=1; count++; next} /<\/p>/{if(count==2 && flag) print content; flag=0; content=""; next} flag && count==2{content=content $0 "\n"}'
```
## Python Solution
```Python
import requests
from bs4 import BeautifulSoup

URL = 'http://web-12.challs.olicyber.it/'

get_req = requests.get(URL)
res = get_req.text

# Create the text parser object, soup
soup = BeautifulSoup(res, "html.parser")
# Isolate the second paragraph of the response
second_paragraph = soup.find_all("p")[1].get_text(strip=True)

print("This is the second paragraph of the response:")
print(second_paragraph)
```
