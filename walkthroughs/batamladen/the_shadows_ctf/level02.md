# SSH Command / Password
ssh the-shadows_level2@api.wargames.batamladen.com -p 3920 Exp1orer
# Concept
Finding *nix hidden files
# Method of solve
* we need to look for hidden files
* we can find them using the `find`
```
find -name ".*" 2>/dev/null
```
* this gives us a lot of output, because there are a lot of hidden files
* we can further refine this command to look for `flag` files:
```
find -name ".*" 2>/dev/null | grep flag
```
* the relevant file is in the `/opt` directory
```
cat /opt/.flag.txt
```






