# URL
https://adventofcode.com/2015/day/9#part2
# Concept
* creating permutation lists
* calculating shortest / longest routes
# Instructions
--- Part Two ---

The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?

# Code
```Python
from itertools import permutations

file_path = 'input.txt' # Replace with your file path

with open(file_path, 'r') as file:
    raw_input = file.readlines()

format_input = []

for i in raw_input:
  format_input.append(i.strip())

'''
In this program we need to calculate shortest distances between
multiple cities, with city being visited once

We'll use the following steps:
1) Take in the input and:
   - figure out the number of unique cities,
     populating a list
   - record the starting city, ending city, and distance
     in a dictionary
2) Create a function that takes in the list of cities and
   outputs a list of lists that contain every possible
   permutation of those cities
3) Create a function that takes in the permutations list of
   lists and calculates the total distance of travel for
   each permutation, recording the distances in a new list
4) Find the lowest value in the final list created in step 3
'''

# Program variables
# The list of unique cities
uniq_cities_list = []
# The dictionary of distances 
dist_dict = {}
# The permutations of all cities
city_perms_list = []
# The distances totals of the city_perms list
perms_dist_list = []

# Populating the unique cities list
for i in format_input:
  city1 = i.split()[0]
  city2 = i.split()[2]
  if city1 not in uniq_cities_list:
    uniq_cities_list.append(city1)
  if city2 not in uniq_cities_list:
    uniq_cities_list.append(city2)

# Populating the distances dictionary
for i in format_input:
  string_list = i.split()
  city1 = string_list[0]
  city2 = string_list[2]
  distance = string_list[-1]
  entry1 = f"{city1} to {city2}"
  entry2 = f"{city2} to {city1}" 
  dist_dict[entry1] = int(distance)
  dist_dict[entry2] = int(distance)

# Populate the permuations list of lists
city_perms_list = [list(p) for p in permutations(uniq_cities_list)]

# Populate the permutation distance list
for i in city_perms_list:
  dist_total = 0
  pairs = [f"{a} to {b}" for a,b in zip(i,i[1:])]
  for j in pairs:
    dist_total += dist_dict[j]
  perms_dist_list.append(dist_total)

print(f"The longest route is: {max(perms_dist_list)}")
```
