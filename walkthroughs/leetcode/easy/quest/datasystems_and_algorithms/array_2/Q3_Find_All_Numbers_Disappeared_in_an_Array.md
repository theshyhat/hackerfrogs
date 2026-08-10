# URL
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Concept
* identifying missing elements in an list
# Instructions
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:

Input: nums = [1,1]
Output: [2]

 

Constraints:

    n == nums.length
    1 <= n <= 105
    1 <= nums[i] <= n

# Method of solve
```Python
'''
This program takes in an integer list, which starts at 1, and
ends at n, where n is the largest integer in the array,
and is also the stopping point

The program must output any numbers missing from the list
in the form of a list
'''
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        exp_list = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in exp_list]

sample_list = [1,1]

solve = Solution()
print(solve.findDisappearedNumbers(sample_list))
```
