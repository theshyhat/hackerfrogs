# URL
https://github.com/cyberstudentsfoundation/csd-ctf/blob/main/rounds/1/Nokia's%20secret/challenge.md
# Concept
* PNG steganography
* ciphertext identification
* vulnerability research
# Method of solve
* we're given a zip file which contains a png picture file
* from the name of the file, `stegedimage.png`, we can guess that we're supposed to run a steganography tool on it:
```
zsteg stegedimage.png
```
* this tool's output lets us know about a Google drive link
* when we navigate to that link in our browser, we see some ciphertext:
```
Dszg Xlnnlm Efomvizyrorgb zmw Vcklhfiv (XEV) rwvmgrurvi rh zhhlxrzgvw drgs gsv nvnlib nzmztvnvmg zmw kilgvxgrlm rhhfvh rm Yrgxlrm Xliv e22 gszg vmzyov zggzxpvih gl nlwrub gsv hglivw hvmwrmt zwwivhh, klgvmgrzoob ivwrivxgrmt Yrgxlrm gizmhzxgrlmh gl dzoovgh lu gsvri ldm xsllhrmt? Dizk rm xhw{}
```
* we don't know what kind of cipher might be used here, so we ID it with a tool
```
https://www.dcode.fr/cipher-identifier
```
* this identifies the cipher used as Atbash, a substitution cipher which reverses the order of letters, with A converted Z and Z converted A, etc, etc..
* if we know the cipher is Atbash, we can decipher it using CyberChef:
```
https://gchq.github.io/CyberChef/#recipe=Atbash_Cipher()&input=RHN6ZyBYbG5ubG0gRWZvbXZpenlyb3JnYiB6bXcgVmNrbGhmaXYgKFhFVikgcnd2bWdydXJ2aSByaCB6aGhseHJ6Z3Z3IGRyZ3MgZ3N2IG52bmxpYiBuem16dHZudm1nIHptdyBraWxndnhncmxtIHJoaGZ2aCBybSBZcmd4bHJtIFhsaXYgZTIyIGdzemcgdm16eW92IHpnZ3p4cHZpaCBnbCBubHdydWIgZ3N2IGhnbGl2dyBodm13cm10IHp3d2l2aGgsIGtsZ3ZtZ3J6b29iIGl2d3Jpdnhncm10IFlyZ3hscm0gZ2l6bWh6eGdybG1oIGdsIGR6b292Z2ggbHUgZ3N2cmkgbGRtIHhzbGxocm10PyBEaXprIHJtIHhod3t9
```
* this last part of the challenge requires to lookup a CVE number associated with Bitcoin vulnerabilities and then wrap that CVE number in a flag wrapped, `csd{}`
* the final flag is `csd{CVE-2023-37192}`
