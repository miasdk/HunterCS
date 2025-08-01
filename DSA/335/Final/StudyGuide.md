# Comprehensive DSA Final Exam Study Guide

## Table of Contents
- [Prioritized Study Plan](#prioritized-study-plan)
- [Part 1: Critical Topics](#part-1-critical-topics)
  - [Algorithm Design and Analysis](#1-algorithm-design-and-analysis-225-points)
  - [AVL Trees](#2-avl-trees-06-points)
  - [Heap Operations](#3-heap-operations-08-points---buildheap-and-percdown)
  - [Hash Table Design and Operations](#4-hash-table-design-and-operations-255-points)
  - [Kruskal's Algorithm](#5-kruskals-algorithm-06-points)
  - [Nearest Neighbor Complexity Analysis](#6-nearest-neighbor-complexity-analysis-212-points)
  - [Quickselect Implementation](#7-quickselect-implementation-610-points)
- [Part 2: Important Topics](#part-2-important-topics-study-these-second)
  - [Dijkstra's Algorithm](#1-dijkstras-algorithm-7512-points)
  - [Prim's Algorithm Complexity](#2-prims-algorithm-complexity-4512-points)
  - [Unordered Map Usage](#3-unordered-map-usage-320-points)
- [Part 3: Review Topics](#part-3-review-topics-reinforce-your-knowledge)
  - [Quicksort Partitioning](#1-quicksort-partitioning-1010-points)
  - [DeleteMin from Heap](#2-deletemin-from-heap-810-points)
  - [Priority Queues](#3-priority-queues-66-points)
  - [Topological Ordering](#4-topological-ordering-33-points)
  - [Time Complexity Analysis](#5-time-complexity-analysis-78-points)
- [Part 4: Graph Algorithms](#part-4-graph-algorithms-chapter-9)
  - [Graph Representations](#1-graph-representations)
  - [Graph Traversals](#2-graph-traversals)
  - [Single-Source Shortest Path](#3-single-source-shortest-path)
  - [Minimum Spanning Trees](#4-minimum-spanning-trees)
  - [Vertex Cover Problem](#5-vertex-cover-problem)
- [Part 5: Greedy Algorithms and Dynamic Programming](#part-5-greedy-algorithms-and-dynamic-programming-chapter-10)
  - [Greedy Algorithms](#1-greedy-algorithms)
  - [Dynamic Programming](#2-dynamic-programming)
- [Time Complexity Cheat Sheet](#time-complexity-cheat-sheet)
- [Exam Preparation Strategy](#exam-preparation-strategy)
  - [Week 1: Critical Topics](#week-1-critical-topics)
  - [Week 2: Important Topics](#week-2-important-topics)
  - [Week 3: Review Topics and Integration](#week-3-review-topics-and-integration)
  - [Daily Practice Schedule](#daily-practice-schedule)
- [Implementation Guidelines for Coding Questions](#implementation-guidelines-for-coding-questions)
  - [General Coding Best Practices](#general-coding-best-practices)
  - [Common C++ STL Containers](#common-c-stl-containers)
  - [Iterating Through Containers](#iterating-through-containers)
  - [Working with Pairs and Maps](#working-with-pairs-and-maps)
- [Additional Insights from Course Homework](#additional-insights-from-course-homework)
  - [From Homework 1-2: Fundamentals](#from-homework-1-2-fundamentals)
  - [From Homework 3-4: Trees and Balanced Trees](#from-homework-3-4-trees-and-balanced-trees)
  - [From Homework 5: Hashing](#from-homework-5-hashing)
  - [From Homework 6: Heaps and Priority Queues](#from-homework-6-heaps-and-priority-queues)
  - [From Homework 7: Sorting and Graph Algorithms](#from-homework-7-sorting-and-graph-algorithms)
  - [From Homework 8: Dynamic Programming](#from-homework-8-dynamic-programming)
- [Algorithm Analysis Techniques](#algorithm-analysis-techniques)
  - [Asymptotic Analysis](#1-asymptotic-analysis)
  - [Recurrence Relations](#2-recurrence-relations)
  - [Amortized Analysis](#3-amortized-analysis)
- [Detailed Analysis of Key Algorithms](#detailed-analysis-of-key-algorithms)
  - [Sorting Algorithms](#1-sorting-algorithms)
  - [Advanced Tree Operations](#2-advanced-tree-operations)
  - [Graph Algorithm Analysis](#3-graph-algorithm-analysis)
- [Study Plan Implementation](#study-plan-implementation)
  - [Week 1: Focusing on Critical Topics](#week-1-focusing-on-critical-topics)
  - [Week 2: Strengthening Important Topics](#week-2-strengthening-important-topics)
  - [Week 3: Integration and Review](#week-3-integration-and-review)
- [Common Mistakes to Avoid](#common-mistakes-to-avoid)
  - [Conceptual Mistakes](#conceptual-mistakes)
  - [Implementation Mistakes](#implementation-mistakes)
  - [Exam-Specific Mistakes](#exam-specific-mistakes)
- [Practice Problems](#practice-problems)
  - [Problem 1: Hash Table Design](#problem-1-hash-table-design)
  - [Problem 2: Graph Algorithm Integration](#problem-2-graph-algorithm-integration)
  - [Problem 3: Dynamic Programming](#problem-3-dynamic-programming)
  - [Problem 4: Balanced Tree Implementation](#problem-4-balanced-tree-implementation)
  - [Problem 5: Multi-Algorithm Problem](#problem-5-multi-algorithm-problem)
- [Conclusion](#conclusion)

## PRIORITIZED STUDY PLAN

Based on your previous exam performance, I've organized this guide with priority levels:
- **CRITICAL** (Areas where you scored poorly, requiring immediate focus)
- **IMPORTANT** (Areas with partial understanding that need strengthening)
- **REVIEW** (Areas where you performed well, but should still review for mastery)

## PART 1: CRITICAL TOPICS (Focus here first)

### 1. Algorithm Design and Analysis (2/25 points)
#### Key Concepts:
- Problem decomposition strategies
- Design paradigms (divide-and-conquer, greedy, dynamic programming)
- Correctness proofs for algorithms
- Time and space complexity analysis
- Amortized analysis

#### Practice Problems:
1. **Club Membership System**: Revisit the "Big Brother" problem from your previous exam. The solution requires:
   - Hash maps for O(1) lookup of person data
   - Ordered maps (BSTs) for time-range queries
   - Iterative search through data structures for point-in-time attendance

2. **Implementation Pattern**:
```cpp
// For question type A (looking up a person's information)
std::unordered_map<std::string, std::pair<time_t, time_t>> personData;
// O(1) lookup to find if person attended and their entry/exit times

// For question type B (finding who entered in a time range)
std::map<time_t, std::string> entryTimes; // Ordered by time
// O(log n) insertion, O(k + log n) range query where k is matching elements

// For question type C (who was present at a specific time)
// Iterate through personData: O(n)
for (const auto& [name, times] : personData) {
    if (times.first <= queryTime && times.second >= queryTime) {
        // Person was present
    }
}
```

### 2. AVL Trees (0/6 points)
#### Key Concepts:
- Balance condition: height difference between children ≤ 1
- Single and double rotations
- Insertion and deletion operations
- Height calculation and balance factor
- Minimal AVL trees

#### Minimal AVL Trees:
- The recurrence relation: `f(h) = f(h-1) + f(h-2) + 1`
- `f(h)` represents the minimum number of nodes in an AVL tree of height h
- Base cases: f(0) = 1, f(1) = 2
- For height 8: f(8) = 88 nodes (work through the recurrence)

#### Rotations:
```
Single Right Rotation:        Single Left Rotation:
    A                              A
   / \                            / \
  B   C    ----->                B   C    ----->
 / \                                / \
D   E                              D   E

    C                              B
   / \                            / \
  B   A                          A   C
 / \                            / \
D   E                          D   E
```

### 3. Heap Operations (0/8 points) - buildHeap and percDown
#### Key Concepts:
- Binary heap properties (structural and heap)
- buildHeap algorithm (O(n) time complexity)
- percolate down operation
- Array representation of heaps

#### buildHeap Implementation:
```cpp
void buildHeap(std::vector<int>& heap) {
    // Start from the middle of the array (last non-leaf)
    for (auto it = heap.begin() + heap.size()/2; it != heap.begin(); --it) {
        // Save value to be percolated down
        *heap.begin() = *it;
        // Percolate it down
        percDown(heap, std::distance(heap.begin(), it));
    }
}
```

#### percDown Implementation:
```cpp
void percDown(std::vector<int>& heap, std::vector<int>::size_type hole) {
    std::vector<int>::size_type child;
    
    // Each iteration moves the hole down one if required
    // Exits loop when the hole is in place
    for (; hole * 2 <= heap.size() - 1; hole = child) {
        child = hole * 2;
        if (child != heap.size() - 1 && heap[child + 1] < heap[child])
            ++child;
        if (heap[child] < heap[0])
            heap[hole] = heap[child];
        else
            break;
    }
    
    // Moves value to be inserted into hole
    heap[hole] = heap[0];
}
```

**Important Note**: In percDown, you cannot use iterators for pointer arithmetic operations like doubling indices. This is why the hole is represented as an index.

### 4. Hash Table Design and Operations (2.5/5 points)
#### Key Concepts:
- Hash functions and their properties
- Collision resolution strategies
- Open addressing (linear probing, quadratic probing, double hashing)
- Separate chaining
- Load factor and rehashing

#### Double Hashing:
```
h(key, i) = (h1(key) + i * h2(key)) % tableSize
```
- h1 and h2 must be relatively prime to tableSize for full coverage
- Common implementations: h2(key) = R - (key % R) where R is prime < tableSize

#### Poor Hash Function Examples:
1. **Modding by non-prime numbers**: Creates patterns in distribution
   - Example: `h(x) = x % 20` will cause collisions for all multiples of 20
   
2. **Maximum load factor too high**: Causes excessive collisions
   - Keep load factor < 0.7 for open addressing, < 0.9 for separate chaining

#### Open Addressing:
- Collision resolution by finding alternative slots within the table
- Techniques: linear probing, quadratic probing, double hashing
- Example using it: linear probing for hash table implementation
- Example not using it: separate chaining with linked lists for collisions

### 5. Kruskal's Algorithm (0/6 points)
#### Key Concepts:
- Minimum Spanning Tree (MST) properties
- Union-Find data structure
- Sorting edges by weight
- Cycle detection

#### Algorithm:
1. Sort all edges in non-decreasing order of weight
2. Pick the smallest edge that doesn't form a cycle with the MST
3. Repeat step 2 until n-1 edges are added (n = number of vertices)

#### Implementation:
```cpp
struct Edge {
    int src, dest, weight;
    bool operator<(const Edge& other) const {
        return weight < other.weight;
    }
};

struct DisjointSet {
    std::vector<int> parent, rank;
    
    DisjointSet(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++)
            parent[i] = i;
    }
    
    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }
    
    void unite(int x, int y) {
        int xRoot = find(x);
        int yRoot = find(y);
        
        if (rank[xRoot] < rank[yRoot])
            parent[xRoot] = yRoot;
        else if (rank[xRoot] > rank[yRoot])
            parent[yRoot] = xRoot;
        else {
            parent[yRoot] = xRoot;
            rank[xRoot]++;
        }
    }
};

std::vector<Edge> kruskalMST(std::vector<Edge>& edges, int V) {
    std::vector<Edge> result;
    std::sort(edges.begin(), edges.end());
    
    DisjointSet ds(V);
    
    for (Edge& edge : edges) {
        int x = ds.find(edge.src);
        int y = ds.find(edge.dest);
        
        if (x != y) {
            result.push_back(edge);
            ds.unite(x, y);
            
            if (result.size() == V - 1) // MST is complete
                break;
        }
    }
    
    return result;
}
```

### 6. Nearest Neighbor Complexity Analysis (2/12 points)
#### Key Concepts:
- Time complexity of operations on different data structures
- Comparison of vectors vs. linked lists for algorithm implementation
- Search, insert, and delete operations in collections

#### Analysis:
- Vector implementation: O(|V|²)
  - Finding nearest unvisited vertex: O(|V|) to search through all vertices
  - For each vertex, we perform this search: O(|V|) * O(|V|) = O(|V|²)
  
- Linked list implementation: O(|V|²)
  - Same asymptotic complexity as vector
  - Slightly more efficient in practice since deletion is O(1) for linked lists vs potentially O(|V|) for vectors
  - The trade-off is that linked lists can be slower due to cache misses

### 7. Quickselect Implementation (6/10 points)
#### Key Concepts:
- Partitioning strategy (same as quicksort)
- Selection of kth smallest element
- Recursive approach with divide-and-conquer

#### Implementation:
```cpp
int quickSelect(std::vector<int>& nums, std::vector<int>::iterator low, 
                std::vector<int>::iterator high, std::vector<int>::iterator k) {
    if (std::distance(low, high) < 10) {
        std::sort(low, high + 1);
        return *k;
    }
    
    auto pivot = partition(nums, low, high);
    int distance = std::distance(low, pivot);
    
    if (distance == std::distance(low, k))
        return *pivot; // Found the kth element
    else if (distance > std::distance(low, k))
        return quickSelect(nums, low, pivot - 1, k); // Look in left half
    else
        return quickSelect(nums, pivot + 1, high, k); // Look in right half
}
```

## PART 2: IMPORTANT TOPICS (Study these second)

### 1. Dijkstra's Algorithm (7.5/12 points)
#### Key Concepts:
- Single-source shortest path algorithm
- Priority queue implementation
- Greedy approach
- Distance and predecessor tracking
- Algorithm trace

#### Implementation:
```cpp
void dijkstra(const Graph& g, int source, std::vector<int>& dist, std::vector<int>& prev) {
    int n = g.size();
    dist.assign(n, std::numeric_limits<int>::max());
    prev.assign(n, -1);
    dist[source] = 0;
    
    std::priority_queue<std::pair<int, int>, 
                         std::vector<std::pair<int, int>>, 
                         std::greater<std::pair<int, int>>> pq;
    pq.push({0, source});
    
    while (!pq.empty()) {
        int u = pq.top().second;
        int d = pq.top().first;
        pq.pop();
        
        if (d > dist[u]) continue; // Skip outdated entries
        
        for (auto& [v, weight] : g[u]) {
            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                prev[v] = u;
                pq.push({dist[v], v});
            }
        }
    }
}
```

### 2. Prim's Algorithm Complexity (4.5/12 points)
#### Key Concepts:
- Minimum Spanning Tree algorithm
- Comparison with Kruskal's algorithm
- Implementation with and without heaps
- Time complexity analysis

#### Complexity Analysis:
- With heaps: O(|E| log |V|)
  - For each vertex, find min edge: O(log |V|) using heap
  - Update heap for adjacent edges: O(|E| log |V|) total

- Without heaps: O(|V|²)
  - For each vertex, find min edge: O(|V|)
  - Repeated for all vertices: O(|V|²)

- When to use each:
  - Heaps better for sparse graphs: |E| ≈ |V|
  - Array-based better for dense graphs: |E| ≈ |V|²

### 3. Unordered Map Usage (3/20 points)
#### Key Concepts:
- Hash-based STL container
- Key-value storage and retrieval
- Performance characteristics
- Use cases

#### Implementation Example:
```cpp
void printBestScores(std::vector<std::pair<std::string, int>> scores) {
    std::unordered_map<std::string, int> best;
    
    for (const auto& [name, score] : scores) {
        // Check if name already exists in map
        if (best.find(name) == best.end()) {
            best[name] = score; // First occurrence
        } else if (score < best[name]) {
            best[name] = score; // Lower score is better
        }
    }
    
    // Print results
    for (const auto& [name, score] : best) {
        std::cout << name << " " << score << std::endl;
    }
}
```

## PART 3: REVIEW TOPICS (Reinforce your knowledge)

### 1. Quicksort Partitioning (10/10 points)
#### Key Concepts:
- Divide-and-conquer paradigm
- Partitioning strategy (Hoare's scheme)
- Pivot selection
- Worst-case and average-case performance

#### Implementation:
```cpp
int partition(std::vector<int>& arr, int low, int high) {
    int pivot = arr[high]; // Choose the last element as pivot
    int i = low - 1; // Index of smaller element
    
    for (int j = low; j < high; j++) {
        // If current element is smaller than the pivot
        if (arr[j] < pivot) {
            i++; // Increment index of smaller element
            std::swap(arr[i], arr[j]);
        }
    }
    
    std::swap(arr[i + 1], arr[high]);
    return i + 1;
}
```

### 2. DeleteMin from Heap (8/10 points)
#### Key Concepts:
- Priority queue fundamentals
- Heap property maintenance
- PercDown operation after removal

#### Implementation:
```cpp
int deleteMin(std::vector<int>& heap) {
    if (heap.size() <= 1)
        throw std::underflow_error("Heap is empty");
    
    int minItem = heap[1]; // Min element is at index 1
    
    // Move the last element to the root
    heap[1] = heap.back();
    heap.pop_back();
    
    if (!heap.empty()) {
        // Restore heap property
        percDown(heap, 1);
    }
    
    return minItem;
}
```

### 3. Priority Queues (6/6 points)
#### Key Concepts:
- ADT operations (insert, deleteMin, findMin)
- Implementation options (binary heap, Fibonacci heap)
- Applications (Dijkstra's algorithm, event simulation)

#### Specific Case of Use:
Priority queues are essential in scenarios where we need to efficiently track the "next best" element, such as:
- Process scheduling
- Dijkstra's algorithm for shortest paths
- Huffman coding
- Event-driven simulation

### 4. Topological Ordering (3/3 points)
#### Key Concepts:
- Definition: linear ordering of vertices such that for every edge (u, v), u comes before v
- Only defined for Directed Acyclic Graphs (DAGs)
- Applications: scheduling, dependency resolution

#### Implementation:
```cpp
void topologicalSortUtil(int v, std::vector<bool>& visited,
                         std::stack<int>& stack, const Graph& graph) {
    visited[v] = true;
    
    // Recur for all adjacent vertices
    for (int u : graph[v]) {
        if (!visited[u])
            topologicalSortUtil(u, visited, stack, graph);
    }
    
    // Push current vertex to stack after all its adjacent are processed
    stack.push(v);
}

std::vector<int> topologicalSort(const Graph& graph, int n) {
    std::stack<int> stack;
    std::vector<bool> visited(n, false);
    
    // Call recursive helper for all vertices
    for (int i = 0; i < n; i++) {
        if (!visited[i])
            topologicalSortUtil(i, visited, stack, graph);
    }
    
    // Stack contains topological sort
    std::vector<int> result;
    while (!stack.empty()) {
        result.push_back(stack.top());
        stack.pop();
    }
    
    return result;
}
```

### 5. Time Complexity Analysis (7/8 points)
#### Key Concepts:
- Big-O, Big-Omega, Big-Theta notations
- Amortized analysis
- Worst-case vs. average-case complexity
- Space complexity considerations

## PART 4: GRAPH ALGORITHMS (Chapter 9)

### 1. Graph Representations
#### Key Concepts:
- Adjacency Matrix: O(V²) space, O(1) edge lookup
- Adjacency List: O(V+E) space, O(degree(v)) edge lookup
- Edge List: O(E) space, O(E) edge lookup

### 2. Graph Traversals
#### Breadth-First Search (BFS):
```cpp
void BFS(const Graph& g, int start) {
    std::vector<bool> visited(g.size(), false);
    std::queue<int> q;
    
    visited[start] = true;
    q.push(start);
    
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        
        // Process vertex v
        
        for (int adj : g[v]) {
            if (!visited[adj]) {
                visited[adj] = true;
                q.push(adj);
            }
        }
    }
}
```

#### Depth-First Search (DFS):
```cpp
void DFS(const Graph& g, int v, std::vector<bool>& visited) {
    visited[v] = true;
    
    // Process vertex v
    
    for (int adj : g[v]) {
        if (!visited[adj]) {
            DFS(g, adj, visited);
        }
    }
}
```

### 3. Single-Source Shortest Path
#### Unweighted Graphs (BFS):
```cpp
void shortestPath(const Graph& g, int start, std::vector<int>& dist) {
    dist.assign(g.size(), -1); // -1 indicates unreachable
    dist[start] = 0;
    
    std::queue<int> q;
    q.push(start);
    
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        
        for (int adj : g[v]) {
            if (dist[adj] == -1) {
                dist[adj] = dist[v] + 1;
                q.push(adj);
            }
        }
    }
}
```

### 4. Minimum Spanning Trees
#### Prim's Algorithm (with priority queue):
```cpp
std::vector<Edge> primMST(const Graph& g) {
    int n = g.size();
    std::vector<Edge> result;
    std::vector<bool> inMST(n, false);
    std::vector<int> key(n, std::numeric_limits<int>::max());
    std::vector<int> parent(n, -1);
    
    std::priority_queue<std::pair<int, int>, 
                        std::vector<std::pair<int, int>>, 
                        std::greater<std::pair<int, int>>> pq;
    
    int start = 0; // Start from vertex 0
    key[start] = 0;
    pq.push({0, start});
    
    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();
        
        if (inMST[u]) continue;
        inMST[u] = true;
        
        if (parent[u] != -1) {
            result.push_back({parent[u], u, key[u]});
        }
        
        for (auto& [v, weight] : g[u]) {
            if (!inMST[v] && weight < key[v]) {
                parent[v] = u;
                key[v] = weight;
                pq.push({key[v], v});
            }
        }
    }
    
    return result;
}
```

### 5. Vertex Cover Problem
#### Key Concepts:
- NP-complete problem
- Finding the smallest set of vertices such that every edge has at least one endpoint in the set
- Approximation algorithms

#### 2-approximation algorithm:
```cpp
std::vector<int> vertexCover(const Graph& g) {
    int n = g.size();
    std::vector<bool> visited(n, false);
    std::vector<int> cover;
    
    // Iterate through all edges
    for (int u = 0; u < n; u++) {
        if (visited[u]) continue;
        
        for (int v : g[u]) {
            if (visited[v]) continue;
            
            // Add both endpoints to the cover
            visited[u] = visited[v] = true;
            cover.push_back(u);
            cover.push_back(v);
            break;
        }
    }
    
    return cover;
}
```

## PART 5: GREEDY ALGORITHMS AND DYNAMIC PROGRAMMING (Chapter 10)

### 1. Greedy Algorithms
#### Key Concepts:
- Making locally optimal choices at each step
- May not always lead to globally optimal solution
- Problems suitable for greedy approach:
  - Minimum spanning tree
  - Huffman coding
  - Activity selection

#### Activity Selection Problem:
```cpp
struct Activity {
    int start, finish;
    bool operator<(const Activity& other) const {
        return finish < other.finish;
    }
};

std::vector<Activity> activitySelection(std::vector<Activity>& activities) {
    std::sort(activities.begin(), activities.end());
    
    std::vector<Activity> result;
    if (activities.empty()) return result;
    
    result.push_back(activities[0]);
    int lastSelected = 0;
    
    for (int i = 1; i < activities.size(); i++) {
        if (activities[i].start >= activities[lastSelected].finish) {
            result.push_back(activities[i]);
            lastSelected = i;
        }
    }
    
    return result;
}
```

### 2. Dynamic Programming
#### Key Concepts:
- Breaking down a problem into simpler subproblems
- Storing solutions to avoid recomputation (memoization)
- Bottom-up vs. top-down approaches
- Suitable problems:
  - Optimal substructure
  - Overlapping subproblems

#### When to use Dynamic Programming:
- When a problem can be broken down into subproblems
- When these subproblems overlap (solved multiple times)
- When the optimal solution can be constructed from optimal solutions to subproblems

#### 0-1 Knapsack Problem:
```cpp
int knapsack(const std::vector<int>& values, const std::vector<int>& weights, 
             int capacity, int n) {
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(capacity + 1, 0));
    
    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= capacity; w++) {
            if (weights[i-1] <= w) {
                dp[i][w] = std::max(values[i-1] + dp[i-1][w-weights[i-1]], 
                                   dp[i-1][w]);
            } else {
                dp[i][w] = dp[i-1][w];
            }
        }
    }
    
    return dp[n][capacity];
}
```

## TIME COMPLEXITY CHEAT SHEET

| Data Structure / Algorithm | Operation | Time Complexity |
|---------------------------|-----------|----------------|
| **Array** | Access | O(1) |
| **Array** | Search | O(n) |
| **Array** | Insertion/Deletion (end) | O(1) |
| **Array** | Insertion/Deletion (arbitrary) | O(n) |
| **Linked List** | Access | O(n) |
| **Linked List** | Search | O(n) |
| **Linked List** | Insertion/Deletion (after finding position) | O(1) |
| **Binary Search Tree (balanced)** | Search/Insert/Delete | O(log n) |
| **Binary Search Tree (unbalanced)** | Search/Insert/Delete | O(n) |
| **AVL Tree** | Search/Insert/Delete | O(log n) |
| **Splay Tree** | Search/Insert/Delete | O(log n) amortized |
| **Hash Table** | Search/Insert/Delete | O(1) average, O(n) worst |
| **Binary Heap** | FindMin/FindMax | O(1) |
| **Binary Heap** | Insert | O(log n) |
| **Binary Heap** | DeleteMin/DeleteMax | O(log n) |
| **Binary Heap** | BuildHeap | O(n) |
| **Sorting Algorithms** | | |
| Quicksort | Average | O(n log n) |
| Quicksort | Worst | O(n²) |
| Mergesort | Average/Worst | O(n log n) |
| Heapsort | Average/Worst | O(n log n) |
| Insertion Sort | Average/Worst | O(n²) |
| Bubble Sort | Average/Worst | O(n²) |
| **Selection Algorithms** | | |
| Quickselect | Average | O(n) |
| Quickselect | Worst | O(n²) |
| **Graph Algorithms** | | |
| DFS/BFS | | O(\|V\| + \|E\|) |
| Dijkstra | With priority queue | O(\|E\| log \|V\|) |
| Dijkstra | Without priority queue | O(\|V\|²) |
| Bellman-Ford | | O(\|V\| \* \|E\|) |
| Floyd-Warshall | | O(\|V\|³) |
| Prim's | With priority queue | O(\|E\| log \|V\|) |
| Prim's | Without priority queue | O(\|V\|²) |
| Kruskal's | | O(\|E\| log \|E\|) or O(\|E\| log \|V\|) |
| Topological Sort | | O(\|V\| + \|E\|) |
| **Other Operations** | | |
| Rehashing | Average | O(n) |
| Find value in unordered_map | Average | O(1) |
| Find key in unordered_map | Average | O(1) |
| Find key in ordered_map | Average | O(log n) |
| Find value in ordered_map | Average | O(n) |
| Partition around pivot | Average | O(n) |
| Insert in splay tree | Worst | O(n) |
| Heapsort on sorted array | | O(n log n) |
| Insertion sort on sorted array | | O(n) |

## EXAM PREPARATION STRATEGY

### Week 1: Critical Topics
- Focus on algorithm design and analysis
- Master heap operations and implementations
- Study hash table design principles
- Practice Kruskal's algorithm and MST construction
- Implement AVL tree operations and minimal AVL tree calculations

### Week 2: Important Topics
- Review Dijkstra's algorithm with detailed tracing
- Compare Prim's and Kruskal's algorithms
- Master unordered map usage in C++
- Practice quickselect implementation
- Review nearest neighbor complexity analysis

### Week 3: Review Topics and Integration
- Connect graph algorithms with data structures
- Practice implementing all key algorithms
- Work through time complexity analysis for all algorithms
- Trace through algorithm execution by hand
- Integrate greedy and dynamic programming concepts

### Daily Practice Schedule:
1. Study theoretical concepts (1 hour)
2. Implement 1-2 algorithms (1-2 hours)
3. Practice trace-through of algorithms (1 hour)
4. Review time complexities (15 minutes)
5. Solve 1-2 practice problems (1 hour)

## IMPLEMENTATION GUIDELINES FOR CODING QUESTIONS

### General Coding Best Practices:
1. Use clear variable names
2. Add comments for complex logic
3. Break down complex functions into smaller ones
4. Check edge cases (empty containers, single elements, etc.)
5. Use appropriate data structures for the problem

### Common C++ STL Containers:
1. `std::vector<T>`: Dynamic array, use for most sequential storage
2. `std::list<T>`: Doubly linked list, use when frequent insertion/deletion is needed
3. `std::unordered_map<K, V>`: Hash table, use for O(1) key-value lookup
4. `std::map<K, V>`: BST-based ordered map, use when ordering is needed
5. `std::priority_queue<T>`: Heap implementation, use for priority queues

### Iterating Through Containers:
```cpp
// Modern C++ range-based for loop (preferred)
for (const auto& item : container) {
    // Use item
}

// Using iterators
for (auto it = container.begin(); it != container.end(); ++it) {
    // Use *it
}
```

### Working with Pairs and Maps:
```cpp
// Accessing pair elements
std::pair<int, std::string> p = {1, "one"};
int first = p.first;
std::string second = p.second;

// Structured bindings (C++17)
auto [key, value] = *map_iterator;

// Inserting into maps
map.insert({key, value});  // or
map[key] = value;
```

## ADDITIONAL INSIGHTS FROM COURSE HOMEWORK

### From Homework 1-2: Fundamentals
- **Move Semantics**: Understanding the purpose and implementation in C++
- **Computational Complexity**: Analysis of algorithms using Big-O notation
- **Algorithm Analysis**: Evaluating efficiency when working with multiple data structures
- **STL Container Operations**: Understanding vector vs. list implementations and their iterator capabilities
- **Vector vs. List Trade-offs**: Performance differences when using operations like removal

### From Homework 3-4: Trees and Balanced Trees
- **AVL Tree Operations**: Insertion, deletion, and rebalancing
- **Tree Rotations**: Single and double rotations for maintaining balance
- **Sliding Window Technique**: Using ordered sets (balanced BSTs) for ranged searches
- **Time Complexity Analysis**: Understanding operations on balanced trees

### From Homework 5: Hashing
- **Hash Functions**: Understanding pros and cons of different implementations
- **Collision Resolution**: Linear probing, quadratic probing, double hashing
- **STL Hash Containers**: unordered_map and unordered_set usage
- **Complexity Analysis**: Hash-based vs. tree-based containers

### From Homework 6: Heaps and Priority Queues
- **Heap Operations**: deleteMin, insert, buildHeap, heapify
- **Priority Queue Implementation**: Using the STL priority_queue container
- **Heap Manipulation**: Direct manipulation vs. using container methods

### From Homework 7: Sorting and Graph Algorithms
- **Sorting Algorithms**: quicksort, mergesort, insertion sort, heapsort
- **Partitioning Strategies**: Hoare partitioning, median-of-3 pivot selection
- **Graph Representations**: Adjacency matrix, adjacency list
- **Shortest Path Algorithms**: Dijkstra's, Floyd-Warshall, Johnson's
- **Minimum Spanning Trees**: Prim's and Kruskal's algorithms

### From Homework 8: Dynamic Programming
- **1D and 2D Dynamic Programming**: Building optimal solutions from subproblems
- **Problem Identification**: Recognizing when DP is applicable
- **Bottom-up vs. Top-down Approaches**: Implementation strategies
- **Overlapping Subproblems and Optimal Substructure**: Key DP characteristics

## ALGORITHM ANALYSIS TECHNIQUES

### 1. Asymptotic Analysis
- **Big-O Notation (O)**: Upper bound on growth rate
- **Big-Omega (Ω)**: Lower bound on growth rate
- **Big-Theta (Θ)**: Tight bound (both upper and lower)
- **Little-o notation (o)**: Upper bound that is not tight

### 2. Recurrence Relations
- Used to analyze recursive algorithms
- Common methods for solving:
  - Substitution method
  - Recursion tree method
  - Master theorem

#### Master Theorem:
For recurrences of the form T(n) = aT(n/b) + f(n), where a ≥ 1 and b > 1:
- If f(n) = O(n^(log_b(a)-ε)) for some ε > 0, then T(n) = Θ(n^(log_b a))
- If f(n) = Θ(n^(log_b a)), then T(n) = Θ(n^(log_b a) * log n)
- If f(n) = Ω(n^(log_b(a)+ε)) for some ε > 0, and if af(n/b) ≤ cf(n) for some c < 1, then T(n) = Θ(f(n))

### 3. Amortized Analysis
- Techniques for analyzing algorithms with operations that occasionally cost more
- Methods:
  - Aggregate analysis
  - Accounting method
  - Potential method

## DETAILED ANALYSIS OF KEY ALGORITHMS

### 1. Sorting Algorithms

#### Quicksort
- **Average Time**: O(n log n)
- **Worst-case Time**: O(n²) when poorly pivoted
- **Space**: O(log n) for recursion stack
- **Key Insights**:
  - Partition-based, divide-and-conquer approach
  - Performance heavily depends on pivot selection
  - Randomized pivot selection helps avoid worst cases
  - In-place sorting algorithm

#### Heapsort
- **Time**: O(n log n) in all cases
- **Space**: O(1) auxiliary space
- **Key Insights**:
  - Uses binary heap data structure
  - First creates a max-heap with buildHeap in O(n) time
  - Then repeatedly extracts max element and restores heap property
  - Guaranteed O(n log n) performance regardless of input

#### Mergesort
- **Time**: O(n log n) in all cases
- **Space**: O(n) auxiliary space
- **Key Insights**:
  - Divide-and-conquer approach
  - Stable sort (maintains relative order of equal elements)
  - Excellent for external sorting where data doesn't fit in memory
  - Not in-place but consistent performance

### 2. Advanced Tree Operations

#### Splay Tree Operations
- **Time**: O(log n) amortized for all operations
- **Insight**: Brings accessed elements to root via rotations
- **Advantages**:
  - Simple implementation
  - Self-adjusting (frequently accessed elements near root)
  - Works well with locality of reference
- **Balancing Strategy**:
  - Zig step (one rotation) for root's child
  - Zig-zig steps (two same-direction rotations)
  - Zig-zag steps (two opposite-direction rotations)

### 3. Graph Algorithm Analysis

#### Bellman-Ford Algorithm
- **Time**: O(|V|·|E|)
- **Purpose**: Single-source shortest paths with negative edge weights
- **Key Insights**:
  - Can detect negative cycles
  - Relaxes all edges |V|-1 times
  - Dynamic programming approach

#### Floyd-Warshall Algorithm
- **Time**: O(|V|³)
- **Purpose**: All-pairs shortest paths
- **Key Insights**:
  - Simple dynamic programming implementation
  - Handles negative edge weights (but not negative cycles)
  - Computes shortest paths between all vertex pairs

#### Network Flow Algorithms
- **Ford-Fulkerson Algorithm**:
  - Time: O(|E|·max_flow) - can be slow for large weights
  - Uses augmenting paths to maximize flow
- **Edmonds-Karp Algorithm**:
  - Time: O(|V|·|E|²)
  - Ford-Fulkerson with BFS for finding augmenting paths
- **Applications**:
  - Maximum bipartite matching
  - Minimum cut problems
  - Assignment problems

## STUDY PLAN IMPLEMENTATION

### Week 1: Focusing on Critical Topics

#### Day 1-2: Heaps and Heap Operations
- Review heap properties and structure
- Implement buildHeap and percDown from scratch
- Practice tracing heap operations by hand
- Implement heapsort algorithm
- Solve problems involving priority queues

#### Day 3-4: AVL Trees
- Review balance conditions and rotations
- Implement AVL insertion with rotations
- Practice minimal AVL tree calculations
- Trace through AVL operations on sample trees
- Compare with other balanced tree structures

#### Day 5-7: Hash Tables and Kruskal's Algorithm
- Implement double hashing collision resolution
- Analyze different hash functions and their properties
- Implement Kruskal's algorithm with Union-Find
- Practice MST construction on sample graphs
- Solve problems combining hash tables and graphs

### Week 2: Strengthening Important Topics

#### Day 8-9: Dijkstra's and Prim's Algorithms
- Implement both algorithms from scratch
- Compare and contrast their approaches
- Analyze time complexity with different data structures
- Solve problems requiring shortest paths or MSTs
- Practice algorithm tracing by hand

#### Day 10-11: Quickselect and STL Maps
- Implement quickselect with correct pivot handling
- Use STL unordered_map and map in various scenarios
- Practice designing solutions with appropriate data structures
- Analyze nearest neighbor and similar algorithms
- Solve coding problems requiring selection algorithms

### Week 3: Integration and Review

#### Day 12-13: Graph Algorithms
- Review all graph representations and traversals
- Practice implementing topological sort
- Solve problems combining multiple graph algorithms
- Review shortest path algorithms (Dijkstra's, Bellman-Ford)
- Connect graph concepts with other data structures

#### Day 14-15: Greedy Algorithms and Dynamic Programming
- Review when each approach is appropriate
- Implement solutions to classic problems
- Practice recognizing problem types
- Connect with previously learned algorithms
- Analyze time and space complexity tradeoffs

#### Day 16-17: Final Review and Integration
- Take practice exams under timed conditions
- Review all time complexities
- Practice implementing any algorithms you're unsure about
- Trace through sample executions of all major algorithms
- Connect concepts across different chapters

## COMMON MISTAKES TO AVOID

### Conceptual Mistakes:
1. **Confusing time complexities**: Especially for similar algorithms (e.g., Dijkstra's vs. Prim's)
2. **Misunderstanding algorithm requirements**: For example, when Dijkstra's algorithm works (no negative weights)
3. **Applying incorrect design paradigms**: Using greedy approach when dynamic programming is needed
4. **Misinterpreting balance conditions**: Especially for AVL trees

### Implementation Mistakes:
1. **Off-by-one errors**: Especially in array indexing and loop conditions
2. **Improper handling of edge cases**: Empty structures, single-element structures, etc.
3. **Incorrect recursive base cases**: Leading to infinite recursion or incorrect results
4. **Pointer errors in tree/graph operations**: Forgetting to update parent pointers or link nodes correctly
5. **Incorrect heap indexing**: Mixing 0-indexed and 1-indexed heap implementations

### Exam-Specific Mistakes:
1. **Not structuring algorithm descriptions clearly**: Making grading difficult
2. **Overcomplicating solutions**: Using complex data structures when simpler ones suffice
3. **Insufficient analysis**: Not fully explaining time/space complexity calculations
4. **Poor time management**: Spending too much time on difficult problems
5. **Incomplete algorithm traces**: Missing steps or making arithmetic errors

## PRACTICE PROBLEMS

### Problem 1: Hash Table Design
Design a custom hash table with the following specifications:
- Handles string keys and integer values
- Uses double hashing for collision resolution
- Automatically resizes when load factor exceeds 0.7
- Provides O(1) average case for lookup, insert, and delete

### Problem 2: Graph Algorithm Integration
Given a weighted, directed graph representing a road network:
- Find the shortest path that visits a subset of specified locations
- Each location has a "value" associated with it
- Determine the path that maximizes the value-to-distance ratio

### Problem 3: Dynamic Programming
A thief is planning to rob houses along a street. Each house has a certain amount of money. The thief cannot rob adjacent houses due to security systems. Design an algorithm to determine the maximum amount the thief can steal.

### Problem 4: Balanced Tree Implementation
Implement an AVL tree with the following operations:
- insert(key, value)
- delete(key)
- findMin() and findMax()
- predecessor(key) and successor(key)
- countNodesInRange(low, high)

### Problem 5: Multi-Algorithm Problem
Implement a data structure that efficiently supports:
- Adding elements
- Removing the smallest element
- Finding the kth smallest element
- Searching for a specific element

## CONCLUSION

Success in your DSA final exam requires:

1. **Comprehensive understanding** of all data structures and algorithms covered
2. **Implementation proficiency** for coding questions
3. **Analytical ability** for complexity analysis and algorithm design
4. **Practice with algorithm tracing** for visualization questions
5. **Integration of concepts** across different chapters

By following this study guide and consistently practicing, you should be well-prepared for all types of questions on your exam. Focus on mastering the critical topics first, then strengthen your understanding of important topics, and finally integrate all concepts through comprehensive review.

Good luck on your exam!