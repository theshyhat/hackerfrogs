# URL
https://adventofcode.com/2025/day/3
# Concept
* returning largest digits in an integer
# Instructions
You descend a short staircase, enter the surprisingly vast lobby, and are quickly cleared by the security checkpoint. When you get to the main elevators, however, you discover that each one has a red light above it: they're all offline.

"Sorry about that," an Elf apologizes as she tinkers with a nearby control panel. "Some kind of electrical surge seems to have fried them. I'll try to get them online soon."

You explain your need to get further underground. "Well, you could at least take the escalator down to the printing department, not that you'd get much further than that without the elevators working. That is, you could if the escalator weren't also offline."

"But, don't worry! It's not fried; it just needs power. Maybe you can get it running while I keep working on the elevators."

There are batteries nearby that can supply emergency power to the escalator for just such an occasion. The batteries are each labeled with their joltage rating, a value from 1 to 9. You make a note of their joltage ratings (your puzzle input). For example:

987654321111111
811111111111119
234234234234278
818181911112111

The batteries are arranged into banks; each line of digits in your input corresponds to a single bank of batteries. Within each bank, you need to turn on exactly two batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. For example, if you have a bank like 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts. (You cannot rearrange batteries.)

You'll need to find the largest possible joltage each bank can produce. In the above example:

    In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
    In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
    In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
    In 818181911112111, the largest joltage you can produce is 92.

The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is 98 + 89 + 78 + 92 = 357.

There are many batteries in front of you. Find the maximum joltage possible from each bank; what is the total output joltage?
# Method of solve
* this code will get the job done
```
file_path = 'input.txt' # Replace with your file path

with open(file_path, 'r') as file:
    raw_list = file.readlines()

# Stripping out newlines
stripped_list = [item.strip() for item in raw_list]

# Define the list of joltages we need to add up later
joltage_list = []

# Define a function that identifies the largest digit in a string
def find_joltage_digits(string):
  largest_digit = 0
  largest_digit_pos = 0
  second_largest = 0
  second_digit_string = ""
  combined_digit = 0
  global joltage_list

  # First loop for largest digit
  for index, digit in enumerate(string,1):
    if int(digit) > largest_digit:
      if index != len(string):
        largest_digit = int(digit)
        largest_digit_pos = index
        print(f"New largest digit found: {digit}")
      else:
        print("Uh-oh! The largest first digit is the last number!\nSkipping...")
        continue
  second_digit_string = string[largest_digit_pos:]
  # Second loop for second largest digit
  for index, digit in enumerate(second_digit_string):
    if int(digit) > second_largest:
      second_largest = int(digit)
      print(f"New second largest digit found: {digit}")
  combined_digit = str(largest_digit) + str(second_largest)
  joltage_list.append(int(combined_digit))
  print(f"Added {combined_digit} to joltage list!")
  return combined_digit

# Get all the joltage numbers
for i in stripped_list:
  find_joltage_digits(i)

print(f"These are all the joltage numbers:\n{joltage_list}")
joltage_sum = sum(joltage_list)
print(f"The sum of all the joltages is:\n{joltage_sum}")
```
