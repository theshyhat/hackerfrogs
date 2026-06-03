# URL
https://hackropole.fr/en/challenges/crypto/fcsc2023-crypto-rot13/
# Concept
* ROT13 encryption
# Method of solve
* just copy all of the text
* and you plug it into CyberChef
`https://cyberchef.io/#recipe=ROT13(true,true,false,13)&input=R0JRQiB5dmZnciA6Ci0gQ252YSAoMiBvbnRocmdncmYpCi0gWW52ZyAoMSB5dmdlcikKLSBQYmV2bmFxZXIgKGZoZWdiaGcgY25mLCBwJ3JmZyBjbmYgb2JhKQotIDQgb25hbmFyZiwgNCBjYnp6cmYsIDQgYmVuYXRyZgotIENiaHlyZyAoNCBzdnlyZ2YgcXIgY2JoeXJnKQotIDEgc3ludCA6IFNQRlB7cnEyNHA3c3E4NnAyczA1MTUzNjZ9Ci0gQ%2BJncmYgKDF4dCkKLSBFdm0gKGZucCBxciAxOHh0KQotIEFiaGV2ZSB6YmEgcXZhYmZuaGVy`
* we can also write out the message to a file and use the Linux `tr` command:
```
cat rot13.txt| tr 'A-Za-z' 'N-ZA-Mn-za-m'
```


