# URL
https://adventofcode.com/2015/day/3
# Description
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

    > delivers presents to 2 houses: one at the starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

# Concept
* recording 2D coordinates
# Code
```Python
def visited_houses(list):
  current_position = [0,0]
  visited_positions = []
  visited_total = 0
  current_direction = ''
  # set the direction
  for i in list:
    if i == '^':
      current_direction = "n"
    elif i == 'v':
      current_direction = "s"
    elif i == '<':
      current_direction = "w"
    else:
      current_direction = "e"
    # set the position
    if current_direction == "n":
      current_position[0] = current_position[0] + 1
    elif current_direction == "s":
      current_position[0] = current_position[0] - 1
    elif current_direction == "w":
      current_position[1] = current_position[1] - 1
    else:
      current_position[1] = current_position[1] + 1
    # add the current position to the visited list
    visited_positions.append(tuple(current_position))
  # total up the unique visited location
  unique_values_set = set(visited_positions)
  visited_total = len(unique_values_set)
  visited_total = visited_total + 1
  return visited_total

file_path = 'input.txt' # Replace with your file path

with open(file_path, 'r') as file:
    raw_input = file.readlines()

mod_list = []

for i in raw_input[0]:
  mod_list.append(i)

mod_list.pop()

print(visited_houses(mod_list))
```
