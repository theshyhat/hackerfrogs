# URL
https://leetcode.com/problems/jewels-and-stones
# Description from Leetcode
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0

# Concept
* find all occurance of a substring inside of a string
# Method of solving (Python Code)
```
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        num_of_jewels = 0
        jewel_list = list(jewels)
        for i in stones:
            if i in jewel_list:
                num_of_jewels += 1
        return num_of_jewels

jewel_string = "aA"
stone_string = "aAAbbbb"

solve = Solution()
run = solve.numJewelsInStones(jewels=jewel_string, stones=stone_string)
print(run)
```
