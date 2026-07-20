# URL
https://leetcode.com/problems/max-consecutive-ones/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
# Instructions
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

 

Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.


# Concept
* keeping a runnning tally inside of a for loop
# Method of solve
```Python
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        current_streak = 0
        max_streak = 0
        for i in nums:
            if i == 1:
                current_streak += 1
            else:
                if current_streak > max_streak:
                    max_streak = current_streak
                current_streak = 0
        if current_streak > max_streak:
            max_streak = current_streak
        return max_streak

test_nums = [0,1,1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1]

solve = Solution()
print(solve.findMaxConsecutiveOnes(test_nums))
```

