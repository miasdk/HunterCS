# CSCI 335 Final Exam B - Complete Solutions
*Based on Theo Jack Orecchio's exam (33.5/110 points)*

---

## Question 1: Dijkstra's Algorithm (10 points)
**Problem**: Compute shortest path from vertex 1 to vertex 5.

### Complete Solution:

**Step 1** (Initial):
| v | known | dv | pv |
|---|-------|----|----|
| 1 | F     | 0  | 0  |
| 2 | F     | ∞  | 0  |
| 3 | F     | ∞  | 0  |
| 4 | F     | ∞  | 0  |
| 5 | F     | ∞  | 0  |

**Step 2** (Process vertex 1, distance = 0):
- Mark v1 as known = T
- Update v2: 0 + 6 = 6, pv = 1
- Update v3: 0 + 2 = 2, pv = 1

| v | known | dv | pv |
|---|-------|----|----|
| 1 | T     | 0  | 0  |
| 2 | F     | 6  | 1  |
| 3 | F     | 2  | 1  |
| 4 | F     | ∞  | 0  |
| 5 | F     | ∞  | 0  |

**Step 3** (Process vertex 3, distance = 2):
- Mark v3 as known = T
- Update v4: 2 + 3 = 5, pv = 3
- Update v5: 2 + 1 = 3, pv = 3

| v | known | dv | pv |
|---|-------|----|----|
| 1 | T     | 0  | 0  |
| 2 | F     | 6  | 1  |
| 3 | T     | 2  | 1  |
| 4 | F     | 5  | 3  |
| 5 | F     | 3  | 3  |

**Step 4** (Process vertex 5, distance = 3):
- Mark v5 as known = T
- Update v4: 3 + 2 = 5, no change (same distance)
- Update v2: 3 + 8 = 11 > 6, no change

| v | known | dv | pv |
|---|-------|----|----|
| 1 | T     | 0  | 0  |
| 2 | F     | 6  | 1  |
| 3 | T     | 2  | 1  |
| 4 | F     | 5  | 3  |
| 5 | T     | 3  | 3  |

**Answer**: Shortest path from 1 to 5 = **3** via path 1→3→5

---

## Question 2: Algorithm Analysis - Prim's (15 points)

### Complete Solution:

**Step-by-Step Analysis**:

1. **Data Structures**:
   - **Adjacency lists**: O(|V| + |E|) space
   - **Min-heap**: Store vertices with minimum edge weights
   - **Boolean array**: Track MST membership

2. **Algorithm Steps**:
   - **Initialize**: Add source to heap with weight 0, others with ∞
   - **Extract minimum**: O(log |V|) per vertex, done |V| times
   - **Edge relaxation**: For each edge, possibly decrease key in heap

3. **Complexity Breakdown**:
   - **Vertex extractions**: |V| × O(log |V|) = O(|V| log |V|)
   - **Edge processing**: Each edge considered once, decrease-key is O(log |V|)
   - **Total edge work**: |E| × O(log |V|) = O(|E| log |V|)

4. **Final Complexity**: O(|V| log |V| + |E| log |V|) = **O(|E| log |V|)**

**Why |E| log |V|**: Each edge is processed exactly once when its source vertex is extracted from the heap, and each processing takes O(log |V|) time for the decrease-key operation.

---

## Question 3: Complexity (15 points)

### Complete Solution:

1. **Insert in a min heap (worst case)**: **O(log n)**
2. **Topological sort using adjacency list**: **O(|V| + |E|)**
3. **Find max in a hash table (average case)**: **O(n)**
4. **Kruskal's algorithm (worst case)**: **O(|E| log |V|)**
5. **Buildheap (worst case)**: **O(n)**
6. **Update value in a hash map (average case)**: **O(1)**
7. **Unweighted single-source shortest path**: **O(|V| + |E|)**
8. **Quickselect (worst case)**: **O(n²)**
9. **Delete in an AVL tree (average case)**: **O(log n)**
10. **Dijkstra's algorithm using update table**: **O(|V|²)**

---

## Question 4: Properties of AVL Tree (4 points)

### Complete Solution:

**Two defining properties**:

1. **Binary Search Tree Property**: 
   - For every node, all values in left subtree < node value < all values in right subtree
   - This applies to EVERY node, not just the root

2. **Balance Property**: 
   - For each node in an AVL tree, the height difference between its left and right children must be at most 1
   - |height(left) - height(right)| ≤ 1 for every node

**Note**: The balance property ensures O(log n) height, making all operations efficient.

---

## Question 5: Properties of Binary Heap (4 points)

### Complete Solution:

**Two defining properties**:

1. **Structure Property**: 
   - A binary heap is structured as a complete binary tree
   - All levels are filled except possibly the last level
   - Last level is filled from left to right

2. **Heap-Order Property**: 
   - **Min-heap**: Each node has value ≤ both children
   - **Max-heap**: Each node has value ≥ both children
   - This ensures the minimum/maximum element is always at the root

---

## Question 6: Asymmetric List Difference (12 points)

### Complete Solution:

```cpp
void printUninvited(const std::vector<std::string>& rsvped, 
                   const std::vector<std::string>& showed) {
    // Use hash set for O(1) lookup
    std::unordered_set<std::string> rsvp_set;
    
    // Put all RSVPed people in hash set
    for (const std::string& person : rsvped) {
        rsvp_set.insert(person);
    }
    
    // Check each person who showed up
    for (const std::string& person : showed) {
        // If they didn't RSVP, print them
        if (rsvp_set.find(person) == rsvp_set.end()) {
            std::cout << person << std::endl;
        }
    }
}
```

**Algorithm**:
1. **Insert all RSVP names** into unordered_set: O(R) where R = |rsvped|
2. **Check each person who showed**: O(S) where S = |showed|
3. **Total complexity**: O(R + S) = **O(n)** linear time

**Key points**:
- Use `unordered_set` for O(1) average lookup
- Hash-based data structure is essential for linear time
- Check existence with `.find() == .end()`

---

## Question 7: Kruskal's Algorithm (6 points)

### Complete Solution:

**Given graph with edges sorted by weight:**

| Step | Edge | Weight | Action | Reason |
|------|------|--------|--------|--------|
| 1 | (3,4) | 1 | Accept | First edge, no cycle |
| 2 | (1,4) | 2 | Accept | Connects different components |
| 3 | (6,7) | 2 | Accept | Connects different components |
| 4 | (2,4) | 3 | Accept | Connects different components |
| 5 | (3,6) | 3 | Accept | Connects different components |
| 6 | (1,3) | 4 | Reject | Creates cycle (1-4-3-1) |
| 7 | (4,7) | 4 | Accept | Completes MST (6 edges for 7 vertices) |

**Final MST edges**: (3,4), (1,4), (6,7), (2,4), (3,6), (4,7)
**Total weight**: 1 + 2 + 2 + 3 + 3 + 4 = **15**

---

## Question 8: 2D Dynamic Programming (15 points)

### Complete Solution:

**Problem**: Count paths in grid with obstacles.

```cpp
int paths(int n, int m, int x, int y) {
    // Create 2D DP array
    vector<vector<int>> dp(n, vector<int>(m, 0));
    
    // Initialize first row
    for (int j = 0; j < m; j++) {
        if (j < y || (0 == x && j == y)) {
            dp[0][j] = 0;  // Obstacle blocks path
        } else {
            dp[0][j] = (j == 0) ? 1 : dp[0][j-1];
        }
    }
    
    // Initialize first column
    for (int i = 0; i < n; i++) {
        if (i < x || (i == x && 0 == y)) {
            dp[i][0] = 0;  // Obstacle blocks path
        } else {
            dp[i][0] = (i == 0) ? 1 : dp[i-1][0];
        }
    }
    
    // Fill the rest of the matrix
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
            if (i == x && j == y) {
                dp[i][j] = 0;  // Obstacle cell
            } else {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
    }
    
    return dp[n-1][m-1];
}
```

**Algorithm**:
1. **Initialize borders** considering obstacle position
2. **Fill matrix** using recurrence: `dp[i][j] = dp[i-1][j] + dp[i][j-1]`
3. **Handle obstacle** by setting `dp[x][y] = 0`
4. **Return** `dp[n-1][m-1]`

---

## Question 9: BuildHeap (5 points)

### Complete Solution:

**Why BuildHeap is O(n)**:

The key insight is that **each node moves down at most its height**, and the **sum of heights of all nodes in a complete binary tree is O(n)**.

**Mathematical proof**:
- **Height 0 nodes**: n/2 nodes, each moves 0 steps
- **Height 1 nodes**: n/4 nodes, each moves ≤ 1 step  
- **Height 2 nodes**: n/8 nodes, each moves ≤ 2 steps
- **Height k nodes**: n/2^(k+1) nodes, each moves ≤ k steps

**Total work**: Σ(k × n/2^(k+1)) for k = 0 to log n

This series converges to **O(n)**, not O(n log n).

**Intuition**: Most nodes are leaves (height 0) and don't move at all. Only a few nodes near the root do significant work.

---

## Question 10: Lower_Bound Raffle (8 points)

### Complete Solution:

**Problem**: Efficiently find smallest number ≥ x in a set.

```cpp
#include <set>

class Raffle {
    std::set<int> tickets;  // Ordered set for O(log n) operations
    
public:
    void addTicket(int number) {
        tickets.insert(number);  // O(log n)
    }
    
    int findWinner(int drawnNumber) {
        auto it = tickets.lower_bound(drawnNumber);  // O(log n)
        if (it != tickets.end()) {
            return *it;
        }
        return -1;  // No valid ticket
    }
};
```

**Algorithm**:
1. **Use ordered set** (std::set) for O(log n) range queries
2. **lower_bound(x)** finds first element ≥ x in O(log n) time
3. **For m queries**: Total complexity O(m log n)

**Why not hash tables**: Hash tables don't maintain order, can't efficiently find "smallest ≥ x"

---

## Question 11: C++ STL Search vs. Lookup (6 points)

### Complete Solution:

**Key differences between ordered and unordered containers**:

1. **Implementation**:
   - **set/map**: Use balanced binary search trees (usually Red-Black trees)
   - **unordered_set/unordered_map**: Use hash tables

2. **Find operation**:
   - **Hash lookup**: Direct access via hash function - O(1) average
   - **BST search**: Navigate tree structure - O(log n)

3. **Complexity differences**:
   - **Unordered containers**: O(1) average, O(n) worst case
   - **Ordered containers**: O(log n) guaranteed

4. **Functionality**:
   - **Same interface**: Both provide `.find()` method
   - **Different implementations**: Hash lookup vs tree traversal
   - **Ordered containers**: Additional benefits like range queries, iteration in sorted order

---

## Question 12: Partial Sorting (10 points)

### Complete Solution:

**Algorithm**: Modified heapsort to find top 10%

**Approach**:
1. **Use heapsort** for guaranteed O(n log n) performance
2. **BuildHeap**: Create initial heap in O(n) time
3. **Extract only 10%**: Instead of n extractions, do only n/10 extractions
4. **Each extraction**: O(log n) time

**Complexity Analysis**:
- **BuildHeap**: O(n) - still need to process entire array
- **Partial extraction**: (n/10) × O(log n) = O(n log n)/10
- **Total**: O(n + n log n) = **O(n log n)** but with **constant factor improvement of ~10x**

**Alternative - QuickSelect approach**:
1. **Partition** until top 10% isolated: Average O(n)
2. **Sort the 10%**: O((n/10) log(n/10)) = O(n log n)/10
3. **Total**: O(n) average case

**Result**: Practical speedup of ~10x while maintaining same asymptotic complexity.