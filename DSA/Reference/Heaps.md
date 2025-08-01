# Comprehensive Guide to Heaps in C++

## Table of Contents
1. [Introduction to Heaps](#introduction-to-heaps)
2. [Heaps vs Priority Queues](#heaps-vs-priority-queues)
3. [Heap Properties](#heap-properties)
4. [Types of Heaps](#types-of-heaps)
5. [Heap Operations](#heap-operations)
   - [Basic Operations](#basic-operations)
   - [Advanced Operations](#advanced-operations)
   - [percolate_up and percolate_down](#percolate_up-and-percolate_down)
6. [Array Implementation](#array-implementation)
   - [0-Indexed Implementation](#0-indexed-implementation)
   - [1-Indexed Implementation](#1-indexed-implementation)
7. [C++ STL Implementation](#c-stl-implementation)
   - [Heap Algorithms](#heap-algorithms)
   - [Priority Queue](#priority-queue)
   - [Custom Comparators](#custom-comparators)
8. [Time and Space Complexity](#time-and-space-complexity)
   - [BuildHeap Analysis](#buildheap-analysis)
   - [Average-Case Analysis](#average-case-analysis)
9. [Implementation Examples](#implementation-examples)
10. [LeetCode Practice Problems](#leetcode-practice-problems)
11. [Advanced Heap Concepts](#advanced-heap-concepts)
12. [Tips and Best Practices](#tips-and-best-practices)

## Introduction to Heaps

A heap is a specialized tree-based data structure that satisfies the heap property. It is a complete binary tree, which means all levels of the tree are fully filled except possibly the last level, which is filled from left to right.

Heaps are commonly used to implement priority queues, which are essential for algorithms like Dijkstra's shortest path, Huffman coding, and heap sort.

## Heaps vs Priority Queues

It's important to understand the distinction between heaps and priority queues:

- **Priority Queue** is an abstract data type (ADT) that defines behavior: elements are served according to their priority rather than their insertion order.
- **Heap** is a specific data structure that efficiently implements the priority queue ADT.

While heaps are often used synonymously with priority queues, they are just one possible implementation of a priority queue (other implementations include ordered arrays or balanced binary search trees).

Priority queues have two primary operations:
1. Insert an element with priority
2. Remove and return the element with highest priority

Heaps excel at these operations but are less efficient for other operations like searching for arbitrary elements or changing the priority of existing elements.

## Heap Properties

1. **Structural Property**: A heap is a complete binary tree.
   - All levels, except possibly the last one, are completely filled.
   - The last level has all nodes as left as possible.

2. **Heap Order Property**: Depends on the type of heap (min heap or max heap).
   - For a **max heap**, the key at each node is greater than or equal to the keys of its children.
   - For a **min heap**, the key at each node is less than or equal to the keys of its children.

3. **Important Implications**:
   - The root always has the highest (max heap) or lowest (min heap) priority.
   - A node must have a higher/lower priority than all its descendants, but there is no guarantee about the relationship between nodes in different branches.
   - There is no implied ordering between siblings or nodes in different branches that are not in a direct ancestor-descendant relationship.

## Types of Heaps

### Max Heap
In a max heap, the key value of a node is greater than or equal to the key values of its children. The largest element is always at the root.

### Min Heap
In a min heap, the key value of a node is less than or equal to the key values of its children. The smallest element is always at the root.

### Other Variants
- **Binomial Heap**: A collection of binomial trees.
- **Fibonacci Heap**: A collection of trees with min-heap or max-heap property.
- **Leftist Heap**: A variant of binary heap where the "shortest path" is always on the right.

## Heap Operations

### Basic Operations

1. **make_heap**: Converting a range of elements into a heap. Time complexity: O(n).

2. **push_heap**: Adding an element to the heap.
   - The element is first added to the end of the range.
   - Then percolate_up is used to restore the heap property.
   - Time complexity: O(log n) worst case, O(1) average case.

3. **pop_heap**: Removing the top element (highest value in a max heap).
   - Moves the top element to the end of the range and reorganizes.
   - The percolate_down operation is used to restore the heap property.
   - Time complexity: O(log n).

4. **top/front**: Viewing the top element without removing it.
   - Time complexity: O(1).

### Advanced Operations

1. **decrease_key**: Decreasing the value of a key.
   - Update the key value.
   - percolate_up to restore the heap property.
   - Time complexity: O(log n).

2. **increase_key**: Increasing the value of a key.
   - Update the key value.
   - percolate_down to restore the heap property.
   - Time complexity: O(log n).

3. **delete**: Removing an arbitrary node from the heap.
   - Typically implemented by decreasing the key to the minimum/maximum, then extracting.
   - Time complexity: O(log n).

4. **merge**: Combining two heaps into one.
   - Time complexity varies by implementation (can be O(n) for binary heaps or O(1) for Fibonacci heaps).

### percolate_up and percolate_down

These are the key internal operations that maintain the heap property:

#### percolate_up
```cpp
void percolate_up(int hole) {
    T tmp = array[hole]; // Save the element
    
    // While not at root and parent has lower priority
    while (hole > 0 && compare(array[(hole-1)/2], tmp)) {
        array[hole] = array[(hole-1)/2]; // Move parent down
        hole = (hole-1)/2; // Move up to parent
    }
    
    array[hole] = tmp; // Place element in final position
}
```

#### percolate_down
```cpp
void percolate_down(int hole) {
    T tmp = array[hole]; // Save element
    int size = array.size();
    int child;
    
    while (2*hole + 1 < size) { // While we have a left child
        child = 2*hole + 1; // Left child
        
        // If right child exists and has higher priority
        if (child + 1 < size && compare(array[child], array[child+1]))
            child++; // Use right child
            
        // If child has higher priority than tmp
        if (compare(tmp, array[child]))
            array[hole] = array[child]; // Move child up
        else
            break; // Found correct position
            
        hole = child; // Move down to child
    }
    
    array[hole] = tmp; // Place element in final position
}
```

## Array Implementation

Since a heap is a complete binary tree, it can be efficiently represented as an array without explicit pointers.

### 0-Indexed Implementation

This is the most common implementation in C++ and the one used by the STL:

- The root is at index 0
- For a node at index `i`:
  - Parent is at index `(i-1)/2`
  - Left child is at index `2*i + 1`
  - Right child is at index `2*i + 2`

### 1-Indexed Implementation

This approach is commonly found in textbooks and some algorithms literature:

- The root is at index 1 (index 0 often used for temporary storage)
- For a node at index `i`:
  - Parent is at index `i/2`
  - Left child is at index `2*i`
  - Right child is at index `2*i + 1`
- All nodes at depth D are located at indices `2^D` through `2^(D+1) - 1`
  - For example, nodes at depth 3 are at indices 8-15

## C++ STL Implementation

C++ Standard Template Library (STL) provides two main ways to work with heaps:

### Heap Algorithms

The STL provides a set of heap algorithms in the `<algorithm>` header that operate on a range of elements to create and manipulate a heap. These functions work on any random-access container (like `std::vector`).

1. **`std::make_heap`**: Converts a range into a heap.
   ```cpp
   std::vector<int> v = {3, 1, 4, 1, 5, 9};
   std::make_heap(v.begin(), v.end()); // Creates a max heap by default
   // For min heap: std::make_heap(v.begin(), v.end(), std::greater<int>{});
   ```
   Time complexity: O(n).

2. **`std::push_heap`**: Adds an element to a heap.
   ```cpp
   v.push_back(6);
   std::push_heap(v.begin(), v.end());
   ```
   Time complexity: O(log n).

3. **`std::pop_heap`**: Removes the largest element from a heap.
   ```cpp
   std::pop_heap(v.begin(), v.end());
   int largest = v.back();
   v.pop_back();
   ```
   Time complexity: O(log n).

4. **`std::sort_heap`**: Sorts elements in a heap.
   ```cpp
   std::sort_heap(v.begin(), v.end());
   ```
   Time complexity: O(n log n).

5. **`std::is_heap`**: Checks if a range is a heap.
   ```cpp
   bool isHeap = std::is_heap(v.begin(), v.end());
   ```
   Time complexity: O(n).

6. **`std::is_heap_until`**: Finds the largest subrange that is a heap.
   ```cpp
   auto it = std::is_heap_until(v.begin(), v.end());
   ```
   Time complexity: O(n).

### Priority Queue

The `std::priority_queue` is a container adapter that provides heap functionality with a simpler interface. It is defined in the `<queue>` header.

```cpp
#include <queue>

// Max heap (default)
std::priority_queue<int> maxHeap;

// Min heap
std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
```

Key member functions:

1. **`push`**: Adds an element to the priority queue.
   ```cpp
   maxHeap.push(42);
   ```
   Time complexity: O(log n).

2. **`pop`**: Removes the top element from the priority queue.
   ```cpp
   maxHeap.pop();
   ```
   Time complexity: O(log n).

3. **`top`**: Returns a reference to the top element.
   ```cpp
   int highest = maxHeap.top();
   ```
   Time complexity: O(1).

4. **`size`**: Returns the number of elements.
   ```cpp
   size_t num = maxHeap.size();
   ```
   Time complexity: O(1).

5. **`empty`**: Checks if the container is empty.
   ```cpp
   bool isEmpty = maxHeap.empty();
   ```
   Time complexity: O(1).

### Custom Comparators

Both heap algorithms and priority queue can use custom comparators to define the ordering:

```cpp
// Custom comparison function
struct CompareHeight {
    bool operator()(const Person& a, const Person& b) {
        return a.height < b.height; // Max heap based on height
    }
};

// Using with priority_queue
std::priority_queue<Person, std::vector<Person>, CompareHeight> pq;

// Using with heap algorithms
std::make_heap(people.begin(), people.end(), CompareHeight());
```

## Time and Space Complexity

### Time Complexity

| Operation             | Binary Heap  | Binomial Heap | Fibonacci Heap |
|-----------------------|--------------|---------------|----------------|
| Find Min/Max          | O(1)         | O(log n)      | O(1)           |
| Insert                | O(log n)     | O(log n)      | O(1) amortized |
| Extract Min/Max       | O(log n)     | O(log n)      | O(log n) amortized |
| Decrease Key          | O(log n)     | O(log n)      | O(1) amortized |
| Merge                 | O(n)         | O(log n)      | O(1)           |
| Delete                | O(log n)     | O(log n)      | O(log n) amortized |
| Build Heap            | O(n)         | O(n)          | O(n)           |

### BuildHeap Analysis

While a naive analysis might suggest that building a heap by inserting n elements one by one would be O(n log n), a tighter analysis shows that it's actually O(n).

#### O(n) BuildHeap Algorithm
```cpp
void build_heap(std::vector<int>& arr) {
    // Start from the last non-leaf node
    for (int i = arr.size()/2 - 1; i >= 0; i--)
        percolate_down(arr, i, arr.size());
}
```

#### Proof of O(n) Time Complexity

The key insight is that not all nodes need to percolate the full log(n) height:

1. A binary heap with n nodes has approximately n/2 leaf nodes (nodes at the bottom level), which don't need any percolation.
2. The next level up has approximately n/4 nodes, each of which might percolate down at most 1 level.
3. The level above that has approximately n/8 nodes, each percolating at most 2 levels.
4. And so on...

This gives us the total work:
```
0·(n/2) + 1·(n/4) + 2·(n/8) + 3·(n/16) + 4·(n/32) + ...
```

This sum converges to n, making the overall time complexity O(n).

### Average-Case Analysis

#### Insert Operation

While insert has a worst-case time complexity of O(log n), the average-case time complexity is actually O(1) under certain conditions:

1. When elements being inserted have the same distribution as elements already in the heap
2. When insertions are not mixed with extractions (which would change the distribution)

In these cases, a newly inserted element is expected to percolate up only a constant number of levels on average.

#### Why O(1) Average Case?

If we assume random insertion, most elements will be placed near the bottom of the heap and will only need to move up a few levels. The probability that an element needs to percolate up to level h decreases exponentially with h.

This constant average behavior is particularly useful for building heaps incrementally in applications where the heap grows gradually.

### Space Complexity

- Binary Heap: O(n)
- Binomial Heap: O(n)
- Fibonacci Heap: O(n)

## Implementation Examples

### Binary Heap Implementation (Following STL Style)

```cpp
#include <vector>
#include <algorithm>
#include <stdexcept>

template <typename T, typename Compare = std::less<T>>
class BinaryHeap {
private:
    std::vector<T> data;
    Compare compare;

    // Helper functions for parent and child indices (0-indexed)
    size_t parent(size_t index) { return (index - 1) / 2; }
    size_t left_child(size_t index) { return 2 * index + 1; }
    size_t right_child(size_t index) { return 2 * index + 2; }

    // Restore heap property upward
    void percolate_up(size_t index) {
        T temp = data[index];  // Store the element

        // Move up until we find the right place
        while (index > 0 && compare(data[parent(index)], temp)) {
            data[index] = data[parent(index)];  // Move parent down
            index = parent(index);              // Move up
        }

        // Place the element in its final position
        data[index] = temp;
    }

    // Restore heap property downward
    void percolate_down(size_t index) {
        T temp = data[index];  // Store the element
        size_t size = data.size();
        size_t child;
        
        // While we have a left child
        while (left_child(index) < size) {
            child = left_child(index);
            
            // Choose the higher priority child
            if (child + 1 < size && compare(data[child], data[child + 1]))
                child++;  // Right child has higher priority
                
            // If child has higher priority than temp
            if (compare(temp, data[child]))
                data[index] = data[child];  // Move child up
            else
                break;  // Found correct position
                
            index = child;  // Move down to child
        }
        
        // Place the element in its final position
        data[index] = temp;
    }

public:
    BinaryHeap() {}
    
    void push(const T& value) {
        data.push_back(value);
        percolate_up(data.size() - 1);
    }
    
    T top() {
        if (empty()) {
            throw std::out_of_range("Heap is empty");
        }
        return data[0];
    }
    
    void pop() {
        if (empty()) {
            throw std::out_of_range("Heap is empty");
        }
        data[0] = data.back();
        data.pop_back();
        if (!empty()) {
            percolate_down(0);
        }
    }
    
    bool empty() const {
        return data.empty();
    }
    
    size_t size() const {
        return data.size();
    }
    
    // Build a heap from an unsorted array in O(n) time
    void make_heap() {
        for (int i = data.size() / 2 - 1; i >= 0; i--) {
            percolate_down(i);
        }
    }
};
```

### Using STL Priority Queue with Custom Objects

```cpp
#include <queue>
#include <string>
#include <vector>
#include <iostream>

struct Task {
    int priority;
    std::string name;
    
    Task(int p, const std::string& n) : priority(p), name(n) {}
    
    // For min heap (lower priority number means higher actual priority)
    bool operator<(const Task& other) const {
        return priority > other.priority;
    }
};

int main() {
    std::priority_queue<Task> taskQueue;
    
    taskQueue.push(Task(3, "Low priority task"));
    taskQueue.push(Task(1, "High priority task"));
    taskQueue.push(Task(2, "Medium priority task"));
    
    while (!taskQueue.empty()) {
        Task t = taskQueue.top();
        taskQueue.pop();
        std::cout << "Processing: " << t.name << " (Priority: " << t.priority << ")\n";
    }
    
    return 0;
}
```

## LeetCode Practice Problems

Here are some useful LeetCode problems to practice heap implementation and usage:

### Easy
1. **Last Stone Weight (Problem 1046)**
   - Description: We have a collection of stones, each stone has a positive integer weight. Each turn, we choose the two heaviest stones and smash them together.
   - Solution Approach: Use a max heap to repeatedly get the two heaviest stones.

### Medium
1. **Top K Frequent Elements (Problem 347)**
   - Description: Given an array of integers and an integer k, return the k most frequent elements.
   - Solution Approach: Use a hash map to count frequencies, then use a min heap of size k to maintain the top k elements.

2. **Kth Largest Element in an Array (Problem 215)**
   - Description: Find the kth largest element in an unsorted array.
   - Solution Approach: Use a min heap of size k to efficiently find the kth largest element.

3. **Find K Pairs with Smallest Sums (Problem 373)**
   - Description: Given two integer arrays nums1 and nums2 sorted in ascending order and an integer k, return the k pairs with the smallest sums.
   - Solution Approach: Use a min heap to efficiently find the k smallest pairs.

### Hard
1. **Merge k Sorted Lists (Problem 23)**
   - Description: Merge k sorted linked lists into one sorted linked list.
   - Solution Approach: Use a min heap to efficiently merge the lists.

2. **Find Median from Data Stream (Problem 295)**
   - Description: Design a data structure that supports adding integers and finding the median.
   - Solution Approach: Use two heaps (a max heap for the lower half and a min heap for the upper half).

3. **Sliding Window Maximum (Problem 239)**
   - Description: Given an array nums and a sliding window of size k, find the maximum element in each window.
   - Solution Approach: Use a heap to efficiently find the maximum in each window.

## Advanced Heap Concepts

### Binomial Heap
A binomial heap is a collection of binomial trees where each tree satisfies the heap property. It offers faster union/merge operations compared to binary heaps.

### Fibonacci Heap
A Fibonacci heap is a collection of trees with min-heap or max-heap property. It provides better amortized time complexity for several operations compared to binary heaps:
- Insert: O(1)
- Find Min/Max: O(1)
- Decrease Key: O(1) amortized
- Union: O(1)

### d-ary Heap
A d-ary heap is a generalization of a binary heap where each node has d children. It can offer better performance for extract-min and decrease-key operations depending on the value of d.

## Tips and Best Practices

1. **Choosing Between Heaps**:
   - Use binary heaps for simplicity and when memory usage is a concern.
   - Consider Fibonacci heaps when you need efficient decrease-key and merge operations.
   - Use binomial heaps when you need efficient merge operations with reasonable decrease-key performance.

2. **STL vs. Custom Implementation**:
   - Use STL's priority_queue when you need a simple priority queue with standard operations.
   - Use STL's heap algorithms when you need more control over the underlying container.
   - Implement a custom heap when you need specialized operations or behaviors.

3. **Performance Considerations**:
   - For large datasets, consider using a d-ary heap with d > 2 to improve the performance of decrease-key operations.
   - When frequently accessing random elements, consider using an indexed heap that allows O(1) access to any element.
   - For graphs with many edges and Dijkstra's algorithm, use a Fibonacci heap for better theoretical performance.
   - Remember that the make_heap operation is O(n), not O(n log n), and should be used when initializing a heap with many elements.

4. **Common Pitfalls**:
   - Forgetting to maintain the heap property after modifying elements.
   - Assuming that heaps provide O(1) access to arbitrary elements.
   - Incorrectly implementing custom comparators, leading to unexpected behavior.
   - Not distinguishing between a heap's conceptual structure (a complete binary tree) and its actual implementation (usually an array).

5. **Implementation Tips**:
   - For 1-indexed arrays (as often seen in textbooks), parent(i) = i/2, left_child(i) = 2*i, right_child(i) = 2*i + 1.
   - For 0-indexed arrays (common in practice), parent(i) = (i-1)/2, left_child(i) = 2*i + 1, right_child(i) = 2*i + 2.
   - Use the "hole" technique for percolation to reduce the number of element swaps.
   - Always handle edge cases properly (empty heap, only one element, etc.).

6. **Optimizing for Specific Use Cases**:
   - When the heap is used for a scheduler with deadlines, consider a calendar queue instead.
   - When operations have different frequencies (e.g., many insertions but few extractions), tune your implementation accordingly.
   - For applications that need both min and max elements frequently, consider a min-max heap.

7. **Heap vs. Other Data Structures**:
   - Heaps excel at finding the min/max element quickly but don't maintain sorted order for all elements.
   - Binary search trees provide O(log n) for a wider range of operations but are more complex.
   - Use heaps when you only need to access the highest/lowest priority element.
   - Use balanced BSTs when you need to find elements by key or maintain a sorted order.
