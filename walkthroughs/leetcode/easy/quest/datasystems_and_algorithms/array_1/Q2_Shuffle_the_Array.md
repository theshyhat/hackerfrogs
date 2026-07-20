# URL
https://leetcode.com/problems/shuffle-the-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
# Concept
* rearranging the contents of arrays
# Instructions
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

 

Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

Example 2:

Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]

Example 3:

Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]

 

Constraints:

    1 <= n <= 500
    nums.length == 2n
    1 <= nums[i] <= 10^3

# Method of solve
```Python
'''
In this challenge we're given a list and
a number where the list will be split into two
E.g., list = [1,2,3,4]
      n = 2
      We should arrange the list
      into two lists: first = [1,2]
                      second = [3,4]

The challenge wants us return a single list
where first[0], then second[0], then first[1], second[1], etc..
'''

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        first = nums[:len(nums)//2]
        second = nums[len(nums)//2:]
        new_list = [None]*(len(first)+len(second))
        new_list[::2] = first
        new_list[1::2] = second
        return new_list

num_list = [1,2,3,4]

solve = Solution()

print(solve.shuffle(num_list,n=2))
```
