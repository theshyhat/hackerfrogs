# URL
https://leetcode.com/problems/find-words-containing-character/description/?envType=problem-list-v2&envId=ew2tef8s
# Instructions
You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.
# Concept
* finding strings in list objects
* iterating over lists
# Code
```
class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        has_letter = []
        for items_index, string in enumerate(words):
            if x in string:
                has_letter.append(items_index)
        return has_letter

words_list = ["abc", "xyz", "abz"]
target_letter = "a"

solve = Solution()
run = solve.findWordsContaining(words=words_list,x=target_letter)

print(run)
```
