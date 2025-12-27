# URL
https://adventofcode.com/2025/day/2
# Concept
* regex on mirrored string values
# Instructions
--- Day 2: Gift Shop ---

You get inside and take the elevator to its only other stop: the gift shop. "Thank you for visiting the North Pole!" gleefully exclaims a nearby sign. You aren't sure who is even allowed to visit the North Pole, but you know you can access the lobby through here, and from there you can access the rest of the North Pole base.

As you make your way through the surprisingly extensive selection, one of the clerks recognizes you and asks for your help.

As it turns out, one of the younger Elves was playing on a gift shop computer and managed to add a whole bunch of invalid product IDs to their gift shop database! Surely, it would be no trouble for you to identify the invalid product IDs for them, right?

They've even checked most of the product ID ranges already; they only have a few product ID ranges (your puzzle input) that you'll need to check. For example:

11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124

(The ID ranges are wrapped here for legibility; in your input, they appear on a single long line.)

The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)

Your job is to find all of the invalid IDs that appear in the given ranges. In the above example:

    11-22 has two invalid IDs, 11 and 22.
    95-115 has one invalid ID, 99.
    998-1012 has one invalid ID, 1010.
    1188511880-1188511890 has one invalid ID, 1188511885.
    222220-222224 has one invalid ID, 222222.
    1698522-1698528 contains no invalid IDs.
    446443-446449 has one invalid ID, 446446.
    38593856-38593862 has one invalid ID, 38593859.
    The rest of the ranges contain no invalid IDs.

Adding up all the invalid IDs in this example produces 1227775554.

What do you get if you add up all of the invalid IDs?

# Method of solve
* this code will get the job done
```
import re

file_path = 'input.txt' # Replace with your file path

with open(file_path, 'r') as file:
    raw_input = file.readlines()

# Create the separated list
raw_string = raw_input[0]
input_list = raw_string.split(",")

# Modify the last object in the list
last_object = input_list[-1]
last_object = last_object[:-1]
input_list[-1] = last_object
print(f"This is the initial list:\n{input_list}")

# Function that expands the range into a list of numbers
def expand_range(range_string):
  number_pair = range_string.split("-")
  first_num = int(number_pair[0])
  second_num = int(number_pair[1])
  expanded_list = list(range(first_num, second_num+1))
  return expanded_list

# ID Check Function
def invalid_check(number_string):
  pattern = r'^(.+)\1$'
  return bool(re.match(pattern, number_string))

invalid_ids = []

# Big loop that checks all the IDs in all the ranges
for i in input_list:
  expanded_list = expand_range(i)
  for num in expanded_list:
    if invalid_check(str(num)):
      invalid_ids.append(int(num))

print(f"Here is the list of all the invalid IDs:\n{invalid_ids}")

# Sum the values of all the invalid IDs
summed_ids = sum(invalid_ids)
print(f"The sum of all the invalid IDs is:\n{summed_ids}")
```

