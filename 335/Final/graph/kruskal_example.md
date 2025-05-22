# Kruskal's Algorithm - Tabular Method Example

## Sample Graph
```
    (A)----2----(B)
     |           |
     3           1
     |           |
    (D)----4----(C)
     |           |
     5           6
     |           |
    (E)----7----(F)
```

## Step 1: List and Sort All Edges

| Edge | Weight |
|------|--------|
| B-C  | 1      |
| A-B  | 2      |
| A-D  | 3      |
| D-C  | 4      |
| D-E  | 5      |
| C-F  | 6      |
| E-F  | 7      |

## Step 2: Apply Kruskal's Algorithm

| Step | Edge | Weight | Action | Reason | MST Edges So Far |
|------|------|--------|--------|--------|------------------|
| 1    | B-C  | 1      | **Accept** | No cycle (first edge) | {B-C} |
| 2    | A-B  | 2      | **Accept** | No cycle | {B-C, A-B} |
| 3    | A-D  | 3      | **Accept** | No cycle | {B-C, A-B, A-D} |
| 4    | D-C  | 4      | **Reject** | Creates cycle A-B-C-D-A | {B-C, A-B, A-D} |
| 5    | D-E  | 5      | **Accept** | No cycle | {B-C, A-B, A-D, D-E} |
| 6    | C-F  | 6      | **Accept** | No cycle (5 edges = V-1, STOP) | {B-C, A-B, A-D, D-E, C-F} |

## Final MST
- **Edges**: A-B, B-C, A-D, D-E, C-F
- **Total Weight**: 2 + 1 + 3 + 5 + 6 = **17**

## Cycle Detection Methods

### Method 1: Union-Find (Disjoint Set)
- Each vertex starts in its own set
- When adding an edge, check if vertices are in the same set
- If same set → cycle exists
- If different sets → no cycle, union the sets

### Method 2: Visual/Component Tracking
- Keep track of connected components
- If an edge connects two vertices already in the same component → cycle
- If edge connects different components → no cycle

## Key Points to Remember

1. **Always sort edges first** by weight (ascending)
2. **Process edges in order** of increasing weight
3. **Stop when you have V-1 edges** (where V = number of vertices)
4. **Reject any edge that creates a cycle**
5. **Total weight = sum of accepted edge weights**

## Practice Tips

1. Draw the graph as you build the MST
2. Keep track of which vertices are connected
3. When in doubt about cycles, trace the path between vertices
4. Remember: MST for V vertices has exactly V-1 edges
