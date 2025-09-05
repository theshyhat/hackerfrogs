# URL
https://hack.arrrg.de/challenge/95
# Category
Web App
# Concept
* embedding fonts into a webpage
# Method of solve
* if we download the font mentioned in the challenge description, we can embed it into a local webpage and read the message mentioned in the description
* first download the font file:
```
wget https://hack.arrrg.de/chals/HackTheWebEnglish-Regular.otf
```
* next we need to create a webpage to host and view in our web browser. We'll name it `index.html` for convenience, and write the following code to it:
```
<!doctype html>
<meta charset="utf-8">
<title>HackTheWeb Font Test</title>
<style>
@font-face {
  font-family: HackTheWeb;
  src: url("HackTheWebEnglish-Regular.otf") format("opentype");
}
body { font-family: HackTheWeb, monospace; }
</style>
<p>ABC EFGHIJ LM OPQRSTUVWX..</p>
```
* note that we put in the same string included in the challenge in the code
* we run the Python HTTP server module to host the page, then load the page in the web browser
```
python -m http.server 80
```
* the answer is `kalligraph`
