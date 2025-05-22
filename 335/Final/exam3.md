# CSCI 335 Exam C - Complete Solutions
*Based on the third exam document*

---

## Question 1: Dijkstra's Algorithm (12 points)
**Problem**: Compute shortest path from vertex 2 to vertex 3.

### Complete Solution:

Looking at the completed table in the exam:

**Final Answer**: 
- **Shortest distance from vertex 2 to vertex 3**: **10**
- **Path**: 2 → 5 → 1 → 3 (following predecessor pointers)

**Verification of key steps**:
- Start from vertex 2 (distance 0)
- Process vertices in order of shortest distance
- Final distances: v1=6, v2=0, v3=10, v4=8, v5=3, v6=4

The student correctly executed Dijkstra's algorithm step by step.

---

## Question 2: Sorted List Intersection (12 points)

### Complete Solution:

**Problem**: Return sorted vector of integers that appear in both lists, with frequency = min of frequencies in each list.

```cpp
std::vector<int> sortedIntersection(const std::vector<int>& list1, 
                                  const std::vector<int>& list2) {
    std::vector<int> result;
    int i = 0, j = 0;
    
    // Two-pointer approach since both lists are sorted
    while (i < list1.size() && j < list2.size()) {
        if (list1[i] < list2[j]) {
            i++;
        } else if (list1[i] > list2[j]) {
            j++;
        } else {
            // Found common element
            result.push_back(list1[i]);
            i++;
            j++;
        }
    }
    
    return result;
}
```

**Alternative O(n) solution using counting**:
```cpp
std::vector<int> sortedIntersection(const std::vector<int>& list1, 
                                  const std::vector<int>& list2) {
    std::unordered_map<int, int> count1, count2;
    
    // Count frequencies in both lists
    for (int x : list1) count1[x]++;
    for (int x : list2) count2[x]++;
    
    std::vector<int> result;
    for (const auto& p : count1) {
        int value = p.first;
        int freq1 = p.second;
        if (count2.count(value)) {
            int freq2 = count2[value];
            // Add min(freq1, freq2) copies to result
            for (int k = 0; k < std::min(freq1, freq2); k++) {
                result.push_back(value);
            }
        }
    }
    
    std::sort(result.begin(), result.end());
    return result;
}
```

**Time Complexity**: O(n + m) where n, m are list sizes
**Space Complexity**: O(min(n, m)) for result

---

## Question 3: Stale Iterator (5 points)

### Complete Solution:

**Definition**: A stale iterator is an iterator that no longer points to valid memory or has been invalidated by container modifications.

**Example of stale iterator**:
```cpp
std::vector<int> vec = {1, 2, 3, 4, 5};
auto it = vec.begin() + 2;  // Points to element at index 2

vec.erase(vec.begin());     // Erase first element
// Now 'it' is stale - it may point to wrong element or invalid memory

std::cout << *it;  // UNDEFINED BEHAVIOR - using stale iterator
```

**What causes stale iterators**:
- Container modifications (insert, erase, resize)
- Memory reallocation (vector growth)
- Container destruction

**How to avoid**:
- Update iterators after modifications
- Use indices instead of iterators when modifying
- Use iterator-safe operations when available

---

## Question 4: Time Complexities (15 points)

### Complete Solution:

1. **DeleteMin in a min heap (worst case)**: **O(log n)**
2. **Topological sort (average case)**: **O(|V| + |E|)**
3. **Find min in a hash table (average case)**: **O(n)**
4. **Kruskal's algorithm (worst case)**: **O(|E| log |E|)** or **O(|E| log |V|)**
5. **Buildheap (worst case)**: **O(n)**
6. **Update value in a hash map (average case)**: **O(1)**
7. **Unweighted single-source shortest path**: **O(|V| + |E|)**
8. **Quickselect (worst case)**: **O(n²)**
9. **Find in an AVL tree (average case)**: **O(log n)**
10. **Prim's algorithm, using heaps**: **O(|E| log |V|)**

---

## Question 5: Quicksort with Median-of-3 (6 points)

### Complete Solution:

**Algorithm**: Choose pivot as median of first, middle, and last elements before partitioning.

**Why it improves performance**:

1. **Avoids worst-case scenarios**: 
   - Regular quicksort degrades to O(n²) on sorted/reverse-sorted arrays
   - Median-of-3 makes this extremely unlikely

2. **Better pivot selection**:
   - First/last/random pivot can be consistently bad
   - Median-of-3 tends to choose pivots closer to true median

3. **Practical improvement**:
   - Reduces average recursion depth
   - More balanced partitions on average
   - Still O(n²) worst case but much less likely

**Example**:
```
Array: [1, 7, 3, 9, 2, 8, 4]
Regular: Might pick 1 (terrible pivot)
Median-of-3: Pick median of {1, 9, 4} = 4 (much better)
```

**Result**: Average case remains O(n log n) but with better constant factors and fewer worst-case occurrences.

---

## Question 6: Binary Search Tree Printing (12 points)

### Complete Solution:

**Problem**: Print BST elements in order.

```cpp
void printTree(BinaryNode* root) {
    if (root == nullptr) {
        return;
    }
    
    // In-order traversal: left -> root -> right
    printTree(root->left);                    // Process left subtree
    std::cout << root->element << " ";        // Process current node
    printTree(root->right);                   // Process right subtree
}
```

**Why in-order traversal**:
- BST property: left < root < right
- In-order visits nodes in sorted order
- Time complexity: O(n) where n = number of nodes
- Space complexity: O(h) where h = height (for recursion stack)

**Alternative iterative solution**:
```cpp
void printTreeIterative(BinaryNode* root) {
    std::stack<BinaryNode*> stk;
    BinaryNode* current = root;
    
    while (current != nullptr || !stk.empty()) {
        // Go to leftmost node
        while (current != nullptr) {
            stk.push(current);
            current = current->left;
        }
        
        // Process current node
        current = stk.top();
        stk.pop();
        std::cout << current->element << " ";
        
        // Move to right subtree
        current = current->right;
    }
}
```

---

## Question 7: Topological Ordering (5 points)

### Complete Solution:

**Answer**: This graph does **NOT** have a topological ordering.

**Reason**: The graph contains **cycles**, and topological ordering only exists for **Directed Acyclic Graphs (DAGs)**.

**Cycle identification**:
Looking at the graph structure, there appears to be a cycle (for example: A→B→E→D→A or similar cycle depending on the exact edge directions).

**Key principle**: 
- **DAG** → Topological ordering exists
- **Contains cycles** → No topological ordering possible
- **Undirected** → Concept doesn't apply

**Detection method**: Use DFS with three colors (white/gray/black) or Kahn's algorithm - if not all vertices are processed, a cycle exists.

---

## Question 8: Quadratic Probing (5 points)

### Complete Solution:

**Advantage of quadratic probing over linear probing**:

**Reduces primary clustering** - the main benefit.

**Explanation**:
- **Linear probing**: Uses probe sequence h(x), h(x)+1, h(x)+2, h(x)+3, ...
- **Quadratic probing**: Uses probe sequence h(x), h(x)+1², h(x)+2², h(x)+3², ...

**Primary clustering problem**:
- In linear probing, consecutive occupied slots create "clusters"
- New insertions that hash anywhere in cluster must probe through entire cluster
- Clusters grow larger over time, making average probe distance worse

**How quadratic helps**:
- Spreads out probe sequences more evenly
- Reduces formation of large consecutive clusters
- Better average performance than linear probing
- Still simpler than double hashing

**Trade-off**: May create secondary clustering (different keys with same hash value follow same probe sequence), but this is less problematic than primary clustering.

---

## Question 9: Mode of Vector (15 points)

### Complete Solution:

**Problem**: Find the most frequently occurring element in O(n) time.

```cpp
int modeOfVector(const std::vector<int>& nums) {
    if (nums.empty()) return -1;  // Handle empty vector
    
    std::unordered_map<int, int> frequency;
    
    // Count frequency of each element - O(n)
    for (int num : nums) {
        frequency[num]++;
    }
    
    // Find element with maximum frequency - O(k) where k = unique elements
    int mode = nums[0];
    int maxCount = 0;
    
    for (const auto& pair : frequency) {
        if (pair.second > maxCount) {
            maxCount = pair.second;
            mode = pair.first;
        }
    }
    
    return mode;
}
```

**Algorithm explanation**:
1. **Hash map counting**: Store frequency of each element
2. **Single pass**: Count all frequencies in O(n) time
3. **Find maximum**: Scan frequency map to find highest count
4. **Return mode**: Element with highest frequency

**Time Complexity**: O(n) where n = vector size
**Space Complexity**: O(k) where k = number of unique elements

**Alternative for small range integers**:
```cpp
int modeOfVectorArray(const std::vector<int>& nums) {
    const int MAX_VAL = 1000;  // Assuming values 0-999
    std::vector<int> count(MAX_VAL, 0);
    
    for (int num : nums) {
        count[num]++;
    }
    
    int mode = 0;
    for (int i = 1; i < MAX_VAL; i++) {
        if (count[i] > count[mode]) {
            mode = i;
        }
    }
    return mode;
}
```

---

## Question 10: AVL Tree Recurrence (5 points)

### Complete Solution:

**Recurrence relation**: S(n) = S(n-1) + S(n-2) + 1

**Base cases**: 
- S(0) = 1 (tree with height 0 has 1 node)
- S(1) = 2 (tree with height 1 has 2 nodes)

**Calculation**:
- S(2) = S(1) + S(0) + 1 = 2 + 1 + 1 = 4
- S(3) = S(2) + S(1) + 1 = 4 + 2 + 1 = 7
- S(4) = S(3) + S(2) + 1 = 7 + 4 + 1 = 12
- S(5) = S(4) + S(3) + 1 = 12 + 7 + 1 = 20

**Explanation**: 
- Minimum AVL tree of height n has one subtree of height n-1 and one of height n-2 (to maintain balance)
- Plus the root node (+1)
- This is essentially Fibonacci sequence with +1 adjustment

---

## Question 11: Binary Heap Properties (4 points)

### Complete Solution:

**Two necessary properties**:

1. **Structure Property**: 
   - Binary heap must be a **complete binary tree**
   - All levels filled except possibly the last level
   - Last level filled from left to right
   - Allows efficient array representation

2. **Heap-Order Property**: 
   - **Min-heap**: Parent ≤ both children for every node
   - **Max-heap**: Parent ≥ both children for every node  
   - Ensures minimum/maximum element is always at root
   - Enables O(1) findMin/findMax operations

**Why both are necessary**:
- **Structure property**: Enables O(log n) insert/delete operations and efficient array storage
- **Heap-order property**: Provides the priority queue semantics and efficient extract-min/max

---

## Question 12: Prim's Algorithm Analysis (12 points)

### Complete Solution:

**Complete complexity analysis of Prim's algorithm using min heap**:

**Data structures needed**:
- **Adjacency lists**: O(|V| + |E|) space for graph representation
- **Min-heap**: Store vertices with their minimum edge weights to current MST
- **Distance array**: Track minimum edge weight for each vertex to MST
- **Boolean array**: Track which vertices are already in MST

**Algorithm complexity breakdown**:

1. **Initialization**: O(|V|)
   - Create distance array, set source to 0, others to ∞
   - Insert all vertices into min-heap
   - Initialize MST membership array

2. **Main loop** (execute |V| times):
   - **Extract minimum**: O(log |V|) per operation
   - **Mark vertex as in MST**: O(1)
   - **Process adjacent edges**: For each neighbor not in MST
     - **Check if edge improves distance**: O(1)
     - **Decrease key in heap**: O(log |V|) if needed

3. **Edge processing analysis**:
   - Each edge is considered exactly **once** (when source vertex is extracted)
   - Total edges processed: |E|
   - Each edge processing may trigger decrease-key: O(log |V|)
   - **Total edge work**: O(|E| log |V|)

4. **Vertex processing**: |V| extractions × O(log |V|) = O(|V| log |V|)

**Final complexity**: O(|V| log |V| + |E| log |V|) = **O(|E| log |V|)**

**When |E| log |V| dominates**: In connected graphs, |E| ≥ |V|-1, so for most practical graphs the edge processing dominates.

---

## Question 13: Approximation Algorithms (4 points)

### Complete Solution:

**What approximation algorithms are used for**:

Approximation algorithms are used to find **near-optimal solutions** to **NP-hard optimization problems** in **polynomial time**.

**Key applications**:

1. **NP-hard problems**: When exact solutions require exponential time
   - Traveling Salesman Problem (TSP)
   - Set Cover Problem  
   - Vertex Cover Problem
   - Bin Packing Problem

2. **Trade accuracy for speed**: Get solutions within known factor of optimal
   - Example: 2-approximation algorithm guarantees solution ≤ 2 × optimal

3. **Large-scale problems**: When exact algorithms are too slow for practical use
   - Network routing optimization
   - Resource allocation
   - Scheduling problems

4. **Real-time systems**: When quick decisions needed with reasonable quality
   - Online algorithms
   - Streaming algorithms

**Example**: 
- **Problem**: TSP on n cities
- **Exact solution**: O(n!) time
- **2-approximation**: O(n³) time, solution ≤ 2 × optimal tour length

**Why useful**: Provides mathematical guarantees on solution quality while maintaining polynomial time complexity.