# URL
https://leetcode.com/problems/defanging-an-ip-address/description/?envType=problem-list-v2&envId=ew2tef8s
# Concept
* string substitution
# Instructions
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
# Python Code
```Python
class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = address.replace(".", "[.]")
        return defanged

solve = Solution()
run = solve.defangIPaddr("127.0.0.1")
print (run)
```
# C Code
```C
#include <stdio.h>
#include <string.h>

char defang_str[25];

char * defangIPaddr(char * address){
  defang_str[0] = '\0';
  int i = 0;
  char defang_pattern[4] = "[.]";
  // Iterate over all characters in "address"
  for (i=0;address[i]!='\0';i++) {
    if (address[i] == '.') {
      strcat(defang_str, defang_pattern);
    }
    else {
        strncat(defang_str,&address[i],1);
    }
  }
  return defang_str;  
}

int main(void){
  printf("%s",defangIPaddr("255.100.50.0"));
}
```
