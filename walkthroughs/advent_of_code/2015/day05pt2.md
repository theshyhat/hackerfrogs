# URL
https://adventofcode.com/2015/day/5
# Concept
* string matching (multiple criteria)
# Instructions
--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

For example:

    qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
    xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
    uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
    ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

How many strings are nice under these new rules?

# Code 
```Python
'''
For this challenge, we need to sort through strings
- 
- return the number of strings that qualify
'''

file_path = 'input.txt' # Replace with your file path

format_list = []
nice_words = 0
vowels = ["a","e","i","o","u"]

def has_double_pairs(word):
  n = 2
  pair_list = [word[i:i+n] for i in range(0, len(word), n)]
  return pair_list
'''
def how_many_nice(list_of_words):
  global nice_words

'''

with open(file_path, 'r') as file:
  raw_input = file.readlines()

for i in raw_input:
  format_list.append(i[:-1])

print(has_double_pairs(format_list))
```

