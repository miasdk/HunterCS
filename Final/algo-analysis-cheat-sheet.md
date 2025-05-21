# Algorithm Analysis & Design Cheat Sheet

This cheat sheet will help you quickly identify the optimal approach and data structures for algorithm design questions based on key terms and requirements in the problem statement.

## 1. Problem Type Identification

### Search Problems
**Key Terms**: "find", "search", "locate", "determine if exists"

| Constraints/Characteristics | Recommended Approach | Time Complexity |
|----------------------------|----------------------|-----------------|
| Sorted data | Binary search | O(log n) |
| Unsorted data | Hash table | O(1) average |
| Multi-dimensional search | Binary search tree, trie, or spatial data structure | O(log n) to O(n) |
| Fuzzy search / similarity | Bloom filters, nearest-neighbor algorithms | Varies |

### Sorting Problems
**Key Terms**: "order", "sort", "arrange", "rank"

| Constraints/Characteristics | Recommended Approach | Time Complexity |
|----------------------------|----------------------|-----------------|
| Small data | Insertion sort | O(n²) |
| General purpose | Quicksort, Merge sort | O(n log n) |
| Stability required | Merge sort | O(n log n) |
| Integer values in range | Counting sort, Radix sort | O(n) |
| External sorting (limited memory) | Merge sort | O(n log n) |
| Nearly sorted data | Insertion sort | O(n) to O(n²) |

### Graph Problems
**Key Terms**: "network", "connection", "path", "route", "circuit", "vertices", "nodes", "edges"

| Constraints/Characteristics | Recommended Approach | Time Complexity |
|----------------------------|----------------------|-----------------|
| Shortest path (non-negative weights) | Dijkstra's algorithm | O(E log V) |
| Shortest path (may have negative weights) | Bellman-Ford algorithm | O(VE) |
| All pairs shortest paths | Floyd-Warshall algorithm | O(V³) |
| Minimum spanning tree | Prim's or Kruskal's algorithm | O(E log V) |
| Connectivity | BFS/DFS | O(V + E) |
| Topological sorting | DFS-based algorithm | O(V + E) |
| Cycle detection | DFS with coloring | O(V + E) |
| Maximum flow | Ford-Fulkerson, Edmonds-Karp | O(E·max_flow), O(VE²) |

### Optimization Problems
**Key Terms**: "maximize", "minimize", "optimal", "most efficient", "best", "least"

| Constraints/Characteristics | Recommended Approach | Time Complexity |
|----------------------------|----------------------|-----------------|
| Can be broken into subproblems | Dynamic programming | Varies |
| Exhibits optimal substructure | Greedy algorithm | Varies |
| Selection problem (kth smallest) | Quickselect | O(n) average |
| Resource allocation | Dynamic programming, Linear programming | Varies |
| NP-hard problems | Approximation algorithms, heuristics | Varies |

### String Problems
**Key Terms**: "substring", "pattern", "match", "text", "character"

| Constraints/Characteristics | Recommended Approach | Time Complexity |
|----------------------------|----------------------|-----------------|
| Pattern matching | KMP, Boyer-Moore | O(n + m) |
| Multiple pattern matching | Aho-Corasick | O(n + m + z) |
| Edit distance | Dynamic programming | O(nm) |
| Substring problems | Suffix trees/arrays, rolling hash | O(n) to O(n log n) |
| Lexicographic ordering | Trie | O(L) per operation |

### Data Structure Design Problems
**Key Terms**: "design", "implement", "create", "support operations"

| Required Operations | Recommended Data Structure | Time Complexity |
|---------------------|----------------------------|-----------------|
| Insert, Delete, Find | Hash table | O(1) average |
| Order statistics, range queries | Balanced BST, Segment tree | O(log n) |
| Min/Max queries | Heap | O(1) for queries, O(log n) for updates |
| Prefix/running sums | Fenwick tree (BIT) | O(log n) |
| LRU Cache | Hash table + Doubly linked list | O(1) per operation |
| Disjoint sets | Union-Find | O(α(n)) per operation |

## 2. Problem Characteristics Analysis

### Scale & Constraints
| Data Size | Acceptable Time Complexities |
|-----------|------------------------------|
| n ≤ 10² | O(n²), O(n²log n), or even O(2ⁿ) may be acceptable |
| 10² < n ≤ 10⁵ | O(n log n) or better |
| 10⁵ < n ≤ 10⁷ | O(n) or better |
| n > 10⁷ | O(n) or better, with careful constant factor optimization |

### Memory Constraints
| Constraint | Approach |
|------------|----------|
| Very limited memory | In-place algorithms, streaming algorithms, external algorithms |
| Standard memory | Regular algorithmic approaches |
| Plenty of memory | Trade space for time with preprocessing or caching |

### Input Distribution
| Distribution Type | Potential Optimization |
|-------------------|------------------------|
| Uniform | Hash-based methods, bucket sort |
| Normal | Quicksort with median-of-3 pivot |
| Skewed | Adaptive algorithms, specialized data structures |
| Unknown | Robust algorithms with good worst-case guarantees |

## 3. Common Design Patterns & Approaches

### Divide and Conquer
**When to Use**: Problem can be broken down into identical smaller subproblems
**Examples**: Merge sort, quicksort, Karatsuba multiplication

### Dynamic Programming
**When to Use**: Problem exhibits optimal substructure and overlapping subproblems
**Examples**: Knapsack, longest common subsequence, matrix chain multiplication

### Greedy Algorithms
**When to Use**: Local optimum choice leads to global optimum
**Examples**: Huffman coding, activity selection, Dijkstra's algorithm

### Backtracking
**When to Use**: Need to find all (or some) solutions, potentially with constraints
**Examples**: N-queens, sudoku solver, combination sum

### Sliding Window
**When to Use**: Need to process subarrays/substrings of varying or fixed length
**Examples**: Maximum sum subarray of size k, longest substring without repeating characters

### Two Pointers
**When to Use**: Array/string problems requiring pair finding or partitioning
**Examples**: Two sum, remove duplicates, container with most water

### Binary Search
**When to Use**: Search space can be divided in half with each step
**Examples**: Finding elements in sorted array, peak finding, minimizing maximum values

### Graph Traversal
**When to Use**: Need to explore relationships or paths in a network
**Examples**: Shortest path, connectivity, cycle detection

### Hashing
**When to Use**: Fast lookup, duplicate detection, caching
**Examples**: Two sum, LRU cache, substring with concatenation of all words

## 4. Key Terms & Pattern Recognition

### Optimization Problems
- **"Maximum/minimum result"** → Dynamic programming, greedy
- **"Optimal arrangement"** → Dynamic programming, sorting
- **"Least cost/most profit"** → Graph algorithms, dynamic programming

### Counting Problems
- **"How many ways"** → Dynamic programming, combinatorics
- **"Count all possible"** → Recursion with memoization, DP
- **"Probability of"** → Dynamic programming with probability

### Existence Problems
- **"Is it possible"** → Graph traversal, backtracking
- **"Can it be divided"** → Dynamic programming, greedy
- **"Does there exist"** → Hash-based approach, binary search

### Constructive Problems
- **"Find any valid"** → Greedy algorithms, constructive approaches
- **"Generate all"** → Backtracking, recursion
- **"Construct a solution"** → Greedy, graph algorithms

## 5. Time Complexity Requirements

If the problem constraints suggest a maximum possible time complexity, use this table to guide your approach selection:

| Max Complexity | Typical Approaches |
|----------------|-------------------|
| O(1) | Direct formula, math solution |
| O(log n) | Binary search, divide and conquer |
| O(n) | Linear scan, two pointers, sliding window |
| O(n log n) | Sorting, heap operations, divide and conquer |
| O(n²) | Nested loops, simple DP, quadratic algorithms |
| O(n³) | Triple nested loops, complex DP |
| O(2ⁿ) | Exponential algorithms, complete search |

## 6. Quick Decision Guide by Problem Domain

### Arrays and Strings
- Sorted array operations → Binary search
- Substring problems → Rolling hash, KMP, suffix structures
- Multiple array comparison → Hash tables, tries
- Subarray sums → Prefix sums, sliding window
- Array rearrangement → Sorting, in-place techniques

### Trees and Graphs
- Path finding → BFS, Dijkstra's, A*
- Tree traversal → DFS, BFS, specialized traversals
- Graph connectivity → Union-Find, DFS
- Tree construction → Construction algorithms, rotations
- Network flow → Ford-Fulkerson, Edmonds-Karp

### Numbers and Math
- Prime numbers → Sieve, primality tests
- GCD/LCM → Euclidean algorithm
- Combinations/permutations → Combinatorial algorithms
- Fast computation → Bit manipulation, math properties

### Data Structure Design
- Fast access → Hash tables
- Ordered operations → Balanced BSTs
- Frequent min/max → Heaps
- Nested ranges → Segment trees, interval trees
- Disjoint data → Union-Find

## 7. Algorithm Design Process

For those longer algorithm design questions, follow this structured approach:

1. **Understand the problem**
   - Identify the core task
   - Note constraints and edge cases
   - Determine acceptable time/space complexity

2. **Choose appropriate data structures**
   - Consider required operations
   - Think about data organization
   - Evaluate time/space trade-offs

3. **Outline the algorithm**
   - High-level steps
   - Core operations and logic
   - Edge case handling

4. **Analyze complexity**
   - Time complexity analysis
   - Space complexity analysis
   - Bottleneck identification

5. **Optimize if needed**
   - Identify potential improvements
   - Consider alternative approaches
   - Address bottlenecks

6. **Present the solution**
   - Clear algorithmic steps
   - Implementation considerations
   - Complexity justification

## 8. Example Pattern Recognition

| Problem Description | Key Pattern | Appropriate Approach |
|--------------------|-------------|----------------------|
| "Find the maximum sum subarray of size k" | Fixed-size window | Sliding window |
| "Find all permutations of the string" | Generate all possibilities | Backtracking |
| "Minimize the maximum difference" | Min-max optimization | Binary search on answer |
| "Count ways to reach the target" | Counting problem | Dynamic programming |
| "Can the array be partitioned equally" | Subset sum | Dynamic programming |
| "Find the shortest path" | Path finding | BFS, Dijkstra's |
| "Design a data structure with O(1) operations" | Fast operations | Hash table based design |
| "Find all pairs that sum to k" | Pair finding | Two pointers, hash table |

Remember to always analyze the constraints and requirements carefully. The key to these algorithm design questions is recognizing the underlying patterns and matching them to the appropriate algorithmic approach and data structures.
