# URL
https://adventofcode.com/2015/day/3
# Concept
* keeping track of 2D coordinates
* alternating between working on different elements in a list
# Instructions
--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

    ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.


# Code
```Python
def visited_houses(list):
  current_position = [[0,0],[0,0]]
  visited_positions = [(0, 0)]
  visited_total = 0
  current_direction = ''
  counter = 0
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
      current_position[counter %2][0] = current_position[counter %2][0] + 1
    elif current_direction == "s":
      current_position[counter %2][0] = current_position[counter %2][0] - 1
    elif current_direction == "w":
      current_position[counter %2][1] = current_position[counter %2][1] - 1
    else:
      current_position[counter %2][1] = current_position[counter %2][1] + 1
    # add the current position to the visited list
    visited_positions.append(tuple(current_position[(counter % 2)]))
    counter = counter + 1
  # total up the unique visited location
  unique_values_set = set(visited_positions)
  visited_total = len(unique_values_set)
  return visited_total

file_path = 'input.txt' # Replace with your file path

with open(file_path, 'r') as file:
    raw_input = file.readlines()

mod_list = []

for i in raw_input[0]:
  mod_list.append(i)

# pop off the last element in the list, which is a \n
mod_list.pop()

print(visited_houses(mod_list))
```
