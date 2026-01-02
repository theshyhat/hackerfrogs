# URL
https://adventofcode.com/2025/day/2
# Concept
* regex on repeated string patterns
# Instructions
The clerk quickly discovers that there are still invalid IDs in the ranges in your list. Maybe the young Elf was doing other silly patterns as well?

Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

From the same example as before:

    11-22 still has two invalid IDs, 11 and 22.
    95-115 now has two invalid IDs, 99 and 111.
    998-1012 now has two invalid IDs, 999 and 1010.
    1188511880-1188511890 still has one invalid ID, 1188511885.
    222220-222224 still has one invalid ID, 222222.
    1698522-1698528 still contains no invalid IDs.
    446443-446449 still has one invalid ID, 446446.
    38593856-38593862 still has one invalid ID, 38593859.
    565653-565659 now has one invalid ID, 565656.
    824824821-824824827 now has one invalid ID, 824824824.
    2121212118-2121212124 now has one invalid ID, 2121212121.

Adding up all the invalid IDs in this example produces 4174379265.

What do you get if you add up all of the invalid IDs using these new rules?
# Method of solve
* this code will get the job done
* note that the only difference between the previous script and this one is a single character in the regex for the `invalid_check` function:
```
pattern = r'^(.+)\1+$'
```
* the `+` symbol in the code causes the regex to match on one *or more* matches on the pattern, as opposed to previous code which only matched if there was a single repeat of the pattern
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
  pattern = r'^(.+)\1+$'
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
