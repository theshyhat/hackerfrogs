# URL
https://training.olicyber.it/challenges#challenge-352
# Concept
* isolating webpage output based on tags
# Method of solve
* the challenge tells us that the flag is formed by concatenating all of the letters that appear in red on this webpage: `http://web-13.challs.olicyber.it/`
* if we look at that page's HTML source, we see that all of the red letters are between these HTML tags: `<span class="red"></span>`
## Curl solve method
* if we save that webpage output to a file named `page.txt`, then we can run the following command to isolate all of the text inside of those HTML tags, and then delete the tags, then delete all of the newlines to give us only the flag value:
```
cat page.txt | grep -oP '<span class="red">.</span>' | sed 's/<[^>]*>//g' | tr -d '\n'
```
* we have to remember to wrap the flag contents in the `flag{}` wrapper
## Python solve method
```
import requests
from bs4 import BeautifulSoup

URL = 'http://web-13.challs.olicyber.it/'
get_req = requests.get(URL)
req_text = get_req.text

soup = BeautifulSoup(req_text, 'html.parser')

tags = soup.find_all('span', class_='red')

letters = ''.join([tag.text for tag in tags])

print(letters)
```
