# Time Complexity Reference Guide for Data Structures & Algorithms

## Table of Contents
1. [Common Data Structures](#common-data-structures)
   - [Arrays](#arrays)
   - [Linked Lists](#linked-lists)
   - [Stacks and Queues](#stacks-and-queues)
   - [Hash Tables](#hash-tables)
   - [Binary Heaps](#binary-heaps)
   - [Binary Search Trees](#binary-search-trees)
   - [AVL Trees](#avl-trees)
   - [Red-Black Trees](#red-black-trees)

2. [Graph Algorithms](#graph-algorithms)
   - [Graph Representations](#graph-representations)
   - [Graph Traversals](#graph-traversals)
   - [Shortest Path Algorithms](#shortest-path-algorithms)
   - [Minimum Spanning Tree](#minimum-spanning-tree)

3. [Sorting Algorithms](#sorting-algorithms)
   - [Comparison-Based Sorts](#comparison-based-sorts)
   - [Non-Comparison Sorts](#non-comparison-sorts)

4. [Searching Algorithms](#searching-algorithms)
   - [Basic Search Algorithms](#basic-search-algorithms)
   - [Tree and Graph Search](#tree-and-graph-search)

5. [Dynamic Programming](#dynamic-programming)
   - [Common DP Problems](#common-dp-problems)

6. [Complexity Hierarchies](#complexity-hierarchies)

7. [STL Container Complexities](#stl-container-complexities)
   - [Vector](#vector)
   - [List](#list)
   - [Deque](#deque)
   - [Set/Map](#setmap)
   - [Unordered_set/Unordered_map](#unordered_setunordered_map)
   - [Priority_queue](#priority_queue)

## Common Data Structures

### Arrays

| Operation | Time Complexity | Notes |
|-----------|-----------------|-------|
| Access by index | O(1) | Direct addressing |
| Insert/delete at end | O(1) | Amortized for dynamic arrays |
| Insert/delete at beginning/middle | O(n) | Requires shifting elements |
| Search (unsorted) | O(n) | Linear search |
| Search (sorted) | O(log n) | Binary search |

### Linked Lists

| Operation | Time Complexity | Notes |
|-----------|-----------------|-------|
| Access by index | O(n) | Must traverse from head/tail |
| Insert/delete at beginning | O(1) | With head pointer |
| Insert/delete at end | O(1) | With tail pointer |
| Insert/delete in middle | O(n) | Must find position first |
| Search | O(n) | Linear traversal |

### Stacks and Queues

| Operation | Time Complexity | Notes |
|-----------|-----------------|-------|
| Push | O(1) | Add element |
| Pop | O(1) | Remove element |
| Peek/Top | O(1) | View top element |
| Search | O(n) | Must traverse the structure |

### Hash Tables

| Operation | Time Complexity (Average) | Time Complexity (Worst) | Notes |
|-----------|---------------------------|-------------------------|-------|
| Insert | O(1) | O(n) | Worst case with many collisions |
| Delete | O(1) | O(n) | Worst case with many collisions |
| Search | O(1) | O(n) | Worst case with many collisions |
| Find max/min | O(n) | O(n) | Must examine all elements |

### Binary Heaps

| Operation | Time Complexity | Notes |
|-----------|-----------------|-------|
| Insert | O(log n) | Percolate up |
| Delete min/max | O(log n) | Remove root and percolate down |
| Find min/max | O(1) | Always at the root |
| BuildHeap | O(n) | Linear time, not O(n log n) |
| Heapify | O(log n) | Restore heap property |

### Binary Search Trees

**Unbalanced BST:**

| Operation | Time Complexity (Average) | Time Complexity (Worst) | Notes |
|-----------|---------------------------|-------------------------|-------|
| Insert | O(log n) | O(n) | Worst case: linear tree |
| Delete | O(log n) | O(n) | Worst case: linear tree |
| Search | O(log n) | O(n) | Worst case: linear tree |
| Find min/max | O(log n) | O(n) | Leftmost/rightmost node |

### AVL Trees

| Operation | Time Complexity | Notes |
|-----------|-----------------|-------|
| Insert | O(log n) | Includes rebalancing |
| Delete | O(log n) | Includes rebalancing |
| Search | O(log n) | Guaranteed due to balance |
| Find min/max | O(log n) | Leftmost/rightmost node |
| Rotation | O(1) | Constant time operation |

### Red-Black Trees

| Operation | Time Complexity | Notes |
|-----------|-----------------|-------|
| Insert | O(log n) | Includes rebalancing |
| Delete | O(log n) | Includes rebalancing |
| Search | O(log n) | Guaranteed due to balance |
| Rotation | O(1) | Constant time operation |

## Graph Algorithms

### Graph Representations

| Representation | Space | Edge Lookup | Adjacency Query | Notes |
|----------------|-------|-------------|-----------------|-------|
| Adjacency Matrix | O(V²) | O(1) | O(1) | Better for dense graphs |
| Adjacency List | O(V+E) | O(E) or O(degree) | O(degree) | Better for sparse graphs |
| Edge List | O(E) | O(E) | O(E) | Simple but inefficient for queries |

### Graph Traversals

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|-----------------|------------------|-------|
| Breadth-First Search (BFS) | O(V + E) | O(V) | Using adjacency list |
| Depth-First Search (DFS) | O(V + E) | O(V) | Using adjacency list |
| Topological Sort | O(V + E) | O(V) | Only for DAGs |

### Shortest Path Algorithms

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|-----------------|------------------|-------|
| Dijkstra's (array) | O(V²) | O(V) | Non-negative weights |
| Dijkstra's (min-heap) | O(E log V) | O(V) | Non-negative weights |
| Bellman-Ford | O(V·E) | O(V) | Handles negative weights |
| Unweighted Shortest Path (BFS) | O(V + E) | O(V) | Unweighted graphs |

### Minimum Spanning Tree

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|-----------------|------------------|-------|
| Prim's (array) | O(V²) | O(V) | Better for dense graphs |
| Prim's (min-heap) | O(E log V) | O(V) | Better for sparse graphs |
| Kruskal's | O(E log E) or O(E log V) | O(V) | Uses disjoint-set |

## Sorting Algorithms

### Comparison-Based Sorts

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable | Notes |
|-----------|-----------|--------------|------------|-------|--------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | With early termination |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Always makes n-1 swaps |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Efficient for small/nearly sorted data |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Consistent performance |
| Quicksort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Depends on pivot selection |
| Heapsort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | In-place, but not stable |

### Non-Comparison Sorts

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|-----------------|------------------|-------|
| Counting Sort | O(n + k) | O(n + k) | k = range of values |
| Radix Sort | O(d(n + k)) | O(n + k) | d = number of digits |
| Bucket Sort | O(n + k) | O(n + k) | Good with uniform distribution |

## Searching Algorithms

### Basic Search Algorithms

| Algorithm | Time Complexity (Average) | Time Complexity (Worst) | Notes |
|-----------|---------------------------|-------------------------|-------|
| Linear Search | O(n) | O(n) | Unsorted data |
| Binary Search | O(log n) | O(log n) | Sorted data |
| Jump Search | O(√n) | O(√n) | Sorted data |

### Tree and Graph Search

| Algorithm | Time Complexity | Notes |
|-----------|-----------------|-------|
| BST Search | O(log n) average, O(n) worst | Depends on tree balance |
| BFS | O(V + E) | Breadth-first search |
| DFS | O(V + E) | Depth-first search |

## Dynamic Programming

### Common DP Problems

| Problem | Time Complexity | Space Complexity | Notes |
|---------|-----------------|------------------|-------|
| Fibonacci | O(n) | O(1) | Iterative solution |
| 0-1 Knapsack | O(n·W) | O(n·W) | n = items, W = capacity |
| Longest Common Subsequence | O(m·n) | O(m·n) | m, n = string lengths |
| Matrix Chain Multiplication | O(n³) | O(n²) | n = number of matrices |
| Shortest Path in DAG | O(V + E) | O(V) | Using topological sort |
| Edit Distance | O(m·n) | O(m·n) | m, n = string lengths |
| Longest Increasing Subsequence | O(n²) or O(n log n) | O(n) | Depends on implementation |

## Complexity Hierarchies

**Common Time Complexities (ordered from fastest to slowest)**:
1. O(1) - Constant
2. O(log n) - Logarithmic
3. O(n) - Linear
4. O(n log n) - Linearithmic
5. O(n²) - Quadratic
6. O(n³) - Cubic
7. O(2ⁿ) - Exponential
8. O(n!) - Factorial

## STL Container Complexities

### Vector

| Operation | Time Complexity | Notes |
|-----------|-----------------|-------|
| Random access | O(1) | Direct indexing |
| Insert/Erase at end | O(1) | Amortized |
| Insert/Erase at beginning/middle | O(n) | Requires shifting elements |
| Find (unsorted) | O(n) | Linear search |
| Size | O(1) | Stored attribute |

### List

| Operation | Time Complexity | Notes |
|-----------|-----------------|-------|
| Access | O(n) | Must traverse from head/tail |
| Insert/Erase at position | O(1) | With iterator to position |
| Find | O(n) | Linear traversal |
| Size | O(1) | Stored attribute |

### Deque

| Operation | Time Complexity | Notes |
|-----------|-----------------|-------|
| Random access | O(1) | Direct indexing |
| Insert/Erase at beginning/end | O(1) | Amortized |
| Insert/Erase in middle | O(n) | Requires shifting elements |
| Find | O(n) | Linear search |
| Size | O(1) | Stored attribute |

### Set/Map

| Operation | Time Complexity | Notes |
|-----------|-----------------|-------|
| Insert | O(log n) | Maintains sorted order |
| Erase | O(log n) | Maintains sorted order |
| Find | O(log n) | Binary search tree |
| lower_bound/upper_bound | O(log n) | Binary search tree |
| Size | O(1) | Stored attribute |

### Unordered_set/Unordered_map

| Operation | Time Complexity (Average) | Time Complexity (Worst) | Notes |
|-----------|---------------------------|-------------------------|-------|
| Insert | O(1) | O(n) | Hash collision worst case |
| Erase | O(1) | O(n) | Hash collision worst case |
| Find | O(1) | O(n) | Hash collision worst case |
| Size | O(1) | O(1) | Stored attribute |

### Priority_queue

| Operation | Time Complexity | Notes |
|-----------|-----------------|-------|
| Push | O(log n) | Upheap operation |
| Pop | O(log n) | Downheap operation |
| Top | O(1) | Access root element |
| Size | O(1) | Stored attribute |
