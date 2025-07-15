# Graph Algorithms Practice Problems

## Contents
1. [Topological Sort](#topological-sort)
2. [Dijkstra's Algorithm](#dijkstras-algorithm)
3. [Prim's Algorithm](#prims-algorithm)
4. [Kruskal's Algorithm](#kruskals-algorithm)
5. [Floyd-Warshall Algorithm](#floyd-warshall-algorithm)
6. [Algorithm Analysis Questions](#algorithm-analysis-questions)

---

## Topological Sort

### Problem 1
Consider the following directed acyclic graph (DAG):

```
    A → B → D
    ↓   ↑   ↓
    C → E → F
    ↓       ↑
    G → H ──┘
```

a) Calculate the indegree of each vertex.
b) Use Kahn's algorithm (indegree method) to find a valid topological ordering.
c) Trace the algorithm step by step using a table showing:
   - Vertices with indegree 0 at each step
   - The vertex removed at each step
   - Updated indegrees after each removal
   - Current partial ordering at each step

### Problem 2
For the following graph representing course prerequisites (an arrow from X to Y means X is a prerequisite for Y):

```
    CS101 → CS201 → CS301
      ↓       ↓      ↑
    MATH101 → CS210 →┘
      ↓
    MATH201
```

a) Find a valid course sequence that satisfies all prerequisites.
b) If MATH201 is also a prerequisite for CS301, does that change your answer? If so, how?
c) What happens if we add a prerequisite that CS301 is required for MATH101? Explain.

---

## Dijkstra's Algorithm

### Problem 1
Consider the following weighted graph:

```
         6
    A -------- B
    |  \       | \
    |   \      |  \
   4|    \ 2   |7  \ 3
    |     \    |    \
    |      \   |     \
    C ------ D ----- E
       3        5
```

a) Use Dijkstra's algorithm to find the shortest path from vertex A to all other vertices.
b) Trace the algorithm using a table with the following columns:
   - Current known vertices
   - Current distances to all vertices
   - Current predecessor of each vertex
   - Vertex selected at each step
   - Vertices whose distances are updated

c) Draw the final shortest path tree rooted at A.

### Problem 2
For the following graph with negative edge weights:

```
         4        2
    A -------- B ----- C
    |          |       |
   2|          |-3     |-1
    |          |       |
    D -------- E ----- F
         1        3
```

a) Apply Dijkstra's algorithm starting from vertex A and show why it might give incorrect results.
b) Identify a specific incorrect shortest path computed by Dijkstra's algorithm.
c) What is the actual shortest path for the case you identified in part b?

---

## Prim's Algorithm

### Problem 1
Consider the following weighted undirected graph:

```
         4
    A -------- B
    |  \       | \
    |   \      |  \
   5|    \ 1   |3  \ 6
    |     \    |    \
    |      \   |     \
    C ------ D ----- E
       2        7
```

a) Use Prim's algorithm starting from vertex A to find a minimum spanning tree.
b) Trace the algorithm step by step using a table showing:
   - Known vertices at each step
   - Current key (edge weight) values
   - Current parent of each vertex
   - Vertex added at each step
   - Updated key values after each step

c) Draw the final MST and calculate its total weight.

### Problem 2
Consider the graph:

```
         2
    P -------- Q
   /|\        /|\
  / | \      / | \
 /  |  \    /  |  \
5   |   4  1   |   3
\   |   /  \   |   /
 \  |  /    \  |  /
  \ | /      \ | /
   \|/        \|/
    R -------- S
         6
```

a) Starting from vertex P, use Prim's algorithm to find an MST. Show the table after each vertex is processed.
b) Explain what would happen if you started Prim's algorithm from vertex R instead. Would the resulting MST be different? Why or why not?

---

## Kruskal's Algorithm

### Problem 1
For the following weighted undirected graph:

```
    A --- 3 --- B
    |           |\
    |           | \
    5           2  6
    |           |  |
    |           |  |
    C --- 4 --- D  |
    |            \ |
    |             \|
    7              E
    |              |
    |              |
    F --- 1 --- G  8
                   |
                   |
                   H
```

a) Sort all edges by weight.
b) Trace Kruskal's algorithm step by step, showing which edges are considered and whether they are accepted or rejected.
c) Draw the final MST and calculate its total weight.

### Problem 2
Consider the following graph:

```
         2
    J -------- K
   /|         /|
  / |        / |
 /  |       /  |
4   |      /   |
\   |5    /3   |7
 \  |    /     |
  \ |   /      |
   \|  /       |
    L -------- M
         6
```

a) Trace Kruskal's algorithm on this graph, showing the edge processing order and the evolving MST.
b) For each edge that is rejected, explain specifically why it was rejected (which cycle would it have created?).
c) Verify that the MST has exactly n-1 edges, where n is the number of vertices.

---

## Floyd-Warshall Algorithm

### Problem 1
Consider the following directed weighted graph:

```
         2
    A -------→ B
    ↑   \      ↓
    |    \     |
   4|     \ 1  |-5
    |      \   |
    |       ↘  ↓
    C ←------ D
        3
```

a) Initialize the distance matrix D⁰ for the Floyd-Warshall algorithm.
b) Compute D¹, D², D³, and D⁴ matrices step by step.
c) Determine the shortest path from A to D and its length.
d) Identify if there are any negative cycles in the graph.

### Problem 2
For the following weighted directed graph:

```
         3        1        -2
    P -------→ Q -------→ R -------→ S
    ↑          |          ↑          |
    |          |          |          |
    |2         |-4        |5         |-1
    |          |          |          |
    |          ↓          |          ↓
    T ←------- U ←------- V ←------- W
         6        -3        2
```

a) Use the Floyd-Warshall algorithm to find the shortest path between all pairs of vertices.
b) Show the matrix D⁰ and the final matrix after the algorithm completes.
c) What is the shortest path from P to W? From W to P?
d) Does this graph contain any negative cycles? If so, identify one.

---

## Algorithm Analysis Questions

### Problem 1
Consider the following pseudocode:

```
function process(Graph G, int n):
    for i = 1 to n:
        for each vertex v in G:
            for each neighbor u of v:
                if distance[v] + weight(v,u) < distance[u]:
                    distance[u] = distance[v] + weight(v,u)
    
    for each vertex v in G:
        for each neighbor u of v:
            if distance[v] + weight(v,u) < distance[u]:
                return "Negative cycle detected"
    
    return distance[]
```

a) What well-known algorithm does this code implement?
b) What is the time complexity of this algorithm in terms of |V| (number of vertices) and |E| (number of edges)?
c) Explain why the last loop is necessary and what it checks for.
d) How would the time complexity change if the graph is represented using an adjacency matrix instead of an adjacency list?

### Problem 2
Consider the following code segment:

```
function mystery(Graph G, Vertex start):
    create queue Q
    mark start as visited
    enqueue start to Q
    
    while Q is not empty:
        vertex v = Q.dequeue()
        
        for each neighbor u of v:
            if u is not visited:
                mark u as visited
                enqueue u to Q
                distance[u] = distance[v] + 1
```

a) What algorithm does this code implement?
b) What does the distance array represent in this context?
c) What is the time complexity of this algorithm for:
   - A graph represented with an adjacency list?
   - A graph represented with an adjacency matrix?
d) How would you modify this algorithm to also output the shortest path (sequence of vertices) from start to any other vertex?

### Problem 3
Analyze the following code segment:

```
function analyze(int n):
    total = 0
    i = n
    while i > 0:
        j = i
        while j > 0:
            total = total + 1
            j = j / 2  // integer division
        i = i - 1
    return total
```

a) Trace the execution of this code for n = 8.
b) Determine the exact number of times the statement "total = total + 1" is executed for n = 8.
c) Find a general formula for the number of times this statement is executed for any value of n.
d) What is the time complexity of this function in big-O notation?

### Problem 4
Consider a graph G with V vertices and E edges:

a) If we use Dijkstra's algorithm with a binary heap, what is the time complexity?
b) If we use Dijkstra's algorithm with a Fibonacci heap, what is the time complexity?
c) For a complete graph (where every vertex is connected to every other vertex), which implementation would be more efficient and why?
d) For a sparse graph where E ≈ V, which implementation would be more efficient and why?

### Problem 5
Consider the scenario where you need to find shortest paths in a graph:

a) When would you use Dijkstra's algorithm instead of the Bellman-Ford algorithm?
b) When would you use the Bellman-Ford algorithm instead of Dijkstra's algorithm?
c) When would you use the Floyd-Warshall algorithm instead of running Dijkstra's algorithm from each vertex?
d) In a graph with V vertices and E edges, what is the crossover point (in terms of graph density) where Floyd-Warshall becomes more efficient than running Dijkstra's V times?
