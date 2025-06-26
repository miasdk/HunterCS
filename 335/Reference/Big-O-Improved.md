# Big-O Notation: Complete Complexity Analysis Guide

## 📋 Table of Contents
- [Overview](#overview)
- [Common Time Complexities](#common-time-complexities)
- [Data Structure Complexities](#data-structure-complexities)
- [Algorithm Complexities](#algorithm-complexities)
- [Complexity Analysis Examples](#complexity-analysis-examples)
- [Best, Average, and Worst Cases](#best-average-and-worst-cases)
- [Space Complexity](#space-complexity)
- [Quick Reference](#quick-reference)

---

## Overview

**Big-O notation** describes the performance or complexity of an algorithm. It measures how the runtime or space requirements grow as the input size increases.

### Key Concepts
- **Asymptotic Analysis**: Focuses on growth rate, not exact runtime
- **Upper Bound**: Big-O represents the worst-case scenario
- **Scalability**: How well an algorithm performs with larger inputs
- **Constants Ignored**: O(2n) = O(n), O(n² + n) = O(n²)

---

## Common Time Complexities

### **O(1) - Constant Time**
**Description**: Runtime doesn't depend on input size
**Examples**:
- Accessing array element by index
- Hash table lookup
- Stack push/pop operations

```cpp
int getFirstElement(int arr[], int size) {
    return arr[0];  // O(1) - always one operation
}
```

### **O(log n) - Logarithmic Time**
**Description**: Runtime grows logarithmically with input size
**Examples**:
- Binary search
- Balanced tree operations
- Divide-and-conquer algorithms

```cpp
int binarySearch(int arr[], int size, int target) {
    int left = 0, right = size - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;  // O(log n) - halves search space each iteration
}
```

### **O(n) - Linear Time**
**Description**: Runtime grows linearly with input size
**Examples**:
- Linear search
- Array traversal
- Linked list operations

```cpp
int findMax(int arr[], int size) {
    int max = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max) max = arr[i];
    }
    return max;  // O(n) - visits each element once
}
```

### **O(n log n) - Linearithmic Time**
**Description**: Runtime grows as n times log n
**Examples**:
- Merge sort
- Quick sort (average case)
- Heap sort

```cpp
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);      // O(n/2 log n/2)
        mergeSort(arr, mid + 1, right); // O(n/2 log n/2)
        merge(arr, left, mid, right);   // O(n)
    }
    // Total: O(n log n)
}
```

### **O(n²) - Quadratic Time**
**Description**: Runtime grows quadratically with input size
**Examples**:
- Bubble sort
- Selection sort
- Nested loops

```cpp
void bubbleSort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
    // O(n²) - nested loops
}
```

### **O(2ⁿ) - Exponential Time**
**Description**: Runtime grows exponentially with input size
**Examples**:
- Recursive Fibonacci
- Subset generation
- Traveling salesman (brute force)

```cpp
int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
    // O(2ⁿ) - each call creates 2 more calls
}
```

### **O(n!) - Factorial Time**
**Description**: Runtime grows factorially with input size
**Examples**:
- Permutation generation
- Traveling salesman (all permutations)
- N-queens problem (brute force)

---

## Data Structure Complexities

| Operation | Array | Linked List | Stack/Queue | Hash Table | BST | AVL Tree | Heap |
|-----------|-------|-------------|-------------|------------|-----|----------|------|
| **Access** | O(1) | O(n) | O(n) | O(1) | O(log n) | O(log n) | O(1) |
| **Search** | O(n) | O(n) | O(n) | O(1) | O(log n) | O(log n) | O(n) |
| **Insertion** | O(n) | O(1) | O(1) | O(1) | O(log n) | O(log n) | O(log n) |
| **Deletion** | O(n) | O(1) | O(1) | O(1) | O(log n) | O(log n) | O(log n) |

### **Key Insights**
- **Arrays**: Fast access, slow insertion/deletion
- **Linked Lists**: Fast insertion/deletion, slow access
- **Hash Tables**: Fast all operations, but no ordering
- **Trees**: Balanced trees provide consistent O(log n) performance
- **Heaps**: Optimized for finding min/max, O(log n) insertion/deletion

---

## Algorithm Complexities

### **Sorting Algorithms**

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable | In-Place |
|-----------|-----------|--------------|------------|-------|--------|----------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | No | Yes |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Yes |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes |

### **Search Algorithms**

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| **Linear Search** | O(n) | O(1) | Works on unsorted data |
| **Binary Search** | O(log n) | O(1) | Requires sorted data |
| **Hash Table Search** | O(1) | O(n) | Average case |

### **Graph Algorithms**

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| **BFS** | O(V + E) | O(V) | Uses queue |
| **DFS** | O(V + E) | O(V) | Uses stack/recursion |
| **Dijkstra's** | O((V + E) log V) | O(V) | With binary heap |
| **Prim's** | O(E log V) | O(V) | With binary heap |
| **Kruskal's** | O(E log E) | O(V) | With union-find |

---

## Complexity Analysis Examples

### **Example 1: Nested Loops**
```cpp
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        // O(1) operation
    }
}
```
**Analysis**: O(n²) - outer loop runs n times, inner loop runs n times for each outer iteration

### **Example 2: Sequential Loops**
```cpp
for (int i = 0; i < n; i++) {
    // O(1) operation
}
for (int j = 0; j < n; j++) {
    // O(1) operation
}
```
**Analysis**: O(n) - loops run sequentially, not nested

### **Example 3: Logarithmic Loop**
```cpp
for (int i = 1; i < n; i *= 2) {
    // O(1) operation
}
```
**Analysis**: O(log n) - i doubles each iteration, so loop runs log₂(n) times

### **Example 4: Mixed Complexity**
```cpp
for (int i = 0; i < n; i++) {
    for (int j = 0; j < i; j++) {
        // O(1) operation
    }
}
```
**Analysis**: O(n²) - inner loop runs 0, 1, 2, ..., n-1 times = n(n-1)/2 = O(n²)

---

## Best, Average, and Worst Cases

### **Best Case**
- **Definition**: Minimum time for any input of size n
- **Notation**: Ω (Big-Omega)
- **Example**: Linear search finding element at first position

### **Average Case**
- **Definition**: Expected time over all possible inputs
- **Notation**: Θ (Big-Theta) when best = worst
- **Example**: Quick sort with random pivot selection

### **Worst Case**
- **Definition**: Maximum time for any input of size n
- **Notation**: O (Big-O)
- **Example**: Linear search when element is not found

### **Example Analysis**
```cpp
int linearSearch(int arr[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}
```
- **Best Case**: Ω(1) - target found at first position
- **Average Case**: Θ(n/2) - target found in middle on average
- **Worst Case**: O(n) - target not found or at last position

---

## Space Complexity

### **Definition**
Space complexity measures the amount of memory an algorithm uses relative to input size.

### **Common Space Complexities**

| Complexity | Description | Examples |
|------------|-------------|----------|
| **O(1)** | Constant space | Variables, counters |
| **O(n)** | Linear space | Arrays, linked lists |
| **O(n²)** | Quadratic space | 2D arrays, adjacency matrices |
| **O(log n)** | Logarithmic space | Recursive algorithms |

### **Example: Recursive vs Iterative**
```cpp
// Recursive Fibonacci - O(n) space due to call stack
int fibRecursive(int n) {
    if (n <= 1) return n;
    return fibRecursive(n-1) + fibRecursive(n-2);
}

// Iterative Fibonacci - O(1) space
int fibIterative(int n) {
    if (n <= 1) return n;
    int prev = 0, curr = 1;
    for (int i = 2; i <= n; i++) {
        int next = prev + curr;
        prev = curr;
        curr = next;
    }
    return curr;
}
```

---

## Quick Reference

### **Complexity Hierarchy** (from fastest to slowest)
1. **O(1)** - Constant
2. **O(log n)** - Logarithmic
3. **O(n)** - Linear
4. **O(n log n)** - Linearithmic
5. **O(n²)** - Quadratic
6. **O(n³)** - Cubic
7. **O(2ⁿ)** - Exponential
8. **O(n!)** - Factorial

### **Common Patterns**
- **Single loop**: O(n)
- **Nested loops**: O(n × m) where n, m are loop bounds
- **Divide and conquer**: Usually O(n log n)
- **Recursive with branching**: Often exponential
- **Hash table operations**: O(1) average case

### **Memory vs Time Trade-offs**
- **Hash tables**: Fast lookup, more memory
- **Arrays**: Fast access, fixed size
- **Linked lists**: Dynamic size, slower access
- **Trees**: Balanced performance, moderate memory

### **Exam Tips**
1. **Always consider the worst case** unless specified otherwise
2. **Ignore constants** in Big-O analysis
3. **Focus on dominant terms** (highest power of n)
4. **Consider both time and space complexity**
5. **Remember that O(1) doesn't mean "instant"** - just constant time

---

## 🎯 Practice Problems

### **Problem 1: Analyze the complexity**
```cpp
int mystery(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i *= 2) {
        for (int j = 0; j < i; j++) {
            sum++;
        }
    }
    return sum;
}
```
**Answer**: O(n) - The inner loop runs 1 + 2 + 4 + ... + n times, which is approximately 2n

### **Problem 2: Compare algorithms**
Which is faster for large n: O(n log n) or O(n²)?
**Answer**: O(n log n) - For large n, log n grows much slower than n

### **Problem 3: Space complexity**
What's the space complexity of merge sort?
**Answer**: O(n) - Requires auxiliary array for merging

---

*Master these complexity concepts and you'll be able to analyze any algorithm's performance!* 