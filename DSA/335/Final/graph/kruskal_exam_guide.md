# Kruskal's Algorithm - Exam Step-by-Step Guide

## Exam Format (Tabular Method)

| Edge | Weight | Action | Reason |
|------|--------|--------|--------|
| A-B  | 1      | Accept | No cycle |
| B-C  | 2      | Accept | No cycle |
| A-C  | 3      | Reject | Creates cycle A-B-C-A |

## Step-by-Step Process

### Step 1: List All Edges by Weight
**CRITICAL**: Always sort edges by weight (ascending order) first!

Example from exam:
```
Original edges: (1,3):4, (3,4):1, (1,4):2, (6,7):2, (2,4):3, etc.
Sorted by weight:
(3,4): weight 1
(1,4): weight 2  
(6,7): weight 2
(2,4): weight 3
...
```

### Step 2: Process Each Edge in Order

For each edge in weight order:
1. **Check if adding this edge creates a cycle**
2. **If NO cycle → ACCEPT (add to MST)**
3. **If cycle → REJECT**
4. **Stop when you have V-1 edges** (where V = number of vertices)

## Cycle Detection Method (Used in Exams)

### Simple Component Tracking
- Keep track of which vertices are connected
- If an edge connects two vertices already in the same component → **CYCLE**
- If an edge connects vertices in different components → **NO CYCLE**

### Example Walkthrough

**Graph with vertices {1,2,3,4,5,6,7}**

**Sorted edges:**
1. (3,4): weight 1
2. (1,4): weight 2
3. (6,7): weight 2
4. (2,4): weight 3
5. (3,6): weight 3
6. (1,3): weight 4
7. (4,7): weight 4

**Processing:**

| Step | Edge | Weight | Action | Reason | Connected Components |
|------|------|--------|--------|--------|---------------------|
| 1 | (3,4) | 1 | **Accept** | First edge, no cycle | {3,4}, {1}, {2}, {5}, {6}, {7} |
| 2 | (1,4) | 2 | **Accept** | Connects different components | {1,3,4}, {2}, {5}, {6}, {7} |
| 3 | (6,7) | 2 | **Accept** | Connects different components | {1,3,4}, {2}, {5}, {6,7} |
| 4 | (2,4) | 3 | **Accept** | Connects different components | {1,2,3,4}, {5}, {6,7} |
| 5 | (3,6) | 3 | **Accept** | Connects different components | {1,2,3,4,6,7}, {5} |
| 6 | (1,3) | 4 | **Reject** | 1 and 3 already connected | {1,2,3,4,6,7}, {5} |

**Stop here**: We have 6 edges accepted, which is V-1 = 7-1 = 6 ✓

## Visual Cycle Check Method

Draw the MST as you build it:
1. Start with isolated vertices
2. Add each accepted edge
3. Before adding new edge, check if it connects vertices already connected by existing path

## Key Exam Points

### Always Remember:
1. **Sort edges by weight first**
2. **Process in order of increasing weight**
3. **Accept if no cycle, reject if cycle**
4. **Stop at V-1 edges**
5. **Show your work in table format**

### Common Mistakes:
- Forgetting to sort edges by weight
- Not stopping after V-1 edges
- Incorrectly detecting cycles
- Adding edges out of weight order

## Final Answer Format

**MST Edges**: List all accepted edges
**Total Weight**: Sum of all accepted edge weights

Example:
- **MST Edges**: (3,4), (1,4), (6,7), (2,4), (3,6)
- **Total Weight**: 1 + 2 + 2 + 3 + 3 = 11

## Exam Success Tips

1. **Work systematically** - don't skip steps
2. **Draw the graph** if it helps visualize cycles
3. **Keep track of connected components** clearly
4. **Double-check edge weights** from the original graph
5. **Count edges** - must have exactly V-1 in final MST