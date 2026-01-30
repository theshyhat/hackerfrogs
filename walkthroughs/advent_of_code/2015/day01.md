# URL
https://adventofcode.com/2015/day/1
# Description
Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

    (()) and ()() both result in floor 0.
    ((( and (()(()( both result in floor 3.
    ))((((( also results in floor 3.
    ()) and ))( both result in floor -1 (the first basement level).
    ))) and )())()) both result in floor -3.

To what floor do the instructions take Santa?
# Concept
* counting characters and returning a result
# Method of solve
* this Python code will solve the first part of the challenge:
```
file_path = 'input.txt' # Replace with your file path

with open(file_path, 'r') as file:
    raw_input = file.readlines()

raw_string = raw_input[0]
raw_list = list(raw_string)
raw_list.pop() 

def get_the_floor(list):
  up_inst = 0
  down_inst = 0
  for i in list:
    if i == '(':
      up_inst += 1
    else:
      down_inst += 1
  return up_inst - down_inst

the_answer = get_the_floor(raw_list)

print(f"The answer is {the_answer}")
```


