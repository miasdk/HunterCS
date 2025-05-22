# Prim's Algorithm - Complete Exam Examples

## Example 1: Step-by-Step Prim's Algorithm

**Problem**: Find the MST using Prim's algorithm starting from vertex A.

```
Graph:
    A----8----B----7----C
    |\        |\        |
    | 4       | 9       2
    |  \      |  \      |
    |   H----11-I       |
    |  /      |  \      |
    | 8       2   4     |
    |/        |    \    |
    G----1----F----6----E
         \    |   /
          2   1  5
           \ | /
            \|/
             D
```

### Step-by-Step Solution:

**Initial**: Start with vertex A

| Step | Available Edges | Choose | Weight | Reason | MST So Far |
|------|----------------|--------|--------|--------|------------|
| 1 | A-B(8), A-H(4), A-G(8) | A-H | 4 | Minimum weight | {A-H} |
| 2 | A-B(8), A-G(8), H-I(11), H-G(8) | A-B or H-G | 8 | Both minimum, choose A-B | {A-H, A-B} |
| 3 | A-G(8), H-I(11), H-G(8), B-C(7), B-I(9) | B-C | 7 | Minimum weight | {A-H, A-B, B-C} |
| 4 | A-G(8), H-I(11), H-G(8), B-I(9), C-E(2) | C-E | 2 | Minimum weight | {A-H, A-B, B-C, C-E} |
| 5 | A-G(8), H-I(11), H-G(8), B-I(9), E-F(6), E-D(5) | E-D | 5 | Minimum weight | {A-H, A-B, B-C, C-E, E-D} |
| 6 | A-G(8), H-I(11), H-G(8), B-I(9), E-F(6), D-F(1), D-G(2) | D-F | 1 | Minimum weight | {A-H, A-B, B-C, C-E, E-D, D-F} |
| 7 | A-G(8), H-I(11), H-G(8), B-I(9), E-F(6), D-G(2), F-G(1), F-I(2) | F-G | 1 | Minimum weight | {A-H, A-B, B-C, C-E, E-D, D-F, F-G} |
| 8 | H-I(11), H-G(8), B-I(9), F-I(2) | F-I | 2 | Minimum weight | {A-H, A-B, B-C, C-E, E-D, D-F, F-G, F-I} |

**Final MST Edges**: A-H, A-B, B-C, C-E, E-D, D-F, F-G, F-I
**Total Weight**: 4 + 8 + 7 + 2 + 5 + 1 + 1 + 2 = **30**

---

## Example 2: Prim's Algorithm Analysis Question

**Question**: Write a full complexity analysis of Prim's algorithm using binary heaps. Include all steps taken and data structures used, stating the complexity of each step and relating that to the overall complexity. [15 pts]

### Complete Solution:

**Data Structures Used:**
- **Adjacency Lists**: O(|V| + |E|) space to represent the graph
- **Min-Heap**: Store vertices with their minimum edge weights to MST
- **Boolean array**: Track which vertices are already in MST - O(|V|) space

**Step-by-Step Analysis:**

1. **Initialization**: 
   - Create adjacency list representation: **O(|V| + |E|)**
   - Initialize heap with all vertices, source with weight 0, others with ∞: **O(|V|)**
   - Initialize MST tracking array: **O(|V|)**

2. **Main Loop** (Execute |V| times):
   - **Extract minimum** from heap: **O(log |V|)** per operation
   - **Mark vertex as in MST**: **O(1)**
   - **For each adjacent edge** to extracted vertex:
     - If neighbor not in MST and edge weight < current key: **O(1)** check
     - **Decrease key** in heap: **O(log |V|)** per operation

3. **Edge Processing Analysis**:
   - Each edge is considered exactly **twice** (once from each endpoint)
   - Total edge considerations: **2|E|**
   - Each consideration may trigger a decrease-key: **O(log |V|)**
   - Total edge processing: **O(|E| log |V|)**

4. **Vertex Processing Analysis**:
   - Extract minimum |V| times: **O(|V| log |V|)**
   - Combined with edge processing: **O(|E| log |V|)**

**Final Complexity**: **O(|E| log |V|)**

**When to Use Heaps vs. Not:**
- **Use heaps when**: Graph is sparse (|E| ≈ |V|)
- **Don't use heaps when**: Graph is dense (|E| ≈ |V|²), simple O(|V|²) is better

---

## Example 3: Prim's vs Kruskal's Comparison

**Question**: Compare Prim's and Kruskal's algorithms. When would you choose each? [8 pts]

### Solution:

| Aspect | Prim's Algorithm | Kruskal's Algorithm |
|--------|------------------|-------------------|
| **Approach** | Grows MST from single vertex | Considers all edges globally |
| **Data Structure** | Min-heap or array | Union-Find (Disjoint Set) |
| **Time Complexity** | O(\|E\| log \|V\|) with heaps<br>O(\|V\|²) without heaps | O(\|E\| log \|V\|) |
| **Best for** | Dense graphs<br>When you need MST from specific vertex | Sparse graphs<br>When edges are pre-sorted |
| **Memory** | O(\|V\|) additional space | O(\|V\|) for Union-Find |
| **Edge Processing** | Only considers edges to current MST | Must sort all edges first |

**Choose Prim's when**:
- Graph is dense (many edges)
- You want MST rooted at specific vertex
- Edges are not pre-sorted

**Choose Kruskal's when**:
- Graph is sparse (few edges)
- Edges are already sorted by weight
- You want globally minimum edges

---

## Example 4: Prim's Algorithm Coding Implementation

**Question**: Implement the key steps of Prim's algorithm using C++ STL containers. [10 pts]

### Solution:

```cpp
#include <vector>
#include <queue>
#include <climits>

struct Edge {
    int to, weight;
};

class PrimsMST {
private:
    std::vector<std::vector<Edge>> adj;
    std::vector<bool> inMST;
    std::vector<int> key;
    int vertices;

public:
    PrimsMST(int V) : vertices(V) {
        adj.resize(V);
        inMST.resize(V, false);
        key.resize(V, INT_MAX);
    }
    
    void addEdge(int u, int v, int weight) {
        adj[u].push_back({v, weight});
        adj[v].push_back({u, weight});
    }
    
    int findMST(int start = 0) {
        // Priority queue: {weight, vertex}
        std::priority_queue<std::pair<int, int>, 
                          std::vector<std::pair<int, int>>,
                          std::greater<>> pq;
        
        // Start from vertex 'start'
        key[start] = 0;
        pq.push({0, start});
        
        int mstWeight = 0;
        
        while (!pq.empty()) {
            int u = pq.top().second;
            int weight = pq.top().first;
            pq.pop();
            
            // Skip if already in MST
            if (inMST[u]) continue;
            
            // Add to MST
            inMST[u] = true;
            mstWeight += weight;
            
            // Check all adjacent vertices
            for (const Edge& edge : adj[u]) {
                int v = edge.to;
                int edgeWeight = edge.weight;
                
                // If v is not in MST and edge weight is smaller
                if (!inMST[v] && edgeWeight < key[v]) {
                    key[v] = edgeWeight;
                    pq.push({edgeWeight, v});
                }
            }
        }
        
        return mstWeight;
    }
};
```

**Time Complexity**: O(|E| log |V|)
**Space Complexity**: O(|V| + |E|)

---

## Example 5: Prim's Algorithm Variations

**Question**: Explain the difference between implementing Prim's algorithm with and without heaps. Analyze the trade-offs. [12 pts]

### Solution:

**Implementation Without Heaps (Simple Array)**:
```cpp
int primSimple(vector<vector<int>>& graph) {
    int V = graph.size();
    vector<int> key(V, INT_MAX);
    vector<bool> inMST(V, false);
    
    key[0] = 0;  // Start from vertex 0
    int mstWeight = 0;
    
    for (int count = 0; count < V; count++) {
        // Find minimum key vertex not in MST
        int u = -1;
        for (int v = 0; v < V; v++) {
            if (!inMST[v] && (u == -1 || key[v] < key[u])) {
                u = v;
            }
        }
        
        inMST[u] = true;
        mstWeight += key[u];
        
        // Update keys of adjacent vertices
        for (int v = 0; v < V; v++) {
            if (graph[u][v] && !inMST[v] && graph[u][v] < key[v]) {
                key[v] = graph[u][v];
            }
        }
    }
    
    return mstWeight;
}
```

**Complexity Comparison**:

| Implementation | Time Complexity | Space Complexity | Best Use Case |
|---------------|-----------------|------------------|---------------|
| **With Heaps** | O(\|E\| log \|V\|) | O(\|V\| + \|E\|) | Sparse graphs (\|E\| ≈ \|V\|) |
| **Without Heaps** | O(\|V\|²) | O(\|V\|²) | Dense graphs (\|E\| ≈ \|V\|²) |

**Trade-off Analysis**:
- **Sparse Graph** (|E| = O(|V|)): Heap version is O(|V| log |V|), simple version is O(|V|²)
- **Dense Graph** (|E| = O(|V|²)): Heap version is O(|V|² log |V|), simple version is O(|V|²)
- **Crossover Point**: When |E| ≈ |V|²/log|V|, both approaches have similar performance

**Recommendation**: Use heaps for sparse graphs, simple array approach for dense graphs.