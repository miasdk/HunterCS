# Dynamic Programming Mastery Guide: 1D and 2D Array Problems in C++

## Table of Contents
1. [Introduction to Dynamic Programming](#introduction-to-dynamic-programming)
2. [Fundamental Principles](#fundamental-principles)
3. [Systematic Approach to DP Problems](#systematic-approach-to-dp-problems)
4. [1D Array Dynamic Programming](#1d-array-dynamic-programming)
5. [2D Array/Matrix Dynamic Programming](#2d-arraymatrix-dynamic-programming)
6. [Problem Collection: 1D Array Problems](#problem-collection-1d-array-problems)
7. [Problem Collection: 2D Array Problems](#problem-collection-2d-array-problems)
8. [Implementation Strategy](#implementation-strategy)
9. [Testing and Debugging Strategies](#testing-and-debugging-strategies)
10. [Practical Tips and Tricks](#practical-tips-and-tricks)
11. [Progression Path](#progression-path)
12. [Decision Flowcharts](#decision-flowcharts)
13. [Conclusion](#conclusion)

## Introduction to Dynamic Programming

Dynamic Programming (DP) is a powerful algorithmic technique for solving complex problems by breaking them down into simpler subproblems. It's particularly effective for optimization problems that exhibit two key properties:

1. **Optimal Substructure**: An optimal solution to the problem contains optimal solutions to its subproblems.
2. **Overlapping Subproblems**: The same subproblems are solved multiple times during computation.

Array-based dynamic programming is one of the most common applications of DP, where states and transitions are represented using 1D or 2D arrays.

## Fundamental Principles

### Core Concepts

1. **Subproblem Definition**: Identify smaller instances of the original problem.
2. **State Representation**: Determine the variables needed to represent a subproblem.
3. **Recurrence Relation**: Define how to compute solutions from previously solved subproblems.
4. **Base Cases**: Define solutions for the smallest subproblems.
5. **State Space**: The collection of all possible states in the problem.
6. **Transitions**: Rules for moving between states.

### Key Approaches in Dynamic Programming

1. **Top-Down (Memoization)**: Recursive approach with caching of results.# Dynamic Programming Mastery Guide: 1D and 2D Array Problems in C++

## Table of Contents
1. [Introduction to Dynamic Programming](#introduction-to-dynamic-programming)
2. [Fundamental Principles](#fundamental-principles)
3. [Systematic Approach to DP Problems](#systematic-approach-to-dp-problems)
4. [1D Array Dynamic Programming](#1d-array-dynamic-programming)
5. [2D Array/Matrix Dynamic Programming](#2d-arraymatrix-dynamic-programming)
6. [Problem Collection: 1D Array Problems](#problem-collection-1d-array-problems)
7. [Problem Collection: 2D Array Problems](#problem-collection-2d-array-problems)
8. [Implementation Strategy](#implementation-strategy)
9. [Testing and Debugging Strategies](#testing-and-debugging-strategies)
10. [Practical Tips and Tricks](#practical-tips-and-tricks)
11. [Progression Path](#progression-path)
12. [Decision Flowcharts](#decision-flowcharts)
13. [Conclusion](#conclusion)

## Introduction to Dynamic Programming

Dynamic Programming (DP) is a powerful algorithmic technique for solving complex problems by breaking them down into simpler subproblems. It's particularly effective for optimization problems that exhibit two key properties:

1. **Optimal Substructure**: An optimal solution to the problem contains optimal solutions to its subproblems.
2. **Overlapping Subproblems**: The same subproblems are solved multiple times during computation.

Array-based dynamic programming is one of the most common applications of DP, where states and transitions are represented using 1D or 2D arrays.

## Fundamental Principles

### Core Concepts

1. **Subproblem Definition**: Identify smaller instances of the original problem.
2. **State Representation**: Determine the variables needed to represent a subproblem.
3. **Recurrence Relation**: Define how to compute solutions from previously solved subproblems.
4. **Base Cases**: Define solutions for the smallest subproblems.
5. **State Space**: The collection of all possible states in the problem.
6. **Transitions**: Rules for moving between states.

### Key Approaches in Dynamic Programming

1. **Top-Down (Memoization)**: Recursive approach with caching of results.
2. **Bottom-Up (Tabulation)**: Iterative approach building solutions from base cases.

### When to Use Dynamic Programming

- Optimization problems (maximize/minimize)
- Counting problems (how many ways)
- Decision problems (is it possible)
- Problems with recursive structure
- Problems with overlapping subproblems

## Systematic Approach to DP Problems

### 1. Define the State

- What information do we need to represent a subproblem?
- For 1D problems: Usually an index `i` or a value `x`.
- For 2D problems: Usually a pair of indices `(i, j)` or additional parameters.

### 2. Establish the Recurrence Relation

- How do we transition between states?
- What decisions or choices are available at each state?
- How do we derive optimal solutions from subproblems?

### 3. Identify Base Cases

- What are the simplest subproblems we can solve directly?
- What happens at boundaries or when the input is empty?

### 4. Determine the Order of Computation

- Which subproblems need to be solved first?
- How do we ensure all dependencies are resolved before computing a state?

### 5. Implement the Solution

- Top-down: Recursive function with memoization
- Bottom-up: Iterative computation with tabulation

### Difference Between 1D and 2D DP Approaches

| Aspect | 1D Dynamic Programming | 2D Dynamic Programming |
|--------|------------------------|------------------------|
| State Representation | Usually single parameter: `dp[i]` | Usually two parameters: `dp[i][j]` |
| Problem Complexity | Generally simpler | Often more complex |
| Space Requirements | O(n) typically | O(n²) or O(n×m) typically |
| Common Applications | Sequences, linear decision making | Matrices, grid problems, comparing sequences |
| Implementation | Usually simpler nested loops | Multiple nested loops, more complex |
| State Transitions | Fewer possible state transitions | More possible state transitions |
| Space Optimization | Often can reduce to O(1) or O(k) | Can sometimes reduce to O(n) or O(2×n) |

## 1D Array Dynamic Programming

### Conceptual Framework

In 1D DP problems, we typically use a single array `dp[]` where each element represents the solution to a subproblem defined by a single parameter (usually an index or value).

#### State Definition

- `dp[i]` typically represents the optimal answer for the subproblem considering elements up to index `i`.

#### Common State Transitions

- From previous states: `dp[i] = f(dp[i-1], dp[i-2], ..., dp[i-k])`
- Considering multiple choices: `dp[i] = optimal(choice1, choice2, ...)`

### Problem Types and Techniques

1. **Linear Sequence Problems**
   - Maximum/minimum sum subarrays
   - Longest increasing subsequences
   
2. **Decision-Making Problems**
   - Take or skip current element
   - Choose one of multiple options
   
3. **Optimization with Constraints**
   - Knapsack problems
   - Problems with limited resources
   
4. **Interval-Based Problems**
   - Problems involving ranges or segments
   - Partitioning problems

### Implementation Templates

#### Top-Down (Memoization)

```cpp
// Recursive function with memoization
int dp[MAX_N];
bool computed[MAX_N];

int solve(int i) {
    // Base cases
    if (i < 0) return 0;
    if (i == 0) return baseValue;
    
    // Return cached result if available
    if (computed[i]) return dp[i];
    
    // Compute result from subproblems
    int result = 0;
    // Example: Choose maximum from previous states
    result = max(solve(i-1) + value1, solve(i-2) + value2);
    
    // Cache and return result
    computed[i] = true;
    dp[i] = result;
    return result;
}
```

#### Bottom-Up (Tabulation)

```cpp
// Iterative function with tabulation
int solve(vector<int>& nums) {
    int n = nums.size();
    vector<int> dp(n+1, 0);
    
    // Base cases
    dp[0] = baseValue;
    
    // Fill dp table
    for (int i = 1; i <= n; i++) {
        // Example: Choose maximum from previous states
        dp[i] = max(dp[i-1] + value1, (i >= 2 ? dp[i-2] + value2 : 0));
    }
    
    return dp[n];
}
```

#### Space-Optimized Implementation

```cpp
// Space-optimized solution
int solve(vector<int>& nums) {
    int n = nums.size();
    
    // Only store necessary previous states
    int prev2 = 0;
    int prev1 = baseValue;
    int current = prev1;
    
    for (int i = 1; i <= n; i++) {
        current = max(prev1 + value1, prev2 + value2);
        prev2 = prev1;
        prev1 = current;
    }
    
    return current;
}
```

## 2D Array/Matrix Dynamic Programming

### Conceptual Framework

In 2D DP problems, we typically use a 2D array `dp[][]` where each element represents the solution to a subproblem defined by two parameters (usually a pair of indices).

#### State Definition

- `dp[i][j]` typically represents the optimal answer for a subproblem defined by coordinates `(i, j)` or considering elements up to indices `i` and `j` in two different contexts.

#### Common State Transitions

- From adjacent cells: `dp[i][j] = f(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`
- Considering multiple paths or choices: `dp[i][j] = optimal(choice1, choice2, ...)`

### Problem Types and Techniques

1. **Grid Traversal with Constraints**
   - Unique paths
   - Path with obstacles
   - Minimum/maximum path sum
   
2. **Matrix Path Optimization**
   - Shortest/longest paths
   - Paths with special properties
   
3. **String Comparison Problems**
   - Longest common subsequence/substring
   - Edit distance
   
4. **Interval-Based Problems**
   - Matrix chain multiplication
   - Burst balloons

### Implementation Templates

#### Top-Down (Memoization)

```cpp
// Recursive function with memoization
int dp[MAX_M][MAX_N];
bool computed[MAX_M][MAX_N];

int solve(int i, int j) {
    // Base cases and boundary checks
    if (i < 0 || j < 0) return INF; // or appropriate value
    if (i == 0 && j == 0) return baseValue;
    
    // Return cached result if available
    if (computed[i][j]) return dp[i][j];
    
    // Compute result from subproblems
    int result = INF; // or appropriate initial value
    
    // Example: Choose minimum path from adjacent cells
    result = min(solve(i-1, j), solve(i, j-1)) + cost[i][j];
    
    // Cache and return result
    computed[i][j] = true;
    dp[i][j] = result;
    return result;
}
```

#### Bottom-Up (Tabulation)

```cpp
// Iterative function with tabulation
int solve(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<int>> dp(m, vector<int>(n, 0));
    
    // Base case
    dp[0][0] = grid[0][0];
    
    // Fill first row
    for (int j = 1; j < n; j++) {
        dp[0][j] = dp[0][j-1] + grid[0][j];
    }
    
    // Fill first column
    for (int i = 1; i < m; i++) {
        dp[i][0] = dp[i-1][0] + grid[i][0];
    }
    
    // Fill rest of the dp table
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
        }
    }
    
    return dp[m-1][n-1];
}
```

#### Space-Optimized Implementation

```cpp
// Space-optimized solution
int solve(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    
    // Only store current and previous row
    vector<int> prev(n, 0);
    vector<int> curr(n, 0);
    
    prev[0] = grid[0][0];
    
    // Fill first row in prev
    for (int j = 1; j < n; j++) {
        prev[j] = prev[j-1] + grid[0][j];
    }
    
    // Process row by row
    for (int i = 1; i < m; i++) {
        curr[0] = prev[0] + grid[i][0];
        
        for (int j = 1; j < n; j++) {
            curr[j] = min(prev[j], curr[j-1]) + grid[i][j];
        }
        
        // Swap rows for next iteration
        prev = curr;
    }
    
    return prev[n-1];
}
```

## Problem Collection: 1D Array Problems

### Problem 1: Maximum Subarray Sum
**Difficulty**: Easy

**Problem Statement**:
Given an array of integers, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Real-World Context**:
This problem simulates financial analysis, where an analyst needs to identify the time period with the maximum profit given daily profit/loss data.

**Recurrence Relation**:
Let `dp[i]` be the maximum sum ending at index `i`.
```
dp[i] = max(nums[i], dp[i-1] + nums[i])
```

**Solutions**:

```cpp
// Tabulated (Bottom-Up) Approach
int maxSubArray(vector<int>& nums) {
    int n = nums.size();
    vector<int> dp(n);
    
    // Base case
    dp[0] = nums[0];
    int maxSum = dp[0];
    
    // Fill dp table
    for (int i = 1; i < n; i++) {
        dp[i] = max(nums[i], dp[i-1] + nums[i]);
        maxSum = max(maxSum, dp[i]);
    }
    
    return maxSum;
}

// Space-Optimized Approach
int maxSubArray(vector<int>& nums) {
    int n = nums.size();
    int currentMax = nums[0];
    int globalMax = nums[0];
    
    for (int i = 1; i < n; i++) {
        currentMax = max(nums[i], currentMax + nums[i]);
        globalMax = max(globalMax, currentMax);
    }
    
    return globalMax;
}
```

**Complexity Analysis**:
- Time Complexity: O(n)
- Space Complexity: O(1) for the optimized solution

### Problem 2: Climb Stairs
**Difficulty**: Easy

**Problem Statement**:
You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Real-World Context**:
This problem models movement planning, like a robot navigating different-sized steps or a player making moves in a board game with specific rules.

**Recurrence Relation**:
Let `dp[i]` be the number of ways to reach step `i`.
```
dp[i] = dp[i-1] + dp[i-2]
```

**Solutions**:

```cpp
// Tabulated (Bottom-Up) Approach
int climbStairs(int n) {
    if (n <= 2) return n;
    
    vector<int> dp(n+1);
    
    // Base cases
    dp[1] = 1;
    dp[2] = 2;
    
    // Fill dp table
    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    
    return dp[n];
}

// Space-Optimized Approach
int climbStairs(int n) {
    if (n <= 2) return n;
    
    int prev2 = 1; // Ways to reach step 1
    int prev1 = 2; // Ways to reach step 2
    int current = 0;
    
    for (int i = 3; i <= n; i++) {
        current = prev1 + prev2;
        prev2 = prev1;
        prev1 = current;
    }
    
    return prev1;
}
```

**Complexity Analysis**:
- Time Complexity: O(n)
- Space Complexity: O(1) for the optimized solution

### Problem 3: House Robber
**Difficulty**: Medium

**Problem Statement**:
A professional robber plans to rob houses along a street. Each house has a certain amount of money stashed. The only constraint is that adjacent houses have connected security systems and will automatically contact the police if two adjacent houses were broken into on the same night. Determine the maximum amount of money the robber can rob tonight without alerting the police.

**Real-World Context**:
This problem models resource allocation with constraints, such as choosing investment opportunities where certain combinations cannot be selected together.

**Recurrence Relation**:
Let `dp[i]` be the maximum amount of money that can be robbed up to house `i`.
```
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
```

**Solutions**:

```cpp
// Tabulated (Bottom-Up) Approach
int rob(vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return 0;
    if (n == 1) return nums[0];
    
    vector<int> dp(n);
    
    // Base cases
    dp[0] = nums[0];
    dp[1] = max(nums[0], nums[1]);
    
    // Fill dp table
    for (int i = 2; i < n; i++) {
        dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
    }
    
    return dp[n-1];
}

// Space-Optimized Approach
int rob(vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return 0;
    if (n == 1) return nums[0];
    
    int prev2 = nums[0];
    int prev1 = max(nums[0], nums[1]);
    
    for (int i = 2; i < n; i++) {
        int current = max(prev1, prev2 + nums[i]);
        prev2 = prev1;
        prev1 = current;
    }
    
    return prev1;
}
```

**Complexity Analysis**:
- Time Complexity: O(n)
- Space Complexity: O(1) for the optimized solution

### Problem 4: Coin Change
**Difficulty**: Medium

**Problem Statement**:
You are given coins of different denominations and a total amount of money. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

**Real-World Context**:
This problem models the classic coin change scenario faced by cashiers and automated vending machines that need to provide optimal change with limited denomination options.

**Recurrence Relation**:
Let `dp[i]` be the fewest number of coins needed to make amount `i`.
```
dp[i] = min(dp[i-coin] + 1) for all coin in coins if i-coin >= 0
```

**Solutions**:

```cpp
// Tabulated (Bottom-Up) Approach
int coinChange(vector<int>& coins, int amount) {
    vector<int> dp(amount + 1, amount + 1);
    
    // Base case
    dp[0] = 0;
    
    // Fill dp table
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

**Complexity Analysis**:
- Time Complexity: O(amount * n) where n is the number of coin denominations
- Space Complexity: O(amount)

### Problem 5: Longest Increasing Subsequence
**Difficulty**: Medium

**Problem Statement**:
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

**Real-World Context**:
This problem models scenarios in genetic sequence analysis, where biologists look for patterns of increasing complexity or growth in DNA or protein sequences.

**Recurrence Relation**:
Let `dp[i]` be the length of the longest increasing subsequence ending at index `i`.
```
dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i]
```

**Solutions**:

```cpp
// Tabulated (Bottom-Up) Approach
int lengthOfLIS(vector<int>& nums) {
    int n = nums.size();
    vector<int> dp(n, 1);
    int maxLength = 1;
    
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        maxLength = max(maxLength, dp[i]);
    }
    
    return maxLength;
}

// Optimized Approach (using binary search)
int lengthOfLIS(vector<int>& nums) {
    vector<int> tails;
    
    for (int num : nums) {
        auto it = lower_bound(tails.begin(), tails.end(), num);
        
        if (it == tails.end()) {
            tails.push_back(num);
        } else {
            *it = num;
        }
    }
    
    return tails.size();
}
```

**Complexity Analysis**:
- Time Complexity: O(n²) for the standard solution, O(n log n) for the optimized approach
- Space Complexity: O(n)

## Problem Collection: 2D Array Problems

### Problem 1: Unique Paths
**Difficulty**: Medium

**Problem Statement**:
A robot is located at the top-left corner of a `m x n` grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there?

**Real-World Context**:
This problem models route planning in grid-based environments like city blocks, warehouse layouts, or circuit board routing.

**Recurrence Relation**:
Let `dp[i][j]` be the number of unique paths to reach position `(i, j)`.
```
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

**Solutions**:

```cpp
// Tabulated (Bottom-Up) Approach
int uniquePaths(int m, int n) {
    vector<vector<int>> dp(m, vector<int>(n, 0));
    
    // Base cases: first row and first column
    for (int i = 0; i < m; i++) {
        dp[i][0] = 1;
    }
    
    for (int j = 0; j < n; j++) {
        dp[0][j] = 1;
    }
    
    // Fill dp table
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = dp[i-1][j] + dp[i][j-1];
        }
    }
    
    return dp[m-1][n-1];
}

// Space-Optimized Approach
int uniquePaths(int m, int n) {
    vector<int> dp(n, 1);
    
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[j] += dp[j-1];
        }
    }
    
    return dp[n-1];
}
```

**Complexity Analysis**:
- Time Complexity: O(m * n)
- Space Complexity: O(n) for the optimized solution

### Problem 2: Minimum Path Sum
**Difficulty**: Medium

**Problem Statement**:
Given a `m x n` grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path. You can only move either down or right at any point in time.

**Real-World Context**:
This problem models cost optimization in network routing, logistics planning, or resource allocation across a grid-based system.

**Recurrence Relation**:
Let `dp[i][j]` be the minimum path sum to reach position `(i, j)`.
```
dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
```

**Solutions**:

```cpp
// Tabulated (Bottom-Up) Approach
int minPathSum(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<int>> dp(m, vector<int>(n, 0));
    
    // Base case
    dp[0][0] = grid[0][0];
    
    // Fill first row
    for (int j = 1; j < n; j++) {
        dp[0][j] = dp[0][j-1] + grid[0][j];
    }
    
    // Fill first column
    for (int i = 1; i < m; i++) {
        dp[i][0] = dp[i-1][0] + grid[i][0];
    }
    
    // Fill rest of the dp table
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]);
        }
    }
    
    return dp[m-1][n-1];
}

// Space-Optimized Approach
int minPathSum(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<int> dp(n, INT_MAX);
    
    dp[0] = grid[0][0];
    
    // Fill first row
    for (int j = 1; j < n; j++) {
        dp[j] = dp[j-1] + grid[0][j];
    }
    
    // Fill rest of the dp table
    for (int i = 1; i < m; i++) {
        dp[0] += grid[i][0];
        
        for (int j = 1; j < n; j++) {
            dp[j] = grid[i][j] + min(dp[j], dp[j-1]);
        }
    }
    
    return dp[n-1];
}
```

**Complexity Analysis**:
- Time Complexity: O(m * n)
- Space Complexity: O(n) for the optimized solution

### Problem 3: Longest Common Subsequence
**Difficulty**: Medium

**Problem Statement**:
Given two strings `text1` and `text2`, return the length of their longest common subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

**Real-World Context**:
This problem is fundamental in bioinformatics for comparing DNA sequences, in version control systems for diff operations, and in plagiarism detection algorithms.

**Recurrence Relation**:
Let `dp[i][j]` be the length of the longest common subsequence of text1[0...i-1] and text2[0...j-1].
```
if text1[i-1] == text2[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

**Solutions**:

```cpp
// Tabulated (Bottom-Up) Approach
int longestCommonSubsequence(string text1, string text2) {
    int m = text1.length();
    int n = text2.length();
    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
    
    // Fill dp table
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

// Space-Optimized Approach
int longestCommonSubsequence(string text1, string text2) {
    int m = text1.length();
    int n = text2.length();
    
    // Ensure text2 is the shorter string to minimize space
    if (m < n) {
        swap(text1, text2);
        swap(m, n);
    }
    
    vector<int> prev(n+1, 0);
    vector<int> curr(n+1, 0);
    
    // Fill dp table
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (text1[i-1] == text2[j-1]) {
                curr[j] = prev[j-1] + 1;
            } else {
                curr[j] = max(prev[j], curr[j-1]);
            }
        }
        // Update prev for next iteration
        prev = curr;
    }
    
    return prev[n];
}
```

**Complexity Analysis**:
- Time Complexity: O(m * n)
- Space Complexity: O(min(m, n)) for the optimized solution

### Problem 4: Edit Distance
**Difficulty**: Hard

**Problem Statement**:
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`. You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

**Real-World Context**:
This problem has applications in spell checking, DNA sequence alignment, and natural language processing for determining how similar two strings are.

**Recurrence Relation**:
Let `dp[i][j]` be the minimum number of operations required to convert word1[0...i-1] to word2[0...j-1].
```
if word1[i-1] == word2[j-1]:
    dp[i][j] = dp[i-1][j-1]
else:
    dp[i][j] = 1 + min(dp[i-1][j],    // Delete
                        dp[i][j-1],    // Insert
                        dp[i-1][j-1])  // Replace
```

**Solutions**:

```cpp
// Tabulated (Bottom-Up) Approach
int minDistance(string word1, string word2) {
    int m = word1.length();
    int n = word2.length();
    vector<vector<int>> dp(m+1, vector<int>(n+1));
    
    // Base cases: converting to empty string
    for (int i = 0; i <= m; i++) {
        dp[i][0] = i; // Delete all characters
    }
    
    for (int j = 0; j <= n; j++) {
        dp[0][j] = j; // Insert all characters
    }
    
    // Fill dp table
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (word1[i-1] == word2[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = 1 + min({dp[i-1][j],    // Delete
                                    dp[i][j-1],    // Insert
                                    dp[i-1][j-1]}); // Replace
            }
        }
    }
    
    return dp[m][n];
}

// Space-Optimized Approach
int minDistance(string word1, string word2) {
    int m = word1.length();
    int n = word2.length();
    
    // We only need two rows: current and previous
    vector<int> prev(n+1);
    vector<int> curr(n+1);
    
    // Initialize the first row
    for (int j = 0; j <= n; j++) {
        prev[j] = j;
    }
    
    // Fill the dp table row by row
    for (int i = 1; i <= m; i++) {
        curr[0] = i; // First column
        
        for (int j = 1; j <= n; j++) {
            if (word1[i-1] == word2[j-1]) {
                curr[j] = prev[j-1];
            } else {
                curr[j] = 1 + min({prev[j],      // Delete
                                   curr[j-1],    // Insert
                                   prev[j-1]});  // Replace
            }
        }
        
        // Update prev for next iteration
        prev = curr;
    }
    
    return prev[n];
}
```

**Complexity Analysis**:
- Time Complexity: O(m * n)
- Space Complexity: O(n) for the optimized solution

### Problem 5: Maximal Square
**Difficulty**: Medium

**Problem Statement**:
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

**Real-World Context**:
This problem models scenarios in image processing, computer vision, and pattern recognition where finding the largest homogeneous region is important.

**Recurrence Relation**:
Let `dp[i][j]` be the side length of the largest square whose bottom-right corner is at position `(i, j)`.
```
if matrix[i][j] == '1':
    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
else:
    dp[i][j] = 0
```

**Solutions**:

```cpp
// Tabulated (Bottom-Up) Approach
int maximalSquare(vector<vector<char>>& matrix) {
    if (matrix.empty() || matrix[0].empty()) return 0;
    
    int m = matrix.size();
    int n = matrix[0].size();
    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
    int maxSide = 0;
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (matrix[i-1][j-1] == '1') {
                dp[i][j] = min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]}) + 1;
                maxSide = max(maxSide, dp[i][j]);
            }
        }
    }
    
    return maxSide * maxSide;
}

// Space-Optimized Approach
int maximalSquare(vector<vector<char>>& matrix) {
    if (matrix.empty() || matrix[0].empty()) return 0;
    
    int m = matrix.size();
    int n = matrix[0].size();
    vector<int> dp(n+1, 0);
    int maxSide = 0;
    int prev = 0; // dp[i-1][j-1]
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            int temp = dp[j]; // Store the current dp[j] before updating
            
            if (matrix[i-1][j-1] == '1') {
                dp[j] = min({dp[j], dp[j-1], prev}) + 1;
                maxSide = max(maxSide, dp[j]);
            } else {
                dp[j] = 0;
            }
            
            prev = temp; // Update prev for the next cell
        }
    }
    
    return maxSide * maxSide;
}
```

**Complexity Analysis**:
- Time Complexity: O(m * n)
- Space Complexity: O(n) for the optimized solution

## Implementation Strategy

### Array Initialization and Boundary Conditions

When implementing dynamic programming solutions, proper array initialization and handling of boundary conditions are crucial:

1. **Initialization**:
   - For maximization problems, initialize the dp array with a very small value or 0.
   - For minimization problems, initialize with a very large value (e.g., INT_MAX).
   - For boolean problems, initialize with false.
   - For counting problems, initialize with 0.

2. **Boundary Conditions**:
   - Include base cases as the first step in your implementation.
   - For 1D arrays, typically dp[0] or dp[1] is initialized explicitly.
   - For 2D arrays, typically the first row and column are initialized explicitly.
   - Handle out-of-bounds checks, especially in recursive implementations.

3. **Buffer Rows/Columns**:
   - Often, it's helpful to add an extra row/column to simplify boundary checking.
   - For example, dp[0][j] might represent an empty first string in string problems.

### Space Optimization Techniques

Many dynamic programming problems can be optimized for space:

1. **Rolling Arrays**:
   - Instead of storing the entire dp table, keep only the last k rows necessary for computation.
   - For 1D problems, often only the last 2-3 values are needed.
   - For 2D problems, often only the current and previous rows are needed.

2. **In-Place Computation**:
   - For some problems, you can update the dp array in place, reducing space complexity.
   - Be careful about the order of updates to avoid overwriting values before they're used.

3. **State Compression**:
   - Use bits to represent states, especially for DP problems with boolean states.
   - This can significantly reduce space requirements for problems with many states.

### Handling Edge Cases

Common edge cases in dynamic programming problems include:

1. **Empty Inputs**:
   - Always consider what happens when the input is empty (e.g., empty array, empty string).

2. **Single Element**:
   - Test your algorithm with inputs containing just one element.

3. **Duplicate Elements**:
   - Ensure your algorithm handles duplicate elements correctly if they can occur.

4. **Negative Values**:
   - For problems involving sums or products, check if negative values affect your solution.

5. **Overflow/Underflow**:
   - Watch for integer overflow/underflow in problems with large inputs or multiplication.

## Testing and Debugging Strategies

### Verifying Correctness

1. **Test with Known Examples**:
   - Start with simple test cases where you can verify the answer manually.
   - Use the examples provided in the problem statement.

2. **Edge Cases Testing**:
   - Empty input
   - Single element
   - All identical elements
   - Increasing/decreasing sequences
   - Maximum/minimum possible values

3. **Trace through the Algorithm**:
   - For small inputs, trace through each step of your algorithm manually.
   - Verify intermediate states against your expected values.

### Common Bugs and Fixes

1. **Initialization Errors**:
   - Forgetting to initialize the dp array properly
   - Not handling base cases correctly

2. **Off-by-One Errors**:
   - Incorrect boundary conditions
   - Accessing dp[i-1] when i could be 0

3. **Recurrence Relation Mistakes**:
   - Incorrectly defining the state transition
   - Using max instead of min or vice versa

4. **Overlapping Subproblem Issues**:
   - Not properly memoizing results in top-down approach
   - Incorrect ordering of computation in bottom-up approach

5. **Range Errors**:
   - Array index out of bounds
   - Not checking constraints before accessing elements

## Practical Tips and Tricks

### State Design Principles

1. **Minimality**:
   - Your state should contain the minimum information needed to solve the subproblem.
   - Extra state variables increase time and space complexity exponentially.

2. **Completeness**:
   - Your state must fully represent the subproblem without ambiguity.
   - Missing information leads to incorrect results.

3. **Non-redundancy**:
   - Avoid redundant state variables that can be derived from others.
   - Each variable should represent a unique aspect of the subproblem.

4. **Accessibility**:
   - States should be easily accessible within your recurrence relation.
   - Use indices or values that can be directly computed.

### Common DP Patterns

1. **Prefix/Suffix Pattern**:
   - dp[i] represents optimal solution for the first/last i elements.
   - Example: Maximum subarray sum, longest increasing subsequence.

2. **Left-Right Pattern**:
   - dp[i][j] represents optimal solution for the range i to j.
   - Example: Matrix chain multiplication, palindrome problems.

3. **Decision Pattern**:
   - dp[i] represents optimal solution when making a specific decision at step i.
   - Example: House robber, take or skip.

4. **Matching Pattern**:
   - dp[i][j] represents optimal solution when matching first i characters with first j characters.
   - Example: Edit distance, longest common subsequence.

5. **Knapsack Pattern**:
   - dp[i][j] represents optimal solution using first i items with j capacity/resources.
   - Example: 0-1 knapsack, coin change.

6. **Grid Pattern**:
   - dp[i][j] represents optimal solution when reaching cell (i,j).
   - Example: Unique paths, minimum path sum.

## Progression Path

Here's a recommended progression path for mastering dynamic programming:

### Beginner Level
1. Maximum Subarray Sum
2. Climb Stairs
3. House Robber
4. Unique Paths

### Intermediate Level
1. Longest Increasing Subsequence
2. Coin Change
3. Edit Distance
4. Minimum Path Sum

### Advanced Level
1. Longest Common Subsequence
2. Maximal Square
3. Regular Expression Matching
4. Burst Balloons

## Decision Flowcharts

### Identifying if DP is Applicable

```
Is there optimal substructure?
|
|-- No --> DP may not be appropriate
|
|-- Yes --> Are there overlapping subproblems?
             |
             |-- No --> Use a different algorithm
             |
             |-- Yes --> DP is likely appropriate
                         |
                         |-- Is the problem about optimization? --> Maximize/minimize
                         |
                         |-- Is the problem about counting? --> Count distinct ways
                         |
                         |-- Is the problem about feasibility? --> Yes/no decision
```

### Choosing Between 1D and 2D DP

```
What is the problem type?
|
|-- Linear sequence or single parameter --> 1D DP
|   (e.g., array problems, single constraint)
|
|-- Two sequences or two parameters --> 2D DP
|   (e.g., string comparison, grid problems)
|
|-- More parameters --> Higher dimensional DP
    (e.g., multiple constraints, multiple objects)
```

### Selecting the DP Approach

```
What's the nature of the problem?
|
|-- Simple problem with limited states --> Tabulation (Bottom-up)
|   - More efficient in time and space
|   - Easier to optimize space
|
|-- Complex problem with many states --> Memoization (Top-down)
|   - Easier to implement
|   - Only computes needed states
|   - Better for sparse state spaces
```

## Conclusion

Dynamic programming is a powerful technique for solving complex optimization problems by breaking them down into simpler subproblems. The key to mastering dynamic programming lies in:

1. **Understanding the Problem Structure**:
   - Identify optimal substructure and overlapping subproblems.
   - Define appropriate states to represent subproblems.

2. **Designing Efficient Algorithms**:
   - Formulate recurrence relations that correctly transition between states.
   - Choose between top-down and bottom-up approaches based on problem characteristics.

3. **Implementing Optimally**:
   - Initialize base cases correctly.
   - Handle edge cases and boundary conditions.
   - Optimize space usage when possible.

4. **Practice and Pattern Recognition**:
   - Familiarize yourself with common DP patterns.
   - Apply these patterns to solve new problems.

By working through the problems in this guide, from simple 1D array problems to complex 2D matrix challenges, you'll develop a solid foundation in dynamic programming and be able to tackle a wide range of algorithmic problems effectively.

Remember that proficiency in dynamic programming comes with practice. Start with simpler problems, understand the core principles, and gradually move to more complex challenges. With each problem you solve, your intuition for when and how to apply dynamic programming will improve.

Good luck on your journey to mastering dynamic programming!## Implementation Strategy

### Array Initialization and Boundary Conditions

When implementing dynamic programming solutions, proper array initialization and handling of boundary conditions are crucial:

1. **Initialization**:
   - For maximization problems, initialize the dp array with a very small value or 0.
   - For minimization problems, initialize with a very large value (e.g., INT_MAX).
   - For boolean problems, initialize with false.
   - For counting problems, initialize with 0.

2. **Boundary Conditions**:
   - Include base cases as the first step in your implementation.
   - For 1D arrays, typically dp[0] or dp[1] is initialized explicitly.
   - For 2D arrays, typically the first row and column are initialized explicitly.
   - Handle out-of-bounds checks, especially in recursive implementations.

3. **Buffer Rows/Columns**:
   - Often, it's helpful to add an extra row/column to simplify boundary checking.
   - For example, dp[0][j] might represent an empty first string in string problems.

### Space Optimization Techniques

Many dynamic programming problems can be optimized for space:

1. **Rolling Arrays**:
   - Instead of storing the entire dp table, keep only the last k rows necessary for computation.
   - For 1D problems, often only the last 2-3 values are needed.
   - For 2D problems, often only the current and previous rows are needed.

2. **In-Place Computation**:
   - For some problems, you can update the dp array in place, reducing space complexity.
   - Be careful about the order of updates to avoid overwriting values before they're used.

3. **State Compression**:
   - Use bits to represent states, especially for DP problems with boolean states.
   - This can significantly reduce space requirements for problems with many states.

### Handling Edge Cases

Common edge cases in dynamic programming problems include:

1. **Empty Inputs**:
   - Always consider what happens when the input is empty (e.g., empty array, empty string).

2. **Single Element**:
   - Test your algorithm with inputs containing just one element.

3. **Duplicate Elements**:
   - Ensure your algorithm handles duplicate elements correctly if they can occur.

4. **Negative Values**:
   - For problems involving sums or products, check if negative values affect your solution.

5. **Overflow/Underflow**:
   - Watch for integer overflow/underflow in problems with large inputs or multiplication.

### Transition Techniques Between 1D and 2D

Sometimes, you can transform a problem between 1D and 2D representations:

1. **Reducing Dimensions**:
   - Some 2D problems can be reduced to 1D by considering one dimension at a time.
   - Common in space optimization where you only need the previous row.

2. **Expanding Dimensions**:
   - Adding an extra dimension can sometimes simplify a complex 1D problem.
   - Useful when states depend on multiple parameters.

3. **State Transformation**:
   - Convert between different state representations to match the problem structure.
   - For example, representing a 2D grid as a 1D array with position = row * cols + col.

## Testing and Debugging Strategies

### Verifying Correctness

1. **Test with Known Examples**:
   - Start with simple test cases where you can verify the answer manually.
   - Use the examples provided in the problem statement.

2. **Edge Cases Testing**:
   - Empty input
   - Single element
   - All identical elements
   - Increasing/decreasing sequences
   - Maximum/minimum possible values

3. **Trace through the Algorithm**:
   - For small inputs, trace through each step of your algorithm manually.
   - Verify intermediate states against your expected values.

### Common Bugs and Fixes

1. **Initialization Errors**:
   - Forgetting to initialize the dp array properly
   - Not handling base cases correctly

2. **Off-by-One Errors**:
   - Incorrect boundary conditions
   - Accessing dp[i-1] when i could be 0

3. **Recurrence Relation Mistakes**:
   - Incorrectly defining the state transition
   - Using max instead of min or vice versa

4. **Overlapping Subproblem Issues**:
   - Not properly memoizing results in top-down approach
   - Incorrect ordering of computation in bottom-up approach

5. **Range Errors**:
   - Array index out of bounds
   - Not checking constraints before accessing elements

### Optimizing Your Solution

1. **Identify Redundant Computations**:
   - Look for calculations that are repeated and can be stored.

2. **Optimize State Space**:
   - Reduce the number of states if possible.
   - Use more compact representations.

3. **Optimize Transitions**:
   - Minimize the number of state transitions checked.
   - Use data structures like priority queues for efficient transitions.

4. **Precomputation**:
   - Precompute values that are used frequently.
   - Use techniques like prefix sums for range queries.

## Practical Tips and Tricks

### State Design Principles

1. **Minimality**:
   - Your state should contain the minimum information needed to solve the subproblem.
   - Extra state variables increase time and space complexity exponentially.

2. **Completeness**:
   - Your state must fully represent the subproblem without ambiguity.
   - Missing information leads to incorrect results.

3. **Non-redundancy**:
   - Avoid redundant state variables that can be derived from others.
   - Each variable should represent a unique aspect of the subproblem.

4. **Accessibility**:
   - States should be easily accessible within your recurrence relation.
   - Use indices or values that can be directly computed.

### Common DP Patterns

1. **Prefix/Suffix Pattern**:
   - dp[i] represents optimal solution for the first/last i elements.
   - Example: Maximum subarray sum, longest increasing subsequence.

2. **Left-Right Pattern**:
   - dp[i][j] represents optimal solution for the range i to j.
   - Example: Burst balloons, palindrome problems.

3. **Decision Pattern**:
   - dp[i] represents optimal solution when making a specific decision at step i.
   - Example: House robber, take or skip.

4. **Matching Pattern**:
   - dp[i][j] represents optimal solution when matching first i characters with first j characters.
   - Example: Edit distance, longest common subsequence.

5. **Knapsack Pattern**:
   - dp[i][j] represents optimal solution using first i items with j capacity/resources.
   - Example: 0-1 knapsack, coin change.

6. **Grid Pattern**:
   - dp[i][j] represents optimal solution when reaching cell (i,j).
   - Example: Unique paths, minimum path sum.

## Progression Path

Here's a recommended progression path for mastering dynamic programming:

### Beginner Level
1. Maximum Subarray Sum
2. Climb Stairs
3. House Robber
4. Unique Paths

### Intermediate Level
1. Longest Increasing Subsequence
2. 0-1 Knapsack
3. Edit Distance
4. Minimum Path Sum

### Advanced Level
1. Longest Common Subsequence
2. Maximal Square
3. Regular Expression Matching
4. Burst Balloons

## Decision Flowcharts

### Identifying if DP is Applicable

```
Is there optimal substructure?
|
|-- No --> DP may not be appropriate
|
|-- Yes --> Are there overlapping subproblems?
             |
             |-- No --> Use a different algorithm
             |
             |-- Yes --> DP is likely appropriate
                         |
                         |-- Is the problem about optimization? --> Maximize/minimize
                         |
                         |-- Is the problem about counting? --> Count distinct ways
                         |
                         |-- Is the problem about feasibility? --> Yes/no decision
```

### Choosing Between 1D and 2D DP

```
What is the problem type?
|
|-- Linear sequence or single parameter --> 1D DP
|   (e.g., array problems, single constraint)
|
|-- Two sequences or two parameters --> 2D DP
|   (e.g., string comparison, grid problems)
|
|-- More parameters --> Higher dimensional DP
    (e.g., multiple constraints, multiple objects)
```

### Selecting the DP Approach

```
What's the nature of the problem?
|
|-- Simple problem with limited states --> Tabulation (Bottom-up)
|   - More efficient in time and space
|   - Easier to optimize space
|
|-- Complex problem with many states --> Memoization (Top-down)
|   - Easier to implement
|   - Only computes needed states
|   - Better for sparse state spaces
```

## Conclusion

Dynamic programming is a powerful technique for solving complex optimization problems by breaking them down into simpler subproblems. The key to mastering dynamic programming lies in:

1. **Understanding the Problem Structure**:
   - Identify optimal substructure and overlapping subproblems.
   - Define appropriate states to represent subproblems.

2. **Designing Efficient Algorithms**:
   - Formulate recurrence relations that correctly transition between states.
   - Choose between top-down and bottom-up approaches based on problem characteristics.

3. **Implementing Optimally**:
   - Initialize base cases correctly.
   - Handle edge cases and boundary conditions.
   - Optimize space usage when possible.

4. **Practice and Pattern Recognition**:
   - Familiarize yourself with common DP patterns.
   - Apply these patterns to solve new problems.

By working through the problems in this guide, from simple 1D array problems to complex 2D matrix challenges, you'll develop a solid foundation in dynamic programming and be able to tackle a wide range of algorithmic problems effectively.

Remember that proficiency in dynamic programming comes with practice. Start with simpler problems, understand the core principles, and gradually move to more complex challenges. With each problem you solve, your intuition for when and how to apply dynamic programming will improve.

Good luck on your journey to mastering dynamic programming!#### Problem 6: Burst Balloons
**Difficulty**: Hard

**Problem Statement**:
You are given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by an array `nums`. You are asked to burst all the balloons. If you burst the ith balloon, you will get nums[i-1] * nums[i] * nums[i+1] coins. After the ith balloon is burst, nums[i-1] and nums[i+1] become adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: If i-1 or i+1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

**Real-World Context**:
This problem models optimization scenarios where the order of operations affects the overall outcome, such as in resource scheduling or task prioritization.

**Test Cases**:
```
Input: [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +  3*5*8   +  1*3*8  + 1*8*1 = 15 + 120 + 24 + 8 = 167

Input: [1,5]
Output: 10
Explanation: burst 5 first to get 1*5*1 = 5 coins, then burst 1 to get 1*1*1 = 1 coins, total is 6. But if burst 1 first, we get 1*1*5 = 5 coins, then burst 5 to get 1*5*1 = 5 coins, total is 10.
```

**Visualization**:
```
For nums = [3,1,5,8]:

DP table (dp[i][j] = max coins from bursting balloons i to j):
    | 0 | 1 | 2 | 3 |
----|---|---|---|---|
  0 | 15| 35| 159| 167|
----|---|---|---|---|
  1 | - | 5 | 45 | 48 |
----|---|---|---|---|
  2 | - | - | 40 | 48 |
----|---|---|---|---|
  3 | - | - | - | 8 |
```

**Recurrence Relation**:
Let `dp[i][j]` be the maximum coins we can get by bursting all balloons from index i to j.
```
dp[i][j] = max(dp[i][k-1] + dp[k+1][j] + nums[i-1] * nums[k] * nums[j+1]) for all k in range(i, j+1)
```

**Solution**:

Recursive (Top-Down) Approach:
```cpp
int maxCoinsRecursive(vector<int>& nums, int i, int j, vector<vector<int>>& memo) {
    // Base case: no balloons to burst
    if (i > j) return 0;
    
    // Return memoized result if available
    if (memo[i][j] != -1) return memo[i][j];
    
    int maxCoins = 0;
    
    // Try to burst each balloon last
    for (int k = i; k <= j; k++) {
        // Left value: 1 if out of bounds, otherwise the value
        int left = (i-1 < 0) ? 1 : nums[i-1];
        // Right value: 1 if out of bounds, otherwise the value
        int right = (j+1 >= nums.size()) ? 1 : nums[j+1];
        
        // Coins from bursting balloons to the left and right
        int leftCoins = maxCoinsRecursive(nums, i, k-1, memo);
        int rightCoins = maxCoinsRecursive(nums, k+1, j, memo);
        
        // Total coins for this choice
        int totalCoins = leftCoins + nums[k] * left * right + rightCoins;
        
        maxCoins = max(maxCoins, totalCoins);
    }
    
    memo[i][j] = maxCoins;
    return maxCoins;
}

int maxCoins(vector<int>& nums) {
    int n = nums.size();
    vector<vector<int>> memo(n, vector<int>(n, -1));
    return maxCoinsRecursive(nums, 0, n-1, memo);
}
```

Memoized (Top-Down) Approach:
```cpp
int maxCoins(vector<int>& nums) {
    int n = nums.size();
    vector<vector<int>> memo(n, vector<int>(n, -1));
    
    function<int(int, int)> dp = [&](int i, int j) {
        // Base case: no balloons to burst
        if (i > j) return 0;
        
        // Return memoized result if available
        if (memo[i][j] != -1) return memo[i][j];
        
        int maxCoins = 0;
        
        // Try to burst each balloon last
        for (int k = i; k <= j; k++) {
            // Values for calculations
            int left = (i-1 < 0) ? 1 : nums[i-1];
            int right = (j+1 >= n) ? 1 : nums[j+1];
            
            // Coins from bursting balloons to the left and right
            int leftCoins = dp(i, k-1);
            int rightCoins = dp(k+1, j);
            
            // Total coins for this choice
            int totalCoins = leftCoins + nums[k] * left * right + rightCoins;
            
            maxCoins = max(maxCoins, totalCoins);
        }
        
        memo[i][j] = maxCoins;
        return maxCoins;
    };
    
    return dp(0, n-1);
}
```

Tabulated (Bottom-Up) Approach:
```cpp
int maxCoins(vector<int>& nums) {
    int n = nums.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    
    // Consider subarrays of length len
    for (int len = 1; len <= n; len++) {
        // Consider all subarrays of length len
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            
            // Try to burst each balloon last
            for (int k = i; k <= j; k++) {
                // Values for calculations
                int left = (i-1 < 0) ? 1 : nums[i-1];
                int right = (j+1 >= n) ? 1 : nums[j+1];
                
                // Coins from bursting balloons to the left and right
                int leftCoins = (k-1 < i) ? 0 : dp[i][k-1];
                int rightCoins = (k+1 > j) ? 0 : dp[k+1][j];
                
                // Total coins for this choice
                int totalCoins = leftCoins + nums[k] * left * right + rightCoins;
                
                dp[i][j] = max(dp[i][j], totalCoins);
            }
        }
    }
    
    return dp[0][n-1];
}
```

**Complexity Analysis**:
- Time Complexity: O(n³) where n is the number of balloons.
- Space Complexity:
  - Recursive/Memoized: O(n²) for the memoization table.
  - Tabulated: O(n²) for the dp table.

**Edge Cases**:
- Empty array: Return 0.
- Single balloon: Return nums[0] (or nums[0] * 1 * 1).
- All balloons with value 0: Return 0.

**Optimization Techniques**:
- For very large arrays, we could consider a greedy approach as a heuristic, although it doesn't guarantee the optimal solution.
- We can add boundary balloons with value 1 to simplify the code and avoid boundary checks.

**DP Table Visualization**:
```
For nums = [3,1,5,8]:

DP table:
    | 0 | 1 | 2 | 3 |
----|---|---|---|---|
  0 | 3 | 30| 159| 167|
----|---|---|---|---|
  1 | - | 1 | 45 | 48 |
----|---|---|---|---|
  2 | - | - | 5 | 40 |
----|---|---|---|---|
  3 | - | - | - | 8 |

Explanation:
- dp[0][0] = 1*3*1 = 3: Maximum coins from bursting only nums[0] = 3
- dp[1][1] = 3*1*5 = 15: Maximum coins from bursting only nums[1] = 1
- dp[0][1] = max(dp[0][0] + 3*1*5, dp[1][1] + 1*3*1) = max(3 + 15, 15 + 3) = 30
    Two ways: burst 3 then 1, or burst 1 then 3
- For dp[0][3] = 167, the optimal order is to burst them in this order:
    1. Burst balloon 1 (index 1): 3*1*5 = 15
    2. Burst balloon 0 (index 0): 1*3*5 = 15
    3. Burst balloon 2 (index 2): 1*5*8 = 40
    4. Burst balloon 3 (index 3): 1*8*1 = 8
    Total: 15 + 15 + 40 + 8 = 167
```

#### Problem 7: Dungeon Game
**Difficulty**: Hard

**Problem Statement**:
The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through to rescue the princess.

The knight has an initial health point. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative values), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive values).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health points so that he can rescue the princess.

**Real-World Context**:
This problem models path finding with resource constraints, similar to robot navigation with limited battery or autonomous vehicle route planning with fuel constraints.

**Test Cases**:
```
Input:
[
  [-2,-3,3],
  [-5,-10,1],
  [10,30,-5]
]
Output: 7
Explanation: The initial health should be at least 7 so that he can survive the path [-2, -3, 3, 1, -5] with final health 1.

Input:
[
  [0]
]
Output: 1
Explanation: The knight is already in the dungeon with the princess. Since starting health cannot be less than 1, return 1.
```

**Visualization**:
```
For the dungeon:
-2 -3  3
-5 -10 1
10  30 -5

DP table (minimum health needed to survive from position (i,j) to the princess):
 7  5  2
 6 11  5
 1  1  6
```

**Recurrence Relation**:
Let `dp[i][j]` be the minimum health needed to survive from position `(i, j)` to the princess.
```
dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
```

**Solution**:

Recursive (Top-Down) Approach:
```cpp
int calculateMinimumHPRecursive(vector<vector<int>>& dungeon, int i, int j, vector<vector<int>>& memo) {
    int m = dungeon.size();
    int n = dungeon[0].size();
    
    // Base case: out of bounds
    if (i >= m || j >= n) return INT_MAX;
    
    // Base case: reached the princess
    if (i == m-1 && j == n-1) {
        return max(1, 1 - dungeon[i][j]);
    }
    
    // Return memoized result if available
    if (memo[i][j] != -1) return memo[i][j];
    
    // Recurrence relation
    int rightHealth = calculateMinimumHPRecursive(dungeon, i, j+1, memo);
    int downHealth = calculateMinimumHPRecursive(dungeon, i+1, j, memo);
    
    int minHealthNeeded = max(1, min(rightHealth, downHealth) - dungeon[i][j]);
    
    memo[i][j] = minHealthNeeded;
    return minHealthNeeded;
}

int calculateMinimumHP(vector<vector<int>>& dungeon) {
    int m = dungeon.size();
    int n = dungeon[0].size();
    vector<vector<int>> memo(m, vector<int>(n, -1));
    return calculateMinimumHPRecursive(dungeon, 0, 0, memo);
}
```

Memoized (Top-Down) Approach:
```cpp
int calculateMinimumHP(vector<vector<int>>& dungeon) {
    int m = dungeon.size();
    int n = dungeon[0].size();
    vector<vector<int>> memo(m, vector<int>(n, -1));
    
    function<int(int, int)> dp = [&](int i, int j) {
        // Base case: out of bounds
        if (i >= m || j >= n) return INT_MAX;
        
        // Base case: reached the princess
        if (i == m-1 && j == n-1) {
            return max(1, 1 - dungeon[i][j]);
        }
        
        // Return memoized result if available
        if (memo[i][j] != -1) return memo[i][j];
        
        // Recurrence relation
        int rightHealth = dp(i, j+1);
        int downHealth = dp(i+1, j);
        
        int minHealthNeeded = max(1, min(rightHealth, downHealth) - dungeon[i][j]);
        
        memo[i][j] = minHealthNeeded;
        return minHealthNeeded;
    };
    
    return dp(0, 0);
}
```

Tabulated (Bottom-Up) Approach:
```cpp
int calculateMinimumHP(vector<vector<int>>& dungeon) {
    int m = dungeon.size();
    int n = dungeon[0].size();
    vector<vector<int>> dp(m+1, vector<int>(n+1, INT_MAX));
    
    // Base case: health needed at princess cell
    dp[m][n-1] = dp[m-1][n] = 1;
    
    // Fill dp table from bottom-right to top-left
    for (int i = m-1; i >= 0; i--) {
        for (int j = n-1; j >= 0; j--) {
            int minHealthNeeded = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j];
            dp[i][j] = max(1, minHealthNeeded);
        }
    }
    
    return dp[0][0];
}
```

Space-Optimized Approach:
```cpp
int calculateMinimumHP(vector<vector<int>>& dungeon) {
    int m = dungeon.size();
    int n = dungeon[0].size();
    vector<int> dp(n+1, INT_MAX);
    
    // Base case: health needed at princess cell
    dp[n-1] = 1;
    
    // Fill dp table from bottom-right to top-left
    for (int i = m-1; i >= 0; i--) {
        for (int j = n-1; j >= 0; j--) {
            int minHealthNeeded = min(dp[j], dp[j+1]) - dungeon[i][j];
            dp[j] = max(1, minHealthNeeded);
        }
    }
    
    return dp[0];
}
```

**Complexity Analysis**:
- Time Complexity: O(m * n) where m and n are the dimensions of the dungeon.
- Space Complexity:
  - Recursive/Memoized: O(m * n) for the memoization table.
  - Tabulated: O(m * n) for the dp table.
  - Space-Optimized: O(n) as we only need one row of the dp table.

**Edge Cases**:
- Single cell dungeon: Return max(1, 1 - dungeon[0][0]).
- All positive values: Return 1 (but still need to compute the dp table).
- All negative values: Need to have enough initial health to survive.

**Optimization Techniques**:
- We can optimize space by only keeping track of one row of the dp table.
- Working backwards from the princess cell to the starting cell simplifies the computation.

**DP Table Visualization**:
```
For the dungeon:
-2 -3  3
-5 -10 1
10  30 -5

DP table (minimum health needed to survive from position (i,j) to the princess):
 7  5  2
 6 11  5
 1  1  6

Explanation:
- dp[2][2] = max(1, 1 - (-5)) = max(1, 6) = 6: Minimum health needed at the princess cell
- dp[2][1] = max(1, dp[2][2] - 30) = max(1, 6 - 30) = max(1, -24) = 1
- dp[2][0] = max(1, dp[2][1] - 10) = max(1, 1 - 10) = max(1, -9) = 1
- dp[1][2] = max(1, dp[2][2] - 1) = max(1, 6 - 1) = max(1, 5) = 5
- dp[1][1] = max(1, min(dp[1][2], dp[2][1]) - (-10)) = max(1, min(5, 1) - (-10)) = max(1, 1 + 10) = 11
- dp[0][0] = max(1, min(dp[0][1], dp[1][0]) - (-2)) = max(1, min(5, 6) - (-2)) = max(1, 5 + 2) = 7
```

#### Problem 8: Interleaving String
**Difficulty**: Medium

**Problem Statement**:
Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an interleaving of `s1` and `s2`.

An interleaving of two strings `s` and `t` is a configuration where `s` and `t` are divided into substrings such that:
- `s = s1 + s2 + ... + sn`
- `t = t1 + t2 + ... + tm`
- `|n - m| <= 1`
- The interleaving is `s1 + t1 + s2 + t2 + ... ` or `t1 + s1 + t2 + s2 + ...`

Note: `a + b` is the concatenation of strings `a` and `b`.

**Real-World Context**:
This problem models scenarios in text processing and compiler design, where we need to verify if a given string follows a pattern formed by interleaving multiple source strings.

**Test Cases**:
```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: s3 is formed by interleaving s1 and s2.

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: s3 cannot be formed by interleaving s1 and s2.

Input: s1 = "", s2 = "", s3 = ""
Output: true
Explanation: Both s1 and s2 are empty, so s3 must also be empty.
```

**Visualization**:
```
For s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac":

DP table (dp[i][j] = can s3[0...i+j-1] be formed by interleaving s1[0...i-1] and s2[0...j-1]?):
     |   | d | b | b | c | a |
-----|---|---|---|---|---|---|
     | T | F | F | F | F | F |
-----|---|---|---|---|---|---|
  a  | T | F | F | F | F | F |
-----|---|---|---|---|---|---|
  a  | T | T | T | T | T | F |
-----|---|---|---|---|---|---|
  b  | F | T | T | F | F | F |
-----|---|---|---|---|---|---|
  c  | F | F | F | T | T | F |
-----|---|---|---|---|---|---|
  c  | F | F | F | F | T | T |
```

**Recurrence Relation**:
Let `dp[i][j]` indicate whether s3[0...i+j-1] can be formed by interleaving s1[0...i-1] and s2[0...j-1].
```
dp[i][j] = (dp[i-1][j] && s1[i-1] == s3[i+j-1]) || (dp[i][j-1] && s2[j-1] == s3[i+j-1])
```

**Solution**:

Recursive (Top-Down) Approach:
```cpp
bool isInterleavingRecursive(string& s1, string& s2, string& s3, int i, int j, vector<vector<int>>& memo) {
    // Base case: reached the end of both strings
    if (i == s1.length() && j == s2.length()) return true;
    
    // Return memoized result if available
    if (memo[i][j] != -1) return memo[i][j];
    
    // Check if current character of s3 matches s1 and recursively check the rest
    if (i < s1.length() && s1[i] == s3[i+j] && isInterleavingRecursive(s1, s2, s3, i+1, j, memo)) {
        memo[i][j] = 1;
        return true;
    }
    
    // Check if current character of s3 matches s2 and recursively check the rest
    if (j < s2.length() && s2[j] == s3[i+j] && isInterleavingRecursive(s1, s2, s3, i, j+1, memo)) {
        memo[i][j] = 1;
        return true;
    }
    
    // Neither matched
    memo[i][j] = 0;
    return false;
}

bool isInterleave(string s1, string s2, string s3) {
    // Quick check for lengths
    if (s1.length() + s2.length() != s3.length()) return false;
    
    vector<vector<int>> memo(s1.length() + 1, vector<int>(s2.length() + 1, -1));
    return isInterleavingRecursive(s1, s2, s3, 0, 0, memo);
}
```

Memoized (Top-Down) Approach:
```cpp
bool isInterleave(string s1, string s2, string s3) {
    // Quick check for lengths
    if (s1.length() + s2.length() != s3.length()) return false;
    
    int m = s1.length();
    int n = s2.length();
    vector<vector<int>> memo(m + 1, vector<int>(n + 1, -1));
    
    function<bool(int, int)> dp = [&](int i, int j) {
        // Base case: reached the end of both strings
        if (i == m && j == n) return true;
        
        // Return memoized result if available
        if (memo[i][j] != -1) return memo[i][j] == 1;
        
        // Check if current character of s3 matches s1 and recursively check the rest
        if (i < m && s1[i] == s3[i+j] && dp(i+1, j)) {
            memo[i][j] = 1;
            return true;
        }
        
        // Check if current character of s3 matches s2 and recursively check the rest
        if (j < n && s2[j] == s3[i+j] && dp(i, j+1)) {
            memo[i][j] = 1;
            return true;
        }
        
        // Neither matched
        memo[i][j] = 0;
        return false;
    };
    
    return dp(0, 0);
}
```

Tabulated (Bottom-Up) Approach:
```cpp
bool isInterleave(string s1, string s2, string s3) {
    // Quick check for lengths
    if (s1.length() + s2.length() != s3.length()) return false;
    
    int m = s1.length();
    int n = s2.length();
    vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
    
    // Base case: empty strings are interleaving
    dp[0][0] = true;
    
    // Fill first row (s1 is empty)
    for (int j = 1; j <= n; j++) {
        dp[0][j] = dp[0][j-1] && s2[j-1] == s3[j-1];
    }
    
    // Fill first column (s2 is empty)
    for (int i = 1; i <= m; i++) {
        dp[i][0] = dp[i-1][0] && s1[i-1] == s3[i-1];
    }
    
    // Fill rest of the dp table
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            dp[i][j] = (dp[i-1][j] && s1[i-1] == s3[i+j-1]) || 
                        (dp[i][j-1] && s2[j-1] == s3[i+j-1]);
        }
    }
    
    return dp[m][n];
}
```

Space-Optimized Approach:
```cpp
bool isInterleave(string s1, string s2, string s3) {
    // Quick check for lengths
    if (s1.length() + s2.length() != s3.length()) return false;
    
    int m = s1.length();
    int n = s2.length();
    
    // Use a single row of dp table
    vector<bool> dp(n + 1, false);
    
    // Base case: empty strings are interleaving
    dp[0] = true;
    
    // Fill first row (s1 is empty)
    for (int j = 1; j <= n; j++) {
        dp[j] = dp[j-1] && s2[j-1] == s3[j-1];
    }
    
    // Fill rest of the dp table row by row
    for (int i = 1; i <= m; i++) {
        dp[0] = dp[0] && s1[i-1] == s3[i-1];
        
        for (int j = 1; j <= n; j++) {
            dp[j] = (dp[j] && s1[i-1] == s3[i+j-1]) || 
                    (dp[j-1] && s2[j-1] == s3[i+j-1]);
        }
    }
    
    return dp[n];
}
```

**Complexity Analysis**:
- Time Complexity: O(m * n) where m and n are the lengths of s1 and s2.
- Space Complexity:
  - Recursive/Memoized: O(m * n) for the memoization table.
  - Tabulated: O(m * n) for the dp table.
  - Space-Optimized: O(n) as we only need one row of the dp table.

**Edge Cases**:
- Empty strings: Return true if all three strings are empty.
- Lengths don't match: Return false immediately.
- One string is empty: Check if the other string equals s3.

**Optimization Techniques**:
- Quick check for lengths before doing any computation.
- We can optimize space by only keeping track of one row of the dp table.

**DP Table Visualization**:
```
For s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac":

DP table:
     |   | d | b | b | c | a |
-----|---|---|---|---|---|---|
     | T | F | F | F | F | F |
-----|---|---|---|---|---|---|
  a  | T | F | F | F | F | F |
-----|---|---|---|---|---|---|
  a  | F | T | F | F | F | F |
-----|---|---|---|---|---|---|
  b  | F | T | T | T | F | F |
-----|---|---|---|---|---|---|
  c  | F | F | F | T | T | F |
-----|---|---|---|---|---|---|
  c  | F | F | F | F | T | T |

Explanation:
- dp[0][0] = true: Empty strings can be interleaved to get an empty string
- dp[1][0] = true && s1[0] == s3[0]: Can form "a" using just s1
- dp[2][0] = true && s1[1] == s3[1]: Can form "aa" using just s1
- dp[2][1] = dp[2][0] && s2[0] == s3[2] = true && 'd' == 'd' = true: Can form "aad" by interleaving "aa" and "d"
- dp[3][3] = dp[2][3] && s1[2] == s3[5] || dp[3][2] && s2[2] == s3[5] = false || true && 'b' == 'b' = true: Can form "aadbb"
- dp[5][5] = true: We can form the complete s3 by interleaving s1 and s2
```

## Implementation Strategy#### Problem 3: Longest Common Subsequence
**Difficulty**: Medium

**Problem Statement**:
Given two strings `text1` and `text2`, return the length of their longest common subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

**Real-World Context**:
This problem is fundamental in bioinformatics for comparing DNA sequences, in version control systems for diff operations, and in plagiarism detection algorithms.

**Test Cases**:
```
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no common subsequence.
```

**Visualization**:
```
For text1 = "abcde", text2 = "ace":

DP table:
     |   | a | c | e
-----|---|---|---|---
     | 0 | 0 | 0 | 0
-----|---|---|---|---
  a  | 0 | 1 | 1 | 1
-----|---|---|---|---
  b  | 0 | 1 | 1 | 1
-----|---|---|---|---
  c  | 0 | 1 | 2 | 2
-----|---|---|---|---
  d  | 0 | 1 | 2 | 2
-----|---|---|---|---
  e  | 0 | 1 | 2 | 3
```

**Recurrence Relation**:
Let `dp[i][j]` be the length of the longest common subsequence of text1[0...i-1] and text2[0...j-1].
```
if text1[i-1] == text2[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

**Solution**:

Recursive (Top-Down) Approach:
```cpp
int longestCommonSubsequenceRecursive(string& text1, string& text2, int i, int j, vector<vector<int>>& memo) {
    // Base cases
    if (i == 0 || j == 0) return 0;
    
    // Return memoized result if available
    if (memo[i][j] != -1) return memo[i][j];
    
    // If current characters match
    if (text1[i-1] == text2[j-1]) {
        memo[i][j] = longestCommonSubsequenceRecursive(text1, text2, i-1, j-1, memo) + 1;
    } else {
        // Characters don't match, take the maximum by either skipping one character from text1 or text2
        memo[i][j] = max(
            longestCommonSubsequenceRecursive(text1, text2, i-1, j, memo),
            longestCommonSubsequenceRecursive(text1, text2, i, j-1, memo)
        );
    }
    
    return memo[i][j];
}

int longestCommonSubsequence(string text1, string text2) {
    int m = text1.length();
    int n = text2.length();
    vector<vector<int>> memo(m+1, vector<int>(n+1, -1));
    return longestCommonSubsequenceRecursive(text1, text2, m, n, memo);
}
```

Memoized (Top-Down) Approach:
```cpp
int longestCommonSubsequence(string text1, string text2) {
    int m = text1.length();
    int n = text2.length();
    vector<vector<int>> memo(m+1, vector<int>(n+1, -1));
    
    function<int(int, int)> dp = [&](int i, int j) {
        // Base cases
        if (i == 0 || j == 0) return 0;
        
        // Return memoized result if available
        if (memo[i][j] != -1) return memo[i][j];
        
        // If current characters match
        if (text1[i-1] == text2[j-1]) {
            memo[i][j] = dp(i-1, j-1) + 1;
        } else {
            // Characters don't match, take the maximum by either skipping one character from text1 or text2
            memo[i][j] = max(dp(i-1, j), dp(i, j-1));
        }
        
        return memo[i][j];
    };
    
    return dp(m, n);
}
```

Tabulated (Bottom-Up) Approach:
```cpp
int longestCommonSubsequence(string text1, string text2) {
    int m = text1.length();
    int n = text2.length();
    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
    
    // Fill dp table
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

Space-Optimized Approach:
```cpp
int longestCommonSubsequence(string text1, string text2) {
    int m = text1.length();
    int n = text2.length();
    
    // Ensure text2 is the shorter string to minimize space
    if (m < n) {
        swap(text1, text2);
        swap(m, n);
    }
    
    vector<int> prev(n+1, 0);
    vector<int> curr(n+1, 0);
    
    // Fill dp table
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (text1[i-1] == text2[j-1]) {
                curr[j] = prev[j-1] + 1;
            } else {
                curr[j] = max(prev[j], curr[j-1]);
            }
        }
        // Update prev for next iteration
        prev = curr;
    }
    
    return prev[n];
}
```

**Complexity Analysis**:
- Time Complexity: O(m * n) where m and n are the lengths of the two strings.
- Space Complexity:
  - Recursive/Memoized: O(m * n) for the memoization table.
  - Tabulated: O(m * n) for the dp table.
  - Space-Optimized: O(min(m, n)) as we only need two rows of the dp table.

**Edge Cases**:
- Empty strings: Return 0.
- One string is a subsequence of the other: Return the length of the shorter string.
- No common characters: Return 0.

**Optimization Techniques**:
- We can optimize space by only keeping track of the current and previous rows.
- We can ensure the second dimension of the dp table is the shorter string to minimize space usage.

**DP Table Visualization**:
```
For text1 = "abcde", text2 = "ace":

DP table:
     |   | a | c | e
-----|---|---|---|---
     | 0 | 0 | 0 | 0
-----|---|---|---|---
  a  | 0 | 1 | 1 | 1
-----|---|---|---|---
  b  | 0 | 1 | 1 | 1
-----|---|---|---|---
  c  | 0 | 1 | 2 | 2
-----|---|---|---|---
  d  | 0 | 1 | 2 | 2
-----|---|---|---|---
  e  | 0 | 1 | 2 | 3

Explanation:
- dp[0][0] = 0: Empty strings have LCS of 0
- dp[1][1] = 1: "a" and "a" have LCS of 1
- dp[2][1] = 1: "ab" and "a" have LCS of 1
- dp[2][2] = 1: "ab" and "ac" have LCS of 1
- dp[3][2] = 2: "abc" and "ac" have LCS of 2 ("ac")
- dp[5][3] = 3: "abcde" and "ace" have LCS of 3 ("ace")
```#### Problem 7: Edit Distance
**Difficulty**: Hard

**Problem Statement**:
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`. You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

**Real-World Context**:
This problem has applications in spell checking, DNA sequence alignment, and natural language processing for determining how similar two strings are.

**Test Cases**:
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: Various operations can achieve this.
```

**Visualization**:
```
For word1 = "horse", word2 = "ros":

DP table:
      | "" | r | o | s
------|----|----|----|----|
 ""   | 0  | 1  | 2 | 3 |
------|----|----|----|----|
 h    | 1  | 1  | 2 | 3 |
------|----|----|----|----|
 o    | 2  | 2  | 1 | 2 |
------|----|----|----|----|
 r    | 3  | 2  | 2 | 2 |
------|----|----|----|----|
 s    | 4  | 3  | 3 | 2 |
------|----|----|----|----|
 e    | 5  | 4  | 4 | 3 |
```

**Recurrence Relation**:
Let `dp[i][j]` be the minimum number of operations required to convert word1[0...i-1] to word2[0...j-1].
```
if word1[i-1] == word2[j-1]:
    dp[i][j] = dp[i-1][j-1]
else:
    dp[i][j] = 1 + min(dp[i-1][j],    // Delete
                        dp[i][j-1],    // Insert
                        dp[i-1][j-1])  // Replace
```

**Solution**:

Recursive (Top-Down) Approach:
```cpp
int minDistanceRecursive(string& word1, string& word2, int i, int j, vector<vector<int>>& memo) {
    // Base cases
    if (i == 0) return j; // Insert all characters of word2
    if (j == 0) return i; // Delete all characters of word1
    
    // Return memoized result if available
    if (memo[i][j] != -1) return memo[i][j];
    
    // If current characters match, no operation needed
    if (word1[i-1] == word2[j-1]) {
        memo[i][j] = minDistanceRecursive(word1, word2, i-1, j-1, memo);
        return memo[i][j];
    }
    
    // Calculate minimum of three operations
    int deleteOp = minDistanceRecursive(word1, word2, i-1, j, memo);
    int insertOp = minDistanceRecursive(word1, word2, i, j-1, memo);
    int replaceOp = minDistanceRecursive(word1, word2, i-1, j-1, memo);
    
    // Cache and return result
    memo[i][j] = 1 + min({deleteOp, insertOp, replaceOp});
    return memo[i][j];
}

int minDistance(string word1, string word2) {
    int m = word1.length();
    int n = word2.length();
    vector<vector<int>> memo(m+1, vector<int>(n+1, -1));
    return minDistanceRecursive(word1, word2, m, n, memo);
}
```

Memoized (Top-Down) Approach:
```cpp
int minDistance(string word1, string word2) {
    int m = word1.length();
    int n = word2.length();
    vector<vector<int>> memo(m+1, vector<int>(n+1, -1));
    
    function<int(int, int)> dp = [&](int i, int j) {
        // Base cases
        if (i == 0) return j; // Insert all characters of word2
        if (j == 0) return i; // Delete all characters of word1
        
        // Return memoized result if available
        if (memo[i][j] != -1) return memo[i][j];
        
        // If current characters match, no operation needed
        if (word1[i-1] == word2[j-1]) {
            memo[i][j] = dp(i-1, j-1);
            return memo[i][j];
        }
        
        // Calculate minimum of three operations
        int deleteOp = dp(i-1, j);
        int insertOp = dp(i, j-1);
        int replaceOp = dp(i-1, j-1);
        
        // Cache and return result
        memo[i][j] = 1 + min({deleteOp, insertOp, replaceOp});
        return memo[i][j];
    };
    
    return dp(m, n);
}
```

Tabulated (Bottom-Up) Approach:
```cpp
int minDistance(string word1, string word2) {
    int m = word1.length();
    int n = word2.length();
    vector<vector<int>> dp(m+1, vector<int>(n+1));
    
    // Base cases: converting to empty string
    for (int i = 0; i <= m; i++) {
        dp[i][0] = i; // Delete all characters
    }
    
    for (int j = 0; j <= n; j++) {
        dp[0][j] = j; // Insert all characters
    }
    
    // Fill dp table
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (word1[i-1] == word2[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = 1 + min({dp[i-1][j],    // Delete
                                    dp[i][j-1],    // Insert
                                    dp[i-1][j-1]}); // Replace
            }
        }
    }
    
    return dp[m][n];
}
```

Space-Optimized Approach:
```cpp
int minDistance(string word1, string word2) {
    int m = word1.length();
    int n = word2.length();
    
    // If one of the strings is empty
    if (m == 0) return n;
    if (n == 0) return m;
    
    // We only need two rows: current and previous
    vector<int> prev(n+1);
    vector<int> curr(n+1);
    
    // Initialize the first row
    for (int j = 0; j <= n; j++) {
        prev[j] = j;
    }
    
    // Fill the dp table row by row
    for (int i = 1; i <= m; i++) {
        curr[0] = i; // First column
        
        for (int j = 1; j <= n; j++) {
            if (word1[i-1] == word2[j-1]) {
                curr[j] = prev[j-1];
            } else {
                curr[j] = 1 + min({prev[j],      // Delete
                                   curr[j-1],    // Insert
                                   prev[j-1]});  // Replace
            }
        }
        
        // Update prev for next iteration
        prev = curr;
    }
    
    return prev[n];
}
```

**Complexity Analysis**:
- Time Complexity: O(m * n) where m and n are the lengths of the two strings.
- Space Complexity:
  - Recursive/Memoized: O(m * n) for the memoization table.
  - Tabulated: O(m * n) for the dp table.
  - Space-Optimized: O(n) as we only need two rows.

**Edge Cases**:
- Empty strings: If either string is empty, return the length of the other string.
- Identical strings: Return 0.
- No common characters: Still works as we can replace all characters.

**Optimization Techniques**:
- We can optimize space by only keeping track of the current and previous rows.
- For specific scenarios (like one string being a substring of another), we can use heuristics to speed up the calculation.

**DP Table Visualization**:
```
For word1 = "horse", word2 = "ros":

DP table:
      | "" | r | o | s
------|----|----|----|----|
 ""   | 0  | 1  | 2 | 3 |
------|----|----|----|----|
 h    | 1  | 1  | 2 | 3 |
------|----|----|----|----|
 o    | 2  | 2  | 1 | 2 |
------|----|----|----|----|
 r    | 3  | 2  | 2 | 2 |
------|----|----|----|----|
 s    | 4  | 3  | 3  | 2 |
------|----|----|----|----|
 e    | 5  | 4  | 4  | 3 |

Explanation for dp[5][3] = 3# Dynamic Programming Mastery Guide: 1D and 2D Array Problems in C++

## Table of Contents
1. [Introduction to Dynamic Programming](#introduction-to-dynamic-programming)
2. [Fundamental Principles](#fundamental-principles)
3. [Systematic Approach to DP Problems](#systematic-approach-to-dp-problems)
4. [1D Array Dynamic Programming](#1d-array-dynamic-programming)
   - [Conceptual Framework](#1d-conceptual-framework)
   - [Problem Types and Techniques](#1d-problem-types-and-techniques)
   - [Implementation Templates](#1d-implementation-templates)
5. [2D Array/Matrix Dynamic Programming](#2d-arraymatrix-dynamic-programming)
   - [Conceptual Framework](#2d-conceptual-framework)
   - [Problem Types and Techniques](#2d-problem-types-and-techniques)
   - [Implementation Templates](#2d-implementation-templates)
6. [Problem Collection](#problem-collection)
   - [1D Array Problems](#1d-array-problems)
   - [2D Array/Matrix Problems](#2d-arraymatrix-problems)
7. [Implementation Strategy](#implementation-strategy)
8. [Testing and Debugging Strategies](#testing-and-debugging-strategies)
9. [Practical Tips and Tricks](#practical-tips-and-tricks)
10. [Advanced DP Techniques](#advanced-dp-techniques)
11. [Common Mistakes and Pitfalls](#common-mistakes-and-pitfalls)
12. [Application to Classic Algorithm Problems](#application-to-classic-algorithm-problems)
13. [Advanced Problem Collection](#advanced-problem-collection)
14. [Progression Path](#progression-path)
15. [Decision Flowcharts](#decision-flowcharts)
16. [Conclusion](#conclusion)

## Introduction to Dynamic Programming

Dynamic Programming (DP) is a powerful algorithmic technique for solving complex problems by breaking them down into simpler subproblems. It's particularly effective for optimization problems that exhibit two key properties:

1. **Optimal Substructure**: An optimal solution to the problem contains optimal solutions to its subproblems.
2. **Overlapping Subproblems**: The same subproblems are solved multiple times during computation.

Array-based dynamic programming is one of the most common applications of DP, where states and transitions are represented using 1D or 2D arrays.

## Fundamental Principles

### Core Concepts

1. **Subproblem Definition**: Identify smaller instances of the original problem.
2. **State Representation**: Determine the variables needed to represent a subproblem.
3. **Recurrence Relation**: Define how to compute solutions from previously solved subproblems.
4. **Base Cases**: Define solutions for the smallest subproblems.
5. **State Space**: The collection of all possible states in the problem.
6. **Transitions**: Rules for moving between states.

### Key Approaches in Dynamic Programming

1. **Top-Down (Memoization)**: Recursive approach with caching of results.
2. **Bottom-Up (Tabulation)**: Iterative approach building solutions from base cases.

### When to Use Dynamic Programming

- Optimization problems (maximize/minimize)
- Counting problems (how many ways)
- Decision problems (is it possible)
- Problems with recursive structure
- Problems with overlapping subproblems

## Systematic Approach to DP Problems

### 1. Define the State

- What information do we need to represent a subproblem?
- For 1D problems: Usually an index `i` or a value `x`.
- For 2D problems: Usually a pair of indices `(i, j)` or additional parameters.

### 2. Establish the Recurrence Relation

- How do we transition between states?
- What decisions or choices are available at each state?
- How do we derive optimal solutions from subproblems?

### 3. Identify Base Cases

- What are the simplest subproblems we can solve directly?
- What happens at boundaries or when the input is empty?

### 4. Determine the Order of Computation

- Which subproblems need to be solved first?
- How do we ensure all dependencies are resolved before computing a state?

### 5. Implement the Solution

- Top-down: Recursive function with memoization
- Bottom-up: Iterative computation with tabulation

### State Transition Diagram

A visual representation of how states depend on each other:

```
   State(i-2) → State(i-1) → State(i)
                    ↑            ↑
                    |            |
             Base Case(0)   Base Case(1)
```

### Difference Between 1D and 2D DP Approaches

| Aspect | 1D Dynamic Programming | 2D Dynamic Programming |
|--------|------------------------|------------------------|
| State Representation | Usually single parameter: `dp[i]` | Usually two parameters: `dp[i][j]` |
| Problem Complexity | Generally simpler | Often more complex |
| Space Requirements | O(n) typically | O(n²) or O(n×m) typically |
| Common Applications | Sequences, linear decision making | Matrices, grid problems, comparing sequences |
| Implementation | Usually simpler nested loops | Multiple nested loops, more complex |
| State Transitions | Fewer possible state transitions | More possible state transitions |
| Space Optimization | Often can reduce to O(1) or O(k) | Can sometimes reduce to O(n) or O(2×n) |

## 1D Array Dynamic Programming

### 1D Conceptual Framework

In 1D DP problems, we typically use a single array `dp[]` where each element represents the solution to a subproblem defined by a single parameter (usually an index or value).

#### State Definition

- `dp[i]` typically represents the optimal answer for the subproblem considering elements up to index `i`.

#### Common State Transitions

- From previous states: `dp[i] = f(dp[i-1], dp[i-2], ..., dp[i-k])`
- Considering multiple choices: `dp[i] = optimal(choice1, choice2, ...)`

### 1D Problem Types and Techniques

1. **Linear Sequence Problems**
   - Maximum/minimum sum subarrays
   - Longest increasing subsequences
   
2. **Decision-Making Problems**
   - Take or skip current element
   - Choose one of multiple options
   
3. **Optimization with Constraints**
   - Knapsack problems
   - Problems with limited resources
   
4. **Interval-Based Problems**
   - Problems involving ranges or segments
   - Partitioning problems
   
5. **State Compression**
   - Using bits to represent states
   - Reducing state space complexity

### 1D Implementation Templates

#### Top-Down (Memoization)

```cpp
// Recursive function with memoization
int dp[MAX_N];
bool computed[MAX_N];

int solve(int i) {
    // Base cases
    if (i < 0) return 0;
    if (i == 0) return baseValue;
    
    // Return cached result if available
    if (computed[i]) return dp[i];
    
    // Compute result from subproblems
    int result = 0;
    // Example: Choose maximum from previous states
    result = max(solve(i-1) + value1, solve(i-2) + value2);
    
    // Cache and return result
    computed[i] = true;
    dp[i] = result;
    return result;
}
```

#### Bottom-Up (Tabulation)

```cpp
// Iterative function with tabulation
int solve(vector<int>& nums) {
    int n = nums.size();
    vector<int> dp(n+1, 0);
    
    // Base cases
    dp[0] = baseValue;
    
    // Fill dp table
    for (int i = 1; i <= n; i++) {
        // Example: Choose maximum from previous states
        dp[i] = max(dp[i-1] + value1, (i >= 2 ? dp[i-2] + value2 : 0));
    }
    
    return dp[n];
}
```

#### Space-Optimized Implementation

```cpp
// Space-optimized solution
int solve(vector<int>& nums) {
    int n = nums.size();
    
    // Only store necessary previous states
    int prev2 = 0;
    int prev1 = baseValue;
    int current = prev1;
    
    for (int i = 1; i <= n; i++) {
        current = max(prev1 + value1, prev2 + value2);
        prev2 = prev1;
        prev1 = current;
    }
    
    return current;
}
```

## 2D Array/Matrix Dynamic Programming

### 2D Conceptual Framework

In 2D DP problems, we typically use a 2D array `dp[][]` where each element represents the solution to a subproblem defined by two parameters (usually a pair of indices).

#### State Definition

- `dp[i][j]` typically represents the optimal answer for a subproblem defined by coordinates `(i, j)` or considering elements up to indices `i` and `j` in two different contexts.

#### Common State Transitions

- From adjacent cells: `dp[i][j] = f(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`
- Considering multiple paths or choices: `dp[i][j] = optimal(choice1, choice2, ...)`

### 2D Problem Types and Techniques

1. **Grid Traversal with Constraints**
   - Unique paths
   - Path with obstacles
   - Minimum/maximum path sum
   
2. **Matrix Path Optimization**
   - Shortest/longest paths
   - Paths with special properties
   
3. **Region Counting/Coloring**
   - Counting regions with properties
   - Coloring or marking regions
   
4. **2D Pattern Analysis**
   - Finding patterns in matrices
   - Matching or comparing patterns
   
5. **Complex State Representation**
   - Additional dimensions or parameters
   - State encoded in matrix cells

### 2D Implementation Templates

#### Top-Down (Memoization)

```cpp
// Recursive function with memoization
int dp[MAX_M][MAX_N];
bool computed[MAX_M][MAX_N];

int solve(int i, int j) {
    // Base cases and boundary checks
    if (i < 0 || j < 0) return INF; // or appropriate value
    if (i == 0 && j == 0) return baseValue;
    
    // Return cached result if available
    if (computed[i][j]) return dp[i][j];
    
    // Compute result from subproblems
    int result = INF; // or appropriate initial value
    
    // Example: Choose minimum path from adjacent cells
    result = min(solve(i-1, j), solve(i, j-1)) + cost[i][j];
    
    // Cache and return result
    computed[i][j] = true;
    dp[i][j] = result;
    return result;
}
```

#### Bottom-Up (Tabulation)

```cpp
// Iterative function with tabulation
int solve(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<int>> dp(m, vector<int>(n, 0));
    
    // Base case
    dp[0][0] = grid[0][0];
    
    // Fill first row
    for (int j = 1; j < n; j++) {
        dp[0][j] = dp[0][j-1] + grid[0][j];
    }
    
    // Fill first column
    for (int i = 1; i < m; i++) {
        dp[i][0] = dp[i-1][0] + grid[i][0];
    }
    
    // Fill rest of the dp table
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
        }
    }
    
    return dp[m-1][n-1];
}
```

#### Space-Optimized Implementation

```cpp
// Space-optimized solution
int solve(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    
    // Only store current and previous row
    vector<int> prev(n, 0);
    vector<int> curr(n, 0);
    
    prev[0] = grid[0][0];
    
    // Fill first row in prev
    for (int j = 1; j < n; j++) {
        prev[j] = prev[j-1] + grid[0][j];
    }
    
    // Process row by row
    for (int i = 1; i < m; i++) {
        curr[0] = prev[0] + grid[i][0];
        
        for (int j = 1; j < n; j++) {
            curr[j] = min(prev[j], curr[j-1]) + grid[i][j];
        }
        
        // Swap rows for next iteration
        prev = curr;
    }
    
    return prev[n-1];
}
```

## Problem Collection

### 1D Array Problems

#### Problem 1: Maximum Subarray Sum
**Difficulty**: Easy

**Problem Statement**:
Given an array of integers, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Real-World Context**:
This problem simulates financial analysis, where an analyst needs to identify the time period with the maximum profit given daily profit/loss data.

**Test Cases**:
```
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6.

Input: [1]
Output: 1

Input: [5, -3, 5]
Output: 7
```

**Visualization**:
```
Array:   [-2,  1, -3,  4, -1,  2,  1, -5,  4]
DP:      [-2,  1, -2,  4,  3,  5,  6,  1,  5]
         ^         ^             ^        ^
       start       |          maximum    end
```

**Recurrence Relation**:
Let `dp[i]` be the maximum sum ending at index `i`.
```
dp[i] = max(nums[i], dp[i-1] + nums[i])
```

**Solution**:

Recursive (Top-Down) Approach:
```cpp
int maxSubArrayRecursive(vector<int>& nums, int i, vector<int>& memo) {
    // Base cases
    if (i < 0) return 0;
    if (i == 0) return nums[0];
    
    // Return memoized result if available
    if (memo[i] != INT_MIN) return memo[i];
    
    // Recurrence relation
    memo[i] = max(nums[i], maxSubArrayRecursive(nums, i-1, memo) + nums[i]);
    return memo[i];
}

int maxSubArray(vector<int>& nums) {
    int n = nums.size();
    vector<int> memo(n, INT_MIN);
    
    // Calculate maximum subarray sum ending at each position
    maxSubArrayRecursive(nums, n-1, memo);
    
    // Find the maximum value in the memo array
    return *max_element(memo.begin(), memo.end());
}
```

Memoized (Top-Down) Approach:
```cpp
int coinChange(vector<int>& coins, int amount) {
    vector<int> memo(amount + 1, INT_MAX);
    
    function<int(int)> dp = [&](int remaining) {
        // Base cases
        if (remaining == 0) return 0;
        if (remaining < 0) return -1;
        
        // Return memoized result if available
        if (memo[remaining] != INT_MAX) return memo[remaining];
        
        int minCoins = INT_MAX;
        
        // Try each coin
        for (int coin : coins) {
            int res = dp(remaining - coin);
            if (res != -1) {
                minCoins = min(minCoins, res + 1);
            }
        }
        
        // Cache and return result
        memo[remaining] = (minCoins == INT_MAX) ? -1 : minCoins;
        return memo[remaining];
    };
    
    return dp(amount);
}
```

Tabulated (Bottom-Up) Approach:
```cpp
int coinChange(vector<int>& coins, int amount) {
    vector<int> dp(amount + 1, amount + 1);
    
    // Base case
    dp[0] = 0;
    
    // Fill dp table
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

Space-Optimized Approach (In this case, the tabulated approach is already optimal in terms of space):
```cpp
int coinChange(vector<int>& coins, int amount) {
    vector<int> dp(amount + 1, amount + 1);
    
    // Base case
    dp[0] = 0;
    
    // Fill dp table
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

**Complexity Analysis**:
- Time Complexity: O(amount * n) where n is the number of coin denominations.
- Space Complexity:
  - Recursive/Memoized: O(amount) for the memoization table and the recursion stack.
  - Tabulated: O(amount) for the dp array.

**Edge Cases**:
- Amount = 0: Return 0 (no coins needed).
- No valid combination: Return -1.
- Multiple valid combinations: Return the one with the fewest coins.

**Optimization Techniques**:
- Sort the coins in decreasing order to potentially find a greedy solution first (doesn't always work but can improve average case).
- Use BFS instead of DP for a potentially faster solution if the coin denominations are large but few in number.

**DP Table Visualization**:
```
For amount=11, coins=[1,2,5]:

amount: 0 1 2 3 4 5 6 7 8 9 10 11
dp[i]:  0 1 1 2 2 1 2 2 3 3  2  3

Building the table:
dp[0] = 0 (base case)
dp[1] = min(dp[1-1] + 1) = dp[0] + 1 = 1
dp[2] = min(dp[2-1] + 1, dp[2-2] + 1) = min(dp[1] + 1, dp[0] + 1) = min(2, 1) = 1
...
dp[11] = min(dp[11-1] + 1, dp[11-2] + 1, dp[11-5] + 1) = min(dp[10] + 1, dp[9] + 1, dp[6] + 1) = min(3, 4, 3) = 3
```
```cpp
int maxSubArray(vector<int>& nums) {
    int n = nums.size();
    vector<int> memo(n, INT_MIN);
    
    function<int(int)> dp = [&](int i) {
        // Base cases
        if (i < 0) return 0;
        if (i == 0) return nums[0];
        
        // Return memoized result if available
        if (memo[i] != INT_MIN) return memo[i];
        
        // Recurrence relation
        memo[i] = max(nums[i], dp(i-1) + nums[i]);
        return memo[i];
    };
    
    dp(n-1);
    return *max_element(memo.begin(), memo.end());
}
```

Tabulated (Bottom-Up) Approach:
```cpp
int maxSubArray(vector<int>& nums) {
    int n = nums.size();
    vector<int> dp(n);
    
    // Base case
    dp[0] = nums[0];
    int maxSum = dp[0];
    
    // Fill dp table
    for (int i = 1; i < n; i++) {
        dp[i] = max(nums[i], dp[i-1] + nums[i]);
        maxSum = max(maxSum, dp[i]);
    }
    
    return maxSum;
}
```

Space-Optimized Approach:
```cpp
int maxSubArray(vector<int>& nums) {
    int n = nums.size();
    int currentMax = nums[0];
    int globalMax = nums[0];
    
    for (int i = 1; i < n; i++) {
        currentMax = max(nums[i], currentMax + nums[i]);
        globalMax = max(globalMax, currentMax);
    }
    
    return globalMax;
}
```

**Complexity Analysis**:
- Time Complexity: O(n) - We process each element once.
- Space Complexity:
  - Recursive/Memoized: O(n) for the memoization table and the recursion stack.
  - Tabulated: O(n) for the dp array.
  - Space-Optimized: O(1) as we only use two variables.

**Edge Cases**:
- All negative numbers: Return the largest (least negative) number.
- Empty array: Typically not allowed by the problem, but would return 0.
- Single element array: Return that element.

**Optimization Techniques**:
- Kadane's Algorithm is essentially the space-optimized solution above.
- We can also track start and end indices of the maximum subarray if needed.

**DP Table Visualization**:
```
Index:  0   1   2   3   4   5   6   7   8
Array: -2   1  -3   4  -1   2   1  -5   4
dp[i]: -2   1  -2   4   3   5   6   1   5

Maximum Subarray Sum: 6 (from index 3 to 6)
```

#### Problem 2: Climb Stairs
**Difficulty**: Easy

**Problem Statement**:
You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Real-World Context**:
This problem simulates movement planning, like a robot navigating different-sized steps or a player making moves in a board game with specific rules.

**Test Cases**:
```
Input: n = 2
Output: 2
Explanation: There are two ways: 1+1 and 2.

Input: n = 3
Output: 3
Explanation: There are three ways: 1+1+1, 1+2, and 2+1.
```

**Visualization**:
```
For n=5:
  Step 5 (goal)
 /        \
Step 4    Step 3
/    \    /    \
3     2   2     1
/\    /\  /\    /\
2 1   1 0 1 0   0
```

**Recurrence Relation**:
Let `dp[i]` be the number of ways to reach step `i`.
```
dp[i] = dp[i-1] + dp[i-2]
```

**Solution**:

Recursive (Top-Down) Approach:
```cpp
int climbStairsRecursive(int n, vector<int>& memo) {
    // Base cases
    if (n <= 0) return 0;
    if (n == 1) return 1;
    if (n == 2) return 2;
    
    // Return memoized result if available
    if (memo[n] != -1) return memo[n];
    
    // Recurrence relation
    memo[n] = climbStairsRecursive(n-1, memo) + climbStairsRecursive(n-2, memo);
    return memo[n];
}

int climbStairs(int n) {
    vector<int> memo(n+1, -1);
    return climbStairsRecursive(n, memo);
}
```

Memoized (Top-Down) Approach:
```cpp
int climbStairs(int n) {
    vector<int> memo(n+1, -1);
    
    function<int(int)> dp = [&](int i) {
        // Base cases
        if (i <= 0) return 0;
        if (i == 1) return 1;
        if (i == 2) return 2;
        
        // Return memoized result if available
        if (memo[i] != -1) return memo[i];
        
        // Recurrence relation
        memo[i] = dp(i-1) + dp(i-2);
        return memo[i];
    };
    
    return dp(n);
}
```

Tabulated (Bottom-Up) Approach:
```cpp
int climbStairs(int n) {
    if (n <= 2) return n;
    
    vector<int> dp(n+1);
    
    // Base cases
    dp[1] = 1;
    dp[2] = 2;
    
    // Fill dp table
    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    
    return dp[n];
}
```

Space-Optimized Approach:
```cpp
int climbStairs(int n) {
    if (n <= 2) return n;
    
    int prev2 = 1; // Ways to reach step 1
    int prev1 = 2; // Ways to reach step 2
    int current = 0;
    
    for (int i = 3; i <= n; i++) {
        current = prev1 + prev2;
        prev2 = prev1;
        prev1 = current;
    }
    
    return prev1;
}
```

**Complexity Analysis**:
- Time Complexity: O(n) - We compute each step once.
- Space Complexity:
  - Recursive/Memoized: O(n) for the memoization table and the recursion stack.
  - Tabulated: O(n) for the dp array.
  - Space-Optimized: O(1) as we only use a constant number of variables.

**Edge Cases**:
- n = 0: Return 0 (typically not part of the problem).
- n = 1: Return 1 (only one way - take one step).
- Very large n: Watch for integer overflow.

**Optimization Techniques**:
- We only need to store the last two results at any point.
- This problem follows the Fibonacci sequence, which has a closed-form solution that can compute the answer in O(1) time.

**DP Table Visualization**:
```
n:      1  2  3  4  5  6  7
dp[n]:  1  2  3  5  8 13 21

For n=5:
- To reach step 5, we can:
  - Take a single step from step 4 (5 ways to reach step 4)
  - Take a double step from step 3 (3 ways to reach step 3)
  - Total: 5 + 3 = 8 ways
```

#### Problem 3: House Robber
**Difficulty**: Medium

**Problem Statement**:
A professional robber plans to rob houses along a street. Each house has a certain amount of money stashed. The only constraint is that adjacent houses have connected security systems and will automatically contact the police if two adjacent houses were broken into on the same night. Determine the maximum amount of money the robber can rob tonight without alerting the police.

**Real-World Context**:
This problem models resource allocation with constraints, such as choosing investment opportunities where certain combinations cannot be selected together.

**Test Cases**:
```
Input: [1, 2, 3, 1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total = 1 + 3 = 4.

Input: [2, 7, 9, 3, 1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1). Total = 2 + 9 + 1 = 12.
```

**Visualization**:
```
Houses:   [1, 2, 3, 1]
          
Decision tree:
          start
         /     \
      Rob 1    Skip 1
       /  \     /   \
   Skip 2  Rob 2   Skip 2
    /       /  \     /  \
 Rob 3    Skip 3  Rob 3
  /        /       /
Skip 4   Rob 4   Skip 4
```

**Recurrence Relation**:
Let `dp[i]` be the maximum amount of money that can be robbed up to house `i`.
```
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
```

**Solution**:

Recursive (Top-Down) Approach:
```cpp
int robRecursive(vector<int>& nums, int i, vector<int>& memo) {
    // Base cases
    if (i < 0) return 0;
    
    // Return memoized result if available
    if (memo[i] != -1) return memo[i];
    
    // Recurrence relation
    memo[i] = max(robRecursive(nums, i-1, memo), robRecursive(nums, i-2, memo) + nums[i]);
    return memo[i];
}

int rob(vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return 0;
    
    vector<int> memo(n, -1);
    return robRecursive(nums, n-1, memo);
}
```

Memoized (Top-Down) Approach:
```cpp
int rob(vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return 0;
    
    vector<int> memo(n, -1);
    
    function<int(int)> dp = [&](int i) {
        // Base cases
        if (i < 0) return 0;
        
        // Return memoized result if available
        if (memo[i] != -1) return memo[i];
        
        // Recurrence relation
        memo[i] = max(dp(i-1), dp(i-2) + nums[i]);
        return memo[i];
    };
    
    return dp(n-1);
}
```

Tabulated (Bottom-Up) Approach:
```cpp
int rob(vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return 0;
    if (n == 1) return nums[0];
    
    vector<int> dp(n);
    
    // Base cases
    dp[0] = nums[0];
    dp[1] = max(nums[0], nums[1]);
    
    // Fill dp table
    for (int i = 2; i < n; i++) {
        dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
    }
    
    return dp[n-1];
}
```

Space-Optimized Approach:
```cpp
int rob(vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return 0;
    if (n == 1) return nums[0];
    
    int prev2 = nums[0];
    int prev1 = max(nums[0], nums[1]);
    
    for (int i = 2; i < n; i++) {
        int current = max(prev1, prev2 + nums[i]);
        prev2 = prev1;
        prev1 = current;
    }
    
    return prev1;
}
```

**Complexity Analysis**:
- Time Complexity: O(n) - We process each house once.
- Space Complexity:
  - Recursive/Memoized: O(n) for the memoization table and the recursion stack.
  - Tabulated: O(n) for the dp array.
  - Space-Optimized: O(1) as we only use a constant number of variables.

**Edge Cases**:
- Empty array: Return 0.
- Single house: Rob that house.
- Two houses: Rob the house with more money.

**Optimization Techniques**:
- Only need to store the last two results at any point.
- For very large inputs, consider using modular arithmetic to prevent overflow.

**DP Table Visualization**:
```
Index:  0  1  2  3  4
Houses: 2  7  9  3  1
dp[i]:  2  7 11 11 12

For each house i:
- If we rob house i: Get money from house i + maximum money from houses 0 to i-2
- If we don't rob house i: Maximum money from houses 0 to i-1
- Choose the maximum of these two options
```

#### Problem 4: Coin Change
**Difficulty**: Medium

**Problem Statement**:
You are given coins of different denominations and a total amount of money. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

**Real-World Context**:
This problem models the classic coin change scenario faced by cashiers and automated vending machines that need to provide optimal change with limited denomination options.

**Test Cases**:
```
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1
Explanation: No combination can make up the amount.

Input: coins = [1], amount = 0
Output: 0
Explanation: No coins needed for zero amount.
```

**Visualization**:
```
For amount=11, coins=[1,2,5]:

amount: 0 1 2 3 4 5 6 7 8 9 10 11
dp[i]:  0 1 1 2 2 1 2 2 3 3  2  3

For amount 11:
- Use coin 1: dp[11-1] + 1 = dp[10] + 1 = 2 + 1 = 3
- Use coin 2: dp[11-2] + 1 = dp[9] + 1 = 3 + 1 = 4
- Use coin 5: dp[11-5] + 1 = dp[6] + 1 = 2 + 1 = 3
Minimum is 3.
```

**Recurrence Relation**:
Let `dp[i]` be the fewest number of coins needed to make amount `i`.
```
dp[i] = min(dp[i-coin] + 1) for all coin in coins if i-coin >= 0
```

**Solution**:

Recursive (Top-Down) Approach:
```cpp
int coinChangeRecursive(vector<int>& coins, int amount, vector<int>& memo) {
    // Base cases
    if (amount == 0) return 0;
    if (amount < 0) return -1;
    
    // Return memoized result if available
    if (memo[amount] != INT_MAX) return memo[amount];
    
    int minCoins = INT_MAX;
    
    // Try each coin
    for (int coin : coins) {
        int res = coinChangeRecursive(coins, amount - coin, memo);
        if (res != -1) {
            minCoins = min(minCoins, res + 1);
        }
    }
    
    // Cache and return result
    memo[amount] = (minCoins == INT_MAX) ? -1 : minCoins;
    return memo[amount];
}

int coinChange(vector<int>& coins, int amount) {
    vector<int> memo(amount + 1, INT_MAX);
    return coinChangeRecursive(coins, amount, memo);
}
