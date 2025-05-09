# Chapter 9: Graph Algorithms - Enhanced Notes

## 9.1 Definitions and Fundamentals

### Basic Graph Terminology
- **Graph G = (V, E)**: Consists of a set of vertices (V) and edges (E)
- **Edge**: A pair (v, w) where v, w ∈ V, sometimes called arcs
- **Adjacency**: In an undirected graph, if (v, w) is an edge, then w is adjacent to v and v is adjacent to w
- **Weighted Edge**: An edge with a third component representing weight or cost

### Paths and Cycles
- **Path**: A sequence of vertices w₁, w₂, w₃, ..., wₙ where (wᵢ, wᵢ₊₁) ∈ E for 1 ≤ i < N
- **Simple Path**: A path where all vertices are distinct (except possibly first and last)
- **Cycle**: A path of length ≥ 1 where w₁ = wₙ
- **Directed Acyclic Graph (DAG)**: A directed graph with no cycles

### Graph Representations

#### Adjacency Matrix
- **Space Requirement**: O(|V|²)
- **Best For**: Dense graphs where |E| = O(|V|²)
- **Drawback**: Wastes space for sparse graphs

#### Adjacency List
- **Space Requirement**: O(|E| + |V|)
- **Best For**: Sparse graphs
- **Implementation**: For each vertex, maintain a list of adjacent vertices
- **Example**: In a street map with Manhattan-like orientation, |E| ≈ 4|V|

## 9.2 Topological Sort

### Definition
A topological sort is an ordering of vertices in a directed acyclic graph (DAG) such that if there is a path from vᵢ to vⱼ, then vⱼ appears after vᵢ in the ordering.

### The Indegree Concept
- **Indegree**: The number of edges pointing TO a vertex
- **Example**:
  ```
  A → B → D
  ↓       ↑
  C ------+
  ```
  - A: indegree 0 (no arrows pointing to A)
  - B: indegree 1 (one arrow from A)
  - C: indegree 1 (one arrow from A)
  - D: indegree 2 (arrows from both B and C)

### Queue-Based Algorithm
1. Calculate the indegree of every vertex
2. Put all vertices with indegree 0 in a queue
3. While the queue is not empty:
   - Dequeue a vertex and add it to the result list
   - For each adjacent vertex, decrease its indegree by 1
   - If any vertex now has indegree 0, enqueue it

### Real-Life Analogy: Dependencies
Think of indegree as a "prerequisites counter":
- Tasks with indegree 0 have no dependencies and can be performed immediately
- When a task is completed, reduce the indegree of dependent tasks
- When a task's indegree becomes 0, it can be performed next

### Code for Topological Sort
```
void Graph::topsort()
{
    for(int counter = 0; counter < NUM_VERTICES; counter++)
    {
        Vertex v = findNewVertexOfIndegreeZero();
        if(v == NOT_A_VERTEX)
            throw CycleFoundException{};
        v.topNum = counter;
        for each Vertex w adjacent to v
            w.indegree--;
    }
}
```

## 9.3 Shortest-Path Algorithms

### Problem Definition
Given a weighted graph G = (V, E) and a starting vertex s, find the shortest weighted path from s to every other vertex in G.

### 9.3.1 Unweighted Shortest Paths (Breadth-First Search)
- **Strategy**: Process vertices in layers (distance 0, then 1, then 2, etc.)
- **Time Complexity**: O(|V| + |E|) using a queue

```
void Graph::unweighted(Vertex s)
{
    for each Vertex v
    {
        v.dist = INFINITY;
        v.known = false;
    }
    s.dist = 0;
    
    for(int currDist = 0; currDist < NUM_VERTICES; currDist++)
        for each Vertex v
            if(!v.known && v.dist == currDist)
            {
                v.known = true;
                for each Vertex w adjacent to v
                    if(w.dist == INFINITY)
                    {
                        w.dist = currDist + 1;
                        w.path = v;
                    }
            }
}
```

### 9.3.2 Dijkstra's Algorithm (Weighted Shortest Paths)
- **Type**: Greedy algorithm
- **Key Idea**: For each vertex, maintain:
  - `known`: Whether the shortest path to this vertex is found
  - `dist`: Current shortest path distance from source
  - `path`: Last vertex on the current shortest path

#### Algorithm Steps:
1. Initialize source vertex distance to 0, all others to INFINITY
2. While there are unknown vertices:
   - Select unknown vertex v with smallest distance
   - Mark v as known
   - For each adjacent unknown vertex w:
     - If path through v is shorter, update w's distance and path

```
void Graph::dijkstra(Vertex s)
{
    for each Vertex v
    {
        v.dist = INFINITY;
        v.known = false;
    }
    s.dist = 0;
    
    while(there is an unknown distance vertex)
    {
        Vertex v = smallest unknown distance vertex;
        v.known = true;
        
        for each Vertex w adjacent to v
            if(!w.known)
            {
                DistType cvw = cost of edge from v to w;
                if(v.dist + cvw < w.dist)
                {
                    // Update w
                    decrease(w.dist to v.dist + cvw);
                    w.path = v;
                }
            }
    }
}
```

### 9.3.3 Graphs with Negative Edge Costs
- Dijkstra's algorithm fails with negative edges
- Modified algorithm:
  - Remove "known" concept (can change decisions)
  - Use a queue-based approach
  - Time complexity: O(|E| · |V|) - much slower than Dijkstra's

### 9.3.4 Printing Paths
```
void Graph::printPath(Vertex v)
{
    if(v.path != NOT_A_VERTEX)
    {
        printPath(v.path);
        cout << " to ";
    }
    cout << v;
}
```

### 9.3.5 All-Pairs Shortest Path
- Find shortest paths between all pairs of vertices
- Can run single-source algorithm |V| times
- O(|V|³) algorithm for dense graphs
- For sparse graphs, running |V| Dijkstra's algorithms with priority queues is faster

## 9.5 Minimum Spanning Tree

### Definition
A minimum spanning tree (MST) of an undirected graph is a tree formed from graph edges that connects all vertices at lowest total cost.

### 9.5.1 Prim's Algorithm
- Similar to Dijkstra's algorithm
- Grow the tree from a starting vertex
- At each step:
  - Select the minimum-weight edge connecting a vertex in the tree to a vertex outside the tree
  - Add that edge and vertex to the tree

#### Key Differences from Dijkstra's Algorithm:
- `dv` is the weight of the shortest edge connecting v to any known vertex
- Update rule: After selecting vertex v, for each unknown w adjacent to v, `dw = min(dw, cw,v)`

### 9.5.2 Kruskal's Algorithm
- Sort edges by weight (smallest first)
- Accept an edge if it doesn't create a cycle
- Maintains a forest (collection of trees) that gradually merges
- Uses Union-Find data structure to check for cycles

#### Algorithm Steps:
1. Start with |V| single-node trees
2. Consider edges in order of increasing weight
3. Add an edge if it connects two different trees
4. Continue until only one tree remains (the MST)

## 9.7 Introduction to NP-Completeness

### Complexity Classes
- Most efficient algorithms run in linear time relative to input size
- **Undecidable Problems**: Mathematically impossible to solve with any algorithm
- **NP Class**: Nondeterministic polynomial-time problems
  - Problems where solutions can be verified quickly (in polynomial time)
  - Many important problems fall into this class
  - No known polynomial-time algorithms to solve them

### Practical Implications
- For NP-Complete problems, we often use:
  - Approximation algorithms
  - Heuristics
  - Special case solutions
  - These will be discussed further in Chapter 10
