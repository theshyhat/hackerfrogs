# username
athena
# password
kmQMpZsXgOsnzGReRcoV
# mission contents
User aura lets us use her new script.
# method of solve
This script was included in the home directory
```
#!/bin/bash
echo "What?"
read hackme
#Secure the condition!
#if [[ $hackme =~ "????????" ]]; then
#exit
#fi
#Add newest Aura pass!
#$hackme AURANEWPASS 2>/dev/null
```
* We guess that we need to supply the name of a command that reads the `AURANEWPASS` file, but nothing seems to work
* The actual problem is the error redirection `2>/dev/null`, which is redirecting everything to `/dev/null`
* So we can solve the problem by using a specific program, either `script` `printf`
```
sudo -u aura /bin/bash -c /pwned/aura/auri.sh
printf
```
