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
'''
For this challenge, we need to sort through strings
- the strings must have 3 vowels (aeiou)
- the strings must have at least one set of double letters
- the strings cannot include the following combos:
  - ab, cd, pq, or xy
- return the number of strings that qualify
'''

file_path = 'input.txt' # Replace with your file path

format_list = []
nice_words = 0
vowels = ["a","e","i","o","u"]
bad_pairs = ["ab", "cd", "pq", "xy"]

def has_double_letters(word):
  # Iterate through the string up to the second-to-last character
  for i in range(len(word) - 1):
    if word[i] == word[i + 1]:
      return True  # Double letters found
  return False # No double letters found after checking the entire string

def has_enough_vowels(word):
  # check if a string has enough vowels to qualify as 'nice'
  vowel_count = 0
  # iterate over all the letters in the word string
  for i in word:
    if i in vowels:
      vowel_count += 1
  # check if the word has 3 or more vowels at the end of the function
  if vowel_count >= 3:
    return True

def has_bad_pairs(word):
  # check if the word has bad pairs of letters
  is_bad = False
  # iterate over the word, and check it doesn't have the bad pairs
  for i in bad_pairs:
    if i in word:
      is_bad = True
      break
  return is_bad

def how_many_nice(list_of_words):
  global nice_words
  # this function returns the number of nice strings from the list
  for i in list_of_words:
    is_good = False
    # check if the string has bad pairs
    if has_bad_pairs(i):
      is_good = False
      continue
    # check if the string has double letters and enough vowels
    if has_double_letters(i) and has_enough_vowels(i):
      is_good = True
    if is_good:
      nice_words += 1
  # return the number of good strings
  return nice_words

with open(file_path, 'r') as file:
  raw_input = file.readlines()

for i in raw_input:
  format_list.append(i[:-1])

print(how_many_nice(format_list))
```

