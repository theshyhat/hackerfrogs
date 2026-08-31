# URL
https://leetcode.com/problems/exclusive-time-of-functions/description/
# Concept
* call stacks
* CPU cycles
# Instructions
On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n - 1.

Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2. Note that a function can be called multiple times, possibly recursively.

A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.

Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i.
# Method of solve
```Python
'''
In our program we need to calculate how much time
each function in a period of time a CPU ran the
function for. There are n numbers of functions,
and the log keeps track of how long each function
ran for. The program must return the number of
time units each function ran for in an integer list.

We need to keep track of the number of functions,
and which function is being run, and for how long.
The call stack can only hold one function at a time,
and when the function is started, it is pushed on the stack,
and when it finishes, it is popped off the stack. There can
be multiple functions on the stack at once.
'''
class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        # the lists to keep track of the stack and functions
        final_list = []
        stack = []
        idAndTime = {}
        curr_time = 0
        time_diff = 0
        # parsing the logs
        for i in logs:
            funcID = int(i.split(':')[0])
            action = i.split(':')[1]
            timeStp = int(i.split(':')[2])
            # populate the function and time dictionary
            # if the entry doesn't already exist
            if funcID not in idAndTime:
                idAndTime[funcID] = 0
            # calculate the time
            if (action == "start" and stack):
                idAndTime[stack[-1]] += (timeStp - curr_time)
            if action == "end":
                timeStp += 1
                idAndTime[funcID] += (timeStp - curr_time)
            # update the call stack (if required)
            if action == "start":
                stack.append(funcID)
            # update the current time
            if curr_time != timeStp:
                curr_time = timeStp
            # pop off the stack if it's an end action
            if action == "end":
                stack.pop()
        # populate the final list
        for i in idAndTime.values():
            final_list.append(i)
        return final_list

sample_n = 2
sample_logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]

solve = Solution()
run = solve.exclusiveTime(sample_n,sample_logs)
print(run)

```
