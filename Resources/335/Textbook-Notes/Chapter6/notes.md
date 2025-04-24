# Binary Heaps & Priority Queues: A Learning Guide

## 1. Priority Queues (Heaps)

### 1.1 What is a Priority Queue?
A priority queue is an abstract data type (ADT) that allows at least the following operations:
- **insert**: Add an element to the queue
- **deleteMin**: Find, return, and remove the minimum element in the queue

Unlike a standard queue (FIFO), a priority queue retrieves elements based on priority rather than insertion order. The element with the highest priority (typically the minimum value) is always removed first.

### 1.2 Simple Implementations

#### 1.2.1 Unsorted Linked List
- **Strategy**: Insert at front, search entire list for minimum when needed
- **Time Complexities**:
  - `insert`: O(1) - Constant time operation
  - `deleteMin`: O(N) - Must search all N elements
- **When it's useful**: If you have many more insertions than deletions

#### 1.2.2 Sorted Linked List
- **Strategy**: Keep list sorted during insertion
- **Time Complexities**:
  - `insert`: O(N) - Must find correct position
  - `deleteMin`: O(1) - Simply remove from front
- **When it's useful**: If you have many more deletions than insertions

#### 1.2.3 Why Binary Heaps?
The above implementations represent trade-offs between efficient insertion and efficient deletion. Binary heaps provide a balanced approach with logarithmic time for both operations.

## 2. Binary Heap Structure & Properties

### 2.1 Complete Binary Tree
A binary heap is organized as a complete binary tree:
- Filled at all levels, except possibly the last level
- The last level is filled from left to right
- All nodes are as far left as possible

**Example of Complete Binary Tree:**
```
       10
     /    \
    15    30
   / \    /
  40 50  100
```

### 2.2 Heap-Order Property
In a min-heap:
- Each node must be less than or equal to all of its descendants
- The minimum element is always at the root

In a max-heap:
- Each node must be greater than or equal to all of its descendants
- The maximum element is always at the root

This guide focuses primarily on min-heaps.

### 2.3 Array Representation
Binary heaps are typically implemented using arrays, not linked nodes, which provides:
- Memory efficiency (no pointers)
- Cache-friendly access patterns
- Simple index-based navigation

**For an element at index i**:
- Left child: 2i
- Right child: 2i + 1
- Parent: ⌊i/2⌋

**Example Mapping**: The tree below as an array would be [-, 10, 15, 30, 40, 50, 100]
```
       10 (1)
     /        \
  15 (2)     30 (3)
   / \        /
40(4) 50(5) 100(6)
```
*(Note: Array indexing typically starts at 1 for easier parent-child calculations)*

## 3. Core Heap Operations

### 3.1 findMin
- **Description**: Returns the minimum element (but doesn't remove it)
- **Implementation**: Simply return the element at the root (index 1)
- **Time Complexity**: O(1)

### 3.2 insert

#### Process:
1. Add the new element at the next available position (to maintain completeness)
2. If heap order is violated, "percolate up" the element until heap order is restored

#### Percolate Up Algorithm:
1. Compare the element with its parent
2. If the element is smaller than its parent, swap them
3. Repeat until heap order is satisfied or we reach the root

#### Example - Inserting 5 into:
```
      10
    /    \
   15    30
  / \    /
 40 50  100
```

**Step 1**: Add 5 at the next available position
```
      10
    /    \
   15    30
  / \    / \
 40 50  100 5
```

**Steps 2-4**: Percolate up until heap order is restored
```
      5
    /   \
   10    30
  / \    / \
 40 15  100 50
```

**Time Complexity**: O(log N) worst case (path from leaf to root)

### 3.3 deleteMin

#### Process:
1. Save the minimum element (root) to return later
2. Move the last element in the heap to the root
3. "Percolate down" this element until heap order is restored
4. Return the saved minimum element

#### Percolate Down Algorithm:
1. Compare the element with its children
2. Swap with the smaller child if it's smaller than the element
3. Repeat until heap order is satisfied or we reach a leaf

#### Example - DeleteMin from:
```
      5
    /   \
   10    30
  / \    / \
 40 15  100 50
```

**Step 1**: Save 5, move 50 (last element) to root
```
      50
    /    \
   10    30
  / \    /
 40 15  100
```

**Steps 2-3**: Percolate down
```
      10
    /    \
   15    30
  / \    /
 40 50  100
```

**Time Complexity**: O(log N) worst case (path from root to leaf)

## 4. Advanced Heap Operations

### 4.1 decreaseKey(p, Δ)
- **Description**: Decreases the value at position p by amount Δ
- **Process**: Decrease the value, then percolate up
- **Time Complexity**: O(log N)
- **Real-world use**: Increasing priority of a process in an OS

### 4.2 increaseKey(p, Δ)
- **Description**: Increases the value at position p by amount Δ
- **Process**: Increase the value, then percolate down
- **Time Complexity**: O(log N)
- **Real-world use**: Decreasing priority of CPU-hogging processes

### 4.3 remove(p)
- **Description**: Removes the element at position p
- **Implementation**: 
  1. decreaseKey(p, ∞) to move it to the root
  2. deleteMin() to remove it
- **Time Complexity**: O(log N)
- **Real-world use**: Removing terminated processes from queue

### 4.4 buildHeap

#### Linear Time Construction
- **Description**: Builds a heap from an unordered array of N elements
- **Naive Approach**: N successive inserts - O(N log N)
- **Efficient Approach**: 
  1. Place all elements in array
  2. Starting from last non-leaf, percolate down each node
  3. Time complexity: O(N)

#### Mathematical Insight
For a perfect binary tree of height h with 2^(h+1)-1 nodes:
- Sum of heights of all nodes = 2^(h+1) - 1 - (h + 1)
- This property helps prove that buildHeap is O(N), not O(N log N)

## 5. Applications of Priority Queues

### 5.1 Selection Problem

#### Problem Definition
Find the kth largest element in a list of N elements.

#### Approaches:
1. **Sort All Elements** - O(N log N)
2. **Algorithm 6A**: 
   - Build min-heap of all N elements: O(N)
   - Perform k deleteMin operations: O(k log N)
   - Total: O(N + k log N)
3. **Algorithm 6B**:
   - Build min-heap of first k elements: O(k)
   - For each remaining element:
     - If larger than minimum in heap, replace minimum
   - Total: O(N log k)
4. **Advanced Algorithms** (mentioned in text):
   - O(N) average time (quickselect)
   - O(N) worst-case time (median of medians)

#### Example:
Finding the 3rd largest element in [7, 2, 10, 4, 8, 1, 5]:
- Using Algorithm 6B:
  1. Build min-heap of first 3 elements: [2, 7, 10]
  2. Process 4: Compare with 2, replace: [4, 7, 10]
  3. Process 8: Compare with 4, replace: [7, 8, 10]
  4. Process 1: Compare with 7, smaller, ignore
  5. Process 5: Compare with 7, smaller, ignore
  6. Result: 3rd largest is minimum of final heap: 7

### 5.2 Event Simulation

#### Problem Description
Simulate a queuing system (like bank tellers):
- k tellers serve customers who arrive and wait in line
- Each customer has an arrival time and service time
- Goal: Gather statistics on wait times, line lengths, etc.

#### Event-Driven Approach:
1. Use a priority queue to store events (arrivals, departures)
2. Process events in chronological order
3. For each arrival:
   - If teller available, assign customer and schedule departure
   - Otherwise, place in waiting queue
4. For each departure:
   - Free up teller
   - If customers waiting, assign next customer and schedule departure

#### Advantages:
- Processes only significant events, not every time unit
- Runtime: O(C log(k+1)) for C customers and k tellers
- Significantly more efficient than time-based simulation

## 6. Implementation Considerations

### 6.1 C++ Implementation Structure

```cpp
template <typename Comparable>
class BinaryHeap {
public:
    // Constructors
    BinaryHeap(int capacity = 100);
    BinaryHeap(const vector<Comparable> & items);
    
    // Core Operations
    bool isEmpty() const;
    const Comparable & findMin() const;
    void insert(const Comparable & x);
    void insert(Comparable && x);  // Move semantics
    void deleteMin();
    void deleteMin(Comparable & minItem);
    void makeEmpty();
    
private:
    int currentSize;               // Number of elements
    vector<Comparable> array;      // The heap array
    
    // Helper methods
    void buildHeap();              // For heapify constructor
    void percolateDown(int hole);  // For deleteMin and buildHeap
};
```

### 6.2 Common Implementation Tips

1. **Array Indexing**: 
   - Start at index 1 (not 0) to simplify parent/child calculations
   - If using 0-indexed arrays, adjust formulas: 
     - Left child: 2i + 1
     - Right child: 2i + 2
     - Parent: ⌊(i-1)/2⌋

2. **Percolate Optimizations**:
   - Avoid swaps by creating a "hole" and filling it at the end
   - This reduces the number of assignments by half

3. **Edge Cases**:
   - Handle nodes with only one child (especially in percolateDown)
   - Check array capacity before insertions

4. **Practical Applications**:
   - System scheduling
   - Network packet routing
   - Dijkstra's algorithm
   - Huffman coding
   - Median maintenance

## 7. Study Questions & Exercises

1. Draw the binary heap that results from inserting 10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, 2 in that order into an initially empty heap.

2. Implement the buildHeap method that constructs a heap in O(N) time. Test it with various inputs.

3. What is the result of performing deleteMin three times on the heap from question 1?

4. Implement a max-heap (where the maximum element is at the root). How would the operations differ?

5. Modify the binary heap implementation to support the decreaseKey operation efficiently.

6. Use a priority queue to sort an array of integers. What is the time complexity?

7. Compare the time complexity of heap sort with other sorting algorithms. When would you choose heap sort over other algorithms?

8. Design a simulation of a hospital emergency room using a priority queue based on the severity of cases.

# Detailed Explanation of Percolate Down

## What is Percolate Down?

Percolate down (also called "heapify" or "sift down") is a fundamental operation used in binary heaps to maintain the heap-order property. It's primarily used in two operations:
1. During `deleteMin`: After removing the root and moving the last element to the root
2. During `buildHeap`: To establish heap order from an unordered array

## The Percolate Down Algorithm

### Conceptual Steps:
1. Start with a "hole" at a particular position (usually the root for `deleteMin`)
2. Compare the element that needs to be placed (the "target element") with the children of the hole
3. Move the smaller child up to the hole position, creating a new hole at that child's position
4. Repeat steps 2-3 until either:
   - The target element is smaller than both children of the hole
   - The hole has no children (reached a leaf)
5. Place the target element in the final hole position

### Detailed Algorithm:

```
percolateDown(hole):
    target = elementToBeReinserted
    
    while hole has at least one child:
        // Find the smaller child
        if hole has only left child OR left child < right child:
            smallerChild = leftChild(hole)
        else:
            smallerChild = rightChild(hole)
            
        // Compare target with smaller child
        if target <= element at smallerChild:
            // Target belongs here, we're done
            break
        
        // Move smaller child up to the hole
        array[hole] = array[smallerChild]
        
        // Move hole down to the smaller child
        hole = smallerChild
    
    // Place target in final hole position
    array[hole] = target
```

## Visual Example

Let's see how percolate down works during a `deleteMin` operation on this heap:

```
      10
    /    \
   15    30
  / \    / \
 40 50  100 60
```

**Step 1**: Remove 10 (min), and move the last element (60) to the root position
```
      60*
    /    \
   15    30
  / \    /
 40 50  100
```

**Step 2**: Compare 60 with its children (15 and 30)
- 15 < 30, so 15 is the smaller child
- 60 > 15, so move 15 up and hole down

```
      15
    /    \
   60*   30
  / \    /
 40 50  100
```

**Step 3**: Compare 60 with its children (40 and 50)
- 40 < 50, so 40 is the smaller child
- 60 > 40, so move 40 up and hole down

```
      15
    /    \
   40    30
  / \    /
 60* 50  100
```

**Step 4**: The hole has no children (it's a leaf), so place 60 in the hole
```
      15
    /    \
   40    30
  / \    /
 60  50  100
```

The percolate down operation is complete, and the heap order has been restored.

## Implementation Optimizations

### 1. Avoiding Swaps
Rather than swapping elements at each step, the algorithm creates a "hole" and only makes the final assignment at the end:
- This reduces the number of assignments from 3 per swap to just 1 per level
- For example, instead of:
  ```
  temp = array[hole]
  array[hole] = array[smallerChild]
  array[smallerChild] = temp
  ```
- We do:
  ```
  array[hole] = array[smallerChild]
  hole = smallerChild
  ```
  And only at the end: `array[hole] = target`

### 2. Common Error: Handling the One-Child Case
A frequent implementation error occurs when a node has only one child. You must:
- Check if the right child exists before comparing
- Only consider the left child if there is no right child
- This usually happens at the second-to-last level of the heap

### 3. Array Boundary Checks
When implementing percolate down, always ensure that child indices are within the array bounds:
- Check that `leftChild(hole) <= currentSize` before accessing the left child
- Check that `rightChild(hole) <= currentSize` before accessing the right child

## Performance Analysis

- Each percolate down operation may require moving down from the root to a leaf
- In a heap with N elements, the height is approximately log₂N
- Therefore, the worst-case time complexity is O(log N)
- However, the average depth to which an element percolates is generally much less than log N

## Role in BuildHeap

When building a heap from an unsorted array:
1. Start from the last non-leaf node (index `N/2`) and work backwards to the root
2. Apply percolate down to each node
3. This establishes the heap order in O(N) time

The intuition is that:
- Leaf nodes (which make up about half the heap) don't need percolate down
- Nodes higher in the tree require more work but there are fewer of them
- Mathematical analysis shows this process is linear, not O(N log N)
