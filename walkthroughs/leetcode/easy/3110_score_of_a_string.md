# URL
https://leetcode.com/problems/score-of-a-string/
# Challenge Description
You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s
# Code
```
class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for index, letter in enumerate(s):
            if index < len(s) - 1:  # Check if there's a next letter
                next_letter = s[index + 1]
                result = ord(letter) - ord(next_letter)
                score += abs(result)
        return score

solve = Solution()
run = solve.scoreOfString(s="hello")
print(run)
```

