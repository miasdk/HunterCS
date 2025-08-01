# Comprehensive Guide to Graph Algorithms and Data Structures in C++

## Table of Contents

1. [Graph Fundamentals](#graph-fundamentals)
   - [Types of Graphs](#types-of-graphs)
   - [Graph Representation](#graph-representation)

2. [Graph Traversal](#graph-traversal)
   - [Breadth-First Search (BFS)](#breadth-first-search-bfs)
   - [Depth-First Search (DFS)](#depth-first-search-dfs)

3. [Greedy Algorithms](#greedy-algorithms)
   - [Characteristics of Greedy Algorithms](#characteristics-of-greedy-algorithms)
   - [Common Greedy Algorithms](#common-greedy-algorithms)

4. [Dijkstra's Algorithm](#dijkstras-algorithm)
   - [Algorithm Steps](#dijkstras-algorithm-steps)
   - [Pseudocode](#dijkstras-pseudocode)
   - [C++ Implementation](#dijkstras-cpp-implementation)
   - [Time Complexity Analysis](#dijkstras-time-complexity)

5. [Prim's Algorithm](#prims-algorithm)
   - [Algorithm Steps](#prims-algorithm-steps)
   - [Pseudocode](#prims-pseudocode)
   - [C++ Implementation](#prims-cpp-implementation)
   - [Time Complexity Analysis](#prims-time-complexity)
   - [Prim's Algorithm Trace Tables](#prims-algorithm-trace-tables)

6. [Adjacency List Implementation](#adjacency-list-implementation)
   - [Definition and Structure](#adjacency-list-definition)
   - [Implementation in C++](#adjacency-list-cpp)
   - [Space Complexity](#adjacency-list-space-complexity)

7. [Heaps](#heaps)
   - [Binary Heaps](#binary-heaps)
   - [Heap Operations](#heap-operations)
   - [Heap Implementation in C++](#heap-implementation-cpp)
   - [Priority Queues in STL](#priority-queues-stl)

8. [STL Containers for Graph Algorithms](#stl-containers-for-graph-algorithms)
   - [Vector](#vector)
   - [List](#list)
   - [Map](#map)
   - [Set](#set)
   - [Priority Queue](#priority-queue)

9. [Differences Between Key Algorithms](#differences-between-key-algorithms)
   - [Dijkstra's vs. Prim's](#dijkstras-vs-prims)
   - [Prim's vs. Kruskal's](#prims-vs-kruskals)

10. [Advanced Topics](#advanced-topics)
    - [Fibonacci Heaps](#fibonacci-heaps)
    - [A* Algorithm](#a-star-algorithm)
    - [Bellman-Ford Algorithm](#bellman-ford-algorithm)
    - [Floyd-Warshall Algorithm](#floyd-warshall-algorithm)

---

## Graph Fundamentals <a name="graph-fundamentals"></a>

### Types of Graphs <a name="types-of-graphs"></a>

- **Undirected Graph**: Edges have no direction, the relationship between vertices is symmetrical.
  - If vertex A connects to vertex B, then B also connects to A.
  - Represented by unordered pairs (A, B).
  - Examples: Friendship networks, road networks with two-way streets.

- **Directed Graph (Digraph)**: Edges have direction, the relationship is asymmetrical.
  - If vertex A has an edge to B, it doesn't mean B has an edge to A.
  - Represented by ordered pairs (A, B), meaning "from A to B".
  - Examples: Web pages with hyperlinks, social media follows, one-way streets.

- **Weighted Graph**: Edges have weights/costs associated with them.
  - Used for representing distances, costs, or capacities.
  - Common in applications like GPS navigation and network flow problems.

- **Unweighted Graph**: Edges have no weights.
  - Used when only the connection matters, not its strength or cost.

### Graph Representation <a name="graph-representation"></a>

Two common methods:

1. **Adjacency Matrix**:
   - A 2D array where cell [i][j] represents an edge from vertex i to vertex j.
   - Uses O(V²) space regardless of the number of edges.
   - Efficient for dense graphs and for checking if an edge exists between two vertices.

   ```cpp
   vector<vector<int>> graph(V, vector<int>(V, 0));  // For V vertices
   ```

2. **Adjacency List**:
   - An array of lists, where each list contains the neighbors of a vertex.
   - Uses O(V+E) space, efficient for sparse graphs.
   - Better for most real-world applications.

   ```cpp
   vector<vector<int>> graph(V);  // For V vertices
   ```

For weighted graphs:

```cpp
vector<vector<pair<int, int>>> graph(V);  // For V vertices, pair(neighbor, weight)
```

---

## Graph Traversal <a name="graph-traversal"></a>

### Breadth-First Search (BFS) <a name="breadth-first-search-bfs"></a>

- Explores all neighbors at the current depth before moving to nodes at the next depth level.
- Uses a queue data structure.
- Time complexity: O(V + E)
- Applications: Shortest path in unweighted graphs, connected components, network broadcasting.

### Depth-First Search (DFS) <a name="depth-first-search-dfs"></a>

- Explores as far as possible along a branch before backtracking.
- Uses a stack data structure (or recursion).
- Time complexity: O(V + E)
- Applications: Topological sorting, cycle detection, path finding, connected components.

---

## Greedy Algorithms <a name="greedy-algorithms"></a>

### Characteristics of Greedy Algorithms <a name="characteristics-of-greedy-algorithms"></a>

1. Make the best choice at each step.
2. Never reconsider previous choices.
3. Simple and efficient.
4. May not guarantee optimal solution for all problems.

### Common Greedy Algorithms <a name="common-greedy-algorithms"></a>

- **Dijkstra's Algorithm**: Finds the shortest paths from a source vertex.
- **Prim's Algorithm**: Finds a minimum spanning tree.
- **Kruskal's Algorithm**: Another approach for finding MST.
- **Huffman Coding**: Optimal prefix coding for data compression.
- **Activity Selection**: Maximum number of non-overlapping activities.

---

## Dijkstra's Algorithm <a name="dijkstras-algorithm"></a>

Dijkstra's algorithm finds the shortest path from a source vertex to all other vertices in a weighted graph with non-negative edge weights.

### Algorithm Steps <a name="dijkstras-algorithm-steps"></a>

1. Initialize distances from source to all vertices as infinity.
2. Set distance to source as 0.
3. Create a priority queue (or min-heap) and add source vertex.
4. While the priority queue is not empty:
   - Extract the vertex with minimum distance.
   - For each adjacent vertex, if the distance through the current vertex is less than its current distance, update its distance.

### Pseudocode <a name="dijkstras-pseudocode"></a>

```
function Dijkstra(Graph, source):
    create vertex set Q
    
    for each vertex v in Graph:
        dist[v] ← INFINITY
        prev[v] ← UNDEFINED
        add v to Q
    
    dist[source] ← 0
    
    while Q is not empty:
        u ← vertex in Q with min dist[u]
        remove u from Q
        
        for each neighbor v of u:
            alt ← dist[u] + length(u, v)
            if alt < dist[v]:
                dist[v] ← alt
                prev[v] ← u
    
    return dist[], prev[]
```

, source});
    
    while (!pq.empty()) {
        // Extract vertex with minimum distance
        int u = pq.top().second;
        int distance = pq.top().first;
        pq.pop();
        
        // If extracted distance is greater than the stored distance, skip
        if (distance > dist[u]) continue;
        
        // Process all adjacent vertices
        for (auto& neighbor : graph[u]) {
            int v = neighbor.first;
            int weight = neighbor.second;
            
            // If there's a shorter path to v through u
            if (dist[u] + weight < dist[v]) {
                // Update distance
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }
    
    // Print distances
    cout << "Vertex\tDistance from Source\n";
    for (int i = 0; i < V; i++) {
        cout << i << "\t" << dist[i] << "\n";
    }
}
```

### Time Complexity Analysis <a name="dijkstra-time-complexity"></a>

- Using an adjacency matrix: O(V²)
- Using an adjacency list with a binary heap: O((V+E) log V)
- Using a Fibonacci heap: O(E + V log V)

---

## Prim's Algorithm <a name="prims-algorithm"></a>

Prim's algorithm finds a minimum spanning tree (MST) for a weighted undirected graph.

### Algorithm Steps <a name="prim-algorithm-steps"></a>

1. Start with any vertex.
2. Repeatedly add the minimum weight edge that connects a vertex in the MST to a vertex not yet in the MST.
3. Repeat until all vertices are included in the MST.

### Pseudocode <a name="prim-pseudocode"></a>

```
function Prim(Graph):
    create empty set MST
    create set Q containing all vertices
    
    for each vertex v in Graph:
        key[v] ← INFINITY
        parent[v] ← UNDEFINED
    
    Select an arbitrary starting vertex root
    key[root] ← 0
    
    while Q is not empty:
        u ← Extract-Min(Q) (vertex with min key)
        add u to MST
        
        for each adjacent vertex v to u:
            if v is in Q and weight(u,v) < key[v]:
                parent[v] ← u
                key[v] ← weight(u,v)
    
    return MST
```

### C++ Implementation <a name="prim-cpp-implementation"></a>

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <limits>
using namespace std;

typedef pair<int, int> pii;  // (weight, vertex)

void primMST(vector<vector<pii>>& graph, int V) {
    // Priority queue to store vertices being processed
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    
    // Start with vertex 0
    int src = 0;
    
    // Array to store constructed MST
    vector<int> parent(V, -1);
    
    // Key values used to pick minimum weight edge
    vector<int> key(V, numeric_limits<int>::max());
    
    // To keep track of vertices included in MST
    vector<bool> inMST(V, false);
    
    // Include first vertex in MST
    pq.push({0, src});
    key[src] = 0;
    
    // Loop until all vertices are included in MST
    while (!pq.empty()) {
        // Extract minimum key vertex
        int u = pq.top().second;
        pq.pop();
        
        // If already included in MST, skip
        if (inMST[u]) continue;
        
        // Include vertex in MST
        inMST[u] = true;
        
        // Process all adjacent vertices
        for (auto& neighbor : graph[u]) {
            int v = neighbor.first;
            int weight = neighbor.second;
            
            // If v is not yet included in MST and weight of (u,v) is less than key of v
            if (!inMST[v] && weight < key[v]) {
                // Update key
                key[v] = weight;
                pq.push({key[v], v});
                parent[v] = u;
            }
        }
    }
    
    // Print MST
    cout << "Edge \tWeight\n";
    for (int i = 1; i < V; i++) {
        cout << parent[i] << " - " << i << " \t" << key[i] << "\n";
    }
}
```

### Time Complexity Analysis <a name="prim-time-complexity"></a>

- Using an adjacency matrix: O(V²)
- Using an adjacency list with a binary heap: O((V+E) log V)
- Using a Fibonacci heap: O(E + V log V)

### Prim's Algorithm Trace Tables <a name="prims-algorithm-trace-tables"></a>

For a sample graph with 5 vertices:

```
    2       3
(0)----(1)----(2)
 |      /\     |
 |     /  \    |
 6    8    7   4
 |   /      \  |
 |  /        \ |
 (3)----------(4)
        5
```

#### Initial State

| Vertex | In MST | Key (Weight) | Parent |
|--------|--------|-------------|--------|
| 0      | No     | 0           | -1     |
| 1      | No     | ∞           | -1     |
| 2      | No     | ∞           | -1     |
| 3      | No     | ∞           | -1     |
| 4      | No     | ∞           | -1     |

#### After Including Vertex 0

| Vertex | In MST | Key (Weight) | Parent |
|--------|--------|-------------|--------|
| 0      | Yes    | 0           | -1     |
| 1      | No     | 2           | 0      |
| 2      | No     | ∞           | -1     |
| 3      | No     | 6           | 0      |
| 4      | No     | ∞           | -1     |

#### After Including Vertex 1

| Vertex | In MST | Key (Weight) | Parent |
|--------|--------|-------------|--------|
| 0      | Yes    | 0           | -1     |
| 1      | Yes    | 2           | 0      |
| 2      | No     | 3           | 1      |
| 3      | No     | 6           | 0      |
| 4      | No     | 7           | 1      |

#### After Including Vertex 2

| Vertex | In MST | Key (Weight) | Parent |
|--------|--------|-------------|--------|
| 0      | Yes    | 0           | -1     |
| 1      | Yes    | 2           | 0      |
| 2      | Yes    | 3           | 1      |
| 3      | No     | 6           | 0      |
| 4      | No     | 4           | 2      |

#### After Including Vertex 4

| Vertex | In MST | Key (Weight) | Parent |
|--------|--------|-------------|--------|
| 0      | Yes    | 0           | -1     |
| 1      | Yes    | 2           | 0      |
| 2      | Yes    | 3           | 1      |
| 3      | No     | 5           | 4      |
| 4      | Yes    | 4           | 2      |

#### Final MST (After Including Vertex 3)

| Vertex | In MST | Key (Weight) | Parent |
|--------|--------|-------------|--------|
| 0      | Yes    | 0           | -1     |
| 1      | Yes    | 2           | 0      |
| 2      | Yes    | 3           | 1      |
| 3      | Yes    | 5           | 4      |
| 4      | Yes    | 4           | 2      |

Resulting MST Edges:
- 0 → 1 (weight: 2)
- 1 → 2 (weight: 3)
- 2 → 4 (weight: 4)
- 4 → 3 (weight: 5)

Total MST weight: 2 + 3 + 4 + 5 = 14

---

## Adjacency List Implementation <a name="adjacency-list-implementation"></a>

### Definition and Structure <a name="adjacency-list-definition"></a>

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list in the collection describes the set of neighbors of a vertex in the graph.

For an undirected graph with vertices 0, 1, 2, 3:
```
0: [1, 2]
1: [0, 3]
2: [0, 3]
3: [1, 2]
```

For a directed graph:
```
0: [1]
1: [3]
2: [0]
3: [2]
```

### Implementation in C++ <a name="adjacency-list-cpp"></a>

**Using STL Vector:**

```cpp
// Unweighted graph
vector<vector<int>> adjacencyList(V);

// Add edge from u to v
adjacencyList[u].push_back(v);

// For undirected graph
adjacencyList[v].push_back(u);
```

**For weighted graphs:**

```cpp
// Weighted graph
vector<vector<pair<int, int>>> adjacencyList(V);  // (vertex, weight)

// Add edge from u to v with weight w
adjacencyList[u].push_back({v, w});

// For undirected graph
adjacencyList[v].push_back({u, w});
```

**Complete Class Implementation:**

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Graph {
private:
    int V;  // Number of vertices
    bool isDirected;  // Whether the graph is directed
    bool isWeighted;  // Whether the graph is weighted
    
    // For unweighted graphs
    vector<vector<int>> adjList;
    
    // For weighted graphs
    vector<vector<pair<int, int>>> weightedAdjList;

public:
    // Constructor for unweighted graph
    Graph(int vertices, bool directed = false) {
        V = vertices;
        isDirected = directed;
        isWeighted = false;
        adjList.resize(V);
    }
    
    // Constructor for weighted graph
    Graph(int vertices, bool directed, bool weighted) {
        V = vertices;
        isDirected = directed;
        isWeighted = weighted;
        
        if (isWeighted) {
            weightedAdjList.resize(V);
        } else {
            adjList.resize(V);
        }
    }
    
    // Add edge to unweighted graph
    void addEdge(int u, int v) {
        if (isWeighted) {
            cout << "This is a weighted graph. Use addWeightedEdge." << endl;
            return;
        }
        
        adjList[u].push_back(v);
        
        if (!isDirected) {
            adjList[v].push_back(u);
        }
    }
    
    // Add edge to weighted graph
    void addWeightedEdge(int u, int v, int weight) {
        if (!isWeighted) {
            cout << "This is an unweighted graph. Use addEdge." << endl;
            return;
        }
        
        weightedAdjList[u].push_back({v, weight});
        
        if (!isDirected) {
            weightedAdjList[v].push_back({u, weight});
        }
    }
    
    // Print the graph
    void printGraph() {
        if (isWeighted) {
            for (int i = 0; i < V; i++) {
                cout << "Vertex " << i << " -> ";
                for (auto edge : weightedAdjList[i]) {
                    cout << "(" << edge.first << ", weight: " << edge.second << ") ";
                }
                cout << endl;
            }
        } else {
            for (int i = 0; i < V; i++) {
                cout << "Vertex " << i << " -> ";
                for (auto neighbor : adjList[i]) {
                    cout << neighbor << " ";
                }
                cout << endl;
            }
        }
    }
};
```

### Space Complexity <a name="adjacency-list-space-complexity"></a>

- Unweighted undirected graph: O(V + 2E)
- Unweighted directed graph: O(V + E)
- Weighted undirected graph: O(V + 2E)
- Weighted directed graph: O(V + E)

---

## Heaps <a name="heaps"></a>

### Binary Heaps <a name="binary-heaps"></a>

A binary heap is a complete binary tree where each node satisfies a specific ordering property:

- **Max Heap**: For every node, the value of the node is greater than or equal to the values of its children.
- **Min Heap**: For every node, the value of the node is less than or equal to the values of its children.

Visual representation of a min-heap:
```
      1
    /   \
   3     6
  / \   /
 5   9 8
```

Array representation: [1, 3, 6, 5, 9, 8]

Key Properties:
1. Complete Binary Tree
2. Heap Property (max or min)
3. Easy array implementation
4. Efficient operations: O(1) for find-min/max, O(log n) for insert/delete

### Heap Operations <a name="heap-operations"></a>

1. **Insert (Push)**: 
   - Add the element at the end of the heap
   - Bubble up the element until the heap property is satisfied
   - Time complexity: O(log n)

2. **Extract Min/Max (Pop)**:
   - Remove the root element (minimum for min-heap, maximum for max-heap)
   - Replace it with the last element
   - Bubble down until the heap property is satisfied
   - Time complexity: O(log n)

3. **Heapify**:
   - Convert an unordered array into a heap structure
   - Time complexity: O(n)

4. **Decrease Key**:
   - Decrease the value of a specific node
   - Bubble up until the heap property is satisfied
   - Time complexity: O(log n)

### Heap Implementation in C++ <a name="heap-implementation-cpp"></a>

```cpp
#include <iostream>
#include <vector>
using namespace std;

class MinHeap {
private:
    vector<int> heap;
    
    // Helper functions
    int parent(int i) { return (i - 1) / 2; }
    int leftChild(int i) { return 2 * i + 1; }
    int rightChild(int i) { return 2 * i + 2; }
    
    // Heapify a subtree with root at index i
    void heapify(int i) {
        int smallest = i;
        int left = leftChild(i);
        int right = rightChild(i);
        
        if (left < heap.size() && heap[left] < heap[smallest])
            smallest = left;
        
        if (right < heap.size() && heap[right] < heap[smallest])
            smallest = right;
        
        if (smallest != i) {
            swap(heap[i], heap[smallest]);
            heapify(smallest);
        }
    }

public:
    MinHeap() {}
    
    // Insert a new element
    void push(int value) {
        // Add new element at the end
        heap.push_back(value);
        
        // Get the index of the new element
        int i = heap.size() - 1;
        
        // Bubble up until the heap property is satisfied
        while (i > 0 && heap[parent(i)] > heap[i]) {
            swap(heap[i], heap[parent(i)]);
            i = parent(i);
        }
    }
    
    // Extract the minimum element
    int pop() {
        if (heap.empty())
            return -1;  // Heap is empty
        
        int root = heap[0];
        
        // Replace root with the last element
        heap[0] = heap.back();
        heap.pop_back();
        
        // Heapify the root
        heapify(0);
        
        return root;
    }
    
    // Get the minimum element without removing it
    int top() {
        if (heap.empty())
            return -1;  // Heap is empty
        
        return heap[0];
    }
    
    // Check if heap is empty
    bool empty() {
        return heap.empty();
    }
    
    // Get the size of the heap
    int size() {
        return heap.size();
    }
    
    // Build a heap from an array
    void buildHeap(vector<int>& arr) {
        heap = arr;
        
        // Start from the last non-leaf node and heapify all nodes
        for (int i = heap.size() / 2 - 1; i >= 0; i--)
            heapify(i);
    }
};
```

### Priority Queues in STL <a name="priority-queues-stl"></a>

The C++ STL provides a priority queue container that implements a heap:

```cpp
#include <iostream>
#include <queue>
using namespace std;

int main() {
    // Max-heap (default)
    priority_queue<int> maxHeap;
    
    // Min-heap
    priority_queue<int, vector<int>, greater<int>> minHeap;
    
    // Operations on max-heap
    maxHeap.push(3);
    maxHeap.push(1);
    maxHeap.push(7);
    maxHeap.push(5);
    
    while (!maxHeap.empty()) {
        cout << maxHeap.top() << " ";  // Prints: 7 5 3 1
        maxHeap.pop();
    }
    cout << endl;
    
    // Operations on min-heap
    minHeap.push(3);
    minHeap.push(1);
    minHeap.push(7);
    minHeap.push(5);
    
    while (!minHeap.empty()) {
        cout << minHeap.top() << " ";  // Prints: 1 3 5 7
        minHeap.pop();
    }
    
    return 0;
}
```

The priority queue is extensively used in graph algorithms like Dijkstra's and Prim's to efficiently find the vertex with the minimum key.

---

## STL Containers for Graph Algorithms <a name="stl-containers-for-graph-algorithms"></a>

### Vector <a name="vector"></a>

- Dynamic arrays that can resize themselves
- Random access is O(1)
- Insertion/deletion at the end is amortized O(1)
- Insertion/deletion in the middle is O(n)
- Commonly used for adjacency lists

```cpp
#include <vector>
vector<int> v;  // Empty vector
vector<int> v(5, 10);  // Vector with 5 elements, all initialized to 10
v.push_back(20);  // Add element at the end
v.pop_back();  // Remove element from the end
v[2] = 15;  // Access and modify element
```

### List <a name="list"></a>

- Doubly linked list
- No random access, but O(1) insertion/deletion anywhere in the list
- Useful for sparse graphs with frequent edge additions/removals

```cpp
#include <list>
list<int> l;  // Empty list
l.push_back(10);  // Add at the end
l.push_front(5);  // Add at the beginning
l.pop_back();  // Remove from the end
l.remove(5);  // Remove all occurrences of 5
```

### Map <a name="map"></a>

- Associative container implemented as Red-Black Trees
- Stores key-value pairs in sorted order
- Useful for graphs with non-integer vertices or sparse graphs

```cpp
#include <map>
map<string, int> m;  // Map with string keys and int values
m["one"] = 1;  // Insert or update
m.erase("one");  // Remove entry
if (m.find("two") != m.end()) {  // Check if key exists
    cout << "Found: " << m["two"] << endl;
}
```

### Set <a name="set"></a>

- Associative container that stores unique elements in sorted order
- Useful for tracking visited vertices and ensuring edge uniqueness

```cpp
#include <set>
set<int> s;  // Empty set
s.insert(10);  // Insert element
s.erase(10);  // Remove element
if (s.find(20) != s.end()) {  // Check if element exists
    cout << "Found 20" << endl;
}
```

### Priority Queue <a name="priority-queue"></a>

- Container adapter that provides constant time lookup of the largest element
- Used in Dijkstra's and Prim's algorithms for efficient vertex extraction

```cpp
#include <queue>
// Max-heap (default)
priority_queue<int> maxHeap;
// Min-heap
priority_queue<int, vector<int>, greater<int>> minHeap;

minHeap.push(30);  // Add element
int min = minHeap.top();  // Get minimum element
minHeap.pop();  // Remove minimum element
```

---

## Differences Between Key Algorithms <a name="differences-between-key-algorithms"></a>

### Dijkstra's vs. Prim's <a name="dijkstras-vs-prims"></a>

While both algorithms use similar techniques (greedy approach with priority queues), they solve different problems:

1. **Purpose**:
   - Dijkstra's: Finds shortest paths from a source to all vertices
   - Prim's: Finds a minimum spanning tree

2. **Applicability**:
   - Dijkstra's: Works on both directed and undirected graphs but requires non-negative weights
   - Prim's: Works only on undirected graphs

3. **Result**:
   - Dijkstra's: A shortest path tree where the path from source to any vertex is shortest
   - Prim's: A minimum spanning tree where total edge weight is minimized

4. **Distance Calculation**:
   - Dijkstra's: Distance is cumulative along the path
   - Prim's: Only considers individual edge weights

### Prim's vs. Kruskal's <a name="prims-vs-kruskals"></a>

Both algorithms find the minimum spanning tree, but use different approaches:

1. **Growth Strategy**:
   - Prim's: Grows a single tree from a starting vertex
   - Kruskal's: Grows a forest of trees that eventually merge into one

2. **Edge Selection**:
   - Prim's: Selects the minimum weight edge that connects a vertex in the MST to a vertex outside
   - Kruskal's: Selects the overall minimum weight edge that doesn't create a cycle