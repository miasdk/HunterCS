# CSCI 335 Comprehensive Exam 2 Study Guide

This guide combines insights from Homework 5, 6, 7, and previous exam patterns to create a complete preparation resource for your upcoming exam.

## Table of Contents
1. [Topic Distribution & Focus Areas](#topic-distribution--focus-areas)
2. [Sorting Algorithms](#sorting-algorithms)
3. [Heap Operations](#heap-operations)
4. [Hash Tables](#hash-tables)
5. [C++ STL Implementation](#c-stl-implementation)
6. [Practice Problems](#practice-problems)
7. [Key Time Complexities to Memorize](#key-time-complexities-to-memorize)
8. [Exam Preparation Strategy](#exam-preparation-strategy)

## Topic Distribution & Focus Areas

Based on previous exams and homework assignments, here's the recommended focus distribution:

| Topic | Percentage | Key Focus Areas |
|-------|------------|----------------|
| **Heap Operations** | 33% | Insertion, deleteMin, buildHeap, complexity analysis |
| **Sorting Algorithms** | 25% | Quicksort, Heapsort, Mergesort, Introsort |
| **Hash Tables** | 20% | Quadratic probing, load factors, collision resolution |
| **STL Implementation** | 22% | Time complexities, hash maps, container usage |

## Sorting Algorithms

### Quicksort
- **Algorithm**: Select pivot, partition array, recursively sort partitions
- **Hoare Partitioning**:
  1. Choose pivot (often median-of-three)
  2. Swap pivot with last element
  3. Two pointers approach: left pointer finds element ≥ pivot, right pointer finds element ≤ pivot
  4. Swap elements at these pointers, continue until pointers cross
  5. Swap pivot back to its correct position
- **Time Complexity**:
  - Best/Average: O(n log n)
  - Worst: O(n²) with poor pivot choice
- **Space Complexity**: O(log n) for recursion
- **Pivot Selection Strategies**:
  - First element (poor for sorted data)
  - Random element (robust)
  - Median-of-three (first, middle, last)
- **Optimization**: Use insertion sort for small partitions (cutoff)

### Heapsort
- **Algorithm**:
  1. Build max heap from array (buildHeap)
  2. Repeatedly extract max and place at end
  3. Reduce heap size and restore heap property
- **Time Complexity**: Always O(n log n)
- **Space Complexity**: O(1) in-place
- **Key Operations**:
  - buildHeap: O(n)
  - extractMax: O(log n) × n times = O(n log n)
- **Implementation with STL**:
  ```cpp
  void myHeapSort(std::vector<int> & nums) {
      std::make_heap(nums.begin(), nums.end());
      for (int i = nums.size() - 1; i > 0; i--) {
          std::pop_heap(nums.begin(), nums.begin() + i + 1);
      }
  }
  ```

### Mergesort
- **Algorithm**: Divide array, recursively sort halves, merge sorted halves
- **Time Complexity**: Always O(n log n)
- **Space Complexity**: O(n) for auxiliary array
- **Key Properties**:
  - Stable sort (preserves order of equal elements)
  - Good for linked lists
  - Predictable performance regardless of input

### Introsort
- **Algorithm**: Hybrid of quicksort, heapsort, and insertion sort
  1. Start with quicksort
  2. If recursion depth exceeds threshold (2×log n), switch to heapsort
  3. For small partitions, use insertion sort
- **Time Complexity**: O(n log n) worst case
- **Advantages**:
  - Combines best qualities of multiple algorithms
  - Good average-case performance
  - Guaranteed worst-case performance
  - Practical for both random and pathological inputs

## Heap Operations

### Binary Heap Structure
- Complete binary tree with heap-order property
- Min heap: parent ≤ children (min at root)
- Max heap: parent ≥ children (max at root)
- Array representation:
  - Parent(i) = ⌊(i-1)/2⌋
  - LeftChild(i) = 2i + 1
  - RightChild(i) = 2i + 2

### Key Operations
- **Insert**: O(log n)
  1. Add to end of heap
  2. Percolate up (compare with parent, swap if needed)
  3. Repeat until heap property restored

  ```cpp
  void insert(const Comparable & x) {
      // Use index 0 as sentinel
      array[0] = x;
      
      // Create hole at end of heap
      int hole = ++currentSize;
      
      // Percolate up
      while(x < array[hole/2]) {
          array[hole] = array[hole/2];
          hole /= 2;
      }
      
      array[hole] = x;
  }
  ```

- **DeleteMin/DeleteMax**: O(log n)
  1. Save root (min/max value)
  2. Replace root with last element
  3. Percolate down (compare with children, swap with smallest/largest)
  4. Repeat until heap property restored

- **BuildHeap**: O(n)
  1. Start with unsorted array
  2. Starting from last non-leaf node, percolate down each node
  3. More efficient than n insertions (O(n) vs O(n log n))

- **Finding Min in Max Heap**: O(n)
  1. Minimum must be in a leaf node
  2. Examine all leaves (roughly n/2 nodes)
  3. Return smallest value found

### Priority Queue Applications
- Implementing Dijkstra's algorithm
- Job scheduling
- Event-driven simulation
- Kth largest/smallest element

## Hash Tables

### Hash Function Design
- **Properties of Good Hash Functions**:
  - Distributes keys uniformly
  - Computationally efficient
  - Minimizes collisions
  - Deterministic

- **Common Hash Functions**:
  - Division method: h(k) = k mod m
  - Multiplication method: h(k) = ⌊m(kA mod 1)⌋
  - Universal hashing: randomly selected function

### Collision Resolution

#### Separate Chaining (Open Hashing)
- Each slot contains a linked list of elements
- Insertion: add to appropriate list
- Search: hash to find list, then search list
- Delete: hash to find list, then remove from list
- **Load Factor**: α = n/m (elements/slots)
  - Average operation time: O(1 + α)
  - Can exceed 1 (multiple items per slot)

#### Open Addressing (Closed Hashing)
- **Linear Probing**: h(k, i) = (h(k) + i) mod m
  - Simple but suffers from primary clustering

- **Quadratic Probing**: h(k, i) = (h(k) + i² + i)/2 mod m
  - Reduces primary clustering
  - May not find all slots (unless table size is prime)

- **Double Hashing**: h(k, i) = (h₁(k) + i·h₂(k)) mod m
  - Eliminates clustering
  - Requires second hash function

### Load Factors and Rehashing
- High load factor increases collision probability
- Rehashing:
  - Create larger table (typically double size)
  - Choose new hash function
  - Reinsert all elements
  - Time complexity: O(n)

### STL Hash Containers
- `unordered_set` and `unordered_map`
- Use separate chaining
- Default max load factor: 1.0
- Automatic rehashing when load factor exceeds max

## C++ STL Implementation

### Common Containers
- `vector`: Dynamic array (O(1) access)
- `list`: Doubly linked list (O(1) insert/remove with iterator)
- `map`/`set`: Red-black tree (O(log n) operations)
- `unordered_map`/`unordered_set`: Hash table (O(1) average operations)

### Time Complexities
- **vector**:
  - Access: O(1)
  - Insert/remove at end: O(1) amortized
  - Insert/remove elsewhere: O(n)

- **unordered_map**:
  - Insert/find/erase key: O(1) average, O(n) worst
  - Find value: O(n)

- **priority_queue**:
  - Push/pop: O(log n)
  - Top: O(1)

### Key STL Algorithm Functions
- `std::make_heap`: O(n)
- `std::push_heap`: O(log n)
- `std::pop_heap`: O(log n)
- `std::sort_heap`: O(n log n)

### Working with Hash Maps
```cpp
// Finding mode (most frequent element) using hash map
void findMode(vector<int>& nums) {
    unordered_map<int, int> counts;
    
    // Count occurrences
    for(int num : nums) {
        counts[num]++;
    }
    
    // Find maximum frequency
    int maxFreq = 0;
    int mode = 0;
    for(const auto& pair : counts) {
        if(pair.second > maxFreq) {
            maxFreq = pair.second;
            mode = pair.first;
        }
    }
    
    cout << "Mode: " << mode << " (occurs " << maxFreq << " times)" << endl;
}
```

## Practice Problems

### Problem 1: Hoare Partitioning
Partition the array [5, 9, 3, 7, 2, 8, 1, 6] using Hoare partitioning with pivot 5.

<details>
<summary>Solution</summary>

1. Swap pivot with last element: [6, 9, 3, 7, 2, 8, 1, 5]
2. Initialize i=0, j=6
3. Find element ≥ 5 from left: 6 at index 0
4. Find element ≤ 5 from right: 1 at index 6
5. Swap: [1, 9, 3, 7, 2, 8, 6, 5]
6. i=1, j=5
7. Find element ≥ 5 from left: 9 at index 1
8. Find element ≤ 5 from right: 2 at index 4
9. Swap: [1, 2, 3, 7, 9, 8, 6, 5]
10. i=3, j=3
11. Since i=j, partition complete
12. Swap pivot with element at position j: [1, 2, 3, 5, 9, 8, 6, 7]
13. Final partitioned array: [1, 2, 3, 5, 9, 8, 6, 7]
</details>

### Problem 2: Heap Insertion
Insert 3 into the min heap [5, 8, 6, 9, 12, 11, 7, 10].

<details>
<summary>Solution</summary>

1. Store 3 at index 0 (sentinel)
2. Insert at end: [5, 8, 6, 9, 12, 11, 7, 10, 3]
3. Percolate up:
   - Compare 3 with parent (12): 3 < 12, swap
   - [5, 8, 6, 9, 3, 11, 7, 10, 12]
   - Compare 3 with parent (8): 3 < 8, swap
   - [5, 3, 6, 9, 8, 11, 7, 10, 12]
   - Compare 3 with parent (5): 3 < 5, swap
   - [3, 5, 6, 9, 8, 11, 7, 10, 12]
4. Final heap: [3, 5, 6, 9, 8, 11, 7, 10, 12]
</details>

### Problem 3: Hash Table with Quadratic Probing
Insert 15, 27, 5, 10, 23 into a hash table with function h(x) = x mod 7 using quadratic probing.

<details>
<summary>Solution</summary>

1. Insert 15: h(15) = 1, place at index 1
2. Insert 27: h(27) = 6, place at index 6
3. Insert 5: h(5) = 5, place at index 5
4. Insert 10: h(10) = 3, place at index 3
5. Insert 23: h(23) = 2, place at index 2

Final table:
- Index 0: empty
- Index 1: 15
- Index 2: 23
- Index 3: 10
- Index 4: empty
- Index 5: 5
- Index 6: 27
</details>

### Problem 4: Complexity Analysis
What is the time complexity of:
```cpp
void mystery(vector<int>& nums) {
    int n = nums.size();
    for(int i = 1; i < n; i *= 2) {
        for(int j = 0; j < n; j++) {
            nums[j] += i;
        }
    }
}
```

<details>
<summary>Solution</summary>

1. Outer loop: i doubles each iteration (1, 2, 4, 8, ...) until reaching n
   - This takes log₂(n) iterations
2. Inner loop: Executes n times for each outer loop iteration
3. Total complexity: O(n log n)
</details>

## Key Time Complexities to Memorize

### Sorting Algorithms
- Insertion Sort: O(n²) average, O(n) best (sorted input)
- Heapsort: O(n log n) always
- Mergesort: O(n log n) always
- Quicksort: O(n log n) average, O(n²) worst
- Introsort: O(n log n) worst case

### Heap Operations
- BuildHeap: O(n) (not O(n log n))
- Insert: O(log n)
- DeleteMin/DeleteMax: O(log n)
- FindMin/FindMax: O(1)
- Find Min in Max Heap: O(n)

### Hash Table Operations
- Insert/Delete/Find: O(1) average, O(n) worst
- Rehashing: O(n)
- Find value (not key): O(n)

### STL Operations
- Rehashing (average case): O(n)
- Find key in unordered_map: O(1) average
- Find key in ordered map: O(log n)
- Partition around pivot: O(n)
- Quickselect (average): O(n)

## Exam Preparation Strategy

### Day Before Exam
1. **Review Key Algorithms** (2 hours)
   - Focus on Hoare partitioning (crucial!)
   - Heap operations (insert, deleteMin)
   - Introsort components and analysis

2. **Practice Complexity Analysis** (1.5 hours)
   - Work through the provided practice problems
   - Analyze runtime of different sorting algorithms
   - Study special cases (all equal elements, sorted input)

3. **Review Hash Tables** (1.5 hours)
   - Collision resolution strategies
   - Load factor impact on performance
   - Rehashing process

4. **Practice Tracing Algorithms** (2 hours)
   - Trace Hoare partitioning on paper
   - Practice heap insertion and deletion
   - Try hash table insertions with different probing strategies

5. **Review STL Implementation** (1 hour)
   - Container time complexities
   - Common operations and their costs
   - STL-based implementations

### Exam Day Tips
1. **Start with what you know**: Answer the questions you're confident about first
2. **Show your work**: For complexity analysis, explain your reasoning step-by-step
3. **Draw diagrams**: Visual representations help with heap and hash table questions
4. **Time management**: Allocate time proportional to point values
5. **Look for shortcuts**: Watch for special cases that simplify analysis

### Focus on High-Value Topics
1. **Hoare partitioning**: Last exam had a major question on this, and many students missed it
2. **Heap operations**: Consistent high-point questions (8-20 pts)
3. **Complexity analysis**: Appears in almost every question
4. **STL implementations**: Knowing container operations is essential

Good luck on your exam!
