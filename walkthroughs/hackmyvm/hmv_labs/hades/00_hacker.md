# username
hacker
# password
begood!
# objective
User acantha has left us a gift to obtain her powers.
# method of solve
There's an SUID binary that our user `hacker` can access. When run, it gives us a shell in the context of the `acantha` user
```
find / -perm -4000 2>/dev/null
```
We find the `gift_hacker` file in the list of SUID binaries. When we run it, we become the `acantha` user, and we can read their password
```
cat /pazz/acantha_pass.txt
```
