# CSCI335 DSA 

![GitHub](https://img.shields.io/badge/Language-C++-blue) 
![GitHub](https://img.shields.io/badge/Status-Active-brightgreen)
![GitHub](https://img.shields.io/badge/Version-V.1_Spring_2025-orange)

A repository for students taking **Software Analysis & Design III at CUNY Hunter College** to review and practice fundamental Data Structures and Algorithms (DSA) concepts. 

**Acknowledgments**
----------------------

-   **Instructor**: Justin Tojeira, CUNY Hunter College.
-   **Textbook**: *Data Structures and Algorithm Analysis in C++* by Mark Allen Weiss.

# A Comprehensive Course Overview 

## Table of Contents
1. [Foundations and Complexity Analysis](#foundations-and-complexity-analysis)
2. [Lists, Vectors, and STL Basics](#lists-vectors-and-stl-basics)
3. [Trees](#trees)
   - [Binary Search Trees](#binary-search-trees)
   - [AVL Trees](#avl-trees)
   - [Splay Trees](#splay-trees)
4. [Hashing](#hashing)
5. [Heaps and Priority Queues](#heaps-and-priority-queues)
6. [Sorting Algorithms](#sorting-algorithms)
7. [Graph Algorithms](#graph-algorithms)
8. [Greedy Algorithms and Dynamic Programming](#greedy-algorithms-and-dynamic-programming)
9. [Time Complexity Reference](#time-complexity-reference)
10. [Exam Focus Areas](#exam-focus-areas)

---

## Foundations and Complexity Analysis

### Core Concepts
- **Big-O notation** and asymptotic analysis
- Differences between best, average, and worst-case analyses
- Time and space complexity
- Empirical analysis of algorithms

### Implementation Notes
- Using chrono library for timing performance
- Analyzing algorithms empirically and comparing to theoretical complexity

### Key Textbook Sections
- Chapter 1 (up to 1.5)
- Chapter 2 (complete)

### Exam Tips
- This material appears primarily in complexity analysis questions and as part of analyzing algorithms
- You'll need to analyze the complexity of various data structures and algorithms
- Be ready to explain why an algorithm has a particular complexity

---

## Lists, Vectors, and STL Basics

### Core Concepts
- Sequence containers: vectors, lists
- Iterators and their properties
- Time complexity of vector vs. list operations
- Linear data structures and operations

### Implementation Notes
- STL methods and iterator methods
- Differences between vector and list iterators
- Efficient iteration techniques
- Proper use of push_back, pop_back, erase, and insert methods

### Key Textbook Sections
- Chapter 3 (3.1, 3.2, 3.3, 3.4, 3.5)

### Exam Tips
- Be prepared to implement algorithms using vectors vs. lists
- Understand tradeoffs between sequence containers
- Know STL methods and their time complexities
- Understand when to use which data structure based on the operations needed

---

## Trees

### Binary Search Trees

#### Core Concepts
- Binary search tree property
- Tree traversals (inorder, preorder, postorder)
- BST insert, find, and remove operations
- Balanced vs. unbalanced trees

#### Implementation Notes
- Pointer-based implementations
- Recursive vs. iterative approaches
- Handling special cases in remove operations

#### Key Textbook Sections
- Chapter 4 (up to 4.4)

### AVL Trees

#### Core Concepts
- AVL balance property: height difference ≤ 1
- Single and double rotations
- Insertion, removal, and rebalancing operations
- Height tracking

#### Implementation Notes
- Implementing rotations efficiently
- Balance factors and height updates
- Insertion and deletion with rebalancing

#### Key Textbook Sections
- Chapter 4 (4.4)

#### Exam Tips
- Understand how to trace AVL tree operations
- Know how to perform single and double rotations
- Be able to identify when a tree needs rebalancing
- Understand the impact of operations on tree height

### Splay Trees

#### Core Concepts
- Self-adjusting property
- Splaying operations (zig, zig-zig, zig-zag)
- Amortized analysis
- Logarithmic worst-case amortized complexity

#### Implementation Notes
- Splaying after access, insertion, or deletion
- Moving frequently accessed nodes to root

#### Key Textbook Sections
- Splay tree sections from the textbook

#### Exam Tips
- Understand the difference between worst-case amortized and average-case complexity
- Know the splaying patterns and operations
- Be able to explain the benefits of splay trees

---

## Hashing

### Core Concepts
- Hash functions and their properties
- Collision resolution strategies
- Load factor and rehashing
- Open addressing vs. separate chaining

### Specific Techniques
- **Double hashing**: Using two hash functions to resolve collisions
- **Linear probing** and **quadratic probing**
- **Separate chaining** with linked lists or other containers
- Universal hashing

### Implementation Notes
- Implementing hash functions
- STL containers: unordered_map, unordered_set
- Handling string keys effectively
- Maintaining appropriate load factors

### Key Textbook Sections
- Chapter 5 (up to 5.6)

### Exam Tips
- Be able to trace hash table operations with different collision strategies
- Understand the impact of load factor on performance
- Know how to analyze hash functions
- Understand the time complexity of operations in different scenarios
- Know when to use ordered vs. unordered containers

---

## Heaps and Priority Queues

### Core Concepts
- Binary heap properties (min heap, max heap)
- Priority queue operations
- Heap implementation using arrays
- BuildHeap, insert, deleteMin, decreaseKey operations

### Implementation Notes
- Array-based implementation
- percDown and buildHeap operations
- Using STL priority_queue
- Index calculations for parent and children
- Special implementation with index 0 unused or storing temporary value

### Key Textbook Sections
- Chapter 6

### Exam Tips
- Understand heap property maintenance
- Be able to trace heap operations
- Know the complexities of heap operations
- Implement buildHeap and deleteMin operations
- Know how to use priority_queue in the STL
- Understand heap applications to sorting algorithms

---

## Sorting Algorithms

### Key Algorithms

#### Comparison Sorts
- **Quicksort** 
  - Partitioning strategies (Hoare, Lomuto)
  - Pivot selection strategies (median-of-three)
  - Average O(n log n), worst-case O(n²)
  
- **Heapsort**
  - Using heap properties for sorting
  - Worst-case O(n log n) with O(1) extra space
  
- **Mergesort**
  - Divide and conquer approach
  - Stable, O(n log n) with O(n) extra space
  
- **Insertion Sort**
  - Simple, efficient for small arrays
  - O(n²) worst-case, O(n) for nearly sorted data

#### Hybrid Sorts
- **Introsort**
  - Combines quicksort, heapsort, and insertion sort
  - Used in many STL implementations
  - O(n log n) worst-case

### Implementation Notes
- Choosing the right sort based on data characteristics
- Using STL sort functions
- Implementing custom comparators
- Optimizations for partially sorted data

### Key Textbook Sections
- Chapter 7

### Exam Tips
- Understand the tradeoffs between sorting algorithms
- Be able to trace sort operations
- Know best/average/worst-case complexities
- Understand when to use each algorithm
- Know special characteristics (stable, in-place, etc.)

---

## Graph Algorithms

### Core Concepts
- Graph representations (adjacency matrix, adjacency list)
- Graph traversals: BFS, DFS
- Directed vs. undirected graphs
- Weighted vs. unweighted graphs
- Topological sorting

### Key Algorithms
- **Shortest Path Algorithms**
  - Dijkstra's algorithm (single-source, non-negative weights)
  - Bellman-Ford algorithm (single-source, handles negative weights)
  - Floyd-Warshall algorithm (all-pairs shortest paths)
  - Johnson's algorithm (all-pairs for sparse graphs)

- **Minimum Spanning Tree**
  - Prim's algorithm 
  - Kruskal's algorithm

- **Special Graph Problems**
  - Vertex Cover
  - Connected Components
  - Strongly Connected Components

### Implementation Notes
- Efficient graph representation choice
- Using priority queues with Dijkstra's algorithm
- Using disjoint sets with Kruskal's algorithm
- Complexity analysis based on graph density

### Key Textbook Sections
- Chapter 9 (except 9.3.4, 9.3.6, 9.4, 9.6)

### Exam Tips
- **EXAM FOCUS AREA - This is half of your exam!**
- Be able to trace through graph algorithms step by step
- Know the correct data structures for each algorithm
- Understand time complexity based on implementation choices
- Be prepared for algorithm design problems with graphs
- Remember topological ordering is only for directed acyclic graphs (DAGs)
- Be able to choose the right algorithm based on problem characteristics

---

## Greedy Algorithms and Dynamic Programming

### Greedy Algorithms
- Characteristics of greedy approach
- Problem examples suitable for greedy solutions
- Proof of correctness
- Limitations

### Dynamic Programming
- Breaking problems into overlapping subproblems
- Memoization and tabulation approaches
- Bottom-up vs. top-down implementation
- Identifying subproblems and optimal substructure

### Implementation Notes
- Building 1D and 2D tables for DP problems
- Recognizing when DP is applicable
- Time and space complexity optimization

### Key Textbook Sections
- Chapter 10 (10.1 introduction, 10.3 introduction, 10.3.1)

### Exam Tips
- **EXAM FOCUS AREA - This is part of the half of your exam!**
- Understand when to apply greedy vs. dynamic programming
- Be able to define subproblems and recurrence relations
- Know how to implement both tabulation and memoization
- Recognize common DP patterns (e.g., subarray problems, Fibonacci-like problems)

---

## Time Complexity Reference

| Data Structure/Algorithm | Average-Case | Worst-Case | Notes |
|--------------------------|--------------|------------|-------|
| **BST Operations**       | O(log n)     | O(n)       | Depends on tree balance |
| **AVL Operations**       | O(log n)     | O(log n)   | Guaranteed balance |
| **Splay Tree (amortized)**| O(log n)   | O(log n)   | Amortized analysis |
| **Hash Table Operations**| O(1)         | O(n)       | Depends on hash function and load factor |
| **Heap Operations**      | O(log n)     | O(log n)   | Insert, deleteMin |
| **BuildHeap**            | O(n)         | O(n)       | Not O(n log n) as might be expected |
| **QuickSort**            | O(n log n)   | O(n²)      | Depends on pivot selection |
| **HeapSort**             | O(n log n)   | O(n log n) | |
| **MergeSort**            | O(n log n)   | O(n log n) | Requires O(n) extra space |
| **Insertion Sort**       | O(n²)        | O(n²)      | O(n) for nearly sorted data |
| **Dijkstra's Algorithm** | O((V+E)log V)| O((V+E)log V) | With binary heap |
| **Prim's Algorithm**     | O(E log V)   | O(E log V) | With binary heap |
| **Kruskal's Algorithm**  | O(E log V)   | O(E log V) | Dominated by sorting edges |
| **Floyd-Warshall**       | O(V³)        | O(V³)      | All-pairs shortest path |
| **Johnson's Algorithm**  | O(V² log V + VE) | O(V² log V + VE) | All-pairs for sparse graphs |

---

## Exam Focus Areas

Based on the course materials, your final exam will focus on:

1. **Graph Algorithms (Chapter 9)**
   - Algorithm tracing (Dijkstra's, Prim's, Kruskal's)
   - Complexity analysis with different implementations
   - Special graph problems (Vertex Cover)
   - Implementation details and efficiency considerations

2. **Greedy Algorithms and Dynamic Programming (Chapter 10)**
   - When to apply each paradigm
   - Implementation approaches
   - Problem-solving strategies

3. **Core Data Structures**
   - AVL Trees operations and balance
   - Heap operations and implementation
   - Hash table design and analysis

4. **Algorithm Analysis**
   - Time and space complexity
   - Implementation trade-offs
   - Efficiency optimizations

5. **Code Implementation**
   - Expect to write or trace code for key algorithms
   - Focus on efficient implementation techniques
   - Special attention to boundary cases and edge conditions

### Final Exam Structure
- 2-3 algorithm analysis/design questions (at least one from Ch. 9-10)
- 2-3 coding questions (at least one from Ch. 9-10)
- 1-2 algorithm trace questions on material from Ch. 9-10
- Complexity questions
- Short-answer questions (except classes and move semantics)

### Key Study Strategies
1. **Practice algorithm tracing**
   - Trace through Dijkstra's, Prim's, and Kruskal's algorithms step-by-step
   - Practice AVL rotations and heap operations

2. **Review implementation details**
   - Focus on buildHeap, percDown, AVL rotations
   - Understand graph algorithm implementations

3. **Master complexity analysis**
   - Be able to analyze any algorithm covered in class
   - Understand how implementation choices affect complexity

4. **Practice coding problems**
   - Implement key algorithms from scratch
   - Focus on efficiency and correctness
