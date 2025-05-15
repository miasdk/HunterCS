# Comprehensive Time Complexity Reference Guide

## 1. Sorting Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity | Stable? |
|-----------|-----------|--------------|------------|------------------|---------|
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Heapsort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Quicksort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Quickselect | O(n) | O(n) | O(n²) | O(log n) | N/A |
| Introsort | O(n log n) | O(n log n) | O(n log n) | O(log n) | No |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |


## 2. Heap Operations

| Operation | Best Case | Average Case | Worst Case |
|-----------|-----------|--------------|------------|
| BuildHeap | O(n) | O(n) | O(n) |
| Insert | O(1) | O(log n) | O(log n) |
| FindMin/FindMax | O(1) | O(1) | O(1) |
| DeleteMin/DeleteMax | O(log n) | O(log n) | O(log n) |
| DecreaseKey | O(1) | O(log n) | O(log n) |
| IncreaseKey | O(1) | O(log n) | O(log n) |
| Merge (binary heaps) | O(n) | O(n) | O(n) |
| Find Min in Max Heap | O(n/2) | O(n/2) | O(n/2) |

## 3. Hash Table Operations

| Operation | Average Case (Separate Chaining) | Worst Case (Separate Chaining) | Average Case (Open Addressing) | Worst Case (Open Addressing) |
|-----------|----------------------------------|--------------------------------|--------------------------------|-------------------------------|
| Insert | O(1) | O(n) | O(1) | O(n) |
| Delete | O(1) | O(n) | O(1) | O(n) |
| Search | O(1) | O(n) | O(1) | O(n) |
| Rehashing | O(n) | O(n) | O(n) | O(n) |

## 4. STL Container Operations

### 4.1 Sequence Containers

| Operation | vector | deque | list | forward_list | array |
|-----------|--------|-------|------|--------------|-------|
| Random Access | O(1) | O(1) | O(n) | N/A | O(1) |
| Insert/Delete at beginning | O(n) | O(1) | O(1) | O(1) | N/A |
| Insert/Delete at end | O(1)* | O(1) | O(1) | N/A | N/A |
| Insert/Delete in middle | O(n) | O(n) | O(1)** | O(1)** | N/A |
| Search | O(n) | O(n) | O(n) | O(n) | O(n) |
| Sort | O(n log n) | O(n log n) | O(n log n) | O(n log n) | O(n log n) |

\* Amortized constant time  
\** With iterator to position

### 4.2 Associative Containers

| Operation | set/multiset | map/multimap | unordered_set/multiset | unordered_map/multimap |
|-----------|--------------|--------------|------------------------|-------------------------|
| Insert | O(log n) | O(log n) | O(1) average, O(n) worst | O(1) average, O(n) worst |
| Delete | O(log n) | O(log n) | O(1) average, O(n) worst | O(1) average, O(n) worst |
| Search | O(log n) | O(log n) | O(1) average, O(n) worst | O(1) average, O(n) worst |
| Traverse in order | O(n) | O(n) | N/A | N/A |

## 5. Partition Operations

| Algorithm | Average Case | Worst Case | Space Complexity |
|-----------|--------------|------------|------------------|
| Hoare Partition | O(n) | O(n) | O(1) |

## 6. Graph Algorithms

| Algorithm | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| BFS | O(V+E) | O(V) |
| DFS | O(V+E) | O(V) |
| Dijkstra's Algorithm | O(E + V log V) | O(V) |
| Bellman-Ford | O(VE) | O(V) |
| Floyd-Warshall | O(V³) | O(V²) |
| Prim's Algorithm | O(E log V) | O(V) |
| Kruskal's Algorithm | O(E log E) | O(V) |
| Topological Sort | O(V+E) | O(V) |

## 7. Important Operations from Exam

| Operation | Time Complexity | Notes |
|-----------|-----------------|-------|
| Rehashing (average case) | O(n) | Linear in the number of elements |
| Find a value in unordered_map | O(1) average, O(n) worst | Hash table lookup |
| Find a key in unordered_map | O(1) average, O(n) worst | Hash table lookup |
| Find a key in ordered map | O(log n) | Binary search tree |
| DeleteMin from min heap | O(log n) | Requires percolate down |
| Partition around pivot | O(n) | Linear scan through all elements |
| Quickselect (average case) | O(n) | Linear time selection algorithm |
| Hoare Partitioning | O(n) | Fewer swaps than Lomuto |
| Finding mode using hash map | O(n) | Single pass with hash map |
| Finding min in max heap | O(n/2) | Must check all leaf nodes |

## 8. Special Cases and Optimizations

| Algorithm | Special Case | Time Complexity |
|-----------|--------------|-----------------|
| Insertion Sort | Already sorted | O(n) |
| Insertion Sort | All elements equal | O(n) |
| Quicksort | Already sorted (naive pivot) | O(n²) |
| Quicksort | All elements equal (naive pivot) | O(n²) |
| Quicksort | Random pivot | O(n log n) expected |
| Heapsort | Any input | O(n log n) |
| Mergesort | Any input | O(n log n) |
| Binary Search | Sorted array | O(log n) |
| Introsort | Any input | O(n log n) |

## 9. Common Mistaken Complexities

| Operation | Common Mistake | Actual Complexity | Reason |
|-----------|---------------|-------------------|--------|
| BuildHeap | O(n log n) | O(n) | The height of most nodes is small |
| Find in hash table | O(n) | O(1) average | Hash function provides direct access |
| Vector resize | O(1) | O(n) | Requires copying all elements |
| priority_queue::top | O(log n) | O(1) | Only returns the top element without modifying |
| unordered_map::count | O(n) | O(1) average | Hash function provides direct access |

## 10. Complexity Analysis Template

When analyzing algorithms, consider:

1. **Identify the operation**: What fundamental operation dominates?
2. **Count iterations**: How many times does the operation repeat?
3. **Consider nesting**: Multiply complexities of nested operations
4. **Identify variables**: Express in terms of input size n
5. **Find dominant term**: Drop lower-order terms and constants

Example for heapsort:
- BuildHeap: O(n)
- n deleteMax operations: n × O(log n) = O(n log n)
- Overall: O(n) + O(n log n) = O(n log n)
