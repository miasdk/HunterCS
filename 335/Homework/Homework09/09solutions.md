# CSCI 335 Dynamic Programming Homework Solutions

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

### Detailed Explanation:
This is a 2D dynamic programming problem where each element is determined by the sum of two elements from the previous row.

#### Key C++ Methods Used:
- **`vector<vector<int>> result(numRows)`**: Creates a 2D vector with `numRows` rows. Initially, these rows are empty vectors.
- **`result[i].resize(i + 1)`**: The `resize()` method changes the size of the vector to the specified number of elements. If the new size is larger, new elements are added and initialized with their default value (0 for integers). This method is essential here because each row in Pascal's Triangle has a different number of elements.

#### Dynamic Programming Approach:
1. **State Definition**: `result[i][j]` represents the value at row i, column j in Pascal's Triangle.
2. **Recurrence Relation**: `result[i][j] = result[i-1][j-1] + result[i-1][j]` for 0 < j < i.
3. **Base Cases**: The first and last elements of each row are 1.

#### Step-by-step Execution:
Let's trace through the algorithm for `numRows = 5`:

1. Initialize `result` as a vector of 5 empty vectors
2. **Row 0**:
   - Resize to length 1: `result[0] = []` → `result[0] = [0]`
   - Set first (and last) element to 1: `result[0] = [1]`
3. **Row 1**:
   - Resize to length 2: `result[1] = []` → `result[1] = [0, 0]`
   - Set first and last elements to 1: `result[1] = [1, 1]`
4. **Row 2**:
   - Resize to length 3: `result[2] = []` → `result[2] = [0, 0, 0]`
   - Set first and last elements to 1: `result[2] = [1, 0, 1]`
   - Calculate middle elements:
     - `result[2][1] = result[1][0] + result[1][1] = 1 + 1 = 2`
   - Final row: `result[2] = [1, 2, 1]`
5. **Row 3**:
   - Resize to length 4: `result[3] = []` → `result[3] = [0, 0, 0, 0]`
   - Set first and last elements to 1: `result[3] = [1, 0, 0, 1]`
   - Calculate middle elements:
     - `result[3][1] = result[2][0] + result[2][1] = 1 + 2 = 3`
     - `result[3][2] = result[2][1] + result[2][2] = 2 + 1 = 3`
   - Final row: `result[3] = [1, 3, 3, 1]`
6. **Row 4**:
   - Resize to length 5: `result[4] = []` → `result[4] = [0, 0, 0, 0, 0]`
   - Set first and last elements to 1: `result[4] = [1, 0, 0, 0, 1]`
   - Calculate middle elements:
     - `result[4][1] = result[3][0] + result[3][1] = 1 + 3 = 4`
     - `result[4][2] = result[3][1] + result[3][2] = 3 + 3 = 6`
     - `result[4][3] = result[3][2] + result[3][3] = 3 + 1 = 4`
   - Final row: `result[4] = [1, 4, 6, 4, 1]`

Final output: `[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]`

**Time Complexity**: O(numRows²)
- We process each cell in the triangle once
- Number of cells: 1 + 2 + 3 + ... + numRows = numRows(numRows+1)/2 → O(numRows²)

**Space Complexity**: O(numRows²)
- We store all cells in the triangle, which is numRows(numRows+1)/2 elements → O(numRows²)

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

### Detailed Explanation:
This is a 1D dynamic programming problem where we calculate the minimum number of perfect squares needed for each value from 1 to n.

#### Key C++ Methods Used:
- **`vector<int> dp(n + 1, INT_MAX)`**: Creates a vector of size n+1 with all elements initialized to INT_MAX (a very large integer value). This initialization is important because we'll be taking the minimum in our DP relation.
- **`min(dp[i], dp[i - j*j] + 1)`**: The `min()` function returns the smaller of the two values. We use this to choose the option that minimizes the number of squares needed.
- **`INT_MAX`**: A constant representing the maximum value of an integer. We use it as an initial value because we want to find the minimum number of squares.

#### Dynamic Programming Approach:
1. **State Definition**: `dp[i]` represents the minimum number of perfect squares that sum to i.
2. **Recurrence Relation**: `dp[i] = min(dp[i], dp[i - j*j] + 1)` for all j where j*j ≤ i.
3. **Base Case**: `dp[0] = 0` (it takes 0 perfect squares to sum to 0).

#### Step-by-step Execution:
Let's trace through the algorithm for `n = 12`:

1. Initialize `dp` as `[0, INT_MAX, INT_MAX, ..., INT_MAX]` of length 13

2. Processing each number from 1 to 12:
   - **i = 1**:
     - j = 1: 1² = 1 ≤ 1, so `dp[1] = min(INT_MAX, dp[0] + 1) = min(INT_MAX, 0 + 1) = 1`
     - Final: `dp[1] = 1` (using 1²)
   
   - **i = 2**:
     - j = 1: 1² = 1 ≤ 2, so `dp[2] = min(INT_MAX, dp[1] + 1) = min(INT_MAX, 1 + 1) = 2`
     - Final: `dp[2] = 2` (using 1² + 1²)
   
   - **i = 3**:
     - j = 1: 1² = 1 ≤ 3, so `dp[3] = min(INT_MAX, dp[2] + 1) = min(INT_MAX, 2 + 1) = 3`
     - Final: `dp[3] = 3` (using 1² + 1² + 1²)
   
   - **i = 4**:
     - j = 1: 1² = 1 ≤ 4, so `dp[4] = min(INT_MAX, dp[3] + 1) = min(INT_MAX, 3 + 1) = 4`
     - j = 2: 2² = 4 ≤ 4, so `dp[4] = min(4, dp[0] + 1) = min(4, 0 + 1) = 1`
     - Final: `dp[4] = 1` (using 2²)
   
   - **i = 5**:
     - j = 1: 1² = 1 ≤ 5, so `dp[5] = min(INT_MAX, dp[4] + 1) = min(INT_MAX, 1 + 1) = 2`
     - j = 2: 2² = 4 ≤ 5, so `dp[5] = min(2, dp[1] + 1) = min(2, 1 + 1) = 2`
     - Final: `dp[5] = 2` (using 1² + 2²)
   
   - Continue this process for i = 6 to 12...
   
   - **i = 12**:
     - j = 1: 1² = 1 ≤ 12, so consider dp[11] + 1
     - j = 2: 2² = 4 ≤ 12, so consider dp[8] + 1
     - j = 3: 3² = 9 ≤ 12, so consider dp[3] + 1
     - Final: `dp[12] = 3` (using 2² + 2² + 2² or 3² + 3 * 1²)

3. Return `dp[12]` = 3

**Time Complexity**: O(n * sqrt(n))
- For each value i from 1 to n, we check all perfect squares up to sqrt(i)
- Number of operations: Σ(sqrt(i)) for i from 1 to n ≈ n * sqrt(n)

**Space Complexity**: O(n)
- We use a DP array of size n+1 to store intermediate results

## Problem 3: Why DP Doesn't Work for Min Time to Reach Last Room
[Link to problem](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/description/)

### Explanation:
This problem cannot be solved efficiently using dynamic programming because it lacks **optimal substructure**. Here's a detailed explanation:

#### Why DP Isn't Suitable:
1. **The State Space is Too Complex**: 
   The state of this problem depends not only on the current room but also on the set of keys collected so far. This creates a state space that grows exponentially with the number of keys (2^k possibilities for k keys).

2. **Path Dependencies Matter**:
   The optimal path to reach any room changes based on which keys you have. For example, the fastest path to room 5 without key 2 might be completely different from the fastest path to room 5 with key 2, because having key 2 might allow you to take shortcuts through locked rooms.

3. **No Clear Subproblem Definition**:
   In dynamic programming, we need to define subproblems whose solutions can be combined to solve the original problem. Here, it's difficult to define a subproblem that doesn't depend on the entire path history (in terms of which keys were collected).

4. **Violation of Optimal Substructure**:
   A problem has optimal substructure if an optimal solution contains optimal solutions to its subproblems. In this case, the optimal path to the last room may involve taking a non-optimal path to an intermediate room specifically to collect a key, which violates this principle.

#### Better Approach: Dijkstra's Algorithm

The problem is better modeled as a shortest path problem in a graph:

```cpp
// Pseudocode for Dijkstra's approach
int findMinimumTime(vector<Room>& rooms) {
    // Priority queue sorts by minimum time first
    // Each state is represented as (time, room_id, bitmask_of_keys)
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> pq;
    
    // Start at room 0 with no keys and 0 time
    pq.push({0, 0, 0});
    
    // Set to keep track of visited states
    set<pair<int, int>> visited; // (room_id, keys_bitmask)
    
    while (!pq.empty()) {
        auto [time, room, keys] = pq.top();
        pq.pop();
        
        // If we've reached the last room, return the time
        if (room == rooms.size() - 1) {
            return time;
        }
        
        // Skip if we've already visited this state
        if (visited.count({room, keys})) {
            continue;
        }
        visited.insert({room, keys});
        
        // Collect any keys in the current room
        int newKeys = keys;
        if (rooms[room].hasKey) {
            newKeys |= (1 << rooms[room].keyId); // Set the bit for this key
        }
        
        // Try to go to each connected room
        for (auto& [nextRoom, nextTime] : rooms[room].connections) {
            // Check if we can unlock the door
            if (rooms[nextRoom].requiresKey && !(newKeys & (1 << rooms[nextRoom].keyId))) {
                continue; // Skip this room if we don't have the required key
            }
            
            // Add next state to priority queue
            pq.push({time + nextTime, nextRoom, newKeys});
        }
    }
    
    return -1; // No path found
}
```

#### Key Concepts in the Dijkstra Implementation:
- **State Representation**: Each state is a tuple (time, room_id, keys) where keys is a bitmask representing which keys we have collected.
- **Priority Queue**: We use a min-priority queue to always explore the path with the smallest time first, guaranteeing that when we first reach the last room, it will be via the shortest path.
- **Visited Set**: We track visited states to avoid exploring the same state multiple times.
- **Bitmask for Keys**: We use a bitmask (an integer where each bit represents whether we have a specific key) for efficient state representation and key checking.

This approach efficiently handles the changing nature of the problem (state space depends on keys collected) while guaranteeing we find the minimum time path.

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

### Detailed Explanation:
This problem asks for the count of all square submatrices with all ones. We use dynamic programming to solve it efficiently.

#### Key C++ Methods Used:
- **`min({a, b, c})`**: This function returns the minimum value among the arguments provided. The curly braces `{}` create an initializer list, allowing us to pass multiple values to the `min` function. This is more concise than nesting multiple calls to the two-argument version of `min`.
- **In-place Modification**: We use the input matrix itself as our DP table to save space. This technique is common in dynamic programming when the original values are no longer needed after they've been processed.

#### Dynamic Programming Approach:
1. **State Definition**: `matrix[i][j]` represents the side length of the largest square with bottom-right corner at (i,j).
2. **Recurrence Relation**: 
   - If the cell is 0, it remains 0
   - If the cell is 1: `matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1`
3. **Base Cases**: Values in the first row and first column remain unchanged.

#### Step-by-step Execution:
Let's trace through the algorithm for the matrix:
```
1 1 1
1 1 1
1 1 1
```

1. Process each cell in order:
   - **First row** (i=0):
     - (0,0): Base case, keeps value 1, count += 1
     - (0,1): Base case, keeps value 1, count += 1
     - (0,2): Base case, keeps value 1, count += 1
   - **Second row** (i=1):
     - (1,0): Base case, keeps value 1, count += 1
     - (1,1): Check min(1,1,1)+1 = 2, update to 2, count += 2
     - (1,2): Check min(1,1,2)+1 = 2, update to 2, count += 2
   - **Third row** (i=2):
     - (2,0): Base case, keeps value 1, count += 1
     - (2,1): Check min(1,2,1)+1 = 2, update to 2, count += 2
     - (2,2): Check min(2,2,2)+1 = 3, update to 3, count += 3

2. Matrix after processing:
   ```
   1 1 1
   1 2 2
   1 2 3
   ```

3. Total count = 1+1+1+1+2+2+1+2+3 = 14

The count represents all possible squares:
- 9 squares of size 1×1
- 4 squares of size 2×2
- 1 square of size 3×3

#### Explanation of the Recurrence Relation:
For a square of side length k with bottom-right corner at (i,j), there must be squares of side length k-1 with bottom-right corners at:
- (i-1,j): The cell above
- (i,j-1): The cell to the left
- (i-1,j-1): The cell diagonally above-left

If any of these squares has a smaller size (e.g., due to a 0 somewhere), the largest square at (i,j) is limited by that smaller size.

**Time Complexity**: O(rows * cols)
- We process each cell exactly once

**Space Complexity**: O(1) additional space
- We reuse the input matrix for our DP table

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

### Detailed Explanation:
This problem asks for the minimum cost to cover all travel days using various duration passes.

#### Key C++ Methods Used:
- **`unordered_set<int> travelDays(days.begin(), days.end())`**: Creates a hash set from the contents of the `days` vector. This allows O(1) lookup to check if a given day is a travel day.
- **`days.back()`**: Returns the last element of the vector, which is the last travel day.
- **`travelDays.find(day) == travelDays.end()`**: Checks if `day` is not in the set. The `end()` method returns an iterator to the position after the last element, which is used to indicate "not found".
- **`max(0, day - 7)`**: Returns the larger of 0 or day-7. This ensures we don't access negative indices in our DP array.
- **`min({a, b, c})`**: Returns the minimum of the three values, using an initializer list.

#### Dynamic Programming Approach:
1. **State Definition**: `dp[i]` represents the minimum cost to cover all travel days up to day i.
2. **Recurrence Relation**: 
   - If day i is not a travel day: `dp[i] = dp[i-1]`
   - If day i is a travel day: `dp[i] = min(dp[i-1] + costs[0], dp[i-7] + costs[1], dp[i-30] + costs[2])`
3. **Base Case**: `dp[0] = 0` (no cost for day 0).

#### Step-by-step Execution:
Let's trace through the algorithm for `days = [1,4,6,7,8,20]` and `costs = [2,7,15]`:

1. Initialize `dp` as `[0, 0, 0, ..., 0]` of length 21
2. Initialize `travelDays` set as `{1, 4, 6, 7, 8, 20}`

3. Processing each day from 1 to 20:
   - **Day 1** (travel day):
     - option1 = dp[0] + costs[0] = 0 + 2 = 2 (1-day pass)
     - option2 = dp[max(0, 1-7)] + costs[1] = dp[0] + 7 = 0 + 7 = 7 (7-day pass)
     - option3 = dp[max(0, 1-30)] + costs[2] = dp[0] + 15 = 0 + 15 = 15 (30-day pass)
     - dp[1] = min(2, 7, 15) = 2
   
   - **Day 2** (not a travel day):
     - dp[2] = dp[1] = 2
   
   - **Day 3** (not a travel day):
     - dp[3] = dp[2] = 2
   
   - **Day 4** (travel day):
     - option1 = dp[3] + costs[0] = 2 + 2 = 4 (1-day pass)
     - option2 = dp[max(0, 4-7)] + costs[1] = dp[0] + 7 = 0 + 7 = 7 (7-day pass)
     - option3 = dp[max(0, 4-30)] + costs[2] = dp[0] + 15 = 0 + 15 = 15 (30-day pass)
     - dp[4] = min(4, 7, 15) = 4
   
   - **Day 5** (not a travel day):
     - dp[5] = dp[4] = 4
   
   - **Day 6** (travel day):
     - option1 = dp[5] + costs[0] = 4 + 2 = 6 (1-day pass)
     - option2 = dp[max(0, 6-7)] + costs[1] = dp[0] + 7 = 0 + 7 = 7 (7-day pass)
     - option3 = dp[max(0, 6-30)] + costs[2] = dp[0] + 15 = 0 + 15 = 15 (30-day pass)
     - dp[6] = min(6, 7, 15) = 6
   
   - **Day 7** (travel day):
     - option1 = dp[6] + costs[0] = 6 + 2 = 8 (1-day pass)
     - option2 = dp[max(0, 7-7)] + costs[1] = dp[0] + 7 = 0 + 7 = 7 (7-day pass)
     - option3 = dp[max(0, 7-30)] + costs[2] = dp[0] + 15 = 0 + 15 = 15 (30-day pass)
     - dp[7] = min(8, 7, 15) = 7
   
   - **Day 8** (travel day):
     - option1 = dp[7] + costs[0] = 7 + 2 = 9 (1-day pass)
     - option2 = dp[max(0, 8-7)] + costs[1] = dp[1] + 7 = 2 + 7 = 9 (7-day pass)
     - option3 = dp[max(0, 8-30)] + costs[2] = dp[0] + 15 = 0 + 15 = 15 (30-day pass)
     - dp[8] = min(9, 9, 15) = 9
   
   - **Days 9-19** (not travel days):
     - dp[9] = dp[8] = 9
     - ...
     - dp[19] = dp[8] = 9
   
   - **Day 20** (travel day):
     - option1 = dp[19] + costs[0] = 9 + 2 = 11 (1-day pass)
     - option2 = dp[max(0, 20-7)] + costs[1] = dp[13] + 7 = 9 + 7 = 16 (7-day pass)
     - option3 = dp[max(0, 20-30)] + costs[2] = dp[0] + 15 = 0 + 15 = 15 (30-day pass)
     - dp[20] = min(11, 16, 15) = 11

4. Return `dp[20]` = 11

#### Explanation of Decision Making:
- For day 1, a 1-day pass is cheapest
- For days 4-6, individual 1-day passes are still optimal
- For day 7, a new 7-day pass becomes optimal (covers days 7-13)
- For day 8, extending with a 1-day pass is tied with a 7-day pass
- For day 20, a 1-day pass is cheapest because the previous cost is already 9

**Time Complexity**: O(lastDay)
- We process each day from 1 to the last travel day once

**Space Complexity**: O(lastDay)
- We use a DP array of size lastDay+1 to store intermediate results

## Final Exam Application
These dynamic programming problems directly relate to what you might see on your final exam:

### 1. Types of DP Problems Covered:
- **1D DP**: Problems 2 and 5 demonstrate DP with a one-dimensional array
- **2D DP**: Problems 1 and 4 show DP with a two-dimensional structure
- **When DP Doesn't Apply**: Problem 3 teaches how to recognize when a different algorithm is more appropriate

### 2. Key DP Concepts Demonstrated:
- **State Definition**: Each problem requires carefully defining what the DP states represent
- **Recurrence Relations**: Formulating the mathematical relationship between states
- **Base Cases**: Identifying the starting points for the DP computation
- **Computation Order**: Determining the correct sequence to fill the DP table
- **Space Optimization**: Problem 4 demonstrates in-place DP to save space

### 3. Problem-Solving Strategies:
- **Breaking down problems**: Reducing complex problems into simpler subproblems
- **Recognizing patterns**: Identifying common DP patterns (grid traversal, counting, minimization)
- **Implementation techniques**: Using appropriate data structures (vectors, sets)
- **Time/space analysis**: Understanding the complexity of different approaches

### 4. Key Methods and Data Structures:
- **Vectors**: `vector<int>`, `vector<vector<int>>`
- **Sets**: `unordered_set<int>`
- **Utility Functions**: `min()`, `max()`
- **Vector Methods**: `resize()`, `back()`
- **STL Constants**: `INT_MAX`

### Study Recommendations for Final:
1. **Practice Identifying DP Problems**: Recognize when a problem can be solved with DP
2. **Develop a Systematic Approach**:
   - Define the state
   - Formulate the recurrence relation
   - Identify base cases
   - Determine computation order
3. **Implement Efficiently**: Pay attention to initialization and edge cases
4. **Analyze Complexity**: Be prepared to calculate time and space complexity
5. **Understand Limitations**: Know when DP is not appropriate (Problem 3)

The skills developed in these problems will be essential for the algorithm design/analysis and coding questions on your final exam, which together make up about half of the exam content.
/problems/pascals-triangle/description/)

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
