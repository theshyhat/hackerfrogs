# URL
https://leetcode.com/problems/convert-date-to-binary
# Challenge description
You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.

date can be written in its binary representation obtained by converting year, month, and day to their binary representations without any leading zeroes and writing them down in year-month-day format.

Return the binary representation of date.

 

Example 1:

Input: date = "2080-02-29"

Output: "100000100000-10-11101"

Explanation:

100000100000, 10, and 11101 are the binary representations of 2080, 02, and 29 respectively.

Example 2:

Input: date = "1900-01-01"

Output: "11101101100-1-1"

Explanation:

11101101100, 1, and 1 are the binary representations of 1900, 1, and 1 respectively.

# Concept
* conversion of decimal numbers to binary numbers
* string formatting
# Code
```
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date_list = date.split("-")
        year = int(date_list[0])
        month = int(date_list[1])
        day = int(date_list[2])
        binary_year = bin(year)
        binary_month = bin(month)
        binary_day = bin(day)
        formatted_year = binary_year[2:]
        formatted_month = binary_month[2:]
        formatted_day = binary_day[2:]
        return f"{formatted_year}-{formatted_month}-{formatted_day}"

test_date = "2080-02-29"

solve = Solution()
run = solve.convertDateToBinary(test_date)
print(run)
```

