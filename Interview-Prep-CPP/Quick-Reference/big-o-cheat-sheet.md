# Big-O Complexity Cheat Sheet

> **Quick reference for interview time complexity analysis**
> 
> *Essential complexity patterns every C++ developer should memorize*

## 🎯 The Big 7 Complexities (Interview Critical)

| Complexity | Name | Growth Rate | Example Algorithms |
|------------|------|-------------|-------------------|
| **O(1)** | Constant | No growth | Array access, hash lookup |
| **O(log n)** | Logarithmic | Slow growth | Binary search, balanced tree |
| **O(n)** | Linear | Direct growth | Linear search, array traversal |
| **O(n log n)** | Linearithmic | Moderate growth | Merge sort, heap sort |
| **O(n²)** | Quadratic | Fast growth | Bubble sort, nested loops |
| **O(2ⁿ)** | Exponential | Extreme growth | Recursive Fibonacci |
| **O(n!)** | Factorial | Catastrophic | All permutations |

---

## 📊 Visual Growth Comparison

```
n=10     n=100    n=1000   n=10000
O(1):    1        1        1        1
O(log n): 3       7        10       13
O(n):    10       100      1000     10000
O(n log n): 33    664      9966     132877
O(n²):   100      10000    1000000  100000000
O(2ⁿ):   1024     2^100    2^1000   2^10000
```

---

## 🚀 STL Container Complexities

### **std::vector**
| Operation | Complexity | Notes |
|-----------|------------|-------|
| Access `vec[i]` | O(1) | Direct memory access |
| Push back `push_back()` | O(1) amortized | Occasional resize |
| Insert middle | O(n) | Shift elements |
| Search unsorted | O(n) | Linear scan |
| Search sorted | O(log n) | Binary search |

### **std::unordered_map**
| Operation | Complexity | Notes |
|-----------|------------|-------|
| Insert `map[key]` | O(1) average | Hash table |
| Lookup `map[key]` | O(1) average | Hash collisions |
| Delete `erase()` | O(1) average | Remove from bucket |
| Iteration | O(n) | Visit all elements |

### **std::map (Red-Black Tree)**
| Operation | Complexity | Notes |
|-----------|------------|-------|
| Insert | O(log n) | Balanced tree |
| Lookup | O(log n) | Tree traversal |
| Delete | O(log n) | Rebalance tree |
| Min/Max | O(log n) | Leftmost/rightmost |

### **std::priority_queue (Binary Heap)**
| Operation | Complexity | Notes |
|-----------|------------|-------|
| Top `top()` | O(1) | Root element |
| Push `push()` | O(log n) | Bubble up |
| Pop `pop()` | O(log n) | Bubble down |
| Build heap | O(n) | Bottom-up construction |

---

## 🎯 Algorithm Complexity Patterns

### **Sorting Algorithms**
```cpp
// O(n²) - Bubble Sort
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n-1-i; j++) {
        if (arr[j] > arr[j+1]) swap(arr[j], arr[j+1]);
    }
}

// O(n log n) - Merge Sort
std::sort(vec.begin(), vec.end());  // STL uses introsort

// O(n) - Counting Sort (limited range)
std::vector<int> count(max_val + 1, 0);
```

### **Search Algorithms**
```cpp
// O(n) - Linear Search
auto it = std::find(vec.begin(), vec.end(), target);

// O(log n) - Binary Search (sorted array)
bool found = std::binary_search(vec.begin(), vec.end(), target);
auto pos = std::lower_bound(vec.begin(), vec.end(), target);
```

### **Tree Traversal**
```cpp
// O(n) - BFS/DFS visit each node once
std::queue<TreeNode*> q;  // BFS
std::stack<TreeNode*> s;  // DFS iterative
// Recursive DFS also O(n) time, O(h) space where h = height
```

### **Graph Algorithms**
```cpp
// O(V + E) - BFS/DFS traversal
// V = vertices, E = edges

// O(E log V) - Dijkstra with binary heap
std::priority_queue<std::pair<int, int>> pq;

// O(V²) - Floyd-Warshall (all pairs shortest path)
for (int k = 0; k < V; k++)
    for (int i = 0; i < V; i++)
        for (int j = 0; j < V; j++)
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
```

---

## 📋 Common Interview Patterns

### **Nested Loops → O(n²)**
```cpp
// Two nested loops of size n
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        // O(1) operation
    }
}
```

### **Divide and Conquer → O(n log n)**
```cpp
// T(n) = 2T(n/2) + O(n)
// Examples: merge sort, quicksort average case
void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);     // T(n/2)
        mergeSort(arr, mid+1, right);  // T(n/2)
        merge(arr, left, mid, right);  // O(n)
    }
}
```

### **Binary Search → O(log n)**
```cpp
// Halve the search space each iteration
int binarySearch(vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```

### **Tree Height → O(log n) vs O(n)**
```cpp
// Balanced tree: O(log n) height
// Unbalanced tree: O(n) height (worst case)
int height(TreeNode* root) {
    if (!root) return 0;
    return 1 + max(height(root->left), height(root->right));
}
```

---

## ⚡ Quick Analysis Rules

### **1. Drop Constants**
- O(2n) = O(n)
- O(n/2) = O(n)
- O(3n² + 5n + 2) = O(n²)

### **2. Focus on Dominant Term**
- O(n² + n + 1) = O(n²)
- O(n log n + n) = O(n log n)
- O(2ⁿ + n³) = O(2ⁿ)

### **3. Different Input Variables**
- O(n + m) - Don't simplify to O(n)
- O(n × m) - Two different inputs

### **4. Sequential vs Nested**
```cpp
// Sequential: O(n + m) = O(n)
for (int i = 0; i < n; i++) { /* O(1) */ }
for (int j = 0; j < n; j++) { /* O(1) */ }

// Nested: O(n × m) = O(n²)
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) { /* O(1) */ }
}
```

### **5. Recursive Complexity**
```cpp
// T(n) = T(n-1) + O(1) → O(n)
// T(n) = T(n/2) + O(1) → O(log n)
// T(n) = 2T(n/2) + O(n) → O(n log n)
// T(n) = 2T(n-1) + O(1) → O(2ⁿ)
```

---

## 🎯 Interview Pro Tips

### **When to Mention Complexity**
1. **Before coding**: "I'll use a hash map for O(1) lookups"
2. **During coding**: "This gives us O(n) time, O(1) space"
3. **After coding**: "Time: O(n log n), Space: O(1)"

### **Space Complexity Don't Forget**
- **Input space doesn't count** (unless you modify it)
- **Recursion uses O(h) space** for call stack
- **Hash tables use O(n) space** for storage

### **Common Optimizations**
- **O(n²) → O(n)**: Use hash table instead of nested loops
- **O(n log n) → O(n)**: Counting sort for limited range
- **O(n) space → O(1)**: Two pointers instead of extra array

---

## 📊 Space vs Time Tradeoffs

| Problem | Time-Optimized | Space-Optimized |
|---------|----------------|-----------------|
| **Two Sum** | O(n) time, O(n) space (hash) | O(n²) time, O(1) space |
| **Fibonacci** | O(n) time, O(1) space (iterative) | O(n) time, O(n) space (memoization) |
| **Reverse Array** | O(n) time, O(1) space (in-place) | O(n) time, O(n) space (new array) |

---

## 🚨 Red Flags in Interviews

### **Avoid These Complexities**
- **O(n!)**: Factorial time (permutations without pruning)
- **O(2ⁿ)**: Exponential time (naive recursion)
- **O(n³)**: Cubic time (usually can be optimized)

### **When Exponential is Acceptable**
- Small input sizes (n ≤ 20)
- No better algorithm exists
- Approximation algorithms available

---

**💡 Master Tip**: Practice explaining complexity in simple terms:
*"This algorithm visits each element once, so it's O(n) linear time."*

---

**🎯 Next Steps**: Practice analyzing code complexity in `Code-Library/Templates/` examples! 