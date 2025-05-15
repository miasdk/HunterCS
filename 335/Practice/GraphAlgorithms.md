# Practice Problems for Graph Algorithms

## Practice Problem 1: Topological Sorting

Consider the following directed acyclic graph:

```
    J → K → M
   ↗  ↑  ↗
  H → L → N
 ↗
P
```

Find a valid topological ordering for this graph. Show your work by listing:
1. The initial indegree of each vertex
2. The sequence in which you process vertices
3. The final topological order

## Practice Problem 2: Dijkstra's Algorithm (Shortest Path)

Consider the following weighted graph:

```
      4       3
    P --- Q --- R
   /|      \   /|
  / |       \ / |
 8  2        X  5
/   |       / \ |
S   |      /   \|
\   |     6     T
 \  |    /     /
  7 |   /     9
   \| /      /
    U ------ V
        1
```

Where the numbers represent edge weights.

Find the shortest path from vertex P to all other vertices using Dijkstra's algorithm. Create a table showing:
1. The state after each vertex is processed (known vertices, distances)
2. The final shortest path distance from P to each vertex
3. The actual path (sequence of vertices) for each shortest path

## Practice Problem 3: Dijkstra's Algorithm with Negative Edge

Create your own example graph with:
1. At least 5 vertices
2. One negative edge (but no negative cycles)
3. A specific source vertex

Then demonstrate how Dijkstra's algorithm produces an incorrect result by:
1. Showing the steps of Dijkstra's algorithm
2. Identifying the correct shortest path
3. Explaining exactly where and why Dijkstra's algorithm fails

## Practice Problem 4: Minimum Spanning Tree

Consider the following weighted undirected graph:

```
     3
  W --- X
 /|\   /|\
/ | \ / | \
5 |  V  | 8
\  4 /|\ 2 /
 \ / | \ /
  Y  |  Z
   \ | /
    \|/
     U
      6
```

Edge weights:
- W-X: 3
- W-Y: 5
- W-V: 4
- X-V: 7
- X-Z: 8
- Y-V: 2
- Y-U: 6
- Z-V: 2
- Z-U: 1

Find a minimum spanning tree using:
1. Prim's algorithm (start at vertex W)
   - Create tables showing each step
   - List the edges in the final MST
   
2. Kruskal's algorithm
   - List all edges sorted by weight
   - Show which edges are included or excluded at each step
   - Draw or describe the final MST

## Practice Problem 5: Algorithm Selection

For each of the following graph scenarios, determine whether Floyd-Warshall or Johnson's algorithm would be more efficient. Justify your answer with calculations:

a) A social network graph with 10,000 users where each user is friends with an average of 150 other users.

b) A complete graph with 500 vertices (every vertex is connected to every other vertex).

c) A grid-like graph where each vertex is connected to at most 4 adjacent vertices (like a chessboard), with a total of 10,000 vertices.

## Practice Problem 6: Bellman-Ford Algorithm

As an extension beyond the homework, implement the Bellman-Ford algorithm on the graph from Problem 3. This will:

1. Show the correct shortest paths in the presence of negative edges
2. Help you understand an alternative to Dijkstra's algorithm
3. Reinforce the concept of edge relaxation

Show:
- The steps of the Bellman-Ford algorithm
- The final shortest path distances
- Verification that Bellman-Ford produces the correct result where Dijkstra's fails

## Practice Problem 7: Combined Problem

Consider a directed weighted graph representing tasks in a project:

```
START → Task A (3 days)  → Task C (5 days) → FINISH
   \                         ↑             ↗
    \→ Task B (2 days) ------+------------
```

Where the weights represent the duration of each task.

1. Find a topological ordering of the tasks.
2. Calculate the earliest possible completion time of the project.
3. Identify the critical path (sequence of tasks that determines the minimum project duration).

This problem combines topological sorting with path finding to demonstrate a real-world application of graph algorithms.

## Practice Problem 8: MST vs. Shortest Path Tree

Using the graph from Problem 2:

1. Find the minimum spanning tree using Prim's algorithm (start at vertex P).
2. Find the shortest path tree from P using Dijkstra's algorithm.
3. Compare and contrast the two trees:
   - Are they the same? If not, what edges differ?
   - What is the total weight of each tree?
   - Explain why they differ (or why they're the same).

This problem helps clarify the difference between minimizing total edge weight (MST) and minimizing path length from a source (shortest path tree).
