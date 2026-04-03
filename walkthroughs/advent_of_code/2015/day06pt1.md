# URL
https://adventofcode.com/2015/day/6
# Concept
* managing large lists
# Instructions
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

    turn on 0,0 through 999,999 would turn on (or leave on) every light.
    toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
    turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?

# Code
'''Python
'''
- In the program, we need lists that represent lights that need
  to be either on or off, and there are 1 million lights
- This program needs to set items in lists to either Off or On (0 or 1)
- There are 3 operations that will happen to the items
  - "turn on" the items (set them to 1)
  - "turn off" the items (set them to 0)
  - "toggle" the items (switch the values from 0 to 1, or vice versa)
- At the end, we need to return the number of items in the
  list that are set to 1

two major lists, x and y lists, and each one of those will have 

main list = grid

x list = grid[0]
y list = grid[1]

x list lights
y list lights
'''

def turn_on(x1, y1, x2, y2):
  # set all of the lights in the x,y coordinates to on (1)
  # turn_on(0,0,1,1) <-- should turn on four lights
  x = x1 
  y = y1
  while x <= x2:
    while y <= y2:
      grid[x][y] = True
      y += 1
    x += 1
    y = y1

def turn_off(x, y):
  x = x1 
  y = y1
  while x <= x2:
    while y <= y2:
      grid[x][y] = False
      y += 1
    x += 1
    y = y1

def toggle(x, y):
  x = x1 
  y = y1
  while x <= x2:
    while y <= y2:
      if grid[x][y] == False:
        grid[x][y] = True
      else:
        grid[x][y] = False
      y += 1
    x += 1
    y = y1

width = 5
height = 5

grid = [[False for x in range(width)] for y in range(height)]
print(grid)

turn_on(0,0,2,2)
print(grid)
'''
file_path = 'input.txt' # Replace with your file path

with open(file_path, 'r') as file:
  raw_input = file.readlines()
'''
'''
