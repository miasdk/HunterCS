### 9.1 Definitions 
A graph G = (V, E) consists of a set of vertices, V, and a set of edges, E. Each edge is a pair
(v, w), where v, w ∈ V. Edges are sometimes referred to as arcs.

In an undirected graph with edge (v, w), and hence
(w, v), w is adjacent to v and v is adjacent to w. Sometimes an edge has a third component,
known as either a weight or a cost.

A path in a graph is a sequence of vertices w1, w2, w3, . . . , wN such that (wi, wi+1) ∈ E
for 1 ≤ i < N.

A simple path is a
path such that all vertices are distinct, except that the first and last could be the same.
A cycle in a directed graph is a path of length at least 1 such that w1 = wN

A directed graph is acyclic if it has
no cycles. A directed acyclic graph is sometimes referred to by its abbreviation, DAG.