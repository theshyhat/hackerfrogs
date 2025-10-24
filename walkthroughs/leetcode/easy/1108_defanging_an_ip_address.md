# URL
https://leetcode.com/problems/defanging-an-ip-address/description/?envType=problem-list-v2&envId=ew2tef8s
# Concept
* string substitution
# Instructions
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
# Code
```
class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = address.replace(".", "[.]")
        return defanged

solve = Solution()
run = solve.defangIPaddr("127.0.0.1")
print (run)
```
