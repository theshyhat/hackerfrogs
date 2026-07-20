# URL
https://leetcode.com/problems/set-mismatch/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii
# Instructions
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:

Input: nums = [1,1]
Output: [1,2]

 

Constraints:

    2 <= nums.length <= 104
    1 <= nums[i] <= 104


# Concept
* iterating over a list
  * find a duplicate element
  * find a missing element in a set
# Method of solve
```Python
'''
In this challenge, we are given a list of numbers
The list have one number duplicated and
one number omitted from the set
The function has to return the duplicated number
and the missing number, as a list
'''

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        dupe = 0
        missing = 0
        set_size = len(nums)
        solve_list = []

        # figure out which number is duplicated
        for i in range(1,set_size + 1):
              num_count = nums.count(i)
              if nums.count(i) == 2:
                  dupe = i
                  break
        # figure out which number is missing
        # remove the dupe
        nums.remove(dupe)
        missing = sum(range(1,set_size + 1)) - sum(nums)

        solve_list.append(dupe)
        solve_list.append(missing)
        return solve_list

sample_set = [1,2,2,4]

solve = Solution()
print(solve.findErrorNums(sample_set))
```
