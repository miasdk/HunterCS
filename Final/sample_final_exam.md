# CSCI 335 Sample Final Exam
**Total Points: 110**

---

## Question 1: Dijkstra's Algorithm (10 points)

Compute the shortest path from vertex A to vertex F using Dijkstra's algorithm. Show each step. You may or may not need all the tables to complete the algorithm.

```
Graph:
    (A)----4----(B)----2----(C)
     |           |           |
     1           3           1
     |           |           |
    (D)----2----(E)----3----(F)
```

**Step 1**
| v | known | dv | pv |
|---|-------|----|----|
| A | F     | 0  | 0  |
| B | F     | ∞  | 0  |
| C | F     | ∞  | 0  |
| D | F     | ∞  | 0  |
| E | F     | ∞  | 0  |
| F | F     | ∞  | 0  |

Complete the remaining steps...

---

## Question 2: Algorithm Analysis - Quicksort with Median-of-3 (15 points)

Write a full complexity analysis of Quicksort with median-of-3 partitioning. Include all steps taken and data structures used, stating the complexity of each step and relating that to the overall complexity.

Explain why median-of-3 partitioning improves average-case performance and what the worst-case scenario becomes.

---

## Question 3: Time Complexities (15 points)

For each algorithm or operation below, write the time complexity in O-notation with a tight bound. For graph algorithms, provide complexity in terms of |V| and/or |E| as appropriate.

- Insert in a max heap (worst case): ________________
- Topological sort using DFS: ________________
- Find value in unordered_map (average case): ________________
- Prim's algorithm using binary heaps: ________________
- BuildHeap (worst case): ________________
- Find key in ordered map (average case): ________________
- Weighted single-source shortest path (Dijkstra's): ________________
- Mergesort (worst case): ________________
- Find in an AVL tree (worst case): ________________
- Insertion sort on already sorted array: ________________

---

## Question 4: Properties of Splay Trees (4 points)

Briefly describe the two key properties that define a splay tree and distinguish it from other BSTs.

---

## Question 5: Properties of Hash Tables (4 points)

Name and briefly explain the two main collision resolution strategies for hash tables, giving one advantage and one disadvantage of each.

---

## Question 6: Best Game Scores (12 points)

You are given a vector of pairs representing game results, where each pair contains a player name (string) and their score (int). Lower scores are better. Print out each player's best (lowest) score. Use hash maps to do this in linear time.

**Function signature:**
```cpp
void printBestScores(std::vector<std::pair<std::string, int>> results) {
    // Your implementation here
}
```

**Sample input:** {("Alice", 85), ("Bob", 92), ("Alice", 78), ("Charlie", 95), ("Bob", 88)}
**Sample output:** Alice 78, Bob 88, Charlie 95

---

## Question 7: Prim's Algorithm (6 points)

Given the following graph, show each step of Prim's algorithm to find the minimum spanning tree. Start from vertex A. List each edge considered, its weight, and whether it's added or not.

```
Graph:
    A----5----B
    |\        |
    | 2       4
    |  \      |
    3   C----1-D
    |  / \    |
    | 6   3   2
    |/     \  |
    E----4---F
```

---

## Question 8: Matrix Chain Multiplication (15 points)

You want to multiply a chain of matrices A₁ × A₂ × A₃ × A₄ where:
- A₁ is 5×4
- A₂ is 4×6  
- A₃ is 6×2
- A₄ is 2×3

Write a dynamic programming solution to find the minimum number of scalar multiplications needed. Show the recurrence relation, base cases, and the final DP table.

---

## Question 9: QuickSelect Analysis (5 points)

Explain why QuickSelect has average-case O(n) complexity but worst-case O(n²) complexity. What causes the worst case, and how can it be avoided in practice?

---

## Question 10: Range Queries with STL (8 points)

You have a list of events, each with a start time and end time. You need to efficiently:
1. Find all events that start between time t₁ and t₂
2. Find all events that are active at time t

Describe what STL containers you would use for each query type and analyze the time complexity. Assume you can preprocess the data.

---

## Question 11: Iterator Invalidation (6 points)

Explain what iterator invalidation means in C++ STL containers. Give a specific example of code that would cause iterator invalidation and explain why it's dangerous. How would you fix the code?

---

## Question 12: Approximate Algorithms (10 points)

You need to find the top 5% of elements in a very large dataset, but you want to trade some accuracy for significant performance improvement. 

Describe an algorithm that could give you approximately the top 5% much faster than exact sorting. Discuss the trade-offs between accuracy and performance, and analyze the time complexity of your approach.

---

# SOLUTIONS

## Question 1 Solution: Dijkstra's Algorithm

**Step 1** (Initial - A is source):
| v | known | dv | pv |
|---|-------|----|----|
| A | F     | 0  | 0  |
| B | F     | ∞  | 0  |
| C | F     | ∞  | 0  |
| D | F     | ∞  | 0  |
| E | F     | ∞  | 0  |
| F | F     | ∞  | 0  |

**Step 2** (Process A - distance 0):
- Mark A as known
- Update B: 0 + 4 = 4, pv = A
- Update D: 0 + 1 = 1, pv = A

| v | known | dv | pv |
|---|-------|----|----|
| A | T     | 0  | 0  |
| B | F     | 4  | A  |
| C | F     | ∞  | 0  |
| D | F     | 1  | A  |
| E | F     | ∞  | 0  |
| F | F     | ∞  | 0  |

**Step 3** (Process D - distance 1):
- Mark D as known
- Update E: 1 + 2 = 3, pv = D

| v | known | dv | pv |
|---|-------|----|----|
| A | T     | 0  | 0  |
| B | F     | 4  | A  |
| C | F     | ∞  | 0  |
| D | T     | 1  | A  |
| E | F     | 3  | D  |
| F | F     | ∞  | 0  |

**Step 4** (Process E - distance 3):
- Mark E as known
- Update B: 3 + 3 = 6 > 4, no change
- Update F: 3 + 3 = 6, pv = E

| v | known | dv | pv |
|---|-------|----|----|
| A | T     | 0  | 0  |
| B | F     | 4  | A  |
| C | F     | ∞  | 0  |
| D | T     | 1  | A  |
| E | T     | 3  | D  |
| F | F     | 6  | E  |

**Step 5** (Process B - distance 4):
- Mark B as known
- Update C: 4 + 2 = 6, pv = B

| v | known | dv | pv |
|---|-------|----|----|
| A | T     | 0  | 0  |
| B | T     | 4  | A  |
| C | F     | 6  | B  |
| D | T     | 1  | A  |
| E | T     | 3  | D  |
| F | F     | 6  | E  |

**Step 6** (Process F or C - both distance 6, choose F):
- Mark F as known
- Update C: 6 + 1 = 7 > 6, no change

Final: **Shortest path A→F = 6** via A→D→E→F

## Question 2 Solution: Quicksort with Median-of-3

**Algorithm Steps:**
1. **Median-of-3 partitioning**: Select first, middle, and last elements. Choose median as pivot. **O(1)**
2. **Partition around pivot**: Rearrange array so elements ≤ pivot are left, > pivot are right. **O(n)**
3. **Recursive calls**: Recursively sort left and right subarrays. **T(k) + T(n-k-1)** where k is partition size

**Complexity Analysis:**
- **Average case**: Median-of-3 tends to choose better pivots than random selection
- Expected partition sizes closer to n/2 each time
- **Recurrence**: T(n) = 2T(n/2) + O(n) = **O(n log n)** average
- **Worst case**: Still **O(n²)** if consistently bad pivots chosen
- **Improvement**: Median-of-3 makes worst case much less likely in practice

**Why it helps**: By choosing median of three elements, we avoid the common worst-case scenarios like already-sorted arrays that would cause standard quicksort to degrade.

## Question 3 Solution: Time Complexities

- Insert in a max heap (worst case): **O(log n)**
- Topological sort using DFS: **O(|V| + |E|)**
- Find value in unordered_map (average case): **O(n)**
- Prim's algorithm using binary heaps: **O(|E| log |V|)**
- BuildHeap (worst case): **O(n)**
- Find key in ordered map (average case): **O(log n)**
- Weighted single-source shortest path (Dijkstra's): **O(|E| log |V|)**
- Mergesort (worst case): **O(n log n)**
- Find in an AVL tree (worst case): **O(log n)**
- Insertion sort on already sorted array: **O(n)**

## Question 4 Solution: Splay Trees

1. **BST Property**: Like all BSTs, maintains the ordering property (left < parent < right)
2. **Splay Operation**: After every access (find, insert, delete), the accessed node is moved to the root through a series of rotations called "splaying"

**Key benefit**: Frequently accessed nodes stay near the root, providing **O(log n) amortized** complexity even though single operations might take **O(n)** in worst case.

## Question 5 Solution: Hash Tables

1. **Separate Chaining**:
   - **Method**: Each bucket contains a linked list of colliding elements
   - **Advantage**: Simple to implement, handles high load factors well
   - **Disadvantage**: Extra memory overhead for pointers, cache performance

2. **Open Addressing** (Linear/Quadratic Probing, Double Hashing):
   - **Method**: Find next available slot using probe sequence
   - **Advantage**: Better cache performance, less memory overhead
   - **Disadvantage**: Performance degrades with high load factor, requires careful deletion

## Question 6 Solution: Best Game Scores

```cpp
void printBestScores(std::vector<std::pair<std::string, int>> results) {
    std::unordered_map<std::string, int> bestScores;
    
    for (const auto& result : results) {
        std::string player = result.first;
        int score = result.second;
        
        // Check if player exists in map
        if (bestScores.find(player) == bestScores.end()) {
            bestScores[player] = score;  // First time seeing this player
        } else if (score < bestScores[player]) {
            bestScores[player] = score;  // Update if better score
        }
    }
    
    // Print results
    for (const auto& entry : bestScores) {
        std::cout << entry.first << " " << entry.second << std::endl;
    }
}
```

**Time Complexity**: O(n) where n is number of game results
**Space Complexity**: O(k) where k is number of unique players

## Question 7 Solution: Prim's Algorithm

Starting from vertex A:

| Step | Edge | Weight | Action | Reason | MST Edges |
|------|------|--------|--------|--------|-----------|
| 1 | A-D | 3 | Accept | Smallest edge from A | {A-D} |
| 2 | A-C | 2 | Accept | Smallest edge to unvisited | {A-D, A-C} |
| 3 | C-D | 1 | Accept | Smallest edge to unvisited | {A-D, A-C, C-D} |
| 4 | D-F | 2 | Accept | Smallest edge to unvisited | {A-D, A-C, C-D, D-F} |
| 5 | C-F | 3 | Reject | F already in MST | {A-D, A-C, C-D, D-F} |
| 6 | F-E | 4 | Accept | Only way to reach E | {A-D, A-C, C-D, D-F, F-E} |
| 7 | A-B | 5 | Accept | Only way to reach B | {A-D, A-C, C-D, D-F, F-E, A-B} |

**Total Weight**: 3 + 2 + 1 + 2 + 4 + 5 = **17**

## Question 8 Solution: Matrix Chain Multiplication

**Recurrence Relation**:
```
m[i][j] = min(m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j])
          for k = i to j-1
```

**Base Case**: m[i][i] = 0 (single matrix requires no multiplication)

**Dimensions**: p = [5, 4, 6, 2, 3] (from matrix dimensions)

**DP Table**:
```
    1    2    3    4
1   0   120  124  132
2   -    0   48   72
3   -    -    0   18
4   -    -    -    0
```

**Answer**: **132 scalar multiplications** minimum

## Question 9 Solution: QuickSelect Analysis

**Average Case O(n)**:
- Each recursive call processes roughly half the array
- T(n) = T(n/2) + O(n) = O(n) by master theorem
- Only recurse on one side (unlike quicksort)

**Worst Case O(n²)**:
- Consistently poor pivot selection (always smallest/largest)
- T(n) = T(n-1) + O(n) = O(n²)
- Process almost entire array each time

**Avoidance Strategies**:
1. **Median-of-3** pivot selection
2. **Randomized** pivot selection
3. **Introselect** (switch to heapselect after too many levels)

## Question 10 Solution: Range Queries

**For Query 1** (Events starting between t₁ and t₂):
- **Container**: `std::map<int, std::vector<Event>>` keyed by start time
- **Method**: Use `lower_bound(t1)` and `upper_bound(t2)`
- **Complexity**: **O(log n + k)** where k is number of results

**For Query 2** (Events active at time t):
- **Container**: Two `std::multimap<int, Event>`: one by start time, one by end time
- **Method**: Find all events that start ≤ t AND end ≥ t
- **Complexity**: **O(log n + k)** using range queries on both maps

**Alternative**: Use interval tree for both queries with **O(log n + k)** complexity.

## Question 11 Solution: Iterator Invalidation

**Definition**: Iterator invalidation occurs when operations on a container make existing iterators invalid (pointing to deallocated or moved memory).

**Dangerous Example**:
```cpp
std::vector<int> vec = {1, 2, 3, 4, 5};
for (auto it = vec.begin(); it != vec.end(); ++it) {
    if (*it == 3) {
        vec.erase(it);  // DANGER: Invalidates iterator
        ++it;           // Undefined behavior!
    }
}
```

**Fix**:
```cpp
for (auto it = vec.begin(); it != vec.end(); ) {
    if (*it == 3) {
        it = vec.erase(it);  // erase() returns next valid iterator
    } else {
        ++it;
    }
}
```

## Question 12 Solution: Approximate Top 5%

**Algorithm**: **Reservoir Sampling + Approximate Sorting**

1. **Maintain small sample**: Keep reservoir of size k = n/20 (5% of data)
2. **Streaming processing**: For each new element:
   - If reservoir not full: add element
   - Otherwise: replace random element with probability k/current_position
3. **Final step**: Sort the small reservoir sample

**Complexity**: 
- **Time**: O(n + k log k) = O(n) for large n
- **Space**: O(k) = O(n/20)
- **vs Exact**: O(n log n) time, O(n) space

**Trade-offs**:
- **Accuracy**: ~95% chance of finding true top 5% (depends on data distribution)
- **Performance**: Linear time vs O(n log n)
- **Memory**: Constant space vs full array storage
- **Streaming**: Can process data as it arrives