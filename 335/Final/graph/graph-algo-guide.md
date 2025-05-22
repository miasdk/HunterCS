# Step-by-Step Guide for Graph Algorithm Questions

This guide provides detailed, methodical approaches for solving graph algorithm questions on your exam, with special focus on Dijkstra's, Prim's, and Kruskal's algorithms. Each algorithm is explained with a step-by-step process, common exam formats, and strategies for avoiding mistakes.

## General Approach to Graph Algorithm Questions

Regardless of the specific algorithm, follow these steps:

1. **Read the problem carefully**
   - Identify the graph type (directed/undirected)
   - Note whether weights are present
   - Identify the specific task (shortest path, MST, etc.)

2. **Draw the graph**
   - Visualize vertices and edges
   - Label weights if applicable
   - Mark source/destination vertices

3. **Choose the appropriate algorithm**
   - Shortest path: Dijkstra's (non-negative weights), Bellman-Ford (may have negative weights)
   - Minimum spanning tree: Prim's or Kruskal's
   - Topological ordering: Topological sort (must be a DAG)

4. **Set up data structures**
   - For exam questions, create tables to track algorithm progress
   - Label column headers clearly
   - Initialize values properly

5. **Execute the algorithm step-by-step**
   - Show all work (partial credit!)
   - Update tables at each step
   - Circle or highlight key decisions

6. **Verify your answer**
   - Check if constraints are met
   - Trace back paths for shortest path problems
   - Count edges for MST problems (should be |V|-1)

7. **Analyze complexity**
   - State time and space complexity if requested
   - Justify your analysis based on implementation details

## Dijkstra's Algorithm

### Problem Format
Most exam questions will ask you to:
- Find the shortest path from vertex A to vertex B
- Trace through the algorithm step by step
- Show all steps in a table format
- Reconstruct the final path

### Required Table Format

|  v  | known |  d_v  |  p_v  |
|-----|-------|-------|-------|
| v₁  |   F   |   ∞   |   0   |
| v₂  |   F   |   0   |   0   |  (source vertex)
| v₃  |   F   |   ∞   |   0   |
| ... |  ...  |  ...  |  ...  |

Where:
- **v**: Vertex identifier
- **known**: Whether vertex has been marked as known (T/F)
- **d_v**: Current best known distance from source
- **p_v**: Predecessor vertex in path

### Step-by-Step Approach

1. **Initialization**:
   - Set distance of source vertex to 0
   - Set all other distances to ∞
   - Set all vertices as unknown (F)
   - Set all predecessors to 0 or null

2. **Main Loop (repeat until destination is known or all vertices are known)**:
   - Select the unknown vertex with smallest distance value (v)
   - Mark v as known (T)
   - For each adjacent vertex u of v that is unknown:
     - Calculate potential new distance: d_v + weight(v,u)
     - If this distance is smaller than current d_u:
       - Update d_u = d_v + weight(v,u)
       - Update p_u = v

3. **For Each Step**:
   - Complete a new table row
   - Bold or highlight the vertex being marked as known
   - Show updated distance and predecessor values
   - Indicate which adjacent vertices are being updated

4. **Path Reconstruction**:
   - Start from destination vertex
   - Follow predecessor pointers back to source
   - Report the path in correct order (source to destination)

### Example

For a graph with vertices 1-5 and source vertex 1:

**Step 1 (Initial Table)**:
|  v  | known |  d_v  |  p_v  |
|-----|-------|-------|-------|
|  1  |   F   |   0   |   0   |
|  2  |   F   |   ∞   |   0   |
|  3  |   F   |   ∞   |   0   |
|  4  |   F   |   ∞   |   0   |
|  5  |   F   |   ∞   |   0   |

**Step 2 (Mark vertex 1 as known)**:
|  v  | known |  d_v  |  p_v  |
|-----|-------|-------|-------|
|  1  |   T   |   0   |   0   |
|  2  |   F   |   5   |   1   |
|  3  |   F   |   2   |   1   |
|  4  |   F   |   ∞   |   0   |
|  5  |   F   |   ∞   |   0   |

And so on...

### Common Mistakes to Avoid
1. Not updating the predecessor when updating a distance
2. Incorrectly selecting the next vertex to mark as known (must be unknown with smallest distance)
3. Forgetting to check if a vertex is already known before considering it for updates
4. Incorrectly updating distances (should only update if new path is shorter)
5. Stopping too early before finding the shortest path to destination

## Prim's Algorithm

### Problem Format
Exam questions typically ask you to:
- Find the minimum spanning tree (MST) of a graph
- Trace through the algorithm step by step
- Show all steps in a table format
- List the edges in the final MST

### Required Table Format

|  v  | known |  d_v  |  p_v  |
|-----|-------|-------|-------|
| v₁  |   F   |   ∞   |   0   |
| v₂  |   F   |   0   |   0   |  (starting vertex)
| v₃  |   F   |   ∞   |   0   |
| ... |  ...  |  ...  |  ...  |

The format is similar to Dijkstra's, but with different interpretations:
- **v**: Vertex identifier
- **known**: Whether vertex is in the MST (T/F)
- **d_v**: Weight of the lightest edge connecting v to the MST
- **p_v**: Vertex in MST that connects to v with weight d_v

### Step-by-Step Approach

1. **Initialization**:
   - Select any starting vertex s
   - Set d_s = 0
   - Set all other distances to ∞
   - Set all vertices as not in MST (F)
   - Set all predecessors to 0 or null

2. **Main Loop (repeat until all vertices are in MST)**:
   - Select the vertex v not in MST with smallest d_v
   - Mark v as in MST (T)
   - Add edge (p_v, v) to the MST (unless v is the starting vertex)
   - For each adjacent vertex u of v that is not in MST:
     - If weight(v,u) < d_u:
       - Update d_u = weight(v,u)
       - Update p_u = v

3. **For Each Step**:
   - Complete a new table row
   - Bold or highlight the vertex being added to MST
   - Show updated d_v and p_v values
   - Indicate which adjacent vertices are being updated

4. **MST Construction**:
   - List all edges in the MST: (p_v₁, v₁), (p_v₂, v₂), ..., (p_vₙ₋₁, vₙ₋₁)
   - Calculate total weight if required
   - Draw the final MST if space permits

### Example

For an undirected graph with vertices 1-5 and starting at vertex 1:

**Step 1 (Initial Table)**:
|  v  | known |  d_v  |  p_v  |
|-----|-------|-------|-------|
|  1  |   F   |   0   |   0   |
|  2  |   F   |   ∞   |   0   |
|  3  |   F   |   ∞   |   0   |
|  4  |   F   |   ∞   |   0   |
|  5  |   F   |   ∞   |   0   |

**Step 2 (Add vertex 1 to MST)**:
|  v  | known |  d_v  |  p_v  |
|-----|-------|-------|-------|
|  1  |   T   |   0   |   0   |
|  2  |   F   |   3   |   1   |
|  3  |   F   |   5   |   1   |
|  4  |   F   |   ∞   |   0   |
|  5  |   F   |   ∞   |   0   |

And so on...

### Common Mistakes to Avoid
1. Confusing Prim's with Dijkstra's (Prim's finds the MST, not shortest paths)
2. Not updating a vertex's distance when a lighter edge is found
3. Incorrectly selecting the next vertex to add to MST
4. Adding an edge to the MST when adding the starting vertex
5. Missing updates to adjacent vertices at each step

## Kruskal's Algorithm

### Problem Format
Exam questions typically ask you to:
- Find the minimum spanning tree (MST) of a graph
- List edges in order of consideration
- Indicate which edges are accepted/rejected
- Provide the final MST

### Required Format

| Edge   | Weight | Action    | Reason                |
|--------|--------|-----------|----------------------|
| (v₁,v₂) |   2    | Accept    | No cycle formed      |
| (v₃,v₄) |   3    | Accept    | No cycle formed      |
| (v₂,v₄) |   4    | Reject    | Would create cycle   |
| ...     |  ...   | ...       | ...                  |

### Step-by-Step Approach

1. **Initialization**:
   - Sort all edges by weight (ascending)
   - Create a disjoint-set (Union-Find) data structure
   - Initialize an empty MST

2. **Main Loop (process edges in sorted order)**:
   - Consider the next lightest edge (u,v)
   - If adding (u,v) doesn't create a cycle:
     - Add (u,v) to the MST
     - Union the sets containing u and v
   - Else:
     - Reject this edge
   - Continue until |V|-1 edges are added or all edges are processed

3. **For Each Step**:
   - Record the edge being considered
   - Indicate whether it's accepted or rejected
   - State the reason (accepted: no cycle formed; rejected: would create cycle)

4. **MST Construction**:
   - List all accepted edges
   - Calculate total weight if required
   - Draw the final MST if space permits

### Example

For an undirected graph with edges sorted by weight:

**Edge Processing**:
| Edge   | Weight | Action    | Reason                |
|--------|--------|-----------|----------------------|
| (1,3)  |   2    | Accept    | No cycle formed      |
| (2,4)  |   3    | Accept    | No cycle formed      |
| (1,2)  |   4    | Accept    | No cycle formed      |
| (3,4)  |   5    | Reject    | Would create cycle   |
| (2,5)  |   6    | Accept    | No cycle formed      |
| (4,5)  |   7    | Reject    | Would create cycle   |

Final MST: edges (1,3), (2,4), (1,2), (2,5) with total weight 15.

### Common Mistakes to Avoid
1. Not sorting edges properly by weight
2. Incorrectly determining whether an edge creates a cycle
3. Continuing to process edges after the MST is complete (should have |V|-1 edges)
4. Forgetting to merge sets after accepting an edge
5. Listing edges in the wrong order of consideration

## Additional Graph Algorithm Tips

### For All Algorithms
1. **Always show your work**
   - Create tables for each step
   - Update all values at each iteration
   - Indicate which vertex/edge is being considered

2. **Check your answer**
   - For shortest path: validate using path reconstruction
   - For MST: ensure exactly |V|-1 edges
   - For both: verify total cost calculation

3. **Watch for special cases**
   - Disconnected graphs
   - Negative weights (not allowed in Dijkstra's)
   - Self-loops or parallel edges

### Implementation Details to Know

1. **Dijkstra's Implementation Variants**
   - Array-based: O(V²) time complexity
   - Min-heap: O(E log V) time complexity
   - Know which one you're expected to trace through

2. **Prim's Implementation Variants**
   - Similar to Dijkstra's with array: O(V²)
   - Similar to Dijkstra's with min-heap: O(E log V)
   - Know which variant to use based on graph density

3. **Kruskal's Implementation Details**
   - Sorting edges: O(E log E) or O(E log V)
   - Union-Find operations: O(E·α(V)) where α is the inverse Ackermann function
   - Overall complexity: O(E log V)

## Practice Strategy

When practicing these algorithms:

1. **Start with small graphs**
   - 4-6 vertices
   - 5-10 edges
   - Various weight distributions

2. **Use different starting vertices**
   - For Dijkstra's and Prim's, results depend on the starting vertex
   - Practice with different starting points to gain confidence

3. **Time yourself**
   - Exam questions often have time pressure
   - Practice completing traces efficiently

4. **Create your own examples**
   - Design graphs with specific challenges
   - Verify your solutions manually

5. **Compare algorithms**
   - Run both Prim's and Kruskal's on the same graph
   - Observe how they build the MST differently
   - Understand when one might be preferable over the other

By following this structured approach to graph algorithm questions, you'll be well-prepared to tackle them on your CSCI 33500 final exam. Remember to show all your work, as partial credit is often awarded for correct steps even if the final answer is incorrect.
