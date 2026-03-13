# URL
https://adventofcode.com/2015/day/5
# Concept
* string matching (multiple criteria)
# Instructions
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

For example:

    ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
    aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
    jchzalrnumimnmhp is naughty because it has no double letter.
    haegwjzuvuyypxyu is naughty because it contains the string xy.
    dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?

# Code (WORK IN PROGRESS)
```Python
file_path = 'input.txt' # Replace with your file path

format_list = []
nice_words = 0
vowels = ["a","e","i","o","u"]

def has_double_letters(word):
  # Iterate through the string up to the second-to-last character
  for i in range(len(word) - 1):
    if word[i] == word[i + 1]:
      return True  # Double letters found
  return False # No double letters found after checking the entire string

def is_nice(word_string):


with open(file_path, 'r') as file:
  raw_input = file.readlines()

for i in raw_input:
  format_list.append(i[:-1])

print(format_list)
```

