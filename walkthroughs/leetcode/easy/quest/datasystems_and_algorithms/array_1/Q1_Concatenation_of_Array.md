# URL
https://leetcode.com/problems/concatenation-of-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
# Concept
* concatenation of array contents
# Instructions
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]

Constraints:

    n == nums.length
    1 <= n <= 1000
    1 <= nums[i] <= 1000


# Method of solve
```Python
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums

num_list = [1,3,3,7]

solve = Solution()

print(solve.getConcatenation(num_list))
```
