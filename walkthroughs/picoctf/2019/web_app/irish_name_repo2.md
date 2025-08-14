# URL
https://play.picoctf.org/practice/challenge/59
# concept
* SQL injection -- auth bypass
* with filters!
# method of solve
* the `or` keyword is being filtered, so we can't use the classic SQL auth bypass payload `' or 1=1 -- `
* the proper payload is `admin' -- `
