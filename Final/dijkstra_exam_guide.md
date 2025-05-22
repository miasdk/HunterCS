# Dijkstra's Algorithm - Exam Step-by-Step Guide

## Table Format (ALWAYS Used on Exams)

| v | known | dv | pv |
|---|-------|----|----|
| v1| F     | ∞  | 0  |
| v2| F     | 0  | 0  |
| v3| F     | ∞  | 0  |
| v4| F     | ∞  | 0  |
| v5| F     | ∞  | 0  |
| v6| F     | ∞  | 0  |

## Column Meanings
- **v**: Vertex name
- **known**: T/F - whether vertex has been processed
- **dv**: Distance from source vertex
- **pv**: Previous vertex (predecessor)

## Step-by-Step Process

### Initial Setup
1. **Set source vertex distance to 0**
2. **All other distances to ∞**
3. **All known = F**
4. **All pv = 0 (or source vertex)**

### For Each Step:
1. **Find unknown vertex with smallest distance**
2. **Mark it as known (T)**
3. **For each adjacent unknown vertex:**
   - Calculate new distance = current vertex distance + edge weight
   - If new distance < current distance: UPDATE both dv and pv
   - If new distance ≥ current distance: DON'T CHANGE

### Example Walkthrough

**Graph**: Vertex 2 is source
```
    (4)----3----(3)
     |           |
     2           1
     |           |
    (2)----4----(5)
     |           |
     3           2
     |           |
    (6)----2----(1)
```

**Step 1** (Initial):
| v | known | dv | pv |
|---|-------|----|----|
| 1 | F     | ∞  | 0  |
| 2 | F     | 0  | 0  |
| 3 | F     | ∞  | 0  |
| 4 | F     | ∞  | 0  |
| 5 | F     | ∞  | 0  |
| 6 | F     | ∞  | 0  |

**Step 2** (Process vertex 2 - smallest unknown distance = 0):
- Mark v2 as known = T
- Check adjacents: v4 (edge weight 4), v5 (edge weight 5)
- v4: 0 + 4 = 4 < ∞ → Update dv=4, pv=2
- v5: 0 + 5 = 5 < ∞ → Update dv=5, pv=2

| v | known | dv | pv |
|---|-------|----|----|
| 1 | F     | ∞  | 0  |
| 2 | T     | 0  | 0  |
| 3 | F     | ∞  | 0  |
| 4 | F     | 4  | 2  |
| 5 | F     | 5  | 2  |
| 6 | F     | ∞  | 0  |

**Step 3** (Process vertex 4 - smallest unknown distance = 4):
- Mark v4 as known = T
- Check adjacents: v3 (edge weight 3), v2 (already known)
- v3: 4 + 3 = 7 < ∞ → Update dv=7, pv=4

## Common Exam Mistakes to Avoid

1. **DON'T update distances to known vertices**
2. **DON'T forget to mark vertex as known when processing**
3. **ALWAYS pick unknown vertex with smallest distance**
4. **UPDATE both dv AND pv when distance improves**
5. **Use the correct edge weights from the graph**

## Final Answer Format
- **Shortest path length**: Final dv value for target vertex
- **Actual path**: Trace backwards using pv values

## Key Points for Exam Success
- Work systematically through each step
- Double-check edge weights from graph
- Mark vertices as known immediately when processing
- Only update distances if the new path is shorter
- Show all work in the table format provided