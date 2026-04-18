# URL
https://adventofcode.com/2015/day/8
# Concept
* string parsing
* string content versus memory content
# Instructions
--- Day 8: Matchsticks ---

Space on the sleigh is limited this year, and so Santa will be bringing his list as a digital copy. He needs to know how much space it will take up when stored.

It is common in many programming languages to provide a way to escape special characters in strings. For example, C, JavaScript, Perl, Python, and even PHP handle special characters in very similar ways.

However, it is important to realize the difference between the number of characters in the code representation of the string literal and the number of characters in the in-memory string itself.

For example:

    "" is 2 characters of code (the two double quotes), but the string contains zero characters.
    "abc" is 5 characters of code, but 3 characters in the string data.
    "aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
    "\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.

Santa's list is a file that contains many double-quoted string literals, one on each line. The only escape sequences used are \\ (which represents a single backslash), \" (which represents a lone double-quote character), and \x plus two hexadecimal characters (which represents a single character with that ASCII code).

Disregarding the whitespace in the file, what is the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file?

For example, given the four strings above, the total number of characters of string code (2 + 5 + 10 + 6 = 23) minus the total number of characters in memory for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.

# Code
```Python
file_path = 'input.txt' # Replace with your file path

with open(file_path, 'r') as file:
    raw_input = file.readlines()

format_input = []

for i in raw_input:
  format_input.append(i.strip())

'''
In this program, we need to process all of the strings
in the input.txt file and keep track of two metrics:
1) the amount of characters in all of the strings
2) the amount of characters in memory

for example, "" is two characters in the string, but
zero characters in memory

At the end of the program, we need to subtract the
amount of characters in memory from the amount of
characters in the strings
'''

# The two variables we need to track to get
# the answer at the end of the program
total_char = 0
total_mem = 0

# There are three possible character escapes in the strings:
# 1) \\ <-- a backslash character
# 2) \" <-- a double-quote character
# 3) \x <-- a hexadecimal code for an ASCII character

# Calculate the total in-memory characters
for i in format_input:
  total_mem += len(eval(i))

# Calculate the total characters
for i in format_input:
#  all_chars = []
#  for j in i:
#    all_chars.append(j)
  total_char += len(i)

the_answer = total_char - total_mem

print(f"Total characters: {total_char}\nTotal memory: {total_mem}")
print(f"The answer we want is: {the_answer}")

```
