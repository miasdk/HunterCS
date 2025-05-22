# Detailed Walkthrough of Key Exam Problems

Based on the exams you've shared, I'll work through some of the most important and commonly tested problems with step-by-step solutions. This will help you understand how to approach each type of question.

## Table of Contents

### Algorithm Tracing & Step-by-Step Solutions
1. [Dijkstra's Algorithm](#1-dijkstras-algorithm)
2. [Prim's Algorithm Analysis](#2-prims-algorithm-analysis)
3. [Time Complexity Analysis](#3-time-complexity-analysis)
4. [Kruskal's Algorithm Trace](#7-kruskals-algorithm-trace)

### Data Structure Properties & Theory
5. [AVL Tree Properties](#4-avl-tree-properties)
6. [Binary Heap Properties](#5-binary-heap-properties)
7. [BuildHeap Analysis](#9-buildheap-analysis)

### Coding & Implementation
8. [Asymmetric List Difference](#6-asymmetric-list-difference)
9. [2D Dynamic Programming: Grid Paths with Obstacles](#8-2d-dynamic-programming-grid-paths-with-obstacles)
10. [Lower Bound Raffle Problem](#10-lower-bound-raffle-problem)
11. [C++ STL Search vs. Lookup](#11-c-stl-search-vs-lookup)
12. [Partial Sorting (Top 10%)](#12-partial-sorting-top-10)

### Core Algorithm Implementation
13. [BuildHeap Implementation and percDown Function](#13-buildheap-implementation-and-percdown-function)
14. [Grid Path Counting with Dynamic Programming](#14-grid-path-counting-with-dynamic-programming)

### Sample Exam Questions
15. [Sample Exam Questions (Based on Actual Course Materials)](#15-sample-exam-questions-based-on-actual-course-materials)
    - Sample Question 1: Coding - Implement percDown
    - Sample Question 2: Algorithm Analysis - Dijkstra's Complexity
    - Sample Question 3: Algorithm Trace - Prim's Algorithm
    - Sample Question 4: Knowledge - AVL Tree Balance Condition

## 1. Dijkstra's Algorithm

This problem appears consistently on exams, and students tend to perform well on it (like the 10/10 score on Exam C).

### Problem:
Compute the shortest path from vertex 1 to vertex 5 using Dijkstra's algorithm. Show each step.

### Solution Approach:

**Step 1: Initialize**
- Create distance table with rows for each vertex
- Set distance of source vertex to 0, all others to ∞
- Mark all vertices as unknown (F = false)
- Initialize predecessor pointers to 0 or null

For example, if starting from vertex 1:
```
v | known | d_v | p_v
-------------------------
1 |   F    |  0  |  0
2 |   F    |  ∞  |  0
3 |   F    |  ∞  |  0
4 |   F    |  ∞  |  0
5 |   F    |  ∞  |  0
```

**Step 2: Main Loop**
- Select the unknown vertex with the smallest distance value (initially the source)
- Mark it as known
- Update distances to all adjacent vertices:
  - For each adjacent vertex v, if distance[current] + edge_weight < distance[v], update distance[v] and set predecessor[v] = current
- Repeat until destination is known or all vertices are known

**Step 3: Extract Path**
- After the algorithm completes, follow predecessor pointers from destination back to source

### Common Mistakes:
- Not updating distance values correctly
- Selecting the wrong vertex as the next "known" vertex
- Not updating predecessor pointers
- Stopping too early or continuing unnecessarily

### Tips:
- Carefully track the state of all tables at each step
- Double-check all calculations and vertex selections
- Make sure you stop when the destination vertex is marked as known (if you only need the path to a specific vertex)

## 2. Prim's Algorithm Analysis

This is a theoretical analysis question that appeared in multiple exams.

### Key Points to Explain:

**1. Overall Complexity: O(|E| log |V|) with binary heaps**
- Explain why: Each edge operation costs O(log |V|) with a binary heap
- Each vertex is extracted from the heap once: O(|V| log |V|)
- Each edge may cause a decrease-key operation: O(|E| log |V|)
- Overall: O(|E| log |V|) since |E| ≥ |V|-1 for a connected graph

**2. Data Structures**
- Adjacency list representation for the graph
- Priority queue (binary heap) to find minimum-weight edge
- Set of visited/unvisited vertices

**3. Key Operations**
- Extract minimum from the heap: O(log |V|)
- Decrease key operations: O(log |V|)
- Adding edges to the heap: O(log |V|)

**4. Comparison with Non-Heap Implementation**
- Without a heap: O(|V|²) because finding the min edge is O(|V|)
- Better for dense graphs where |E| approaches |V|²
- Heap implementation better for sparse graphs

**5. Why O(|E| log |V|) and not O(|E| log |E|)**?
- Since |E| is at most |V|², log |E| ≤ 2 log |V|
- Therefore, O(|E| log |E|) = O(|E| log |V|)

### Example Explanation:
"Prim's algorithm using binary heaps has a time complexity of O(|E| log |V|). We use an adjacency list to represent the graph and a binary heap to efficiently find the next closest vertex to add to our MST. Starting from any vertex, we add all edges from that vertex to our heap. Then we repeatedly extract the minimum-weight edge that connects a vertex not in our MST, add that vertex to our MST, and add all new edges from that vertex to the heap. Each extraction takes O(log |V|) time. Each edge might cause a decrease-key operation, also taking O(log |V|) time. Since we process each vertex once and potentially every edge, the total complexity is O(|V| log |V| + |E| log |V|) = O(|E| log |V|) since |E| ≥ |V| for a connected graph."

## 3. Time Complexity Analysis

This is a fundamental question type that typically asks for the Big-O complexity of various operations.

### Key Complexities to Memorize:

**Data Structure Operations:**
- **Hash Table:** 
  - Insert/Delete/Find: O(1) average, O(n) worst-case
  - Find max/min: O(n)

- **Binary Heap:**
  - Insert: O(log n)
  - Delete Min/Max: O(log n)
  - BuildHeap: O(n)

- **AVL Tree/Red-Black Tree:**
  - Insert/Delete/Find: O(log n)

- **Unordered Array:**
  - Search: O(n)
  - Insert (at end): O(1)
  - Delete: O(n)

**Algorithm Complexities:**
- **Dijkstra's Algorithm:**
  - With array: O(|V|²)
  - With binary heap: O(|E| log |V|)

- **Prim's Algorithm:**
  - With array: O(|V|²)
  - With binary heap: O(|E| log |V|)

- **Kruskal's Algorithm:** O(|E| log |E|) or O(|E| log |V|)
  
- **Topological Sort:** O(|V| + |E|)
  
- **Unweighted Shortest Path (BFS):** O(|V| + |E|)

- **Sorting Algorithms:**
  - Quicksort: O(n log n) average, O(n²) worst-case
  - Mergesort: O(n log n) worst-case
  - Heapsort: O(n log n) worst-case
  - Quickselect: O(n) average, O(n²) worst-case

### Example Analysis:
For "Delete Min in a min heap (worst case)" → O(log n)
Explanation: Removing the minimum element requires replacing the root with the last element and then percolating down. The percolation may need to go all the way down to a leaf, which takes O(log n) time in the worst case.

## 4. 2D Dynamic Programming: Grid Paths with Obstacles

This is a classic DP problem that appeared in Exam C (Question 8) and tests your understanding of DP principles.

### Problem:
Find the number of paths from the top-left to bottom-right of an n×m grid, moving either down or right each time, with an obstacle at position (x,y).

### Solution Approach:

**Step 1: Setup the DP Table**
```cpp
int paths(int n, int m, int x, int y) {
    // Create a 2D DP array
    vector<vector<int>> grid(n, vector<int>(m, 0));
    
    // Set the obstacle
    grid[x][y] = -1;
    
    // Initialize first column and row
    for (int i = 0; i < n && grid[i][0] != -1; i++) {
        grid[i][0] = 1;
    }
    for (int j = 0; j < m && grid[0][j] != -1; j++) {
        grid[0][j] = 1;
    }
    
    // If obstacle is in first row/column, cells after it are unreachable
    if (x == 0) {
        for (int j = y + 1; j < m; j++) {
            grid[0][j] = 0;
        }
    }
    if (y == 0) {
        for (int i = x + 1; i < n; i++) {
            grid[i][0] = 0;
        }
    }
```

**Step 2: Fill the DP Table**
```cpp
    // Fill the rest of the grid
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
            if (grid[i][j] == -1) {
                grid[i][j] = 0;  // Cannot pass through obstacle
            } else {
                // Paths = paths from above + paths from left
                grid[i][j] = (grid[i-1][j] > 0 ? grid[i-1][j] : 0) + 
                             (grid[i][j-1] > 0 ? grid[i][j-1] : 0);
            }
        }
    }
    
    // Return the answer (paths to bottom-right)
    return grid[n-1][m-1];
}
```

### Key Insights:
- The recurrence relation is dp[i][j] = dp[i-1][j] + dp[i][j-1] for cells without obstacles
- Cells with obstacles have 0 paths
- Cells after an obstacle in the first row or column are unreachable if you can only move right or down
- This problem tests both DP understanding and careful handling of edge cases

## 5. BuildHeap Analysis

This theoretical question about why BuildHeap is O(n) despite calling an O(log n) operation n times is a common sticking point.

### Key Insight:
The time complexity of BuildHeap is O(n), not O(n log n) as might be initially expected.

### Explanation:
The critical insight is that not all percolate-down operations take the full O(log n) time:

1. **Height Distribution**:
   - In a binary heap with n nodes, approximately n/2 nodes are leaves (height 0)
   - Approximately n/4 nodes have height 1
   - Approximately n/8 nodes have height 2
   - And so on...

2. **Work Per Node**:
   - A node at height h requires at most h operations to percolate down
   - Leaves (height 0) require 0 operations
   - Nodes at height 1 require at most 1 operation
   - Nodes at height 2 require at most 2 operations
   - And so on...

3. **Total Work**:
   - Total work = (n/4 × 1) + (n/8 × 2) + (n/16 × 3) + ...
   - This sum converges to approximately 2n operations
   - Therefore, the time complexity is O(n)

### Mathematical Proof:
```
Total work = ∑(h=0 to log n) (n/2^(h+1) × h)
           = n × ∑(h=0 to log n) (h/2^(h+1))
           = n × ∑(h=0 to log n) (h/2 × 1/2^h)
           = n/2 × ∑(h=0 to log n) (h/2^h)
```

This sum converges to a constant, so the complexity is O(n).

## 6. Lower Bound Raffle Problem

This problem from Exam C (Question 10) tests your understanding of ordered containers and binary search.

### Problem:
In a raffle with n players choosing numbers from 1 to n², and m prizes where each prize has a random number drawn, find the winner for each prize efficiently.

### Solution Approach:

**Step 1: Store Player Numbers in an Ordered Set**
```cpp
// Store player numbers in an ordered container
set<int> playerNumbers;
for (int num : playerChoices) {
    playerNumbers.insert(num);
}
```

**Step 2: Find Winner for Each Prize**
```cpp
vector<int> findWinners(vector<int>& prizeNumbers) {
    vector<int> winners;
    for (int prizeNumber : prizeNumbers) {
        // Find the smallest number >= prizeNumber
        auto it = playerNumbers.lower_bound(prizeNumber);
        
        // If no such number exists, wrap around to the smallest number
        if (it == playerNumbers.end()) {
            it = playerNumbers.begin();
        }
        
        winners.push_back(*it);
    }
    return winners;
}
```

### Time Complexity:
- Building the set: O(n log n)
- Finding each winner: O(log n)
- Overall: O(n log n + m log n)

### Key Points:
- Use `lower_bound` for the "next greater or equal" operation
- Handle wrap-around case when no greater number exists
- This problem tests understanding of BST operations and efficiency

## 7. Kruskal's Algorithm Trace

This problem appeared in multiple exams and tests your ability to trace through Kruskal's algorithm for finding a minimum spanning tree.

### Solution Process:

**Step 1: Sort all edges by weight**
Create a list of all edges with their weights, sorted from smallest to largest.

**Step 2: Initialize the algorithm**
- Create a disjoint-set data structure for all vertices
- Initialize an empty MST

**Step 3: Process edges in order**
For each edge (u,v) with weight w:
- If adding (u,v) doesn't create a cycle in the MST:
  - Add (u,v) to the MST
  - Union the sets containing u and v
- Else:
  - Reject this edge
- Stop when |V|-1 edges have been added to the MST

**Step 4: Return the MST**

### Example Trace (Using the graph from Exam C):
1. Edge (3,4) with weight 1: Accept (no cycle)
2. Edge (1,4) with weight 2: Accept (no cycle)
3. Edge (6,7) with weight 2: Accept (no cycle)
4. Edge (1,2) with weight 3: Reject (would create a cycle)
5. Edge (3,7) with weight 3: Accept (no cycle)
6. Edge (4,7) with weight 4: Reject (would create a cycle)
7. Edge (2,3) with weight 5: Reject (would create a cycle)
8. Edge (4,6) with weight 5: Reject (would create a cycle)
9. Edge (1,5) with weight 6: Accept (no cycle)
10. MST is complete with 5 edges

### Key Points:
- Always process edges in order of increasing weight
- Use a Union-Find data structure to efficiently detect cycles
- Stop when |V|-1 edges have been added
- The MST is guaranteed to be minimum weight

## 8. Asymmetric List Difference

This problem tests your understanding of hash tables for efficient lookup.

### Problem:
Given two lists of guests (RSVP list and attendance list), find all guests who showed up without RSVPing.

### Solution:
```cpp
void printUninvited(const list<string>& rsvped, const list<string>& showed) {
    // Step 1: Insert all RSVP names into a hash set for O(1) lookup
    unordered_set<string> rsvpSet;
    for (const auto& name : rsvped) {
        rsvpSet.insert(name);
    }
    
    // Step 2: Check each person who showed up
    for (const auto& name : showed) {
        // If they're not in the RSVP set, they showed up without RSVPing
        if (rsvpSet.find(name) == rsvpSet.end()) {
            cout << name << endl;
        }
    }
}
```

### Key Points:
- Hash set provides O(1) lookup time
- Overall time complexity is O(n) where n is the total number of names
- Using ordered containers would result in O(n log n) time complexity
- Using nested loops would result in O(n²) time complexity

## 9. Partial Sorting (Top 10%)

This problem tests your understanding of sorting algorithms and how to optimize them for a specific use case.

### Problem:
Given a large list of test scores, efficiently find the top 10% without fully sorting the entire list.

### Solution Approach 1: Modified Heapsort
```cpp
vector<int> topTenPercent(vector<int>& scores) {
    int k = scores.size() / 10;  // Top 10%
    vector<int> result(k);
    
    // Create a min-heap of size k
    priority_queue<int, vector<int>, greater<int>> minHeap;
    
    // Insert first k elements
    for (int i = 0; i < k; i++) {
        minHeap.push(scores[i]);
    }
    
    // For each remaining element
    for (int i = k; i < scores.size(); i++) {
        // If current element is larger than the smallest in heap
        if (scores[i] > minHeap.top()) {
            minHeap.pop();          // Remove smallest
            minHeap.push(scores[i]); // Add current
        }
    }
    
    // Extract the k largest elements
    for (int i = k - 1; i >= 0; i--) {
        result[i] = minHeap.top();
        minHeap.pop();
    }
    
    return result;
}
```

### Solution Approach 2: Quickselect
```cpp
vector<int> topTenPercent(vector<int>& scores) {
    int k = scores.size() / 10;  // Top 10%
    
    // Use quickselect to find the kth largest element
    nth_element(scores.begin(), scores.begin() + k - 1, scores.end(), greater<int>());
    
    // Copy the k largest elements
    vector<int> result(scores.begin(), scores.begin() + k);
    
    // Sort them if needed
    sort(result.begin(), result.end(), greater<int>());
    
    return result;
}
```

### Complexity Analysis:
- Heap approach: O(n log k) where k is 10% of n
- Quickselect approach: O(n) average case
- Both are much better than full sorting: O(n log n)

### Key Points:
- The optimization relies on not sorting the entire list
- The top 10% is a small fraction of the list (k << n)
- Heapsort and quickselect are both suitable approaches
- std::nth_element is a built-in implementation of quickselect

## 10. C++ STL Search vs. Lookup

This conceptual question requires understanding the difference between operations in ordered and unordered STL containers.

### Key Differences:

1. **Underlying Data Structures**:
   - Ordered containers (map, set): Balanced binary search trees
   - Unordered containers (unordered_map, unordered_set): Hash tables

2. **Operation Complexity**:
   - Ordered containers:
     - find(): O(log n)
     - insert(): O(log n)
     - erase(): O(log n)
   - Unordered containers:
     - find(): O(1) average, O(n) worst case
     - insert(): O(1) average, O(n) worst case
     - erase(): O(1) average, O(n) worst case

3. **Element Organization**:
   - Ordered containers: Elements stored in sorted order
   - Unordered containers: Element order not guaranteed

4. **Additional Operations**:
   - Ordered containers: Support range queries and operations like lower_bound, upper_bound
   - Unordered containers: No range queries, but faster for single-element operations

### Example Explanation:
"The main difference between search and lookup operations in C++ STL containers is their underlying implementation and complexity. Set and map use balanced binary search trees, requiring a search operation with O(log n) complexity. In contrast, unordered_set and unordered_map use hash tables, enabling lookup operations with O(1) average time complexity. The term 'lookup' reflects the direct access nature of hash tables, while 'search' indicates the need to traverse the tree structure to find an element."

## 11. AVL Tree Properties

This conceptual question tests your understanding of AVL tree balance conditions.

### Key Properties:

1. **Binary Search Tree Property**:
   - For every node, all keys in its left subtree are less than the node's key
   - For every node, all keys in its right subtree are greater than the node's key

2. **Balance Condition**:
   - For every node, the heights of its left and right subtrees differ by at most 1
   - |height(left) - height(right)| ≤ 1

3. **Height Balance**:
   - The height of an AVL tree with n nodes is O(log n)
   - This guarantees O(log n) operations for insert, delete, and find

4. **Rebalancing Operations**:
   - Single rotations: LL, RR 
   - Double rotations: LR, RL
   - Performed when balance condition is violated after insert/delete

### Example Explanation:
"An AVL tree has two key properties: First, it is a binary search tree where for each node, all keys in the left subtree are smaller and all keys in the right subtree are larger. Second, it maintains the balance condition that for every node, the heights of its left and right subtrees differ by at most 1. This height-balance property ensures that operations like search, insert, and delete remain efficient with O(log n) time complexity."

## 12. Binary Heap Properties

This conceptual question tests your understanding of binary heap structure and ordering.

### Key Properties:

1. **Structure Property**:
   - A binary heap is a complete binary tree
   - All levels are filled except possibly the last level
   - The last level is filled from left to right

2. **Heap-Order Property**:
   - Min-heap: Every parent node has a value less than or equal to its children
   - Max-heap: Every parent node has a value greater than or equal to its children

3. **Indexing in Array Representation**:
   - For a node at index i:
     - Left child: 2i (or 2i+1 if using 0-based indexing)
     - Right child: 2i+1 (or 2i+2 if using 0-based indexing)
     - Parent: ⌊i/2⌋ (or ⌊(i-1)/2⌋ if using 0-based indexing)

4. **Key Operations**:
   - insert: O(log n)
   - deleteMin/deleteMax: O(log n)
   - findMin/findMax: O(1)
   - buildHeap: O(n)

### Example Explanation:
"A binary heap has two essential properties: First, it is a complete binary tree where all levels except possibly the last are completely filled, and the last level is filled from left to right. Second, it satisfies the heap-order property, which for a min-heap means each node's value is less than or equal to its children's values (or for a max-heap, greater than or equal). These properties enable efficient priority queue operations and form the basis for the heap sort algorithm."

## 13. BuildHeap Implementation and percDown Function

This coding question tests your ability to implement the BuildHeap algorithm and understand the percDown operation.

### percDown Function (Core Heap Operation):

The percDown function is fundamental to heap operations. It maintains the heap property by "percolating down" a value from a given position until it finds the correct location.

```cpp
void percDown(std::vector<int>& heap, std::vector<int>::size_type hole) {
    std::vector<int>::size_type child;
    // Each iteration moves the hole down one if required.
    // Exits loop when the hole is in place.
    for (; hole * 2 <= heap.size() - 1; hole = child) {
        child = hole * 2;
        if (child != heap.size() - 1 && heap[child + 1] < heap[child])
            ++child;
        if (heap[child] < heap[0])
            heap[hole] = heap[child];
        else
            break;
    }
    // Moves value to be inserted into hole
    heap[hole] = heap[0];
}
```

### How percDown Works:
1. **Input**: A heap array and a "hole" position that may violate the heap property
2. **Process**: 
   - The value to be placed is temporarily stored in heap[0]
   - Starting from the hole, compare with children
   - Move the smaller child up to the hole position
   - Continue down the tree until the correct position is found
3. **Output**: The value from heap[0] is placed in its final position

### Key Details:
- **Child calculation**: `child = hole * 2` (left child in 1-indexed heap)
- **Find smaller child**: Compare `heap[child]` and `heap[child + 1]`
- **Move up smaller child**: If `heap[child] < heap[0]`, move child to hole
- **Termination**: When heap[child] ≥ heap[0], we've found the right spot

### BuildHeap Implementation:
```cpp
void buildHeap(std::vector<int>& heap) {
    // Start from the last non-leaf node and work up to the root
    for (auto i = heap.size()/2; i > 0; --i) {
        // Save the value to be percolated
        heap[0] = heap[i];
        // Percolate down
        percDown(heap, i);
    }
}
```

### Time Complexity Analysis:
- **percDown**: O(log n) - may traverse from root to leaf
- **buildHeap**: O(n) - despite calling percDown n/2 times
- **Why buildHeap is O(n)**: Most nodes are near the bottom of the tree and don't move far

### Common Exam Applications:
1. **Heapsort**: Uses percDown for the "sift-down" operation after removing the root
2. **Priority Queue**: percDown maintains heap property after deleteMin
3. **BuildHeap**: Converts an unordered array into a heap efficiently

### Example Trace:
For array [10, 5, 3, 4, 1] becoming a min-heap:

```
Initial: [10, 5, 3, 4, 1]
After buildHeap: [1, 4, 3, 5, 10]

Step-by-step:
1. Start at position 2 (heap.size()/2): element 3
2. percDown(heap, 2): 3 is already smaller than its children
3. Move to position 1: element 5
4. percDown(heap, 1): 5 > 1, so 1 moves up, 5 moves down
```

### Key Points for Exams:
- BuildHeap starts from the middle of the array (last non-leaf node)
- Works backward toward the root  
- percDown is the core operation that maintains heap property
- The complexity is O(n) despite calling percDown (O(log n)) n/2 times
- This approach transforms an unordered array into a valid heap in-place
- Understanding percDown is essential for heapsort and priority queue operations

## 15. Sample Exam Questions (Based on Actual Course Materials)

These are representative questions that closely match the format and content of actual exam questions.

### Sample Question 1: Coding - Implement percDown

**Question**: Implement percDown. In this implementation, the heap starts at index 1, the value to be placed is in index 0, and the position of the hole is passed as a parameter. You are not permitted to use a temp variable for the value, it must remain in index 0 until the hole has been moved into its final position, and only then can it be placed in the hole.

```cpp
void percDown(std::vector<int>& heap, std::vector<int>::size_type hole) {
    // code here
}
```

**Solution**:
```cpp
void percDown(std::vector<int>& heap, std::vector<int>::size_type hole) {
    std::vector<int>::size_type child;
    
    // Each iteration moves the hole down one if required
    // Exits loop when the hole is in place
    for (; hole * 2 <= heap.size() - 1; hole = child) {
        child = hole * 2;  // Left child
        
        // Find smaller child (for min heap)
        if (child != heap.size() - 1 && heap[child + 1] < heap[child])
            ++child;  // Use right child instead
        
        // If child is smaller than value to be placed (heap[0])
        if (heap[child] < heap[0])
            heap[hole] = heap[child];  // Move child up to hole
        else
            break;  // Found correct position
    }
    
    // Place the value from index 0 into its final position
    heap[hole] = heap[0];
}
```

**Key Points**:
- Heap uses 1-based indexing (index 0 stores the temporary value)
- Left child of node i is at index 2*i
- Right child of node i is at index 2*i+1
- Always choose the smaller child to maintain min-heap property
- No temporary variables allowed - value stays in heap[0] until final placement

### Sample Question 2: Algorithm Analysis - Dijkstra's Complexity

**Question**: Analyze the complexity of Dijkstra's algorithm: 
a) using an update table and iterating through it each time you need to find the next shortest-path node, and 
b) keeping unvisited nodes in a min heap ordered by their dv (shortest known path). 
State and prove the complexity of each. Which is better for sparse graphs, and why?

**Solution**:

#### Part A: Update Table Implementation

**Complexity**: O(|V|²)

**Proof**:
- Finding the next node to visit requires iterating through the table to find the unvisited node with the shortest potential path: O(|V|)
- Marking that node as visited: O(1)
- Looking at all edges going out from the selected node and updating unvisited neighbors: O(1) per update with a lookup table
- Total iterations: |V| (one for each vertex)
- Most expensive operation per iteration: O(|V|) for finding the minimum
- Overall: |V| iterations × O(|V|) = O(|V|²)
- Additionally, examining all edges across all iterations: O(|E|) total
- Since |E| ≤ |V|², the O(|V|²) term dominates
- Using an adjacency matrix doesn't change the complexity since matrix traversal is also O(|V|²)

#### Part B: Min-Heap Implementation

**Complexity**: O(|E| log |V|)

**Proof**:
- Using a min heap reduces deleteMin time to O(log |V|) instead of O(|V|)
- However, heaps aren't efficient for modifying elements (decreaseKey is expensive)
- Solution: Push a new entry for each path discovery instead of updating existing entries
- This means the heap size becomes O(|E|) rather than O(|V|)
- We perform O(|E|) heap operations, each costing O(log |E|)
- Total complexity: O(|E| log |E|)
- Since |E| ≤ |V|², we have log |E| ≤ 2 log |V|, so O(|E| log |E|) = O(|E| log |V|)
- This approach requires an adjacency list (adjacency matrix would add O(|V|²) just for iteration)

#### Which is Better for Sparse Graphs?

**Min heaps are better for sparse graphs**.

**Reasoning**:
- In sparse graphs, |E| = O(|V|) (approximately linear in the number of vertices)
- Update table: O(|V|²)
- Min heap: O(|E| log |V|) = O(|V| log |V|) for sparse graphs
- Since log |V| grows much slower than |V|, O(|V| log |V|) < O(|V|²) for large graphs
- For dense graphs where |E| ≈ |V|², both approaches have similar performance, but the update table might be simpler to implement

### Sample Question 3: Algorithm Trace - Prim's Algorithm

**Question**: Given the following graph, draw out the partial minimum spanning tree as it would be after each step of Prim's algorithm:

```
        2
   v₁ ——————— v₂
4 / |    3     | \ 10
 /  |1         |7 \
v₃  |    2     |   v₅
 \  v₄ ——————— v₇  /
5 \  |8    1    |6 /
   \ |    4     | /
    v₆ ——————— v₇
```

**Solution** (Starting from v₁):

**Step 1**: Start with v₁
- MST: {v₁}
- Available edges: (v₁,v₂,2), (v₁,v₃,4), (v₁,v₄,1)
- Choose: (v₁,v₄,1) - minimum weight

**Step 2**: Add v₄ to MST
- MST: {v₁, v₄}
- Available edges: (v₁,v₂,2), (v₁,v₃,4), (v₄,v₃,2), (v₄,v₅,7), (v₄,v₆,8)
- Choose: (v₁,v₂,2) or (v₄,v₃,2) - both have weight 2
- Let's choose: (v₁,v₂,2)

**Step 3**: Add v₂ to MST
- MST: {v₁, v₄, v₂}
- Available edges: (v₁,v₃,4), (v₄,v₃,2), (v₄,v₅,7), (v₄,v₆,8), (v₂,v₅,10)
- Choose: (v₄,v₃,2) - minimum weight

**Step 4**: Add v₃ to MST
- MST: {v₁, v₄, v₂, v₃}
- Available edges: (v₄,v₅,7), (v₄,v₆,8), (v₂,v₅,10), (v₃,v₆,5)
- Choose: (v₃,v₆,5) - minimum weight

**Step 5**: Add v₆ to MST
- MST: {v₁, v₄, v₂, v₃, v₆}
- Available edges: (v₄,v₅,7), (v₂,v₅,10), (v₆,v₇,1)
- Choose: (v₆,v₇,1) - minimum weight

**Step 6**: Add v₇ to MST
- MST: {v₁, v₄, v₂, v₃, v₆, v₇}
- Available edges: (v₄,v₅,7), (v₂,v₅,10), (v₇,v₅,6)
- Choose: (v₇,v₅,6) - minimum weight

**Final MST edges**: 
- (v₁,v₄,1)
- (v₁,v₂,2) 
- (v₄,v₃,2)
- (v₃,v₆,5)
- (v₆,v₇,1)
- (v₇,v₅,6)

**Total weight**: 1 + 2 + 2 + 5 + 1 + 6 = 17

### Sample Question 4: Knowledge - AVL Tree Balance Condition

**Question**: What is the balance condition (i.e. the defining property) of an AVL tree?

**Answer**: 
The balance condition of an AVL tree is that **for every node in the tree, the heights of its left and right subtrees must differ by at most 1**.

**Formal Definition**:
For any node n in an AVL tree:
|height(left_subtree(n)) - height(right_subtree(n))| ≤ 1

**Key Points**:
- This condition must hold for EVERY node in the tree, not just the root
- The height of an empty subtree (null) is considered to be -1
- This balance condition ensures that the tree height is always O(log n)
- When insertions or deletions violate this condition, rotations are performed to restore balance
- AVL trees guarantee O(log n) time complexity for search, insertion, and deletion operations due to this balance condition

**Balance Factor**:
The balance factor of a node is defined as:
Balance Factor = height(left_subtree) - height(right_subtree)

For an AVL tree, the balance factor of every node must be -1, 0, or +1.

