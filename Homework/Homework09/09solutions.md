# CSCI 335 Dynamic Programming Homework 09 Solutions

## Due: Thursday, May 15, before class
## Required Problems: 1, 2, 3
## Optional Problems: 4, 5

## Problem 1: Pascal's Triangle
[Link to problem](https://leetcode.com/problems/pascals-triangle/description/)

### Solution:
```cpp
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        // Initialize the result with the appropriate number of rows
        vector<vector<int>> result(numRows);
        
        // Fill in each row
        for (int i = 0; i < numRows; i++) {
            // Each row has i+1 elements
            result[i].resize(i + 1);
            
            // First and last elements in each row are always 1
            result[i][0] = result[i][i] = 1;
            
            // Calculate middle elements using the recurrence relation
            for (int j = 1; j < i; j++) {
                result[i][j] = result[i-1][j-1] + result[i-1][j];
            }
        }
        
        return result;
    }
};
```

### Explanation:
This is a 2D dynamic programming problem where each element is determined by the sum of two elements from the previous row.

1. **State Definition**: `result[i][j]` represents the value at row i, column j in Pascal's Triangle.
2. **Recurrence Relation**: `result[i][j] = result[i-1][j-1] + result[i-1][j]` for 0 < j < i.
3. **Base Cases**: The first and last elements of each row are 1.

**Time Complexity**: O(numRows²) - We fill each position in the triangle once.
**Space Complexity**: O(numRows²) - We store the entire triangle.

## Problem 2: Perfect Squares
[Link to problem](https://leetcode.com/problems/perfect-squares/description/)

### Solution:
```cpp
class Solution {
public:
    int numSquares(int n) {
        // Create a DP array to store the minimum number of perfect squares
        vector<int> dp(n + 1, INT_MAX);
        
        // Base case: 0 requires 0 perfect squares
        dp[0] = 0;
        
        // Fill the dp array from 1 to n
        for (int i = 1; i <= n; i++) {
            // Try all possible perfect squares less than or equal to i
            for (int j = 1; j * j <= i; j++) {
                // Update dp[i] to be minimum of current value and dp[i - j*j] + 1
                dp[i] = min(dp[i], dp[i - j*j] + 1);
            }
        }
        
        return dp[n];
    }
};
```

### Explanation:
This is a 1D dynamic programming problem where we calculate the minimum number of perfect squares needed for each value from 1 to n.

1. **State Definition**: `dp[i]` represents the minimum number of perfect squares that sum to i.
2. **Recurrence Relation**: `dp[i] = min(dp[i], dp[i - j*j] + 1)` for all j where j*j ≤ i.
3. **Base Case**: `dp[0] = 0` (it takes 0 perfect squares to sum to 0).

For each number i, we try all possible perfect squares j*j that are less than or equal to i. We take the minimum of:
- Current value of dp[i]
- dp[i - j*j] + 1 (the minimum squares needed for i-j*j, plus 1 more square j*j)

**Time Complexity**: O(n * sqrt(n)) - For each value from 1 to n, we check all perfect squares up to sqrt(i).
**Space Complexity**: O(n) - We use a DP array of size n+1.

## Problem 3: Why DP Doesn't Work for Min Time to Reach Last Room
[Link to problem](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/description/)

### Explanation:
This problem cannot be solved efficiently using dynamic programming because it lacks **optimal substructure**. Here's why:

1. **The State Space is Too Complex**: 
   The state of this problem depends not only on the current room but also on the set of keys collected so far. This creates a state space that grows exponentially with the number of keys.

2. **Path Dependencies Matter**:
   The optimal path to the last room depends heavily on which keys you've collected along the way. This means that decisions made early in the path affect which paths are even available later.

3. **No Clear Recurrence Relation**:
   It's difficult to define a simple recurrence relation that relates the solution for a room to the solutions for other rooms because the accessibility of rooms changes based on which keys you have.

### Better Approach: Dijkstra's Algorithm

The problem is better modeled as a shortest path problem on a graph:
- Nodes represent states (room, set_of_keys_collected)
- Edges represent transitions between rooms with weights equal to the time taken
- We want to find the shortest path from (room 0, no keys) to (last room, any keys)

Dijkstra's algorithm efficiently finds the shortest path by:
1. Always exploring the path with the minimum time so far
2. Using a priority queue to select the next state to explore
3. Tracking visited states to avoid redundant work

This approach handles the changing state space (which keys we have) while guaranteeing we find the minimum time path.

## Problem 4: Count Square Submatrices with All Ones (Optional)
[Link to problem](https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/)

### Solution:
```cpp
class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int rows = matrix.size();
        if (rows == 0) return 0;
        int cols = matrix[0].size();
        
        int count = 0;
        
        // Use the matrix itself as the DP table
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // For cells in first row or column, keep their original values
                if (i == 0 || j == 0) {
                    count += matrix[i][j];
                } 
                // For other cells, if it's a 1, check the minimum of three adjacent cells
                else if (matrix[i][j] == 1) {
                    matrix[i][j] = min({matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]}) + 1;
                    count += matrix[i][j];
                }
            }
        }
        
        return count;
    }
};
```

### Explanation:
As suggested in the hint, we overwrite each "1" in the matrix to represent the size of the largest square that has that cell as its bottom-right corner.

1. **State Definition**: `matrix[i][j]` represents the side length of the largest square with bottom-right corner at (i,j).
2. **Recurrence Relation**: 
   - If the cell is 0, it remains 0
   - If the cell is 1: `matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1`
3. **Base Cases**: Values in the first row and first column remain unchanged.

The key insight is that a square of size k can exist at position (i,j) only if squares of size k-1 exist at positions (i-1,j), (i,j-1), and (i-1,j-1). We then add up all the values in the modified matrix to get the total count of squares.

**Time Complexity**: O(rows * cols) - We process each cell exactly once.
**Space Complexity**: O(1) additional space - We reuse the input matrix for our DP table.

## Problem 5: Minimum Cost for Tickets (Optional)
[Link to problem](https://leetcode.com/problems/minimum-cost-for-tickets/description/)

### Solution:
```cpp
class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        // Get the last travel day
        int lastDay = days.back();
        
        // Create a set of travel days for O(1) lookup
        unordered_set<int> travelDays(days.begin(), days.end());
        
        // DP array to store minimum cost up to each day
        vector<int> dp(lastDay + 1, 0);
        
        for (int day = 1; day <= lastDay; day++) {
            // If not a travel day, cost is same as previous day
            if (travelDays.find(day) == travelDays.end()) {
                dp[day] = dp[day - 1];
                continue;
            }
            
            // Consider all three pass options
            // 1-day pass
            int option1 = dp[day - 1] + costs[0];
            
            // 7-day pass
            int option2 = dp[max(0, day - 7)] + costs[1];
            
            // 30-day pass
            int option3 = dp[max(0, day - 30)] + costs[2];
            
            // Take the minimum of all three options
            dp[day] = min({option1, option2, option3});
        }
        
        return dp[lastDay];
    }
};
```

### Explanation:
This is a 1D dynamic programming problem where we calculate the minimum cost to cover travel days up to each day:

1. **State Definition**: `dp[i]` represents the minimum cost to cover all travel days up to day i.
2. **Recurrence Relation**: 
   - If day i is not a travel day: `dp[i] = dp[i-1]`
   - If day i is a travel day: `dp[i] = min(dp[i-1] + costs[0], dp[i-7] + costs[1], dp[i-30] + costs[2])`
3. **Base Case**: `dp[0] = 0` (no cost for day 0).

For each travel day, we have three options:
1. Buy a 1-day pass for that day
2. Buy a 7-day pass covering that day (and potentially future days)
3. Buy a 30-day pass covering that day (and potentially future days)

We choose the option that minimizes the total cost.

**Time Complexity**: O(lastDay) - We process each day from 1 to the last travel day once.
**Space Complexity**: O(lastDay) - We use a DP array of size lastDay+1.

## Final Exam Application
These dynamic programming problems directly relate to what you might see on your final exam:

1. **1D and 2D DP Patterns**: Problems 1, 2, 4, and 5 cover both 1D and 2D dynamic programming approaches.

2. **DP vs. Other Algorithms**: Problem 3 helps you understand when DP is not appropriate and how to recognize when graph algorithms are better suited.

3. **State Design and Recurrence Relations**: Each problem requires defining clear states and formulating recurrence relations, which is a crucial skill for algorithm design questions.

4. **Time and Space Complexity Analysis**: Understanding the complexity of DP solutions will be essential for the exam.

For your final exam preparation, make sure you understand:
- How to identify problems suitable for dynamic programming
- How to define appropriate states and recurrence relations
- How to implement both 1D and 2D dynamic programming solutions
- How to analyze the time and space complexity of your solutions
