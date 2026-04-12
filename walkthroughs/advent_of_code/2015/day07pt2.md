# URL
https://adventofcode.com/2015/day/7
# Instructions
--- Part Two ---

Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?

# Concept
* changing arbitrary values and re-calculating
# Code
```Python
'''
In this program we need to take in instructions,
perform bitwise operations, and assign the result
to variables.

At the end of the operations, we need to return
the value of the 'a' variable.
'''
# Variables to keep track of wires

wire_dict = {}
cache = {}

# A function to get the hard value, to be used with the evaluate function
def get_value(token):
    if token.isdigit():
        return int(token)
    return evaluate(token)

# A function to evaluate the values of the wires in the dictionary
def evaluate(wire):
    if wire in cache:
        return cache[wire]

    inst = wire_dict[wire]

    if len(inst) == 1:
        result = get_value(inst[0])

    elif len(inst) == 2:
        result = ~get_value(inst[1])

    elif len(inst) == 3:
        left = get_value(inst[0])
        op = inst[1]
        right = get_value(inst[2])

        if op == 'AND':
            result = left & right
        elif op == 'OR':
            result = left | right
        elif op == 'LSHIFT':
            result = left << right
        else:
            result = left >> right

    # Perform a bitwise AND operation with 0xFFFF
    # to restrict the result to a 16-bit integer
    result &= 0xFFFF
    cache[wire] = result
    return result

# Create the command input list

file_path = 'input.txt' # Replace with your file path

with open(file_path, 'r') as file:
  raw_input = file.readlines()

# Format the instruction strings

format_list = []

for i in raw_input:
  format_list.append(i.strip())

# Populate the wires dictionary

for i in format_list:
  line_list = i.split()
  eq_list = line_list[:-2]
  wire_name = line_list[-1]
  wire_dict[wire_name] = eq_list

# Run the evaluate function over the entire wires dictionary

for i in wire_dict:
  evaluate(i)

# Additional code for part 2
# Get the original value for 'a'
part1 = evaluate('a')
# Reassign the instructions for 'b' with
# value of 'a'
wire_dict['b'] = [str(part1)]
# Clear the cache dictionary
cache = {}
# Re-evaluate 'a'
part2 = evaluate('a')
print(part2)
```
