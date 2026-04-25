# URL
https://adventofcode.com/2015/day/9
# Concept
* calculating shortest distances
# Instructions
--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141

The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982

The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?

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

print(f"The shortest route is: {min(perms_dist_list)}")
```

