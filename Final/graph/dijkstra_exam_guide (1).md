# Dijkstra's Algorithm - CORRECTED Exam Step-by-Step Guide

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

## CORRECTED Example Walkthrough

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

**CAREFUL EDGE READING**:
- 2→4: weight **2** (not 4!)
- 2→5: weight **4** 
- 2→6: weight **3**

**Step 1** (Initial - vertex 2 is source):
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
- Check adjacents from graph: v4 (edge weight **2**), v5 (edge weight **4**), v6 (edge weight **3**)
- v4: 0 + 2 = 2 < ∞ → Update dv=2, pv=2
- v5: 0 + 4 = 4 < ∞ → Update dv=4, pv=2  
- v6: 0 + 3 = 3 < ∞ → Update dv=3, pv=2

| v | known | dv | pv |
|---|-------|----|----|
| 1 | F     | ∞  | 0  |
| 2 | T     | 0  | 0  |
| 3 | F     | ∞  | 0  |
| 4 | F     | 2  | 2  |
| 5 | F     | 4  | 2  |
| 6 | F     | 3  | 2  |

**Step 3** (Process vertex 4 - smallest unknown distance = 2):
- Mark v4 as known = T
- Check adjacents: v3 (edge weight **3**), v1 (edge weight **1**)
- v3: 2 + 3 = 5 < ∞ → Update dv=5, pv=4
- v1: 2 + 1 = 3 < ∞ → Update dv=3, pv=4

| v | known | dv | pv |
|---|-------|----|----|
| 1 | F     | 3  | 4  |
| 2 | T     | 0  | 0  |
| 3 | F     | 5  | 4  |
| 4 | T     | 2  | 2  |
| 5 | F     | 4  | 2  |
| 6 | F     | 3  | 2  |

**Step 4** (Process vertex 1 or 6 - both distance = 3, choose v1):
- Mark v1 as known = T
- Check adjacents: v3 (edge weight **1**), v5 (edge weight **2**)
- v3: 3 + 1 = 4 < 5 → Update dv=4, pv=1
- v5: 3 + 2 = 5 > 4, no change

| v | known | dv | pv |
|---|-------|----|----|
| 1 | T     | 3  | 4  |
| 2 | T     | 0  | 0  |
| 3 | F     | 4  | 1  |
| 4 | T     | 2  | 2  |
| 5 | F     | 4  | 2  |
| 6 | F     | 3  | 2  |

**Step 5** (Process vertex 6 - distance = 3):
- Mark v6 as known = T
- Check adjacents: v5 (edge weight **2**)
- v5: 3 + 2 = 5 > 4, no change

| v | known | dv | pv |
|---|-------|----|----|
| 1 | T     | 3  | 4  |
| 2 | T     | 0  | 0  |
| 3 | F     | 4  | 1  |
| 4 | T     | 2  | 2  |
| 5 | F     | 4  | 2  |
| 6 | T     | 3  | 2  |

**Step 6** (Process vertex 3 or 5 - both distance = 4, choose v3):
- Mark v3 as known = T
- Check adjacents: already processed

| v | known | dv | pv |
|---|-------|----|----|
| 1 | T     | 3  | 4  |
| 2 | T     | 0  | 0  |
| 3 | T     | 4  | 1  |
| 4 | T     | 2  | 2  |
| 5 | F     | 4  | 2  |
| 6 | T     | 3  | 2  |

**Step 7** (Process vertex 5 - distance = 4):
- Mark v5 as known = T
- All vertices now processed

**FINAL DISTANCES FROM VERTEX 2**:
- To vertex 1: **3** (path: 2→4→1)
- To vertex 3: **4** (path: 2→4→1→3)  
- To vertex 4: **2** (path: 2→4)
- To vertex 5: **4** (path: 2→5)
- To vertex 6: **3** (path: 2→6)

## CRITICAL EXAM REMINDERS

1. **READ EDGE WEIGHTS CAREFULLY** - This is the #1 source of errors
2. **Double-check your graph reading** before starting
3. **Write down edge weights** if the graph is complex
4. **Verify your arithmetic** at each step
5. **Show ALL work** in the table format

## Common Exam Mistakes to Avoid

1. **Misreading edge weights** (like I initially did!)
2. **Forgetting to mark vertex as known**
3. **Not updating both dv AND pv**
4. **Processing vertices in wrong order**
5. **Arithmetic errors in distance calculations**

## Exam Success Strategy

1. **Trace the graph carefully** - spend 30 seconds identifying all edges
2. **Work systematically** - don't rush
3. **Check each calculation** before moving to next step
4. **Use the table format exactly** as shown
5. **Verify final answer makes sense**

Thank you for catching my error - this kind of attention to detail is exactly what you need for exam success!