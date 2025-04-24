# Homework 6: Heaps - Solutions and Explanations

## Part 1: Textbook Questions

### 6.1 Insert and FindMin Time Complexity

**Question:** Can both insert and `findMin` be implemented in constant time?

**Answer:** No, both operations cannot be constant time simultaneously.

**Explanation:**
- `findMin` is always O(1) in a min heap because the minimum element is always at the root (index 1).
- `insert` requires O(log N) time in the worst case. When inserting an element:
  - The new element is placed at the end of the heap
  - It then needs to "bubble up" (percolate up) to maintain the heap property
  - In the worst case, it might need to move all the way up to the root, which takes O(log N) time
  - In the best case (when the element is larger than its parent), insert can be O(1)

The fundamental constraint is that to maintain the heap property where the minimum element is always at the root, you must spend time organizing the elements when inserting them.

### 6.2 Binary Heap Construction

**a. Show the result of inserting 10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, and 2, one at a time, into an initially empty binary heap.**

Step-by-step construction by insertion:

1. Start with: [10]
2. Insert 12: [10, 12]
3. Insert 1: [1, 10, 12]
4. Insert 14: [1, 10, 12, 14]
5. Insert 6: [1, 6, 12, 14, 10]
6. Insert 5: [1, 6, 5, 14, 10, 12]
7. Insert 8: [1, 6, 5, 14, 10, 12, 8]
8. Insert 15: [1, 6, 5, 14, 10, 12, 8, 15]
9. Insert 3: [1, 3, 5, 6, 10, 12, 8, 15, 14]
10. Insert 9: [1, 3, 5, 6, 9, 12, 8, 15, 14, 10]
11. Insert 7: [1, 3, 5, 6, 9, 12, 7, 15, 14, 10, 8]
12. Insert 4: [1, 3, 5, 4, 9, 12, 7, 15, 14, 10, 8, 6]
13. Insert 11: [1, 3, 5, 4, 9, 11, 7, 15, 14, 10, 8, 6, 12]
14. Insert 13: [1, 3, 5, 4, 9, 11, 7, 15, 14, 10, 8, 6, 12, 13]
15. Insert 2: [1, 2, 5, 4, 3, 11, 7, 15, 14, 10, 8, 6, 12, 13, 9]

Final min heap:
```
          1
       /     \
      2       5
    /   \    / \
   4     3  11  7
  / \   / \  / \
15  14 10 8 6  12
/ \
13 9
```

**b. Show the result of using the linear-time algorithm to build a binary heap using the same input.**

The linear-time buildHeap algorithm works by:
1. Placing all elements in the array (without concern for heap property)
2. Starting from the last non-leaf node (index n/2), perform percolateDown on each node

Starting with array: [10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, 2]

1. Last non-leaf node is at index 7 (value 8). Percolate down.
2. Move to index 6 (value 5). Percolate down.
3. Continue up to index 1 (value 10).

The resulting min heap after buildHeap would be:
[1, 2, 5, 3, 6, 11, 8, 15, 4, 9, 7, 10, 12, 13, 14]

In tree form:
```
          1
       /     \
      2       5
    /   \    / \
   3     6  11  8
  / \   / \  / \
15  4  9  7 10 12
/ \
13 14
```

### 6.3 DeleteMin Operations

Perform three deleteMin operations on the heap from 6.2.

Starting with the heap from 6.2b: [1, 2, 5, 3, 6, 11, 8, 15, 4, 9, 7, 10, 12, 13, 14]

**First deleteMin:**
1. Remove 1 (root)
2. Replace with 14 (last element)
3. Percolate down: Swap 14 with 2, then with 3, then with 4
4. Result: [2, 3, 5, 4, 6, 11, 8, 15, 14, 9, 7, 10, 12, 13]

**Second deleteMin:**
1. Remove 2 (root)
2. Replace with 13 (last element)
3. Percolate down: Swap 13 with 3, then with 4
4. Result: [3, 4, 5, 13, 6, 11, 8, 15, 14, 9, 7, 10, 12]

**Third deleteMin:**
1. Remove 3 (root)
2. Replace with 12 (last element)
3. Percolate down: Swap 12 with 4, then with 13
4. Result: [4, 6, 5, 13, 9, 11, 8, 15, 14, 12, 7, 10]

After three deleteMin operations, the heap is:
```
         4
      /     \
     6       5
   /   \    / \
  13    9  11  8
 / \   / \
15 14 12  7
     /
    10
```

### 6.4 Array Size for Binary Trees

**a. A binary tree that has two extra levels (slightly unbalanced)**

For a complete binary tree with N nodes, the array size needed is N.
If we add two extra levels, the maximum number of nodes becomes:
- Complete tree with height h has 2^h - 1 nodes
- With 2 extra levels: 2^(h+2) - 1 = 4 * 2^h - 1 = 4N - 3

So the array must be of size 4N - 3 in the worst case.

**b. A binary tree that has a deepest node at depth 2 log N**

The depth of a complete binary tree with N nodes is approximately log₂N.
If the deepest node is at depth 2 log₂N, the array size needed is:
2^(2 log₂N) = N^2

So the array must be of size N^2 in the worst case.

**c. A binary tree that has a deepest node at depth 4.1 log N**

Similarly, the array size needed is:
2^(4.1 log₂N) = N^4.1

So the array must be of size N^4.1 in the worst case.

**d. The worst-case binary tree**

The worst case is a completely skewed tree (essentially a linked list) where each node has only a right child. For a tree with N nodes, the maximum index is 2^N - 1.

So the array must be of size 2^N - 1 in the worst case.

### 6.5 Rewrite BinaryHeap insert routine with sentinel

```cpp
void insert(const Comparable & x) {
    // Use position 0 to store the item being inserted
    array[0] = x;
    
    // If the heap is full, resize the array
    if(currentSize == array.size() - 1)
        array.resize(array.size() * 2);
    
    // Create a hole at the end of the heap
    int hole = ++currentSize;
    
    // Percolate up: while the hole's parent is greater than x,
    // move the parent down and move the hole up
    while(x < array[hole/2]) {
        array[hole] = array[hole/2];
        hole /= 2;
    }
    
    // Place x in the final hole position
    array[hole] = x;
}
```

This implementation uses position 0 as a sentinel to simplify the percolate up process. The key advantages are:
1. No need to check if we've reached the root (index 1) in the loop condition
2. No need for a separate temporary variable to store x during percolation
3. Slightly more efficient and cleaner code

### 6.6 Number of nodes in the large heap in Figure 6.13

The heap in Figure 6.13 appears to be a complete binary tree with height h = 8 (the longest path from root to leaf).

A complete binary tree with height h has between 2^h and 2^(h+1) - 1 nodes.
For h = 8, that's between 2^8 = 256 and 2^9 - 1 = 511 nodes.

### 6.7 BuildHeap Comparisons

**Prove that buildHeap does at most 2N-2 comparisons between elements.**

1. The number of comparisons in percolateDown depends on the height of the node
2. A node at height h requires at most 2h comparisons
3. In a heap of N elements, the number of nodes at height h is at most ⌊N/2^(h+1)⌋
4. Total comparisons = ∑(h=0 to log N) 2h·⌊N/2^(h+1)⌋

This sum can be proven to be at most 2N-2 by:
- Substituting ⌊N/2^(h+1)⌋ with N/2^(h+1)
- Simplifying the sum: 2N·∑(h=0 to log N) h/2^(h+1)
- This geometric series converges to 2N-2

### 6.8 Maximum Item in a Heap

**a. Prove that the maximum item in the heap must be at one of the leaves**

In a min heap, every node is less than or equal to its children. Therefore, any non-leaf node is smaller than both its children, which means it cannot be the maximum element. The maximum must be at a leaf node.

**b. Prove that there are exactly ⌊N/2⌋ leaves**

In a complete binary tree with N nodes:
- Nodes are numbered 1 to N level by level
- Leaf nodes are those without children
- A node i is a leaf if 2i > N (its left child index exceeds N)
- The first leaf node is at index ⌊N/2⌋ + 1
- The number of leaves is N - ⌊N/2⌋ = ⌈N/2⌉

Therefore, a heap with N nodes has exactly ⌈N/2⌉ leaves.

**c. Every leaf must be examined to find the maximum**

Since the maximum element can be any of the leaves, and there's no ordering among leaves in a min heap, we must examine every leaf to find the maximum element. There's no way to determine which leaf contains the maximum without checking each one.

### 6.10 Finding Nodes Less Than Value X

**a. Algorithm to find all nodes less than some value X in O(K) time**

```
findLessThanX(heap, X):
    result = empty list
    if heap is empty or heap.root >= X:
        return result
    
    Q = queue containing the root
    while Q is not empty:
        node = Q.dequeue()
        result.add(node)
        
        if node.left exists and node.left.value < X:
            Q.enqueue(node.left)
        if node.right exists and node.right.value < X:
            Q.enqueue(node.right)
    
    return result
```

This algorithm performs a modified breadth-first search, only visiting nodes with values less than X. Since we only process nodes that will be included in the result, the time complexity is O(K) where K is the number of nodes with values less than X.

**b. Extension to other heap structures**

This algorithm works for:
- Binary heaps: Direct application
- Leftist heaps: Works the same way
- Skew heaps: Works the same way

For Binomial and Fibonacci heaps, which consist of multiple trees, the algorithm would need to be modified to:
1. Start with all roots that are less than X
2. Apply the same BFS-like approach to each tree

### 6.18 Min-Max Heap

**a. Finding minimum and maximum elements**

In a min-max heap:
- The minimum element is at the root (index 1) since even-depth levels (including 0) follow min-heap property
- The maximum element is the largest among the children of the root (typically indices 2 and 3) since odd-depth levels follow max-heap property

**b. Algorithm to insert a new node**

```
insert(x):
    // Add the new element at the end of the heap
    heap[++size] = x
    
    // Percolate up based on level
    percolateUp(size)

percolateUp(i):
    // If at even level (min level)
    if (level(i) is even):
        // If element is greater than its parent (violating min-heap property)
        if (i > 1 and heap[i] > heap[parent(i)]):
            // Swap with parent
            swap(heap[i], heap[parent(i)])
            // Percolate up following max-heap property
            maxPercolateUp(parent(i))
        else:
            // Percolate up following min-heap property
            minPercolateUp(i)
    // If at odd level (max level)
    else:
        // If element is less than its parent (violating max-heap property)
        if (i > 1 and heap[i] < heap[parent(i)]):
            // Swap with parent
            swap(heap[i], heap[parent(i)])
            // Percolate up following min-heap property
            minPercolateUp(parent(i))
        else:
            // Percolate up following max-heap property
            maxPercolateUp(i)
```

**c. Algorithm for deleteMin and deleteMax**

```
deleteMin():
    // Save the minimum (root)
    min = heap[1]
    
    // Replace root with last element
    heap[1] = heap[size--]
    
    // Percolate down through min levels
    minPercolateDown(1)
    
    return min

deleteMax():
    // Find the maximum among root's children
    if (size <= 1):
        return null // No maximum
    
    maxIndex = 2 // Assume left child is max
    if (size > 2 and heap[3] > heap[2]):
        maxIndex = 3 // Right child is max
    
    // Save the maximum
    max = heap[maxIndex]
    
    // Replace max with last element
    heap[maxIndex] = heap[size--]
    
    // Percolate down through max levels
    maxPercolateDown(maxIndex)
    
    return max
```

**d. Building a min-max heap in linear time**

Yes, a min-max heap can be built in linear time using a bottom-up approach similar to the standard buildHeap algorithm:

```
buildMinMaxHeap(array):
    // Initialize heap with array elements
    heap = array
    size = array.length
    
    // Start from the last non-leaf node and percolate down
    for (i = size/2; i >= 1; i--):
        if (level(i) is even):
            minPercolateDown(i)
        else:
            maxPercolateDown(i)
```

This algorithm has O(n) time complexity using the same analysis as the standard buildHeap algorithm.

## Part 2: DeleteMin Operation

Perform a deleteMin operation on the min heap: `[-, 3, 6, 5, 7, 12, 9, 13, 11, 8]`

**Step 1:** Save the minimum (3) from the root and replace it with the last element (8)
- Heap becomes: `[-, 8, 6, 5, 7, 12, 9, 13, 11, -]`

**Step 2:** Percolate down - Compare 8 with its children (6 and 5)
- 5 is smaller, so swap 8 with 5
- Heap becomes: `[-, 5, 6, 8, 7, 12, 9, 13, 11, -]`

**Step 3:** Continue percolating down from position 3
- Compare 8 with its children (7 and 9)
- 7 is smaller, so swap 8 with 7
- Heap becomes: `[-, 5, 6, 7, 8, 12, 9, 13, 11, -]`

The final min heap after deleteMin is: `[-, 5, 6, 7, 8, 12, 9, 13, 11]`

## Part 3: Kth Largest Element in a Stream

**Problem:** Implement a class that maintains the kth largest element in a stream of integers.

```cpp
class KthLargest {
private:
    priority_queue<int, vector<int>, greater<int>> min_heap; // Min heap
    int k;
    
public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        // Initialize with elements from nums
        for (int num : nums) {
            add(num);
        }
    }
    
    int add(int val) {
        // If heap size < k, just add the element
        if (min_heap.size() < k) {
            min_heap.push(val);
        } 
        // If the new element is larger than the smallest element in heap
        else if (val > min_heap.top()) {
            min_heap.pop(); // Remove the smallest
            min_heap.push(val); // Add the new element
        }
        
        // Return the kth largest (top of min heap)
        return min_heap.top();
    }
};
```

**Explanation:**
- We maintain a min heap of size k that contains the k largest elements seen so far
- The smallest element in this heap (the root) is the kth largest element overall
- When adding a new element:
  - If the heap has fewer than k elements, we add it
  - If the heap is full, we add the new element only if it's larger than the smallest element in the heap
  - This ensures we always maintain the k largest elements

**Time Complexity:**
- Initialization: O(n log k) - we process n elements with log k operations each
- Add operation: O(log k) - heap operations are logarithmic in the size of the heap

**Space Complexity:** O(k) - we maintain a heap of at most k elements

## Part 4: Efficiency Improvements

To improve the efficiency of the KthLargest solution by directly manipulating the underlying vector:

```cpp
class KthLargest {
private:
    vector<int> heap; // Min heap
    int k;
    
public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        // Reserve space to avoid reallocations
        heap.reserve(k + 1);
        
        // Process the initial elements
        for (int num : nums) {
            add(num);
        }
    }
    
    int add(int val) {
        // If heap has fewer than k elements
        if (heap.size() < k) {
            heap.push_back(val);
            // Percolate up
            int index = heap.size() - 1;
            while (index > 0 && heap[(index - 1) / 2] > heap[index]) {
                swap(heap[index], heap[(index - 1) / 2]);
                index = (index - 1) / 2;
            }
        } 
        // If the new element is larger than the smallest element
        else if (val > heap[0]) {
            // Replace the root with the new element
            heap[0] = val;
            // Percolate down
            int index = 0;
            while (true) {
                int smallest = index;
                int left = 2 * index + 1;
                int right = 2 * index + 2;
                
                if (left < heap.size() && heap[left] < heap[smallest])
                    smallest = left;
                if (right < heap.size() && heap[right] < heap[smallest])
                    smallest = right;
                
                if (smallest == index)
                    break;
                    
                swap(heap[index], heap[smallest]);
                index = smallest;
            }
        }
        
        // Return the kth largest (top of min heap)
        return heap.empty() ? -1 : heap[0];
    }
};
```

**Efficiency Improvements:**
1. **Memory Management:**
   - Reserving space for the vector upfront avoids costly reallocations
   - Direct array access is faster than using STL container methods

2. **Reduced Function Call Overhead:**
   - Implementing percolate up/down manually avoids the overhead of priority_queue methods
   - We can optimize the specific case we're handling (fixed-size min heap)

3. **Early Termination:**
   - We can add early-exit conditions specific to our use case
   - For example, if val <= heap[0] and the heap is full, we can return immediately

4. **Cache Efficiency:**
   - Contiguous memory in a vector provides better cache locality
   - Custom implementation allows for more cache-friendly operations

This custom implementation can be more efficient than using STL priority_queue, especially for specific use cases like this one where we maintain a fixed-size heap and have a specialized insertion pattern.
