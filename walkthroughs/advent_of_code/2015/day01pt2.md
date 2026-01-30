# URL
https://adventofcode.com/2015/day/1#part2
# Instructions
--- Part Two ---

Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

    ) causes him to enter the basement at character position 1.
    ()()) causes him to enter the basement at character position 5.

What is the position of the character that causes Santa to first enter the basement?
# Concept
* enumerate the list of strings and find out which at position a certain event occurs
# Method of solve
* we've modified the script to solve the second part:
```
file_path = 'input.txt' # Replace with your file path

with open(file_path, 'r') as file:
    raw_input = file.readlines()

raw_string = raw_input[0]
raw_list = list(raw_string)
raw_list.pop() 

enum_list = enumerate(raw_list, 1)

def get_basement_pos(enum_list):
  position = 0
  in_basement = False
  for i,j in enum_list:
    if j == '(':
      position += 1
    else:
      position -= 1
    if position == (-1):
      in_basement = True
    if in_basement:
      print(f"Santa enters the basement at position {i}.")
      break

get_basement_pos(enum_list)
```
