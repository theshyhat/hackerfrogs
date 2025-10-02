# URL
https://training.olicyber.it/challenges#challenge-354
# Concept
* scraping webpages for links
* scraping webpages for string patterns
# Method of solve
* the challenge asks us to visit this page and extract all of the links on the page: `http://web-15.challs.olicyber.it/`
* we have to search inside the contents of the linked webpages for the flag
## Linux Command Method
* we can use a combination of `wget`, `cat`, and `grep` to download all the files from that website and search inside of all the contents:
```
wget -r -l 1 -np http://web-15.challs.olicyber.it/ | cat web-15.challs.olicyber.it/* | grep -oP 'flag\{[^}]+\}'
```
## Python Method
```
import requests
from bs4 import BeautifulSoup, Comment
import re
from urllib.parse import urljoin, urlparse

URL = 'http://web-15.challs.olicyber.it/'
get_req = requests.get(URL)
req_text = get_req.text

base_url = 'http://web-15.challs.olicyber.it'
base_domain = urlparse(base_url).netloc

soup = BeautifulSoup(req_text, 'html.parser')

# Extract the links from the landing page
links = []

for link in soup.find_all('link', href=True):
    # Convert relative URLs to absolute
    absolute_url = urljoin(base_url, link['href'])
    
    # Check if it belongs to the same domain
    if urlparse(absolute_url).netloc == base_domain:
        links.append(absolute_url)

for link in soup.find_all('script', src=True):
    # Convert relative URLs to absolute
    absolute_url = urljoin(base_url, link['src'])
    
    # Check if it belongs to the same domain
    if urlparse(absolute_url).netloc == base_domain:
        links.append(absolute_url)

for link in links:
    # visit all the links and search for the flag pattern
    link_get_req = requests.get(link)
    link_req_text = link_get_req.text

    flags = re.findall(r'flag\{[^}]+\}', link_req_text)
    print(flags)
```
