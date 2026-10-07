# URL
https://leetcode.com/problems/richest-customer-wealth
# Challenge description
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

 

Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.

Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.

Example 3:

Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17

# Concept
* summing up all the numbers in different lists
* returning the largest number
# Python Code
```Python
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        richest_value = 0
        for account in accounts:
            if sum(account) > richest_value:
                richest_value = sum(account)
        return richest_value

test_account = [[1,5],[7,3],[3,5]]

solve = Solution()
run = solve.maximumWealth(accounts=test_account)
print(run)
```
# C Code
```C
#include <stdio.h>
#include <stdlib.h>

// The function declaration
int maximumWealth(int** accounts, int accountsSize, int* accountsColSize) {
int i = 0, j = 0;
  int biggest = 0;
  int current = 0;
  for (i = 0; i < accountsSize; i++) {
    for (j = 0; j < accountsColSize[i]; j++) {
      current += accounts[i][j];
    }
    if (current > biggest) {
        biggest = current;
    }
    current = 0;
  }
  return biggest;
}

int main() {
    // Let's create a 3x2 grid (3 customers, 2 accounts each)
    int rows = 3;
    int cols = 2;

    // 1. Set up 'accounts' (int**)
    int** accounts = (int**)malloc(rows * sizeof(int*));
    for (int i = 0; i < rows; i++) {
        accounts[i] = (int*)malloc(cols * sizeof(int));
    }

    // Populate the grid with some money data
    // Customer 0: [$1, $2] -> Total $3
    accounts[0][0] = 1; accounts[0][1] = 2; 
    // Customer 1: [$3, $5] -> Total $8 (Richest!)
    accounts[1][0] = 3; accounts[1][1] = 5; 
    // Customer 2: [$2, $1] -> Total $3
    accounts[2][0] = 2; accounts[2][1] = 1; 

    // 2. Set up 'accountsSize' (int)
    int accountsSize = rows;

    // 3. Set up 'accountsColSize' (int*)
    // We need an array of size 3, where each element is '2' (columns)
    int* accountsColSize = (int*)malloc(rows * sizeof(int));
    for (int i = 0; i < rows; i++) {
        accountsColSize[i] = cols;
    }

    // --- MAKING THE CALL ---
    int richest = maximumWealth(accounts, accountsSize, accountsColSize);

    printf("The maximum wealth is: %d\n", richest); // Output should be 8

    // (Good practice: free memory here afterward)
    return 0;
}
```
