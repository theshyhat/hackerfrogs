# URL
https://adventofcode.com/2015/day/6
# Concept
* managing large lists
* 2d coordinates
# Instructions
--- Part Two ---

You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

    turn on 0,0 through 0,0 would increase the total brightness by 1.
    toggle 0,0 through 999,999 would increase the total brightness by 2000000.

# Code
```Python
'''
- In the new version of the program the lights now contain
  a numerical value that represents how bright the light is
- The brightness value for each light starts at 0, and has no
  upper limit to its value
- But the brightness cannot be lower than 0
- The operations now do different things:
  - the "turn on" operation now increases the brightness of
    each light by 1
  - the "turn off" operation now decreases the brightness
    of each light by 1, with a minimum value of 0
  - the "toggle" operation now increases the brightness of
    each light by 2
- At the end of the program, we get the sum of all the brightness
  values from the lights
'''

# Define the Grid As a List of Lists

width = 1000
height = 1000

grid = [[0 for x in range(width)] for y in range(height)]

true_count = sum(sum(row) for row in grid)

print(true_count)

# Define the three operations we can apply to the Grid list contents

def turn_on(x1, y1, x2, y2):
  # set all of the lights in the x,y coordinates to on (1)
  # turn_on(0,0,1,1) <-- should turn on four lights
  x = x1 
  y = y1
  while x <= x2:
    while y <= y2:
      grid[y][x] += 1
      y += 1
    x += 1
    y = y1

def turn_off(x1, y1, x2, y2):
  x = x1 
  y = y1
  while x <= x2:
    while y <= y2:
      if grid[y][x] != 0:
        grid[y][x] -= 1
      y += 1
    x += 1
    y = y1

def toggle(x1, y1, x2, y2):
  x = x1 
  y = y1
  while x <= x2:
    while y <= y2:
      grid[y][x] += 2
      y += 1
    x += 1
    y = y1

# Create a function to run the operations

def choose_an_operation(order_str):
  order_list = order_str.split()
  start_x = int(order_list[-5])
  start_y = int(order_list[-4])
  end_x = int(order_list[-2])
  end_y = int(order_list[-1])
  current_order = order_list[-6]

  if current_order == 'toggle':
    toggle(start_x,start_y,end_x,end_y)
  elif current_order == 'on':
    turn_on(start_x,start_y,end_x,end_y)
  else:
    turn_off(start_x,start_y,end_x,end_y)

# Create the command input list

file_path = 'input.txt' # Replace with your file path

with open(file_path, 'r') as file:
  raw_input = file.readlines()

# Format the instruction strings

format_list = []

for i in raw_input:
  temp_str = i[:-1]
  rep_str = temp_str.replace(",", " ")
  format_list.append(rep_str)

for i in format_list:
  choose_an_operation(i)

true_count = sum(sum(row) for row in grid)
print(true_count)
```
