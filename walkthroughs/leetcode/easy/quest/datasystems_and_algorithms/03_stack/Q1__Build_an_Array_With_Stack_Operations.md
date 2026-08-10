# URL
https://leetcode.com/problems/build-an-array-with-stack-operations
# Concept
* build a specific list with memory stack-like operations
# Instructions
You are given an integer array target and an integer n.

You have an empty stack with the two following operations:

    "Push": pushes an integer to the top of the stack.
    "Pop": removes the integer on the top of the stack.

You also have a stream of the integers in the range [1, n].

Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to target. You should follow the following rules:

    If the stream of the integers is not empty, pick the next integer from the stream and push it to the top of the stack.
    If the stack is not empty, pop the integer at the top of the stack.
    If, at any moment, the elements in the stack (from the bottom to the top) are equal to target, do not read new integers from the stream and do not do more operations on the stack.

Return the stack operations needed to build target following the mentioned rules. If there are multiple valid answers, return any of them.

 

Example 1:

Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation: Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Pop the integer on the top of the stack. s = [1].
Read 3 from the stream and push it to the stack. s = [1,3].

Example 2:

Input: target = [1,2,3], n = 3
Output: ["Push","Push","Push"]
Explanation: Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Read 3 from the stream and push it to the stack. s = [1,2,3].

Example 3:

Input: target = [1,2], n = 4
Output: ["Push","Push"]
Explanation: Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Since the stack (from the bottom to the top) is equal to target, we stop the stack operations.
The answers that read integer 3 from the stream are not accepted.

 

Constraints:

    1 <= target.length <= 100
    1 <= n <= 100
    1 <= target[i] <= n
    target is strictly increasing.


# Method of solve
```Python
'''
We are given a target list, which has the numbers and positions
we want to create

We are to populate a list, called the "stack" with the
elements in the target list

We are also given a number which is the largest number
in a list of integers that we populate the "stack" with,
called the stream

We have two operations we can do to our list:
Push: which appends to the end of the stack list, the current
number in the stream
Pop: which removes the last element in the stack list

We need to record which operations (push and pop) we
did to arrive at our solution, and return it at the
end of the program
'''
class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        instruct_list = []
        # keep track of the elements in the stack
        stack_elements = 0
        # keep track of position to check in the target
        target_pos = 0
        # run the loop a number of times equal to n
        for i in range(1,n+1):
            # always push
            instruct_list.append("Push")
            stack_elements += 1
            print("We pushed!")
            # and if the next element in the target
            # is more than the next iteration number
            if i < target[target_pos]:
                instruct_list.append("Pop")
                stack_elements -= 1
                print("We popped!")
            # increment the target_pos value
            if stack_elements != target_pos:
                target_pos += 1
            # check if our target length matches our elements
            if stack_elements == len(target):
                return instruct_list

sample_list = [1,2,3]
sample_n = 3

solve = Solution()
print(solve.buildArray(sample_list,sample_n))
```
