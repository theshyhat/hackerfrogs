# URL
https://adventofcode.com/2015/day/2#part2
# Instructions
--- Part Two ---

The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

    A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
    A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.

How many total feet of ribbon should they order?
# Concept
* more math functions
# Code
```
file_path = 'input.txt' # Replace with your file path

with open(file_path, 'r') as file:
    raw_input = file.readlines()

mod_list = []

for i in raw_input:
  mod_list.append(i[:-1])

def calc_ribbon(list):
  total = 0
  for i in list:
    dimensions = i.split('x')
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])
    dimension_list = [l,w,h]
    dimension_list.sort()
    shortest_side = dimension_list[0]
    second_shortest = dimension_list[1]
    ribbon_wrap = (shortest_side * 2) + (second_shortest * 2)
    total += ribbon_wrap
    cubic_dimensions = l*w*h
    total += cubic_dimensions
  return total

print(calc_ribbon(mod_list))
```

