# Minimum Vertex Cover - Complete Exam Guide

## 1. Core Definitions (Must Know for Exam)

### Vertex Cover
**Definition**: A vertex cover of a graph G = (V, E) is a subset S ⊆ V such that **every edge** in E has **at least one endpoint** in S.

**Key Point**: If you remove all vertices in the vertex cover, **no edges remain** in the graph.

### Minimum Vertex Cover
**Definition**: A vertex cover with the **smallest possible number of vertices**.

**Example**:
```
Graph: A—B—C
       |   |
       D—E—F

Possible vertex covers:
- {A, B, C, D, E, F} ✓ (size 6)
- {B, D, E} ✓ (size 3) 
- {A, C, E} ✓ (size 3)
- {B, E} ✗ (edge D-E not covered)

Minimum vertex cover: {B, D, E} or {A, C, E} (size 3)
```

## 2. Problem Classification

### NP-Hard Problem
- **No polynomial-time algorithm** known for optimal solution
- **Exponential time** required for exact solutions on large graphs
- **Approximation algorithms** used in practice

### Practical Implications
- **Small graphs**: Can solve exactly
- **Large graphs**: Must use heuristics
- **Real-world**: Accept "good enough" solutions

## 3. Greedy Heuristic Algorithm

### Algorithm Steps
```
1. WHILE graph has edges:
   a. Find vertex with HIGHEST DEGREE
   b. Add vertex to cover set
   c. Remove vertex and ALL its edges
2. RETURN cover set
```

### Why This Works
- **High-degree vertices** cover many edges at once
- **Greedy choice** reduces problem size quickly
- **Simple to implement** and understand

### Approximation Ratio
- **Guarantee**: Solution ≤ 2 × optimal size
- **Never worse** than twice the minimum
- **Often much better** in practice

## 4. Step-by-Step Example

### Given Graph:
```
    A----B----C
    |    |    |
    D----E----F
```

**Edges**: A-B, B-C, A-D, B-E, C-F, D-E, E-F

### Execution:

**Step 1**: Calculate degrees
- A: 2, B: 3, C: 2, D: 2, E: 3, F: 2
- **Highest degree**: B and E (both 3), choose B

**Step 2**: Add B to cover, remove B and its edges
- **Cover**: {B}
- **Remaining edges**: A-D, C-F, D-E, E-F
- **New degrees**: A: 1, C: 1, D: 2, E: 2, F: 2

**Step 3**: Choose highest degree vertex
- **Highest degree**: D, E, or F (all 2), choose E

**Step 4**: Add E to cover, remove E and its edges  
- **Cover**: {B, E}
- **Remaining edges**: A-D, C-F
- **New degrees**: A: 1, C: 1, D: 1, F: 1

**Step 5**: Choose any vertex with edges
- Choose A, add to cover, remove A-D edge
- **Cover**: {B, E, A}
- **Remaining edges**: C-F

**Step 6**: Choose vertex for remaining edge
- Choose C, add to cover, remove C-F edge
- **Cover**: {B, E, A, C}
- **No edges remain**

**Final Answer**: Vertex cover = {A, B, C, E} (size 4)

## 5. Implementation Concepts

### Data Structures
```cpp
// Graph representation
std::unordered_map<std::string, std::unordered_set<std::string>> graph;

// Vertex cover result
std::unordered_set<std::string> cover;
```

### Key Operations
1. **Find max degree vertex**: O(V) scan
2. **Remove vertex and edges**: O(degree) updates  
3. **Check if edges remain**: O(V) check

### Time Complexity
- **Overall**: O(V² + E) where V = vertices, E = edges
- **Each iteration**: O(V) to find max degree
- **V iterations maximum**: Each adds one vertex to cover

## 6. Real-World Applications

### Airport Security (From Project)
- **Vertices**: Airports (JFK, LGA, ORD)
- **Edges**: Flights between airports
- **Goal**: Minimum airports with TSA agents to monitor all flights

### Other Applications
- **Network Security**: Monitor key network nodes
- **Resource Allocation**: Minimum service centers
- **Biological Networks**: Key proteins in interactions
- **Circuit Testing**: Minimum test points

## 7. Exam Question Types

### Type 1: Execute Algorithm
**Given a graph, find vertex cover using greedy algorithm**

**Format**:
```
Graph: [visual representation]
Show each step: vertex chosen, edges removed, remaining graph
Final answer: vertex cover set and size
```

### Type 2: Verify Solution
**Is the given set a valid vertex cover?**

**Method**: Check that every edge has ≥1 endpoint in the set

### Type 3: Compare Solutions
**Which vertex cover is smaller? Is it minimum?**

**Key**: Smaller size is better, but proving minimum requires exhaustive check

### Type 4: Definition Questions
- "What is a vertex cover?"
- "Why is minimum vertex cover NP-hard?"
- "What is the approximation ratio of greedy algorithm?"

## 8. Common Exam Mistakes

### Mistake 1: Wrong Definition
❌ "Cover all vertices" 
✅ "Cover all **edges**"

### Mistake 2: Missing Edges
❌ Forgetting to check all edges are covered
✅ Systematic verification of each edge

### Mistake 3: Degree Calculation
❌ Not updating degrees after vertex removal
✅ Recalculate degrees after each step

### Mistake 4: Stopping Early
❌ Stopping when no high-degree vertices remain
✅ Continue until **no edges** remain

## 9. Exam Tips

### Before Starting
1. **List all edges** clearly
2. **Count vertices** to estimate answer size
3. **Draw the graph** if not provided

### During Execution
1. **Show degree calculations** at each step
2. **Clearly mark removed vertices/edges**
3. **Update remaining graph** after each step
4. **Verify no edges remain** at the end

### Final Check
1. **Count cover size**
2. **Verify every edge has ≥1 endpoint in cover**
3. **State approximation guarantee** if asked

## 10. Quick Reference

### Algorithm Template
```
Cover = {}
WHILE edges exist:
    v = vertex with max degree
    Cover = Cover ∪ {v}
    Remove v and all incident edges
RETURN Cover
```

### Key Facts
- **Problem Type**: NP-hard optimization
- **Approximation Ratio**: ≤ 2 × optimal
- **Time Complexity**: O(V² + E)
- **Space Complexity**: O(V + E)

### Verification Method
```
For each edge (u,v):
    IF u ∉ Cover AND v ∉ Cover:
        RETURN "Not a valid cover"
RETURN "Valid cover"
```

## 11. Practice Strategy

1. **Master the definition** - can you explain vertex cover clearly?
2. **Practice small examples** - 4-6 vertex graphs
3. **Trace the algorithm** - step by step execution
4. **Verify solutions** - check that all edges are covered
5. **Understand approximation** - why greedy works, what it guarantees

### Sample Practice Graph
```
    1----2
    |\  /|
    | \/ |
    |/  \|
    3----4

Execute greedy algorithm:
- Calculate degrees
- Choose highest degree vertex
- Remove and update
- Repeat until done
```

**Remember**: The goal is to cover ALL edges with the FEWEST vertices possible!