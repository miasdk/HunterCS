# CSCI 335 Final Exam A - Complete Solutions
*Based on Dawa Sonam's exam (43/100 points)*

---

## Question 1: Dijkstra's Algorithm (12 points)
**Problem**: Compute shortest path from vertex 2 to vertex 3 using Dijkstra's algorithm.

### Complete Solution:

**Graph Analysis**: From the provided graph:
- Vertices: 1, 2, 3, 4, 5, 6
- Start from vertex 2

**Step 1** (Initial):
| v | known | dv | pv |
|---|-------|----|----|
| 1 | F     | ∞  | 0  |
| 2 | F     | 0  | 0  |
| 3 | F     | ∞  | 0  |
| 4 | F     | ∞  | 0  |
| 5 | F     | ∞  | 0  |
| 6 | F     | ∞  | 0  |

**Step 2** (Process vertex 2, distance = 0):
- Mark v2 as known = T
- Update adjacents: v4 (weight 4), v5 (weight 2), v6 (weight 3)

| v | known | dv | pv |
|---|-------|----|----|
| 1 | F     | ∞  | 0  |
| 2 | T     | 0  | 0  |
| 3 | F     | ∞  | 0  |
| 4 | F     | 4  | 2  |
| 5 | F     | 2  | 2  |
| 6 | F     | 3  | 2  |

**Step 3** (Process vertex 5, distance = 2):
- Mark v5 as known = T
- Update adjacents: v1 (weight 2), v3 (weight 1)

| v | known | dv | pv |
|---|-------|----|----|
| 1 | F     | 4  | 5  |
| 2 | T     | 0  | 0  |
| 3 | F     | 3  | 5  |
| 4 | F     | 4  | 2  |
| 5 | T     | 2  | 2  |
| 6 | F     | 3  | 2  |

**Continuing steps...**

**Final Answer**: Shortest path from 2 to 3 = **3** via path 2→5→3

---

## Question 2: Complexity Analysis - Prim's Algorithm (12 points)

### Complete Solution:

**Prim's with heaps: O(|E| log |V|)**

**Proof**: 
1. **Initialize heap** with all vertices: O(|V|)
2. **Extract minimum |V| times**: O(|V| log |V|)
3. **Process each edge once** for decrease-key operations: O(|E| log |V|)
4. **Total**: O(|V| log |V| + |E| log |V|) = O(|E| log |V|)

**Prim's without heaps: O(|V|²)**

**Proof**:
1. **For each of |V| vertices**, find minimum key vertex: O(|V|)
2. **Update keys** for adjacent vertices: O(|V|) per iteration
3. **Total**: O(|V|²)

**When to use heaps**: 
- **Sparse graphs** (|E| ≈ |V|): Heap version is O(|V| log |V|) vs O(|V|²)
- **Dense graphs** (|E| ≈ |V|²): Simple version is better

---

## Question 3: Minimal AVL Trees (6 points)

### Complete Solution:

**Recurrence relation**: f(h) = f(h-1) + f(h-2) + 1

**Where**: f(h) = minimum number of nodes in AVL tree of height h

**Base cases**:
- f(0) = 1 (single node)
- f(1) = 2 (root + one child)

**Calculation for height 7**:
- f(0) = 1
- f(1) = 2  
- f(2) = f(1) + f(0) + 1 = 2 + 1 + 1 = 4
- f(3) = f(2) + f(1) + 1 = 4 + 2 + 1 = 7
- f(4) = f(3) + f(2) + 1 = 7 + 4 + 1 = 12
- f(5) = f(4) + f(3) + 1 = 12 + 7 + 1 = 20
- f(6) = f(5) + f(4) + 1 = 20 + 12 + 1 = 33
- f(7) = f(6) + f(5) + 1 = 33 + 20 + 1 = 54

**Answer**: **54 nodes**

---

## Question 4: Coding - buildHeap (8 points)

### Complete Solution:

```cpp
void buildHeap(std::vector<int>& heap) {
    // Start from last internal node and work backwards
    for (auto it = heap.begin() + heap.size()/2; it != heap.begin(); --it) {
        // Move element to index 0 temporarily
        *(heap.begin()) = *it;
        // Percolate down from this position
        percolateDown(heap, it - heap.begin());
    }
    // Handle the root (index 0)
    percolateDown(heap, 0);
}
```

**Key Points**:
- Start from `heap.size()/2` (last internal node)
- Use iterators, not array subscripting
- Decrement iterator to work backwards
- Call percolateDown for each position

---

## Question 5: Follow up - percDown (4 points)

### Complete Solution:

**Problem**: Iterators don't support arbitrary arithmetic operations like doubling indices.

**Explanation**: In `percolateDown`, you need to access child nodes at positions `2*i+1` and `2*i+2`. Iterators are designed for sequential access and don't support operations like `it * 2`. This requires either:

1. **Converting to indices**: `int index = it - heap.begin()`
2. **Using array notation**: Direct index arithmetic
3. **Iterator arithmetic**: Complex calculations with `std::advance()`

**Solution**: Use indices instead of iterators for heap operations requiring positional arithmetic.

---

## Question 6: Topological Orderings (3 points)

### Complete Solution:

**Answer**: **Directed Acyclic Graphs (DAGs)**

**Explanation**: 
- Must be **directed** (edges have direction)
- Must be **acyclic** (no cycles)
- If cycles exist, no topological ordering is possible
- If undirected, concept doesn't apply

---

## Question 7: Complexity (8 points)

### Complete Solution:

1. **Unweighted single-source shortest path**: **O(|V| + |E|)**
2. **Heapsort (worst case)**: **O(n log n)**
3. **Quickselect (worst case)**: **O(n²)**
4. **Insert in a splay tree (worst case)**: **O(n)**
5. **Kruskal's Algorithm**: **O(|E| log |V|)**
6. **Quicksort (average case)**: **O(n log n)**
7. **Dijkstra's algorithm using a priority queue**: **O(|E| log |V|)**
8. **Insert in an AVL tree (worst case)**: **O(log n)**

---

## Question 8: Priority Queues (6 points)

### Complete Solution:

**Situation**: When implementing a priority queue where you need **decrease-key** operations efficiently.

**Example**: Dijkstra's algorithm or Prim's algorithm implementations.

**Why binary heap isn't best**:
- Binary heaps don't efficiently support **decrease-key** operations
- Finding an arbitrary element in heap takes O(n) time
- **Better alternatives**: Fibonacci heaps (O(1) decrease-key) or d-ary heaps

**Explanation**: While binary heaps are excellent for basic priority queue operations, algorithms requiring frequent priority updates need specialized data structures.

---

## Question 9: Coding - quickSelect (10 points)

### Complete Solution:

```cpp
int quickSelect(std::vector<int>& nums, int low, int high, int k) {
    if (high - low < 10) {
        std::sort(nums.begin() + low, nums.begin() + high + 1);
        return nums[k];
    }
    
    auto pivot = partition(nums, low, high);
    
    if (pivot == k) {
        return nums[k];  // Found the k-th element
    } else if (pivot > k) {
        return quickSelect(nums, low, pivot - 1, k);  // Search left
    } else {
        return quickSelect(nums, pivot + 1, high, k); // Search right
    }
}
```

**Key Points**:
- Check if `pivot == k` before recursing
- Correct if/else logic for left vs right recursion
- Base case for small arrays
- Only recurse on one side (unlike quicksort)

---

## Question 10: Complexity Analysis - Nearest Neighbor (12 points)

### Complete Solution:

**Vector Implementation**: **O(|V|²)**
- **Delete operation**: O(|V|) to remove element and shift
- **Search operation**: O(|V|) to find nearest neighbor
- **Total**: O(|V|) operations × O(|V|) each = O(|V|²)

**Linked List Implementation**: **O(|V|²)**
- **Delete operation**: O(1) if you have iterator/pointer
- **Search operation**: O(|V|) to traverse and find nearest
- **Total**: Still O(|V|²) because search dominates

**Practical Difference**:
- **Vector**: Better cache performance, 2n operations per iteration
- **List**: Better deletion (O(1) vs O(|V|)), but same asymptotic complexity
- **List is faster in practice** due to efficient deletion

---

## Question 11: Double Hashing (8 points)

### Complete Solution:

**Problem**: Poor hash functions in double hashing create clustering and poor distribution.

**Example**: 
- **Primary hash**: h₁(x) = x mod 10
- **Secondary hash**: h₂(x) = 1 (constant)
- **Problem**: Secondary hash doesn't provide variation, creates linear probing

**Better Example**:
- **Primary hash**: h₁(x) = x mod m
- **Secondary hash**: h₂(x) = 7 - (x mod 7)
- **Ensures**: h₂(x) never equals 0, creates better probe sequences

**Requirements for good double hashing**:
1. h₂(x) must never be 0
2. h₂(x) should be relatively prime to table size
3. Both functions should distribute keys uniformly

---

## Question 12: Kruskal's Algorithm (6 points)

### Complete Solution:

**Given Graph** with edges sorted by weight:

| Step | Edge | Weight | Action | Reason |
|------|------|--------|--------|--------|
| 1 | (v₁,v₃) | 1 | Accept | First edge |
| 2 | (v₁,v₂) | 2 | Accept | No cycle |
| 3 | (v₂,v₄) | 3 | Accept | No cycle |
| 4 | (v₃,v₄) | 2 | Accept | No cycle |
| 5 | (v₄,v₅) | 4 | Accept | No cycle |
| 6 | (v₂,v₅) | 3 | Accept | Completes MST |

**Final MST**: Contains V-1 = 6 edges
**Total Weight**: 1 + 2 + 3 + 2 + 4 + 3 = **15**

---

## Question 13: Open Addressing (5 points)

### Complete Solution:

**Open Addressing**: Hash table collision resolution where all elements are stored directly in the table array.

**Uses Open Addressing**:
- **Linear probing**: h(x) + i mod m
- **Quadratic probing**: h(x) + i² mod m  
- **Double hashing**: h₁(x) + i·h₂(x) mod m

**Doesn't Use Open Addressing**:
- **Separate chaining**: Uses linked lists/arrays at each bucket
- **Perfect hashing**: Pre-computed perfect hash function