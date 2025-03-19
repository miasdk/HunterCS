# Dynamic Programming Cheat Sheet

## Key Concepts
- **Memoization**: Store results of expensive function calls and reuse them.
- **Tabulation**: Build a table iteratively to store results of subproblems.

## Common Problems
| Problem                     | Description                          | Time Complexity | Space Complexity |
|-----------------------------|--------------------------------------|-----------------|------------------|
| Fibonacci Sequence          | Compute the nth Fibonacci number    | O(n)            | O(n)             |
| 0/1 Knapsack                | Maximize value without exceeding capacity | O(nW)         | O(nW)            |
| Longest Common Subsequence (LCS) | Find the longest subsequence common to two strings | O(mn) | O(mn) |
| Coin Change                 | Minimum number of coins to make a value | O(nV)          | O(V)             |

## Steps to Solve DP Problems
1. Define the problem recursively.
2. Identify overlapping subproblems.
3. Decide between memoization or tabulation.
4. Implement the solution.