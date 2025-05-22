# Dynamic Programming Guide with Practice Problems

Dynamic Programming (DP) is a powerful technique for solving complex problems by breaking them down into simpler subproblems. This guide covers the core concepts, implementation strategies, and practice problems to help you master DP for your CSCI 33500 final exam.

## Core Concepts

### What is Dynamic Programming?

Dynamic Programming is an algorithmic paradigm that solves complex problems by breaking them down into simpler subproblems and storing the results of these subproblems to avoid redundant computations.

### When to Use Dynamic Programming?

A problem is suitable for dynamic programming when it has the following properties:

1. **Optimal Substructure**: The optimal solution to the problem can be constructed from optimal solutions of its subproblems.

2. **Overlapping Subproblems**: The problem can be broken down into subproblems that are reused multiple times.

### Key Benefits of Dynamic Programming:
- Improves time complexity by eliminating redundant calculations
- Provides a systematic approach to optimization problems
- Works well for problems requiring counting arrangements or finding optimal values

## Implementation Approaches

There are two primary ways to implement dynamic programming solutions:

### 1. Top-Down Approach (Memoization)

In this approach, we start from the main problem and recursively solve its subproblems, storing the results to avoid recalculation.

```cpp
// Example: Fibonacci sequence with memoization
int fibonacci(int n, vector<int>& memo) {
    if (n <= 1) return n;
    
    // If already calculated, return stored result
    if (memo[n] != -1) return memo[n];
    
    // Calculate and store result
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo);
    return memo[n];
}

int fib(int n) {
    vector<int> memo(n+1, -1);
    return fibonacci(n, memo);
}
```

**Advantages**:
- Easier to implement for complex problems
- Only calculates necessary subproblems
- Preserves the recursive structure of the problem

**Disadvantages**:
- Stack overflow for very large inputs
- Overhead of recursion

### 2. Bottom-Up Approach (Tabulation)

In this approach, we start from the smallest subproblems and iteratively build up the solution to the main problem.

```cpp
// Example: Fibonacci sequence with tabulation
int fibonacci(int n) {
    if (n <= 1) return n;
    
    vector<int> dp(n+1);
    dp[0] = 0;
    dp[1] = 1;
    
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    
    return dp[n];
}
```

**Advantages**:
- No recursion overhead
- No stack overflow risk
- Often more efficient in terms of constant factors

**Disadvantages**:
- Sometimes less intuitive than the top-down approach
- May compute unnecessary subproblems

### 3. Space Optimization

Many DP problems allow for space optimization where you don't need to store the entire DP table.

```cpp
// Example: Space-optimized Fibonacci
int fibonacci(int n) {
    if (n <= 1) return n;
    
    int prev = 0;
    int curr = 1;
    
    for (int i = 2; i <= n; i++) {
        int next = prev + curr;
        prev = curr;
        curr = next;
    }
    
    return curr;
}
```

## Common DP Problem Patterns

### 1. Linear Sequence DP

**Pattern**: The state depends on previous elements in a sequence.
**Examples**: Fibonacci, maximum subarray sum

```cpp
// Maximum Subarray Sum
int maxSubArray(vector<int>& nums) {
    int currMax = nums[0];
    int globalMax = nums[0];
    
    for (int i = 1; i < nums.size(); i++) {
        currMax = max(nums[i], currMax + nums[i]);
        globalMax = max(globalMax, currMax);
    }
    
    return globalMax;
}
```

### 2. Two-Dimensional DP

**Pattern**: The state depends on a grid or matrix of previous results.
**Examples**: Grid path problems, edit distance

```cpp
// Grid Path Count
int uniquePaths(int m, int n) {
    vector<vector<int>> dp(m, vector<int>(n, 1));
    
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = dp[i-1][j] + dp[i][j-1];
        }
    }
    
    return dp[m-1][n-1];
}
```

### 3. State Transition DP

**Pattern**: DP state includes multiple variables, with complex transitions.
**Examples**: Knapsack problem, state machines

```cpp
// 0/1 Knapsack Problem
int knapsack(vector<int>& weights, vector<int>& values, int capacity) {
    int n = weights.size();
    vector<vector<int>> dp(n+1, vector<int>(capacity+1, 0));
    
    for (int i = 1; i <= n; i++) {
        for (int w = 1; w <= capacity; w++) {
            if (weights[i-1] <= w) {
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w]);
            } else {
                dp[i][w] = dp[i-1][w];
            }
        }
    }
    
    return dp[n][capacity];
}
```

### 4. Interval DP

**Pattern**: The state represents results for intervals of the input.
**Examples**: Matrix chain multiplication, optimal binary search tree

```cpp
// Matrix Chain Multiplication
int matrixChainMultiplication(vector<int>& dims) {
    int n = dims.size() - 1;
    vector<vector<int>> dp(n, vector<int>(n, 0));
    
    for (int len = 2; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            dp[i][j] = INT_MAX;
            
            for (int k = i; k < j; k++) {
                int cost = dp[i][k] + dp[k+1][j] + dims[i] * dims[k+1] * dims[j+1];
                dp[i][j] = min(dp[i][j], cost);
            }
        }
    }
    
    return dp[0][n-1];
}
```

### 5. Decision Making DP

**Pattern**: At each step, you need to make optimal decisions.
**Examples**: Stock buying/selling, game theory problems

```cpp
// Best Time to Buy and Sell Stock with Cooldown
int maxProfit(vector<int>& prices) {
    int n = prices.size();
    if (n <= 1) return 0;
    
    vector<int> buy(n, 0);
    vector<int> sell(n, 0);
    vector<int> cooldown(n, 0);
    
    buy[0] = -prices[0];
    
    for (int i = 1; i < n; i++) {
        buy[i] = max(buy[i-1], cooldown[i-1] - prices[i]);
        sell[i] = buy[i-1] + prices[i];
        cooldown[i] = max(cooldown[i-1], sell[i-1]);
    }
    
    return max(sell[n-1], cooldown[n-1]);
}
```

## Step-by-Step DP Problem Solving

Follow these steps to systematically approach dynamic programming problems:

### 1. Identify Subproblems
- Determine what a subproblem looks like
- Understand how subproblems relate to each other

### 2. Define State Variables
- What information do you need to uniquely identify a subproblem?
- Keep the number of state variables minimal but sufficient

### 3. Formulate the Recurrence Relation
- Express the solution to a problem in terms of solutions to smaller subproblems
- Identify base cases

### 4. Determine Calculation Order
- Ensure that subproblems are solved before they are needed
- For bottom-up: determine the iteration order
- For top-down: ensure proper memoization

### 5. Implement the Solution
- Choose between top-down and bottom-up approaches
- Consider space optimizations

### 6. Analyze Complexity
- Time complexity: number of subproblems × cost per subproblem
- Space complexity: size of memoization array or DP table

## Common Dynamic Programming Problems

### 1. Fibonacci Sequence

**Problem**: Find the nth Fibonacci number (F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1).

**DP Approach**:
- **State**: dp[i] = ith Fibonacci number
- **Recurrence**: dp[i] = dp[i-1] + dp[i-2]
- **Base Cases**: dp[0] = 0, dp[1] = 1

```cpp
int fibonacci(int n) {
    if (n <= 1) return n;
    
    vector<int> dp(n+1);
    dp[0] = 0;
    dp[1] = 1;
    
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    
    return dp[n];
}
```

**Time Complexity**: O(n)
**Space Complexity**: O(n), can be optimized to O(1)

### 2. Longest Increasing Subsequence (LIS)

**Problem**: Find the length of the longest subsequence in an array such that all elements of the subsequence are sorted in increasing order.

**DP Approach**:
- **State**: dp[i] = length of LIS ending at index i
- **Recurrence**: dp[i] = max(dp[j] + 1) for all j < i where arr[j] < arr[i]
- **Base Case**: dp[i] = 1 for all i (minimum LIS is of length 1)

```cpp
int lengthOfLIS(vector<int>& nums) {
    int n = nums.size();
    vector<int> dp(n, 1);
    int maxLen = 1;
    
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        maxLen = max(maxLen, dp[i]);
    }
    
    return maxLen;
}
```

**Time Complexity**: O(n²)
**Space Complexity**: O(n)

### 3. Coin Change

**Problem**: Given a set of coin denominations and a target amount, find the minimum number of coins needed to make up the amount.

**DP Approach**:
- **State**: dp[i] = minimum coins needed to make amount i
- **Recurrence**: dp[i] = min(dp[i], dp[i-coin] + 1) for each coin
- **Base Case**: dp[0] = 0, dp[i] = ∞ for i > 0

```cpp
int coinChange(vector<int>& coins, int amount) {
    vector<int> dp(amount + 1, amount + 1);
    dp[0] = 0;
    
    for (int i = 1; i <= amount; i++) {
        for (int coin : coins) {
            if (coin <= i) {
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }
    }
    
    return dp[amount] > amount ? -1 : dp[amount];
}
```

**Time Complexity**: O(amount × number of coins)
**Space Complexity**: O(amount)

### 4. Longest Common Subsequence (LCS)

**Problem**: Find the longest subsequence common to two sequences.

**DP Approach**:
- **State**: dp[i][j] = length of LCS of first i characters of string1 and first j characters of string2
- **Recurrence**: 
  - If characters match: dp[i][j] = dp[i-1][j-1] + 1
  - If not: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
- **Base Case**: dp[0][j] = dp[i][0] = 0

```cpp
int longestCommonSubsequence(string text1, string text2) {
    int m = text1.length();
    int n = text2.length();
    
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (text1[i-1] == text2[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    
    return dp[m][n];
}
```

**Time Complexity**: O(m × n)
**Space Complexity**: O(m × n), can be optimized to O(min(m, n))

### 5. Knapsack Problem

**Problem**: Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value.

**DP Approach**:
- **State**: dp[i][w] = maximum value that can be obtained using first i items and weight limit w
- **Recurrence**: 
  - Include item i: dp[i][w] = value[i-1] + dp[i-1][w-weight[i-1]] (if weight[i-1] ≤ w)
  - Exclude item i: dp[i][w] = dp[i-1][w]
  - Take maximum of the two options
- **Base Case**: dp[0][w] = 0 for all w

```cpp
int knapsack(vector<int>& weights, vector<int>& values, int W) {
    int n = weights.size();
    vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));
    
    for (int i = 1; i <= n; i++) {
        for (int w = 1; w <= W; w++) {
            if (weights[i-1] <= w) {
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w]);
            } else {
                dp[i][w] = dp[i-1][w];
            }
        }
    }
    
    return dp[n][W];
}
```

**Time Complexity**: O(n × W)
**Space Complexity**: O(n × W), can be optimized to O(W)

### 6. Edit Distance

**Problem**: Given two strings, find the minimum number of operations (insert, delete, replace) required to convert one string to another.

**DP Approach**:
- **State**: dp[i][j] = minimum edit distance between first i characters of string1 and first j characters of string2
- **Recurrence**: 
  - If characters match: dp[i][j] = dp[i-1][j-1]
  - If not: dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
- **Base Case**: dp[i][0] = i, dp[0][j] = j

```cpp
int minDistance(string word1, string word2) {
    int m = word1.length();
    int n = word2.length();
    
    vector<vector<int>> dp(m + 1, vector<int>(n + 1));
    
    // Base cases
    for (int i = 0; i <= m; i++) dp[i][0] = i;
    for (int j = 0; j <= n; j++) dp[0][j] = j;
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (word1[i-1] == word2[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = 1 + min({dp[i-1][j-1], dp[i-1][j], dp[i][j-1]});
            }
        }
    }
    
    return dp[m][n];
}
```

**Time Complexity**: O(m × n)
**Space Complexity**: O(m × n), can be optimized to O(min(m, n))

## Practice Problems (Exam-Style)

Here are some practice problems similar to what you might encounter on your exam:

### Problem 1: Maximum Path Sum in Grid

Given an m × n grid filled with non-negative numbers, find a path from top left to bottom right, which maximizes the sum of all numbers along its path. You can only move either down or right at any point.

**Approach**:
- **State**: dp[i][j] = maximum path sum to reach cell (i,j)
- **Recurrence**: dp[i][j] = grid[i][j] + max(dp[i-1][j], dp[i][j-1])
- **Base Cases**: 
  - dp[0][0] = grid[0][0]
  - dp[i][0] = dp[i-1][0] + grid[i][0] for i > 0
  - dp[0][j] = dp[0][j-1] + grid[0][j] for j > 0

```cpp
int maxPathSum(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    
    vector<vector<int>> dp(m, vector<int>(n, 0));
    dp[0][0] = grid[0][0];
    
    // Fill first column
    for (int i = 1; i < m; i++) {
        dp[i][0] = dp[i-1][0] + grid[i][0];
    }
    
    // Fill first row
    for (int j = 1; j < n; j++) {
        dp[0][j] = dp[0][j-1] + grid[0][j];
    }
    
    // Fill rest of dp table
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = grid[i][j] + max(dp[i-1][j], dp[i][j-1]);
        }
    }
    
    return dp[m-1][n-1];
}
```

**Time Complexity**: O(m × n)
**Space Complexity**: O(m × n), can be optimized to O(n)

### Problem 2: Count Ways to Reach a Score

Given a score n and three possible scores (3, 5, 10) for each move, find the number of ways to reach exactly score n.

**Approach**:
- **State**: dp[i] = number of ways to reach score i
- **Recurrence**: dp[i] = dp[i-3] + dp[i-5] + dp[i-10] if i ≥ respective score
- **Base Case**: dp[0] = 1 (one way to reach score 0: by not making any move)

```cpp
int countWaysToScore(int n) {
    vector<int> dp(n + 1, 0);
    dp[0] = 1;
    vector<int> scores = {3, 5, 10};
    
    for (int score : scores) {
        for (int i = score; i <= n; i++) {
            dp[i] += dp[i - score];
        }
    }
    
    return dp[n];
}
```

**Time Complexity**: O(n)
**Space Complexity**: O(n)

### Problem 3: Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s.

**Approach**:
- **State**: dp[i][j] = length of longest palindromic subsequence in substring s[i...j]
- **Recurrence**: 
  - If s[i] == s[j], dp[i][j] = dp[i+1][j-1] + 2
  - Otherwise, dp[i][j] = max(dp[i+1][j], dp[i][j-1])
- **Base Case**: dp[i][i] = 1 (single character is a palindrome of length 1)

```cpp
int longestPalindromeSubseq(string s) {
    int n = s.length();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    
    // Base case: single character subsequences
    for (int i = 0; i < n; i++) {
        dp[i][i] = 1;
    }
    
    // Fill the dp table
    for (int len = 2; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            if (s[i] == s[j]) {
                dp[i][j] = dp[i+1][j-1] + 2;
            } else {
                dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
            }
        }
    }
    
    return dp[0][n-1];
}
```

**Time Complexity**: O(n²)
**Space Complexity**: O(n²)

### Problem 4: Maximum Product Subarray

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

**Approach**:
- **States**: 
  - maxProd[i] = maximum product ending at index i
  - minProd[i] = minimum product ending at index i (to handle negative numbers)
- **Recurrence**: 
  - maxProd[i] = max(nums[i], nums[i] * maxProd[i-1], nums[i] * minProd[i-1])
  - minProd[i] = min(nums[i], nums[i] * maxProd[i-1], nums[i] * minProd[i-1])
- **Base Case**: maxProd[0] = minProd[0] = nums[0]

```cpp
int maxProduct(vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return 0;
    
    int maxProd = nums[0];
    int minProd = nums[0];
    int result = nums[0];
    
    for (int i = 1; i < n; i++) {
        int temp = maxProd;
        maxProd = max({nums[i], nums[i] * maxProd, nums[i] * minProd});
        minProd = min({nums[i], nums[i] * temp, nums[i] * minProd});
        result = max(result, maxProd);
    }
    
    return result;
}
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

### Problem 5: Minimum Path Sum in Triangle

Given a triangle array, find the minimum path sum from top to bottom. Each step you may move to an adjacent number of the row below.

**Approach**:
- **State**: dp[i][j] = minimum path sum to reach position (i,j) in the triangle
- **Recurrence**: dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])
- **Base Case**: dp[0][0] = triangle[0][0]

```cpp
int minimumTotal(vector<vector<int>>& triangle) {
    int n = triangle.size();
    vector<vector<int>> dp = triangle; // Copy the triangle
    
    for (int i = 1; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            if (j == 0) {
                dp[i][j] += dp[i-1][j]; // Only can come from above
            } else if (j == i) {
                dp[i][j] += dp[i-1][j-1]; // Only can come from above-left
            } else {
                dp[i][j] += min(dp[i-1][j-1], dp[i-1][j]); // Can come from above or above-left
            }
        }
    }
    
    return *min_element(dp[n-1].begin(), dp[n-1].end());
}
```

**Time Complexity**: O(n²), where n is the number of rows in the triangle
**Space Complexity**: O(n²), can be optimized to O(n)

### Problem 6: Word Break

Given a string s and a dictionary of strings wordDict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

**Approach**:
- **State**: dp[i] = whether the substring s[0...i-1] can be segmented into dictionary words
- **Recurrence**: dp[i] = true if dp[j] is true and s[j...i-1] is in the dictionary, for any j < i
- **Base Case**: dp[0] = true (empty string can always be segmented)

```cpp
bool wordBreak(string s, vector<string>& wordDict) {
    int n = s.length();
    vector<bool> dp(n + 1, false);
    dp[0] = true; // Empty string is always valid
    
    unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
    
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            if (dp[j] && wordSet.find(s.substr(j, i - j)) != wordSet.end()) {
                dp[i] = true;
                break;
            }
        }
    }
    
    return dp[n];
}
```

**Time Complexity**: O(n³) due to the substring operations, can be optimized
**Space Complexity**: O(n)

### Problem 7: Unique Binary Search Trees

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

**Approach**:
- **State**: dp[i] = number of unique BSTs with i nodes
- **Recurrence**: dp[i] = sum of dp[j-1] * dp[i-j] for j from 1 to i
- **Base Cases**: dp[0] = dp[1] = 1

```cpp
int numTrees(int n) {
    vector<int> dp(n + 1, 0);
    dp[0] = 1;
    dp[1] = 1;
    
    for (int i = 2; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            dp[i] += dp[j-1] * dp[i-j];
        }
    }
    
    return dp[n];
}
```

**Time Complexity**: O(n²)
**Space Complexity**: O(n)

### Problem 8: Best Time to Buy and Sell Stock with Cooldown

Say you have an array prices where prices[i] is the price of a given stock on the ith day. Find the maximum profit you can achieve. You may complete as many transactions as you like with the following restrictions:
- After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

**Approach**:
- **States**: 
  - buy[i] = maximum profit ending with a buy on day i or before
  - sell[i] = maximum profit ending with a sell on day i or before
  - cool[i] = maximum profit ending with a cooldown on day i or before
- **Recurrence**:
  - buy[i] = max(buy[i-1], cool[i-1] - prices[i])
  - sell[i] = max(sell[i-1], buy[i-1] + prices[i])
  - cool[i] = max(cool[i-1], sell[i-1])
- **Base Cases**: buy[0] = -prices[0], sell[0] = 0, cool[0] = 0

```cpp
int maxProfit(vector<int>& prices) {
    int n = prices.size();
    if (n <= 1) return 0;
    
    vector<int> buy(n, 0);
    vector<int> sell(n, 0);
    vector<int> cool(n, 0);
    
    buy[0] = -prices[0];
    
    for (int i = 1; i < n; i++) {
        buy[i] = max(buy[i-1], cool[i-1] - prices[i]);
        sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
        cool[i] = max(cool[i-1], sell[i-1]);
    }
    
    return max(sell[n-1], cool[n-1]);
}
```

**Time Complexity**: O(n)
**Space Complexity**: O(n), can be optimized to O(1)

### Problem 9: Minimum Falling Path Sum

Given an n x n matrix of integers, find the minimum sum of a falling path through the matrix. A falling path starts at any element in the first row and chooses one element from each row. The next row's choice must be in a column that is different from the previous row's column by at most one.

**Approach**:
- **State**: dp[i][j] = minimum falling path sum ending at position (i,j)
- **Recurrence**: dp[i][j] = matrix[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
- **Base Case**: dp[0][j] = matrix[0][j] for all j

```cpp
int minFallingPathSum(vector<vector<int>>& matrix) {
    int n = matrix.size();
    
    vector<vector<int>> dp = matrix; // Copy the matrix
    
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < n; j++) {
            // Calculate minimum from the three possible positions in the row above
            int left = (j > 0) ? dp[i-1][j-1] : INT_MAX;
            int up = dp[i-1][j];
            int right = (j < n-1) ? dp[i-1][j+1] : INT_MAX;
            
            dp[i][j] += min({left, up, right});
        }
    }
    
    return *min_element(dp[n-1].begin(), dp[n-1].end());
}
```

**Time Complexity**: O(n²)
**Space Complexity**: O(n²), can be optimized to O(n)

### Problem 10: Maximum Length of Pair Chain

You are given an array of pairs where pairs[i] = [lefti, righti] and lefti < righti. A pair chain is formed if for all 1 <= i < length, the right element of the ith pair is less than the left element of the (i+1)th pair. Return the length of the longest chain which can be formed.

**Approach**:
- **State**: dp[i] = length of the longest chain ending with pair i
- **Recurrence**: dp[i] = max(dp[j] + 1) for all j < i where pairs[j][1] < pairs[i][0]
- **Base Case**: dp[i] = 1 for all i (minimum chain length is 1)

```cpp
int findLongestChain(vector<vector<int>>& pairs) {
    int n = pairs.size();
    
    // Sort pairs by the first element
    sort(pairs.begin(), pairs.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });
    
    vector<int> dp(n, 1);
    int maxLength = 1;
    
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (pairs[j][1] < pairs[i][0]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        maxLength = max(maxLength, dp[i]);
    }
    
    return maxLength;
}
```

**Time Complexity**: O(n²)
**Space Complexity**: O(n)

## Common DP Exam Question Patterns

When preparing for your exam, be aware of these common DP question patterns:

1. **Pattern Recognition**: Identifying if a problem can be solved using DP
   - Look for optimal substructure and overlapping subproblems
   - Recognize common patterns like sequence, grid, or state transition

2. **State Definition**: Defining the state variables that uniquely identify subproblems
   - Single-variable states: dp[i]
   - Two-variable states: dp[i][j]
   - Multi-variable states: dp[i][j][k]

3. **Recurrence Relation Derivation**: Formulating the relationship between states
   - Understand the decisions that can be made at each state
   - Express current state in terms of previous states

4. **Base Case Identification**: Determining the simplest subproblems
   - Usually correspond to edge cases like empty arrays or strings
   - Serve as the foundation for building up the solution

5. **Implementation Approach Selection**: Choosing between top-down and bottom-up
   - Consider problem constraints, required information, and personal preference
   - Understand trade-offs in terms of simplicity, efficiency, and stack space

6. **Space Optimization**: Reducing memory usage
   - Recognize when only the last few states are needed
   - Convert 2D DP arrays to 1D when appropriate

7. **Path Reconstruction**: Retrieving the actual solution, not just its value
   - Track decisions made during DP computation
   - Backtrack through the DP table to reconstruct the path

## Exam Practice Tips

1. **Systematically identify the DP structure**:
   - Is there optimal substructure? (Can optimal solutions be built from optimal subsolutions?)
   - Are there overlapping subproblems? (Are the same subproblems solved multiple times?)

2. **Define the state clearly**:
   - What information do you need to uniquely identify a subproblem?
   - Keep the state as simple as possible while still capturing the necessary information

3. **Write out the recurrence relation explicitly**:
   - Make sure your recurrence relation covers all possible cases
   - Double-check edge cases and their handling

4. **Work through small examples by hand**:
   - Manually trace through the DP calculation for a small input
   - Verify that your recurrence relation produces the expected results

5. **Consider both implementation approaches**:
   - Top-down (memoization) is often more intuitive and easier to implement
   - Bottom-up (tabulation) is usually more efficient and avoids recursion overhead

6. **Watch for optimization opportunities**:
   - Can you reduce the state space?
   - Is there a more efficient way to compute or represent the states?

7. **Analyze time and space complexity**:
   - Count the number of distinct subproblems and the cost per subproblem
   - Consider if space optimization is possible

## Conclusion

Dynamic Programming is a powerful technique that can solve a wide range of optimization problems by breaking them down into simpler subproblems. By following a systematic approach, you can identify when to use DP, how to structure your solution, and how to implement it efficiently.

Remember the key principles:
- Identify optimal substructure and overlapping subproblems
- Define appropriate state variables
- Formulate correct recurrence relations
- Implement using top-down or bottom-up approach
- Optimize space usage when possible

With practice and understanding of these fundamental concepts, you'll be well-prepared to tackle DP problems on your final exam.
