# URL
https://training.olicyber.it/challenges#challenge-355
# Concept
* spidering a website
* searching the website for specific strings
# Method of solve
* we need to map out a website, then search within the website webpages for the flag string
* the flag string, we are told, is within an `h1` tag
## Curl (Wget)
* first run wget to get a list of links:
```
wget --no-clobber --no-parent --spider -r http://web-16.challs.olicyber.it/ 2>&1 | grep '^--' | awk '{print $3}' | tee urls.txt
```
* afterwards, we have a list of URLs, but there are duplicate URLs in that list, so need to format that list
```
sort urls.txt | uniq > sorted_urls.txt
```
* now we can feed this list of URLs into a bash script to get the flag
```
#!/bin/bash

while read url; do
    echo "Checking: $url"
    
    # Capture the grep result in a variable
    result=$(curl -s "$url" | grep -i "flag")
    
    # Check if result is NOT empty (flag was found)
    if [ -n "$result" ]; then
        echo "We found the flag! Exiting."
        echo "$result"  # Print the flag
        exit 0  # Exit with success (0 = success, not 1)
    fi
done < sorted_urls.txt
```
## Python
```
# Web Spider with Flag Detection using BeautifulSoup
# Install requirements: pip install beautifulsoup4 requests

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

def is_valid_url(url, base_domain):
    """
    Check if URL is valid and belongs to the same domain.
    
    Parameters:
        url (str): URL to validate
        base_domain (str): Base domain to restrict crawling
    
    Returns:
        bool: True if URL is valid and on same domain
    """
    # Parse the URL
    parsed = urlparse(url)
    
    # Check if it's a valid HTTP/HTTPS URL
    if parsed.scheme not in ['http', 'https']:
        return False
    
    # Check if it belongs to the same domain (prevent crawling external sites)
    if base_domain not in parsed.netloc:
        return False
    
    return True


def find_flag_in_text(text):
    """
    Search for flag pattern in text.
    
    Parameters:
        text (str): Text to search
    
    Returns:
        str or None: The flag if found, None otherwise
    """
    # Search for pattern: flag{...}
    # This regex matches "flag{" followed by any characters until "}"
    match = re.search(r'flag\{[^}]+\}', text, re.IGNORECASE)
    
    if match:
        return match.group(0)
    
    return None


def spider_website(start_url, max_pages=100):
    """
    Spider a website starting from start_url, looking for a flag.
    Stops when flag is found or max_pages is reached.
    
    Parameters:
        start_url (str): Starting URL to begin crawling
        max_pages (int): Maximum number of pages to visit
    
    Returns:
        str or None: The flag if found, None otherwise
    """
    # Set to track visited URLs (prevents revisiting)
    visited = set()
    
    # Queue of URLs to visit (start with the initial URL)
    to_visit = [start_url]
    
    # Extract base domain for validation
    base_domain = urlparse(start_url).netloc
    
    # Counter for pages visited
    pages_visited = 0
    
    print(f"Starting spider from: {start_url}")
    print(f"Base domain: {base_domain}")
    print(f"Max pages to visit: {max_pages}")
    print("=" * 60)
    
    # Main crawling loop
    while to_visit and pages_visited < max_pages:
        # Get next URL from queue
        current_url = to_visit.pop(0)
        
        # Skip if already visited
        if current_url in visited:
            continue
        
        # Mark as visited
        visited.add(current_url)
        pages_visited += 1
        
        print(f"\n[{pages_visited}] Visiting: {current_url}")
        
        try:
            # Fetch the webpage
            # timeout=10 means wait max 10 seconds for response
            response = requests.get(current_url, timeout=10)
            response.raise_for_status()  # Raise exception for bad status codes
            
            # Get the page content
            page_content = response.text
            
            # Check if flag is in the raw HTML
            flag = find_flag_in_text(page_content)
            if flag:
                print("\n" + "=" * 60)
                print("🎉 FLAG FOUND! 🎉")
                print("=" * 60)
                print(f"URL: {current_url}")
                print(f"Flag: {flag}")
                print("=" * 60)
                return flag
            
            # Parse HTML with BeautifulSoup
            soup = BeautifulSoup(page_content, 'html.parser')
            
            # Also check visible text on page
            visible_text = soup.get_text()
            flag = find_flag_in_text(visible_text)
            if flag:
                print("\n" + "=" * 60)
                print("🎉 FLAG FOUND! 🎉")
                print("=" * 60)
                print(f"URL: {current_url}")
                print(f"Flag: {flag}")
                print("=" * 60)
                return flag
            
            # Find all links on the page
            links = soup.find_all('a', href=True)
            
            # Add new links to queue
            new_links_count = 0
            for link in links:
                # Convert relative URLs to absolute URLs
                absolute_url = urljoin(current_url, link['href'])
                
                # Remove fragment (#section) from URL
                absolute_url = absolute_url.split('#')[0]
                
                # Check if URL is valid and not already visited
                if is_valid_url(absolute_url, base_domain) and absolute_url not in visited:
                    if absolute_url not in to_visit:
                        to_visit.append(absolute_url)
                        new_links_count += 1
            
            print(f"   Found {new_links_count} new links")
            print(f"   Queue size: {len(to_visit)}, Visited: {len(visited)}")
            
        except requests.exceptions.RequestException as e:
            # Handle network errors
            print(f"   ✗ Error fetching page: {e}")
            continue
        
        except Exception as e:
            # Handle other errors
            print(f"   ✗ Unexpected error: {e}")
            continue
    
    # Flag not found
    print("\n" + "=" * 60)
    print("Spider completed")
    print(f"Pages visited: {pages_visited}")
    print(f"Flag not found")
    print("=" * 60)
    return None


# Main script execution
if __name__ == "__main__":
    # Target website to spider
    # Change this to your CTF challenge URL
    target_url = "http://web-16.challs.olicyber.it/"
    
    # Maximum pages to visit (prevents infinite crawling)
    max_pages = 800
    
    # Start spidering
    flag = spider_website(target_url, max_pages=max_pages)
    
    if flag:
        print(f"\n✅ Success! Flag: {flag}")
    else:
        print("\n❌ Flag not found in visited pages")

```

