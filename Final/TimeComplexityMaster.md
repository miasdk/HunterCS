# Comprehensive DSA Time Complexity Reference
## (Based on CSCI 33500 Course Material)

## Table of Contents

1. [Data Structure Operations](#data-structure-operations)
   - [Array/Vector](#arrayvector)
   - [Linked List](#linked-list-singlydoubly)
   - [Stack](#stack-using-array-or-linked-list)
   - [Queue](#queue-using-array-or-linked-list)
   - [Binary Heap](#binary-heap)
   - [Binary Search Tree (Unbalanced)](#binary-search-tree-unbalanced)
   - [AVL Tree](#avl-tree)
   - [Splay Tree](#splay-tree)
   - [Hash Table](#hash-table)
   - [Hash Table Collision Resolution](#hash-table-collision-resolution-strategies)
   - [Graph Representation](#graph-representation)

2. [Sorting Algorithms](#sorting-algorithms)

3. [Selection Algorithms](#selection-algorithms)

4. [Graph Algorithms](#graph-algorithms)
   - [Traversal](#traversal)
   - [Shortest Path](#shortest-path)
   - [Minimum Spanning Tree](#minimum-spanning-tree)
   - [Misc Graph Algorithms](#misc-graph-algorithms)

5. [Dynamic Programming Algorithms](#dynamic-programming-algorithms)

6. [STL Container Complexity (C++)](#stl-container-complexity-c)
   - [std::vector](#stdvector)
   - [std::list](#stdlist)
   - [std::deque](#stddeque)
   - [std::map / std::set](#stdmap--stdset-red-black-tree)
   - [std::unordered_map / std::unordered_set](#stdunordered_map--stdunordered_set-hash-table)
   - [std::priority_queue](#stdpriority_queue-binary-heap)

7. [Special Cases to Remember](#special-cases-to-remember)

## Data Structure Operations

### Array/Vector
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Access by index | O(1) | O(1) | Direct memory address calculation |
| Search (unsorted) | O(n) | O(n) | Linear scan required |
| Search (sorted) | O(log n) | O(log n) | Using binary search |
| Insert/Delete (at end) | O(1) amortized | O(1) amortized | May require occasional resize |
| Insert/Delete (at beginning/middle) | O(n) | O(n) | Requires shifting elements |
| Push/Pop (at end) | O(1) amortized | O(1) amortized | Vector may need to resize |

### Linked List (Singly/Doubly)
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Access by index | O(n) | O(n) | Must traverse from head/tail |
| Search | O(n) | O(n) | Must traverse to find element |
| Insert/Delete (at beginning) | O(1) | O(1) | Just update head pointer |
| Insert/Delete (at middle with pointer) | O(1) | O(1) | Given direct pointer to node |
| Insert/Delete (at middle w/o pointer) | O(n) | O(n) | Must traverse to find position first |
| Insert/Delete (at end with tail pointer) | O(1) | O(1) | With tail pointer maintained |
| Insert/Delete (at end w/o tail pointer) | O(n) | O(n) | Must traverse to end first |

### Stack (using Array or Linked List)
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Push | O(1) | O(1) | Amortized if using vector |
| Pop | O(1) | O(1) | Amortized if using vector |
| Peek (Top) | O(1) | O(1) | Just return last element |
| Search | O(n) | O(n) | Must scan all elements |
| Size | O(1) | O(1) | If size counter maintained |

### Queue (using Array or Linked List)
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Enqueue | O(1) | O(1) | Add to back of queue |
| Dequeue | O(1) | O(1) | Remove from front of queue |
| Peek (Front) | O(1) | O(1) | Just return front element |
| Search | O(n) | O(n) | Must scan all elements |
| Size | O(1) | O(1) | If size counter maintained |

### Binary Heap
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| FindMin/FindMax | O(1) | O(1) | Root element |
| Insert | O(log n) | O(log n) | Percolate up |
| DeleteMin/DeleteMax | O(log n) | O(log n) | Remove root & percolate down |
| BuildHeap | O(n) | O(n) | Not O(n log n) as might be expected |
| Heapify | O(log n) | O(log n) | Restore heap property for subtree |
| Decrease/Increase Key | O(log n) | O(log n) | Update & restore heap property |

### Binary Search Tree (Unbalanced)
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Search | O(log n) | O(n) | Degenerate case is linked list |
| Insert | O(log n) | O(n) | Find position then insert |
| Delete | O(log n) | O(n) | Find, then remove and fix links |
| FindMin/FindMax | O(log n) | O(n) | Leftmost/rightmost node |
| Successor/Predecessor | O(log n) | O(n) | Next/previous in sorted order |
| Height | O(log n) | O(n) | For balanced vs. degenerate trees |

### AVL Tree
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Search | O(log n) | O(log n) | Tree height always O(log n) |
| Insert | O(log n) | O(log n) | Find position, insert, rebalance |
| Delete | O(log n) | O(log n) | Remove, then rebalance |
| FindMin/FindMax | O(log n) | O(log n) | Leftmost/rightmost node |
| Successor/Predecessor | O(log n) | O(log n) | Next/previous in sorted order |
| Single Rotation | O(1) | O(1) | Constant pointer operations |
| Double Rotation | O(1) | O(1) | Two single rotations |
| Minimal AVL Tree of Height h | N/A | N/A | Follows recurrence: f(h) = f(h-1) + f(h-2) + 1 |

### Splay Tree
| Operation | Average Case | Worst Case | Amortized | Notes |
|-----------|--------------|------------|-----------|-------|
| Search | O(log n) | O(n) | O(log n) | Find and splay to root |
| Insert | O(log n) | O(n) | O(log n) | Insert and splay to root |
| Delete | O(log n) | O(n) | O(log n) | Find, splay, delete, reconnect |
| FindMin/FindMax | O(log n) | O(n) | O(log n) | Find and splay to root |

### Hash Table
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Search | O(1) | O(n) | Worst case with bad hash function |
| Insert | O(1) | O(n) | Depends on collision resolution |
| Delete | O(1) | O(n) | Depends on collision resolution |
| Rehashing | O(n) | O(n) | Must rehash all elements |

#### Hash Table (Collision Resolution Strategies)
| Strategy | Search (Avg) | Insert (Avg) | Search (Worst) | Insert (Worst) | Notes |
|----------|--------------|--------------|----------------|----------------|-------|
| Separate Chaining | O(1 + α) | O(1 + α) | O(n) | O(n) | α = load factor |
| Linear Probing | O(1/(1-α)) | O(1/(1-α)) | O(n) | O(n) | Primary clustering |
| Quadratic Probing | O(1/(1-α)) | O(1/(1-α)) | O(n) | O(n) | Secondary clustering |
| Double Hashing | O(1/(1-α)) | O(1/(1-α)) | O(n) | O(n) | Better distribution |

### Graph Representation
| Structure | Space | Add Vertex | Add Edge | Remove Vertex | Remove Edge | Query Edge | Query Adjacent Vertices |
|-----------|-------|------------|----------|---------------|-------------|------------|-------------------------|
| Adjacency Matrix | O(V²) | O(V²) | O(1) | O(V²) | O(1) | O(1) | O(V) |
| Adjacency List | O(V+E) | O(1) | O(1) | O(V+E) | O(E) or O(degree(v)) | O(degree(v)) | O(degree(v)) |
| Edge List | O(E) | O(1) | O(1) | O(E) | O(E) | O(E) | O(E) |

## Sorting Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable | Notes |
|-----------|-----------|--------------|------------|-------|--------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | With early stopping |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Always makes n(n-1)/2 comparisons |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Efficient for small or nearly sorted data |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Divide and conquer |
| Quicksort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | In-place with O(log n) stack |
| Heapsort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | In-place sort |
| Shell Sort | O(n log n) | O(n^(4/3)) | O(n²) | O(1) | No | Improvement on insertion sort |
| Introsort | O(n log n) | O(n log n) | O(n log n) | O(log n) | No | Hybrid sort (quicksort, heapsort, insertion) |

## Selection Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space | Notes |
|-----------|-----------|--------------|------------|-------|-------|
| Quickselect | O(n) | O(n) | O(n²) | O(1) | Selection uses partitioning |

## Graph Algorithms

### Traversal
| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Breadth-First Search (BFS) | O(V+E) | O(V) | Uses queue |
| Depth-First Search (DFS) | O(V+E) | O(V) | Uses stack or recursion |
| Topological Sort | O(V+E) | O(V) | For DAGs only |

### Shortest Path
| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Dijkstra's (binary heap) | O(E log V) | O(V) | No negative weights |
| Dijkstra's (adjacency matrix) | O(V²) | O(V) | Dense graphs |
| Bellman-Ford | O(V·E) | O(V) | Handles negative weights |
| Floyd-Warshall (all pairs) | O(V³) | O(V²) | Dynamic programming approach |
| Johnson's (all pairs) | O(V² log V + V·E) | O(V²) | For sparse graphs |
| Unweighted Shortest Path (BFS) | O(V+E) | O(V) | All edges have equal weight |

### Minimum Spanning Tree
| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Prim's (binary heap) | O(E log V) | O(V) | Grows single tree |
| Prim's (adjacency matrix) | O(V²) | O(V) | For dense graphs |
| Kruskal's | O(E log E) or O(E log V) | O(V) | Uses Union-Find |

### Misc Graph Algorithms
| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Detect Cycle | O(V+E) | O(V) | Using DFS |
| Bipartite Check | O(V+E) | O(V) | Using BFS/DFS |
| Connected Components | O(V+E) | O(V) | Using DFS |
| Strongly Connected Components | O(V+E) | O(V) | Using Kosaraju's algorithm |
| Vertex Cover | NP-complete | - | 2-approximation in O(V+E) |

## Dynamic Programming Algorithms

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Fibonacci Sequence | O(n) | O(n) or O(1) | With memoization or tabulation |
| Longest Common Subsequence | O(m·n) | O(m·n) | Two sequences of length m, n |
| 0/1 Knapsack | O(n·W) | O(n·W) | n items, capacity W |
| Coin Change (minimum coins) | O(n·amount) | O(amount) | For n denominations |
| Longest Increasing Subsequence | O(n²) or O(n log n) | O(n) | In an array of length n |

## STL Container Complexity (C++)

### std::vector
| Operation | Time Complexity |
|-----------|----------------|
| Random access | O(1) |
| Insert/erase at end | O(1) amortized |
| Insert/erase at middle | O(n) |
| Size | O(1) |

### std::list
| Operation | Time Complexity |
|-----------|----------------|
| Random access | O(n) |
| Insert/erase at position | O(1) with iterator |
| Splice | O(1) |
| Size | O(1) |

### std::deque
| Operation | Time Complexity |
|-----------|----------------|
| Random access | O(1) |
| Insert/erase at begin/end | O(1) amortized |
| Insert/erase at middle | O(n) |

### std::map / std::set (Red-Black Tree)
| Operation | Time Complexity |
|-----------|----------------|
| Insert | O(log n) |
| Erase | O(log n) |
| Find | O(log n) |
| Lower/Upper bound | O(log n) |

### std::unordered_map / std::unordered_set (Hash Table)
| Operation | Time Complexity |
|-----------|----------------|
| Insert | O(1) average, O(n) worst |
| Erase | O(1) average, O(n) worst |
| Find | O(1) average, O(n) worst |

### std::priority_queue (Binary Heap)
| Operation | Time Complexity |
|-----------|----------------|
| Push | O(log n) |
| Pop | O(log n) |
| Top | O(1) |

## Special Cases to Remember

1. **BuildHeap Complexity**: 
   - Despite calling percolateDown (O(log n)) on n/2 elements, the tight bound is O(n)
   - This is because percolateDown costs less for nodes near the leaves

2. **AVL Tree Minimal Size**: 
   - Height h: Minimum nodes = f(h) = f(h-1) + f(h-2) + 1
   - Base cases: f(0) = 1, f(1) = 2
   - Height 8: 88 nodes

3. **Hash Table Load Factor**: 
   - Optimal around 0.7 for open addressing
   - Can be higher for separate chaining
   - Performance degrades as load factor approaches 1

4. **Dijkstra's vs. Prim's**:
   - Both use similar structure with priority queues
   - Dijkstra's tracks distance from source
   - Prim's tracks distance to MST

5. **When to Use Binary Heaps vs. Other Structures**:
   - Binary heaps efficient for basic priority queue
   - Inefficient for arbitrary deletion/decrease key
   - Fibonacci heaps theoretically better for decrease key (O(1) amortized)

6. **Topological Sort Requirement**:
   - Only defined for Directed Acyclic Graphs (DAGs)
   - Multiple valid orderings may exist

7. **Binary Search Tree Worst Case**:
   - Happens when tree degenerates to linked list (e.g., sorted insertions)
   - AVL/Red-Black trees prevent this degeneration

8. **Double Hashing Requirements**:
   - Second hash function must never return 0
   - Ideally, second hash and table size are relatively prime# Comprehensive DSA Time Complexity Reference
## (Based on CSCI 33500 Course Material)

## Data Structure Operations

### Array/Vector
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Access by index | O(1) | O(1) | Direct memory address calculation |
| Search (unsorted) | O(n) | O(n) | Linear scan required |
| Search (sorted) | O(log n) | O(log n) | Using binary search |
| Insert/Delete (at end) | O(1) amortized | O(1) amortized | May require occasional resize |
| Insert/Delete (at beginning/middle) | O(n) | O(n) | Requires shifting elements |
| Push/Pop (at end) | O(1) amortized | O(1) amortized | Vector may need to resize |

### Linked List (Singly/Doubly)
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Access by index | O(n) | O(n) | Must traverse from head/tail |
| Search | O(n) | O(n) | Must traverse to find element |
| Insert/Delete (at beginning) | O(1) | O(1) | Just update head pointer |
| Insert/Delete (at middle with pointer) | O(1) | O(1) | Given direct pointer to node |
| Insert/Delete (at middle w/o pointer) | O(n) | O(n) | Must traverse to find position first |
| Insert/Delete (at end with tail pointer) | O(1) | O(1) | With tail pointer maintained |
| Insert/Delete (at end w/o tail pointer) | O(n) | O(n) | Must traverse to end first |

### Stack (using Array or Linked List)
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Push | O(1) | O(1) | Amortized if using vector |
| Pop | O(1) | O(1) | Amortized if using vector |
| Peek (Top) | O(1) | O(1) | Just return last element |
| Search | O(n) | O(n) | Must scan all elements |
| Size | O(1) | O(1) | If size counter maintained |

### Queue (using Array or Linked List)
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Enqueue | O(1) | O(1) | Add to back of queue |
| Dequeue | O(1) | O(1) | Remove from front of queue |
| Peek (Front) | O(1) | O(1) | Just return front element |
| Search | O(n) | O(n) | Must scan all elements |
| Size | O(1) | O(1) | If size counter maintained |

### Binary Heap
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| FindMin/FindMax | O(1) | O(1) | Root element |
| Insert | O(log n) | O(log n) | Percolate up |
| DeleteMin/DeleteMax | O(log n) | O(log n) | Remove root & percolate down |
| BuildHeap | O(n) | O(n) | Not O(n log n) as might be expected |
| Heapify | O(log n) | O(log n) | Restore heap property for subtree |
| Decrease/Increase Key | O(log n) | O(log n) | Update & restore heap property |

### Binary Search Tree (Unbalanced)
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Search | O(log n) | O(n) | Degenerate case is linked list |
| Insert | O(log n) | O(n) | Find position then insert |
| Delete | O(log n) | O(n) | Find, then remove and fix links |
| FindMin/FindMax | O(log n) | O(n) | Leftmost/rightmost node |
| Successor/Predecessor | O(log n) | O(n) | Next/previous in sorted order |
| Height | O(log n) | O(n) | For balanced vs. degenerate trees |

### AVL Tree
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Search | O(log n) | O(log n) | Tree height always O(log n) |
| Insert | O(log n) | O(log n) | Find position, insert, rebalance |
| Delete | O(log n) | O(log n) | Remove, then rebalance |
| FindMin/FindMax | O(log n) | O(log n) | Leftmost/rightmost node |
| Successor/Predecessor | O(log n) | O(log n) | Next/previous in sorted order |
| Single Rotation | O(1) | O(1) | Constant pointer operations |
| Double Rotation | O(1) | O(1) | Two single rotations |
| Minimal AVL Tree of Height h | N/A | N/A | Follows recurrence: f(h) = f(h-1) + f(h-2) + 1 |

### Splay Tree
| Operation | Average Case | Worst Case | Amortized | Notes |
|-----------|--------------|------------|-----------|-------|
| Search | O(log n) | O(n) | O(log n) | Find and splay to root |
| Insert | O(log n) | O(n) | O(log n) | Insert and splay to root |
| Delete | O(log n) | O(n) | O(log n) | Find, splay, delete, reconnect |
| FindMin/FindMax | O(log n) | O(n) | O(log n) | Find and splay to root |

### Hash Table
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Search | O(1) | O(n) | Worst case with bad hash function |
| Insert | O(1) | O(n) | Depends on collision resolution |
| Delete | O(1) | O(n) | Depends on collision resolution |
| Rehashing | O(n) | O(n) | Must rehash all elements |

#### Hash Table (Collision Resolution Strategies)
| Strategy | Search (Avg) | Insert (Avg) | Search (Worst) | Insert (Worst) | Notes |
|----------|--------------|--------------|----------------|----------------|-------|
| Separate Chaining | O(1 + α) | O(1 + α) | O(n) | O(n) | α = load factor |
| Linear Probing | O(1/(1-α)) | O(1/(1-α)) | O(n) | O(n) | Primary clustering |
| Quadratic Probing | O(1/(1-α)) | O(1/(1-α)) | O(n) | O(n) | Secondary clustering |
| Double Hashing | O(1/(1-α)) | O(1/(1-α)) | O(n) | O(n) | Better distribution |

### Graph Representation
| Structure | Space | Add Vertex | Add Edge | Remove Vertex | Remove Edge | Query Edge | Query Adjacent Vertices |
|-----------|-------|------------|----------|---------------|-------------|------------|-------------------------|
| Adjacency Matrix | O(V²) | O(V²) | O(1) | O(V²) | O(1) | O(1) | O(V) |
| Adjacency List | O(V+E) | O(1) | O(1) | O(V+E) | O(E) or O(degree(v)) | O(degree(v)) | O(degree(v)) |
| Edge List | O(E) | O(1) | O(1) | O(E) | O(E) | O(E) | O(E) |

## Sorting Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable | Notes |
|-----------|-----------|--------------|------------|-------|--------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | With early stopping |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Always makes n(n-1)/2 comparisons |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Efficient for small or nearly sorted data |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Divide and conquer |
| Quicksort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | In-place with O(log n) stack |
| Heapsort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | In-place sort |
| Shell Sort | O(n log n) | O(n^(4/3)) | O(n²) | O(1) | No | Improvement on insertion sort |
| Introsort | O(n log n) | O(n log n) | O(n log n) | O(log n) | No | Hybrid sort (quicksort, heapsort, insertion) |

## Selection Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space | Notes |
|-----------|-----------|--------------|------------|-------|-------|
| Quickselect | O(n) | O(n) | O(n²) | O(1) | Selection uses partitioning |

## Graph Algorithms

### Traversal
| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Breadth-First Search (BFS) | O(V+E) | O(V) | Uses queue |
| Depth-First Search (DFS) | O(V+E) | O(V) | Uses stack or recursion |
| Topological Sort | O(V+E) | O(V) | For DAGs only |

### Shortest Path
| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Dijkstra's (binary heap) | O(E log V) | O(V) | No negative weights |
| Dijkstra's (adjacency matrix) | O(V²) | O(V) | Dense graphs |
| Bellman-Ford | O(V·E) | O(V) | Handles negative weights |
| Floyd-Warshall (all pairs) | O(V³) | O(V²) | Dynamic programming approach |
| Johnson's (all pairs) | O(V² log V + V·E) | O(V²) | For sparse graphs |
| Unweighted Shortest Path (BFS) | O(V+E) | O(V) | All edges have equal weight |

### Minimum Spanning Tree
| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Prim's (binary heap) | O(E log V) | O(V) | Grows single tree |
| Prim's (adjacency matrix) | O(V²) | O(V) | For dense graphs |
| Kruskal's | O(E log E) or O(E log V) | O(V) | Uses Union-Find |

### Misc Graph Algorithms
| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Detect Cycle | O(V+E) | O(V) | Using DFS |
| Bipartite Check | O(V+E) | O(V) | Using BFS/DFS |
| Connected Components | O(V+E) | O(V) | Using DFS |
| Strongly Connected Components | O(V+E) | O(V) | Using Kosaraju's algorithm |
| Vertex Cover | NP-complete | - | 2-approximation in O(V+E) |

## Dynamic Programming Algorithms

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Fibonacci Sequence | O(n) | O(n) or O(1) | With memoization or tabulation |
| Longest Common Subsequence | O(m·n) | O(m·n) | Two sequences of length m, n |
| 0/1 Knapsack | O(n·W) | O(n·W) | n items, capacity W |
| Coin Change (minimum coins) | O(n·amount) | O(amount) | For n denominations |
| Longest Increasing Subsequence | O(n²) or O(n log n) | O(n) | In an array of length n |

## STL Container Complexity (C++)

### std::vector
| Operation | Time Complexity |
|-----------|----------------|
| Random access | O(1) |
| Insert/erase at end | O(1) amortized |
| Insert/erase at middle | O(n) |
| Size | O(1) |

### std::list
| Operation | Time Complexity |
|-----------|----------------|
| Random access | O(n) |
| Insert/erase at position | O(1) with iterator |
| Splice | O(1) |
| Size | O(1) |

### std::deque
| Operation | Time Complexity |
|-----------|----------------|
| Random access | O(1) |
| Insert/erase at begin/end | O(1) amortized |
| Insert/erase at middle | O(n) |

### std::map / std::set (Red-Black Tree)
| Operation | Time Complexity |
|-----------|----------------|
| Insert | O(log n) |
| Erase | O(log n) |
| Find | O(log n) |
| Lower/Upper bound | O(log n) |

### std::unordered_map / std::unordered_set (Hash Table)
| Operation | Time Complexity |
|-----------|----------------|
| Insert | O(1) average, O(n) worst |
| Erase | O(1) average, O(n) worst |
| Find | O(1) average, O(n) worst |

### std::priority_queue (Binary Heap)
| Operation | Time Complexity |
|-----------|----------------|
| Push | O(log n) |
| Pop | O(log n) |
| Top | O(1) |

## Special Cases to Remember

1. **BuildHeap Complexity**: 
   - Despite calling percolateDown (O(log n)) on n/2 elements, the tight bound is O(n)
   - This is because percolateDown costs less for nodes near the leaves

2. **AVL Tree Minimal Size**: 
   - Height h: Minimum nodes = f(h) = f(h-1) + f(h-2) + 1
   - Base cases: f(0) = 1, f(1) = 2
   - Height 8: 88 nodes

3. **Hash Table Load Factor**: 
   - Optimal around 0.7 for open addressing
   - Can be higher for separate chaining
   - Performance degrades as load factor approaches 1

4. **Dijkstra's vs. Prim's**:
   - Both use similar structure with priority queues
   - Dijkstra's tracks distance from source
   - Prim's tracks distance to MST

5. **When to Use Binary Heaps vs. Other Structures**:
   - Binary heaps efficient for basic priority queue
   - Inefficient for arbitrary deletion/decrease key
   - Fibonacci heaps theoretically better for decrease key (O(1) amortized)

6. **Topological Sort Requirement**:
   - Only defined for Directed Acyclic Graphs (DAGs)
   - Multiple valid orderings may exist

7. **Binary Search Tree Worst Case**:
   - Happens when tree degenerates to linked list (e.g., sorted insertions)
   - AVL/Red-Black trees prevent this degeneration

8. **Double Hashing Requirements**:
   - Second hash function must never return 0
   - Ideally, second hash and table size are relatively prime| Longest Palindromic Substring | O(n²) naive, O(n) Manacher's | O(n) | Find longest palindrome |
| Longest Common Prefix | O(S) | O(1) | S = sum of all string lengths |
| Suffix Array Construction | O(n log n) | O(n) | n = string length |
| Burrows-Wheeler Transform | O(n) | O(n) | Used in compression |
| Trie Construction | O(L) | O(L·σ) | L = sum of string lengths, σ = alphabet size |

## Computational Geometry Algorithms

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Convex Hull (Graham Scan) | O(n log n) | O(n) | n = number of points |
| Convex Hull (Jarvis March) | O(n·h) | O(h) | h = points on hull |
| Line Intersection | O(n²) | O(n) | Checking all pairs |
| Closest Pair of Points | O(n log n) | O(n) | Divide and conquer |
| Point in Polygon | O(n) | O(1) | n = vertices of polygon |
| Segment Intersection | O(n log n) | O(n) | Sweep line algorithm |
| Delaunay Triangulation | O(n log n) | O(n) | For points in 2D plane |
| Voronoi Diagram | O(n log n) | O(n) | Dual of Delaunay triangulation |

## Number Theory Algorithms

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| GCD (Euclidean Algorithm) | O(log min(a,b)) | O(1) | For two numbers |
| Extended Euclidean Algorithm | O(log min(a,b)) | O(1) | Find x,y for ax+by=gcd(a,b) |
| Prime Factorization | O(√n) | O(log n) | Naive approach |
| Sieve of Eratosthenes | O(n log log n) | O(n) | Find all primes up to n |
| Miller-Rabin Primality Test | O(k log# Comprehensive Data Structures & Algorithms Time Complexity Reference

## Data Structure Operations

### Array/Vector
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Access by index | O(1) | O(1) | Direct memory address calculation |
| Search (unsorted) | O(n) | O(n) | Linear scan required |
| Search (sorted) | O(log n) | O(log n) | Using binary search |
| Insert/Delete (at end) | O(1) amortized | O(1) amortized | May require occasional resize |
| Insert/Delete (at beginning/middle) | O(n) | O(n) | Requires shifting elements |
| Push/Pop (at end) | O(1) amortized | O(1) amortized | Vector may need to resize |
| Resize | O(n) | O(n) | Need to copy all elements |

### Linked List (Singly/Doubly)
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Access by index | O(n) | O(n) | Must traverse from head/tail |
| Search | O(n) | O(n) | Must traverse to find element |
| Insert/Delete (at beginning) | O(1) | O(1) | Just update head pointer |
| Insert/Delete (at middle with pointer) | O(1) | O(1) | Given direct pointer to node |
| Insert/Delete (at middle w/o pointer) | O(n) | O(n) | Must traverse to find position first |
| Insert/Delete (at end with tail pointer) | O(1) | O(1) | With tail pointer maintained |
| Insert/Delete (at end w/o tail pointer) | O(n) | O(n) | Must traverse to end first |
| Reverse | O(n) | O(n) | Must update all links |
| Merge two lists | O(1) | O(1) | If end pointers are known |

### Stack (using Array or Linked List)
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Push | O(1) | O(1) | Amortized if using vector |
| Pop | O(1) | O(1) | Amortized if using vector |
| Peek (Top) | O(1) | O(1) | Just return last element |
| Search | O(n) | O(n) | Must scan all elements |
| Size | O(1) | O(1) | If size counter maintained |
| isEmpty | O(1) | O(1) | Check if size == 0 |

### Queue (using Array or Linked List)
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Enqueue | O(1) | O(1) | Add to back of queue |
| Dequeue | O(1) | O(1) | Remove from front of queue |
| Peek (Front) | O(1) | O(1) | Just return front element |
| Search | O(n) | O(n) | Must scan all elements |
| Size | O(1) | O(1) | If size counter maintained |
| isEmpty | O(1) | O(1) | Check if size == 0 |

### Deque (Double-ended Queue)
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| PushFront | O(1) | O(1) | Amortized for std::deque |
| PopFront | O(1) | O(1) | Remove from front |
| PushBack | O(1) | O(1) | Amortized for std::deque |
| PopBack | O(1) | O(1) | Remove from back |
| Access by index | O(1) | O(1) | For std::deque |
| Size | O(1) | O(1) | If size counter maintained |

### Binary Heap
| Operation | Average Case | Worst Case | Amortized | Notes |
|-----------|--------------|------------|-----------|-------|
| FindMin/FindMax | O(1) | O(1) | O(1) | Root element |
| Insert | O(log n) | O(log n) | O(log n) | Percolate up |
| DeleteMin/DeleteMax | O(log n) | O(log n) | O(log n) | Remove root & percolate down |
| ExtractMin/ExtractMax | O(log n) | O(log n) | O(log n) | Combined find and delete |
| DecreaseKey/IncreaseKey | O(log n) | O(log n) | O(log n) | Update & restore heap property |
| Delete arbitrary element | O(log n) | O(log n) | O(log n) | With index or pointer to element |
| BuildHeap | O(n) | O(n) | O(n) | Not O(n log n) as might be expected |
| Heapify | O(log n) | O(log n) | O(log n) | Restore heap property for subtree |
| Merge two heaps | O(n) | O(n) | O(n) | Naively combining then buildHeap |

### Fibonacci Heap
| Operation | Average Case | Worst Case | Amortized | Notes |
|-----------|--------------|------------|-----------|-------|
| FindMin | O(1) | O(1) | O(1) | Maintained pointer to min |
| Insert | O(1) | O(1) | O(1) | Add to root list |
| Merge | O(1) | O(1) | O(1) | Concatenate root lists |
| DecreaseKey | O(1) | O(n) | O(1) | Cut from parent & add to root list |
| Delete | O(log n) | O(n) | O(log n) | Deletion uses extractMin |
| ExtractMin | O(log n) | O(n) | O(log n) | Consolidate trees after removing min |

### Binary Search Tree (Unbalanced)
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Search | O(log n) | O(n) | Degenerate case is linked list |
| Insert | O(log n) | O(n) | Find position then insert |
| Delete | O(log n) | O(n) | Find, then remove and fix links |
| FindMin/FindMax | O(log n) | O(n) | Leftmost/rightmost node |
| Successor/Predecessor | O(log n) | O(n) | May need to traverse up from leaves |
| InOrder Traversal | O(n) | O(n) | Visit all nodes |
| Height | O(log n) | O(n) | For balanced vs. degenerate trees |
| Construct from sorted array | O(n) | O(n) | Results in skewed tree |
| Balance | O(n log n) | O(n log n) | Sort then build balanced tree |

### AVL Tree
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Search | O(log n) | O(log n) | Tree height always O(log n) |
| Insert | O(log n) | O(log n) | Find position, insert, rebalance |
| Delete | O(log n) | O(log n) | Remove, then rebalance |
| FindMin/FindMax | O(log n) | O(log n) | Leftmost/rightmost node |
| Successor/Predecessor | O(log n) | O(log n) | Next/previous in sorted order |
| Rebalance after insert | O(log n) | O(log n) | Up to log n rebalance operations |
| Rebalance after delete | O(log n) | O(log n) | Up to log n rebalance operations |
| Single Rotation | O(1) | O(1) | Constant pointer operations |
| Double Rotation | O(1) | O(1) | Two single rotations |
| Balance check | O(1) | O(1) | Check height difference of children |
| Height update | O(1) | O(1) | Based on child heights |
| Build minimal AVL | O(n) | O(n) | For height h: ~1.44^h nodes minimum |
| Verify AVL property | O(n) | O(n) | Check every node's balance factor |

### Red-Black Tree
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Search | O(log n) | O(log n) | Tree height always O(log n) |
| Insert | O(log n) | O(log n) | Find position, insert, recolor/rotate |
| Delete | O(log n) | O(log n) | Remove, then recolor/rotate |
| FindMin/FindMax | O(log n) | O(log n) | Leftmost/rightmost node |
| Successor/Predecessor | O(log n) | O(log n) | Next/previous in sorted order |
| Color Flip | O(1) | O(1) | Constant operation |
| Rotation | O(1) | O(1) | Constant pointer operations |
| Recolor/Rotate after insert | O(log n) | O(log n) | At most O(log n) operations |
| Recolor/Rotate after delete | O(log n) | O(log n) | At most O(log n) operations |
| Verify RB properties | O(n) | O(n) | Check all 5 properties |

### Splay Tree
| Operation | Average Case | Worst Case | Amortized | Notes |
|-----------|--------------|------------|-----------|-------|
| Search | O(log n) | O(n) | O(log n) | Find and splay to root |
| Insert | O(log n) | O(n) | O(log n) | Insert and splay to root |
| Delete | O(log n) | O(n) | O(log n) | Find, splay, delete, reconnect |
| FindMin/FindMax | O(log n) | O(n) | O(log n) | Find and splay to root |
| Access | O(log n) | O(n) | O(log n) | Brings accessed element to root |
| Join | O(log n) | O(n) | O(log n) | Splay max of first tree |
| Split | O(log n) | O(n) | O(log n) | Splay the split element |
| Zig step | O(1) | O(1) | O(1) | Single rotation |
| Zig-zig step | O(1) | O(1) | O(1) | Two rotations in same direction |
| Zig-zag step | O(1) | O(1) | O(1) | Two rotations in opposite directions |

### B-Tree
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Search | O(log_m n) | O(log_m n) | m is order of tree |
| Insert | O(log_m n) | O(log_m n) | Find position, split if necessary |
| Delete | O(log_m n) | O(log_m n) | Find, remove, rebalance |
| Traverse | O(n) | O(n) | Visit all nodes |
| Height | O(log_m n) | O(log_m n) | Much smaller than BST for large m |
| Split | O(1) | O(1) | Separate node into two |
| Merge | O(1) | O(1) | Combine two nodes |

### Hash Table
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Search | O(1) | O(n) | Worst case with bad hash function |
| Insert | O(1) | O(n) | Depends on collision resolution |
| Delete | O(1) | O(n) | Depends on collision resolution |
| Rehashing | O(n) | O(n) | Must rehash all elements |
| GetLoadFactor | O(1) | O(1) | Calculate elements/size |

#### Hash Table (Collision Resolution Strategies)
| Strategy | Search (Avg) | Insert (Avg) | Search (Worst) | Insert (Worst) | Notes |
|----------|--------------|--------------|----------------|----------------|-------|
| Separate Chaining | O(1 + α) | O(1 + α) | O(n) | O(n) | α = load factor |
| Linear Probing | O(1 / (1-α)) | O(1 / (1-α)) | O(n) | O(n) | Primary clustering |
| Quadratic Probing | O(1 / (1-α)) | O(1 / (1-α)) | O(n) | O(n) | Secondary clustering |
| Double Hashing | O(1 / (1-α)) | O(1 / (1-α)) | O(n) | O(n) | Better distribution |
| Robin Hood Hashing | O(1) | O(1) | O(log n) | O(log n) | Reduces variance |
| Cuckoo Hashing | O(1) | O(1) amortized | O(1) | O(n) | Worst case is rehash |
| Perfect Hashing | O(1) | N/A | O(1) | N/A | Static set only |

### Trie (Prefix Tree)
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Search | O(m) | O(m) | m = length of key |
| Insert | O(m) | O(m) | Add new nodes as needed |
| Delete | O(m) | O(m) | Remove path if unused |
| Prefix Search | O(p) + O(n) | O(p) + O(n) | p = prefix length, n = matches |
| Lexicographic Sort | O(n) | O(n) | Pre-order traversal |
| Space Usage | O(ALPHABET_SIZE * n * m) | O(ALPHABET_SIZE * n * m) | Can be space inefficient |

### Suffix Tree/Array
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Construction (naive) | O(n²) | O(n²) | n = string length |
| Construction (Ukkonen's) | O(n) | O(n) | For suffix tree |
| Construction (suffix array) | O(n log n) | O(n log n) | Using sorting |
| Pattern Matching | O(m + occ) | O(m + occ) | m = pattern length, occ = occurrences |
| Longest Common Substring | O(n) | O(n) | After construction |
| Longest Repeated Substring | O(n) | O(n) | After construction |

### Bloom Filter
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Insert | O(k) | O(k) | k = number of hash functions |
| Lookup | O(k) | O(k) | False positives possible |
| Delete | Not supported | Not supported | Cannot remove elements |
| Union/Intersection | O(n) | O(n) | Bitwise operations on filters |

### Skip List
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Search | O(log n) | O(n) | With high probability O(log n) |
| Insert | O(log n) | O(n) | Requires random level generation |
| Delete | O(log n) | O(n) | Find then remove |
| FindMin/FindMax | O(1) | O(1) | First/last in bottom list |
| Successor/Predecessor | O(1) | O(1) | Next/previous in level |

### Disjoint Set (Union-Find)
| Operation | Average Case | Worst Case | Amortized | Notes |
|-----------|--------------|------------|-----------|-------|
| MakeSet | O(1) | O(1) | O(1) | Create singleton set |
| Find | O(α(n)) | O(log n) | O(α(n)) | With path compression |
| Union | O(α(n)) | O(log n) | O(α(n)) | With rank/size heuristic |
| Connected | O(α(n)) | O(log n) | O(α(n)) | Same as Find |

Note: α(n) is the inverse Ackermann function, which grows extremely slowly. For all practical purposes, α(n) ≤ 4.

### Segment Tree
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Construction | O(n) | O(n) | Bottom-up building |
| Query (Range) | O(log n) | O(log n) | Navigate tree |
| Update (Point) | O(log n) | O(log n) | Update path to root |
| Update (Range) | O(log n) | O(log n) | With lazy propagation |

### Fenwick Tree (Binary Indexed Tree)
| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Construction | O(n) | O(n) | Bottom-up building |
| Query (Prefix Sum) | O(log n) | O(log n) | Navigate ancestors |
| Update (Point) | O(log n) | O(log n) | Update affected ranges |
| Range Query | O(log n) | O(log n) | Two prefix queries |

### Graph Representation
| Structure | Space | Add Vertex | Add Edge | Remove Vertex | Remove Edge | Query Edge | Query Adjacent Vertices |
|-----------|-------|------------|----------|---------------|-------------|------------|-------------------------|
| Adjacency Matrix | O(V²) | O(V²) | O(1) | O(V²) | O(1) | O(1) | O(V) |
| Adjacency List | O(V+E) | O(1) | O(1) | O(V+E) | O(E) or O(degree(v)) | O(degree(v)) | O(degree(v)) |
| Edge List | O(E) | O(1) | O(1) | O(E) | O(E) | O(E) | O(E) |
| Incidence Matrix | O(V·E) | O(V·E) | O(V) | O(V·E) | O(V) | O(V) | O(E) |

## Sorting Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable | Notes |
|-----------|-----------|--------------|------------|-------|--------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | With early stopping |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Always makes n(n-1)/2 comparisons |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Efficient for small or nearly sorted data |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Divide and conquer |
| Quicksort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | In-place with O(log n) stack |
| Heapsort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | In-place sort |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(n+k) | Yes | k is range of input values |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n+k) | Yes | k is number of digits |
| Bucket Sort | O(n+k) | O(n+k) | O(n²) | O(n+k) | Yes | Depends on distribution |
| Shell Sort | O(n log n) | O(n^(4/3)) to O(n^(3/2)) | O(n²) | O(1) | No | Improvement on insertion sort |
| Tim Sort | O(n) | O(n log n) | O(n log n) | O(n) | Yes | Hybrid of merge and insertion sort |
| Introsort | O(n log n) | O(n log n) | O(n log n) | O(log n) | No | Hybrid of quicksort, heapsort, insertion sort |
| Library Sort | O(n) | O(n log n) | O(n log n) | O(n) | Yes | Insertion sort with gaps |

## Selection Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space | Notes |
|-----------|-----------|--------------|------------|-------|-------|
| Quickselect | O(n) | O(n) | O(n²) | O(1) | In-place partitioning |
| Introselect | O(n) | O(n) | O(n) | O(1) | Quickselect + fallback to median of medians |
| MedianOfMedians | O(n) | O(n) | O(n) | O(n) | Guaranteed linear time |
| Min/Max Selection | O(n) | O(n) | O(n) | O(1) | Single pass through array |
| Min and Max | O(n) | O(n) | O(n) | O(1) | 3n/2 comparisons using pairs |
| Selection with BST | O(n log k) | O(n log k) | O(n log k) | O(k) | When k << n |
| Selection with Heap | O(n + k log n) | O(n + k log n) | O(n + k log n) | O(n) | For k-th smallest |

## Graph Algorithms

### Traversal
| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Breadth-First Search (BFS) | O(V+E) | O(V) | Uses queue |
| Depth-First Search (DFS) | O(V+E) | O(V) | Uses stack or recursion |
| Iterative Deepening DFS | O(V·d) | O(d) | d = solution depth |
| Bipartite Checking | O(V+E) | O(V) | Using BFS or DFS |
| Connected Components | O(V+E) | O(V) | Using DFS |

### Shortest Path
| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Dijkstra's (binary heap) | O(E log V) | O(V) | No negative weights |
| Dijkstra's (Fibonacci heap) | O(E + V log V) | O(V) | Theoretical improvement |
| Dijkstra's (adjacency matrix) | O(V²) | O(V) | Dense graphs |
| Bellman-Ford | O(V·E) | O(V) | Handles negative weights |
| SPFA (Shortest Path Faster Algorithm) | O(E) average, O(V·E) worst | O(V) | Optimized Bellman-Ford |
| Floyd-Warshall (all pairs) | O(V³) | O(V²) | Dynamic programming approach |
| Johnson's (all pairs) | O(V² log V + V·E) | O(V²) | Combines Dijkstra and Bellman-Ford |
| A* Search | O(E) | O(V) | Best-case with perfect heuristic |
| Bidirectional Search | O(b^(d/2)) | O(b^(d/2)) | b = branching factor, d = depth |

### Minimum Spanning Tree
| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Prim's (binary heap) | O(E log V) | O(V) | Grows single tree |
| Prim's (Fibonacci heap) | O(E + V log V) | O(V) | Theoretical improvement |
| Prim's (adjacency matrix) | O(V²) | O(V) | For dense graphs |
| Kruskal's | O(E log E) or O(E log V) | O(V) | Uses Union-Find |
| Borůvka's | O(E log V) | O(V) | Grows multiple trees |
| Reverse-Delete | O(E log E log V) | O(E) | Kruskal's in reverse |

### Strongly Connected Components
| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Kosaraju's | O(V+E) | O(V) | Two DFS passes |
| Tarjan's | O(V+E) | O(V) | Single DFS pass |
| Gabow's | O(V+E) | O(V) | Similar to Tarjan's |

### Topological Sort
| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| DFS-based | O(V+E) | O(V) | Uses finish times |
| Kahn's (BFS-based) | O(V+E) | O(V) | Uses in-degree counters |
| Lexicographically smallest | O(V+E) | O(V+E) | Using priority queue |

### Cycle Detection
| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| DFS | O(V+E) | O(V) | Using recursion stack |
| Union-Find | O(E·α(V)) | O(V) | For undirected graphs |
| Floyd's Tortoise and Hare | O(V+E) | O(1) | For directed graphs |
| Checking if DAG | O(V+E) | O(V) | Using topological sort |

### Network Flow
| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Ford-Fulkerson | O(E·max_flow) | O(V+E) | Using DFS |
| Edmonds-Karp | O(V·E²) | O(V+E) | Ford-Fulkerson with BFS |
| Dinic's | O(V²·E) | O(V+E) | Using blocking flows |
| Push-Relabel | O(V²·E) | O(V²) | Preflow approach |
| MPM (Malhotra, Pramodh-Kumar, Maheshwari) | O(V³) | O(V²) | Blocking flow approach |

### Maximum Bipartite Matching
| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Ford-Fulkerson | O(V·E) | O(V+E) | For bipartite graphs |
| Hopcroft-Karp | O(E·√V) | O(V+E) | Improved for bipartite |
| Hungarian Algorithm | O(V³) | O(V²) | For weighted bipartite matching |

### Miscellaneous Graph Algorithms
| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Articulation Points | O(V+E) | O(V) | Using Tarjan's algorithm |
| Bridges | O(V+E) | O(V) | Using Tarjan's algorithm |
| Biconnected Components | O(V+E) | O(V+E) | Using Tarjan's algorithm |
| Eulerian Path/Circuit | O(V+E) | O(V+E) | Check degrees & connectivity |
| Hamiltonian Path | NP-complete | - | No efficient algorithm known |
| Minimum Vertex Cover | NP-complete | - | 2-approximation in O(V+E) |
| Maximum Independent Set | NP-complete | - | Complement of vertex cover |
| Graph Coloring | NP-complete | - | Greedy algorithm: O(V+E) |
| Traveling Salesman | NP-complete | - | Dynamic programming: O(2^V · V²) |

## Dynamic Programming Algorithms

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Fibonacci Sequence | O(n) | O(1) iterative, O(n) memoization | Classic example |
| Longest Common Subsequence | O(m·n) | O(m·n) or O(min(m,n)) | Two sequences |
| Edit Distance (Levenshtein) | O(m·n) | O(m·n) or O(min(m,n)) | Two strings |
| Knapsack Problem (0/1) | O(n·W) | O(n·W) or O(W) | n items, capacity W |
| Knapsack Problem (Unbounded) | O(n·W) | O(W) | Can take multiple of each item |
| Matrix Chain Multiplication | O(n³) | O(n²) | Optimal parenthesization |
| Longest Increasing Subsequence | O(n²) or O(n log n) | O(n) | With patience sort |
| Coin Change (minimum coins) | O(n·amount) | O(amount) | Dynamic programming |
| Coin Change (number of ways) | O(n·amount) | O(amount) | Dynamic programming |
| Subset Sum | O(n·sum) | O(sum) | Check if subset sums to target |
| Partition Problem | O(n·sum) | O(sum) | Equal sum subsets |
| Rod Cutting | O(n²) | O(n) | Maximize revenue |
| Maximum Subarray | O(n) | O(1) | Kadane's algorithm |
| Optimal Binary Search Tree | O(n³) | O(n²) | Minimize expected search time |
| Word Break | O(n²·m) | O(n) | n = string length, m = dictionary size |
| Regular Expression Matching | O(m·n) | O(m·n) | m = pattern length, n = string length |

## String Algorithms

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Naive String Matching | O(n·m) | O(1) | n = text length, m = pattern length |
| Rabin-Karp | O(n+m) average, O(n·m) worst | O(1) | Uses rolling hash |
| Knuth-Morris-Pratt (KMP) | O(n+m) | O(m) | Uses prefix function |
| Boyer-Moore | O(n·m) worst, O(n/m) best | O(m+σ) | σ = alphabet size |
| Aho-Corasick | O(n+m+z) | O(m) | z = number of pattern occurrences |
| Z Algorithm | O(n+m) | O(n+m) | For pattern matching |
| Manacher's Algorithm | O(n) | O(n) | Find all palindromic substrings |
| Longest Palindromic Substring | O(n²) naive, O(n) Manacher's | O(n) | Fin# Comprehensive Data Structures & Algorithms Time Complexity Reference

## Data Structure Operations

### Array/Vector
| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Access by index | O(1) | O(1) |
| Search (unsorted) | O(n) | O(n) |
| Search (sorted) | O(log n) | O(log n) |
| Insert/Delete (at end) | O(1) | O(1) |
| Insert/Delete (at beginning/middle) | O(n) | O(n) |
| Push/Pop (at end) | O(1) amortized | O(1) amortized |

### Linked List (Singly/Doubly)
| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Access by index | O(n) | O(n) |
| Search | O(n) | O(n) |
| Insert/Delete (at beginning) | O(1) | O(1) |
| Insert/Delete (at middle with pointer) | O(1) | O(1) |
| Insert/Delete (at middle w/o pointer) | O(n) | O(n) |
| Insert/Delete (at end with tail pointer) | O(1) | O(1) |
| Insert/Delete (at end w/o tail pointer) | O(n) | O(n) |

### Stack (using Array or Linked List)
| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Push | O(1) | O(1) |
| Pop | O(1) | O(1) |
| Peek (Top) | O(1) | O(1) |
| Search | O(n) | O(n) |
| Size | O(1) | O(1) |

### Queue (using Array or Linked List)
| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Enqueue | O(1) | O(1) |
| Dequeue | O(1) | O(1) |
| Peek (Front) | O(1) | O(1) |
| Search | O(n) | O(n) |
| Size | O(1) | O(1) |

### Binary Heap
| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Find Min/Max | O(1) | O(1) |
| Insert | O(log n) | O(log n) |
| Delete Min/Max | O(log n) | O(log n) |
| Extract Min/Max | O(log n) | O(log n) |
| Decrease/Increase Key | O(log n) | O(log n) |
| BuildHeap | O(n) | O(n) |
| Heapify | O(log n) | O(log n) |
| Merge | O(n) | O(n) |

### Binary Search Tree (Unbalanced)
| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| FindMin/FindMax | O(log n) | O(n) |
| Successor/Predecessor | O(log n) | O(n) |
| Height | O(log n) | O(n) |

### AVL Tree
| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Search | O(log n) | O(log n) |
| Insert | O(log n) | O(log n) |
| Delete | O(log n) | O(log n) |
| FindMin/FindMax | O(log n) | O(log n) |
| Successor/Predecessor | O(log n) | O(log n) |
| Height | O(log n) | O(log n) |
| Rebalance (rotation) | O(1) | O(1) |

### Red-Black Tree
| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Search | O(log n) | O(log n) |
| Insert | O(log n) | O(log n) |
| Delete | O(log n) | O(log n) |
| FindMin/FindMax | O(log n) | O(log n) |
| Successor/Predecessor | O(log n) | O(log n) |
| Height | O(log n) | O(log n) |
| Rebalance (rotation) | O(1) | O(1) |

### Splay Tree
| Operation | Average Case | Worst Case | Amortized |
|-----------|--------------|------------|-----------|
| Search | O(log n) | O(n) | O(log n) |
| Insert | O(log n) | O(n) | O(log n) |
| Delete | O(log n) | O(n) | O(log n) |
| FindMin/FindMax | O(log n) | O(n) | O(log n) |

### Hash Table
| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Search | O(1) | O(n) |
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Rehashing | O(n) | O(n) |

#### Hash Table (Collision Resolution Strategies)
| Strategy | Search (Average) | Insert (Average) | Search (Worst) | Insert (Worst) |
|----------|------------------|------------------|----------------|----------------|
| Separate Chaining | O(1 + α) | O(1 + α) | O(n) | O(n) |
| Linear Probing | O(1 / (1-α)) | O(1 / (1-α)) | O(n) | O(n) |
| Quadratic Probing | O(1 / (1-α)) | O(1 / (1-α)) | O(n) | O(n) |
| Double Hashing | O(1 / (1-α)) | O(1 / (1-α)) | O(n) | O(n) |

Note: α = load factor (number of elements / table size)

### Trie (Prefix Tree)
| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Search | O(m) | O(m) |
| Insert | O(m) | O(m) |
| Delete | O(m) | O(m) |
| Prefix Search | O(m) | O(m) |

Note: m = length of string/key

### Graph Representation
| Structure | Space | Add Vertex | Add Edge | Remove Vertex | Remove Edge | Query Edge |
|-----------|-------|------------|----------|---------------|-------------|------------|
| Adjacency Matrix | O(V²) | O(V²) | O(1) | O(V²) | O(1) | O(1) |
| Adjacency List | O(V+E) | O(1) | O(1) | O(V+E) | O(E) | O(degree(v)) |
| Edge List | O(E) | O(1) | O(1) | O(E) | O(E) | O(E) |

## Sorting Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable |
|-----------|-----------|--------------|------------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quicksort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heapsort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(n+k) | Yes |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n+k) | Yes |
| Bucket Sort | O(n+k) | O(n+k) | O(n²) | O(n) | Yes |
| Shell Sort | O(n log n) | O(n log n) to O(n^(3/2)) | O(n²) | O(1) | No |
| Introsort | O(n log n) | O(n log n) | O(n log n) | O(log n) | No |

Note: k = range of input values or number of digits in Radix Sort

## Selection Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| Quickselect | O(n) | O(n) | O(n²) | O(1) |
| Introselect | O(n) | O(n) | O(n) | O(1) |
| MedianOfMedians | O(n) | O(n) | O(n) | O(n) |

## Graph Algorithms

### Traversal
| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Breadth-First Search (BFS) | O(V+E) | O(V) |
| Depth-First Search (DFS) | O(V+E) | O(V) |

### Shortest Path
| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Dijkstra's (using adjacency list + binary heap) | O(E log V) | O(V) | No negative weights |
| Dijkstra's (using adjacency matrix) | O(V²) | O(V) | No negative weights |
| Bellman-Ford | O(V·E) | O(V) | Can detect negative cycles |
| Floyd-Warshall (all pairs) | O(V³) | O(V²) | Handles negative weights |
| Johnson's (all pairs) | O(V² log V + V·E) | O(V²) | Better than Floyd-Warshall for sparse graphs |
| A* Search | O(E) | O(V) | Best-case with good heuristic |

### Minimum Spanning Tree
| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Prim's (using adjacency list + binary heap) | O(E log V) | O(V) |
| Prim's (using adjacency matrix) | O(V²) | O(V) |
| Kruskal's | O(E log E) or O(E log V) | O(V) |
| Borůvka's | O(E log V) | O(V) |

### Strongly Connected Components
| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Kosaraju's | O(V+E) | O(V) |
| Tarjan's | O(V+E) | O(V) |

### Topological Sort
| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| DFS-based | O(V+E) | O(V) |
| Kahn's (BFS-based) | O(V+E) | O(V) |

### Network Flow
| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Ford-Fulkerson | O(E·max_flow) | O(V+E) |
| Edmonds-Karp | O(V·E²) | O(V+E) |
| Dinic's | O(V²·E) | O(V+E) |
| Push-Relabel | O(V²·E) | O(V²) |

### Miscellaneous
| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Union-Find | O(α(n)) per operation | O(n) | α is inverse Ackermann function, practically constant |
| Articulation Points | O(V+E) | O(V) | Using Tarjan's algorithm |
| Bridges | O(V+E) | O(V) | Using Tarjan's algorithm |
| Bipartite Checking | O(V+E) | O(V) | Using BFS or DFS |
| Cycle Detection | O(V+E) | O(V) | Using DFS |

## Dynamic Programming Algorithms

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Fibonacci Sequence | O(n) | O(1) iterative, O(n) memoization |
| Longest Common Subsequence | O(m·n) | O(m·n) or O(min(m,n)) |
| Edit Distance | O(m·n) | O(m·n) or O(min(m,n)) |
| Knapsack Problem (0/1) | O(n·W) | O(n·W) or O(W) |
| Matrix Chain Multiplication | O(n³) | O(n²) |
| Longest Increasing Subsequence | O(n²) or O(n log n) | O(n) |
| Coin Change (minimum coins) | O(n·amount) | O(amount) |
| Subset Sum | O(n·sum) | O(sum) |
| All Pairs Shortest Path (DP) | O(V³) | O(V²) |

## String Algorithms

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Naive String Matching | O(n·m) | O(1) | n = text length, m = pattern length |
| Rabin-Karp | O(n+m) average, O(n·m) worst | O(1) | Uses rolling hash |
| Knuth-Morris-Pratt (KMP) | O(n+m) | O(m) | Uses prefix function |
| Boyer-Moore | O(n·m) worst, O(n/m) best | O(m+σ) | σ = alphabet size |
| Aho-Corasick | O(n+m+z) | O(m) | z = number of pattern occurrences |
| Longest Palindromic Substring | O(n²) naive, O(n) Manacher's | O(n) | |

## Computational Complexity Classes
- P: Problems solvable in polynomial time
- NP: Problems verifiable in polynomial time
- NP-Complete: Hardest problems in NP (all NP problems reduce to them)
- NP-Hard: At least as hard as the hardest problems in NP

## STL Container Complexity

### std::vector
| Operation | Time Complexity |
|-----------|----------------|
| Random access | O(1) |
| Insert/erase at end | O(1) amortized |
| Insert/erase at middle | O(n) |
| Find | O(n) |

### std::list
| Operation | Time Complexity |
|-----------|----------------|
| Random access | O(n) |
| Insert/erase at position | O(1) with iterator |
| Find | O(n) |
| Splice | O(1) |

### std::deque
| Operation | Time Complexity |
|-----------|----------------|
| Random access | O(1) |
| Insert/erase at begin/end | O(1) amortized |
| Insert/erase at middle | O(n) |

### std::map / std::set (Red-Black Tree)
| Operation | Time Complexity |
|-----------|----------------|
| Insert | O(log n) |
| Erase | O(log n) |
| Find | O(log n) |
| Lower/Upper bound | O(log n) |
| Range query | O(log n + k) |

### std::unordered_map / std::unordered_set (Hash Table)
| Operation | Time Complexity |
|-----------|----------------|
| Insert | O(1) average, O(n) worst |
| Erase | O(1) average, O(n) worst |
| Find | O(1) average, O(n) worst |

### std::priority_queue (Binary Heap)
| Operation | Time Complexity |
|-----------|----------------|
| Push | O(log n) |
| Pop | O(log n) |
| Top | O(1) |

## Special Cases to Remember

1. **Minimal AVL Tree Size**: 
   - Height h: Nodes = f(h) = f(h-1) + f(h-2) + 1
   - Base cases: f(0) = 1, f(1) = 2
   - Height 8: 88 nodes

2. **BuildHeap Time Complexity**:
   - O(n) despite having n calls to percolate down (each O(log n))
   - Tighter analysis shows the actual complexity is O(n)

3. **Dijkstra's vs. Prim's**:
   - Both use similar greedy approach with priority queues
   - Dijkstra's: Updates distances from source
   - Prim's: Updates distances to MST

4. **When Binary Heaps Are Suboptimal**:
   - Fibonacci heaps better for decreaseKey operations (O(1) amortized)
   - Binary heaps still have O(log n) for decreaseKey

5. **Optimal Hash Table Load Factor**:
   - Open addressing: ~70% before performance degrades
   - Separate chaining: Can go above 100% but typically kept around 70-80%

6. **Quicksort vs. Quickselect**:
   - Quicksort: O(n log n) average, sorts everything
   - Quickselect: O(n) average, finds kth element only