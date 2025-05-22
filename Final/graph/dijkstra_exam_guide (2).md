# Dijkstra's Algorithm - CORRECT Exam Step-by-Step Guide

## Table Format (ALWAYS Used on Exams)

| v | known | dv | pv |
|---|-------|----|----|
| v1| F     | ∞  | 0  |
| v2| F     | 0  | 0  |
| v3| F     | ∞  | 0  |
| v4| F     | ∞  | 0  |
| v5| F     | ∞  | 0  |
| v6| F     | ∞  | 0  |

## THE EXACT GRAPH YOU PROVIDED:

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

**EDGE LIST FROM THIS GRAPH:**
- 4↔3: weight 3
- 4↔2: weight 2  
- 3↔5: weight 1
- 2↔5: weight 4
- 2↔6: weight 3
- 5↔1: weight 2
- 6↔1: weight 2

**Starting from vertex 2:**

**STEP 1** (Initial):
| v | known | dv | pv |
|---|-------|----|----|
| 1 | F     | ∞  | 0  |
| 2 | F     | 0  | 0  |
| 3 | F     | ∞  | 0  |
| 4 | F     | ∞  | 0  |
| 5 | F     | ∞  | 0  |
| 6 | F     | ∞  | 0  |

**STEP 2** (Process vertex 2 - distance = 0):
- Mark v2 as known = T
- Adjacent to vertex 2: v4 (weight 2), v5 (weight 4), v6 (weight 3)
- v4: 0 + 2 = 2 → Update dv=2, pv=2
- v5: 0 + 4 = 4 → Update dv=4, pv=2
- v6: 0 + 3 = 3 → Update dv=3, pv=2

| v | known | dv | pv |
|---|-------|----|----|
| 1 | F     | ∞  | 0  |
| 2 | T     | 0  | 0  |
| 3 | F     | ∞  | 0  |
| 4 | F     | 2  | 2  |
| 5 | F     | 4  | 2  |
| 6 | F     | 3  | 2  |

**STEP 3** (Process vertex 4 - smallest unknown distance = 2):
- Mark v4 as known = T
- Adjacent to vertex 4: v3 (weight 3), v2 (already known)
- v3: 2 + 3 = 5 → Update dv=5, pv=4

| v | known | dv | pv |
|---|-------|----|----|
| 1 | F     | ∞  | 0  |
| 2 | T     | 0  | 0  |
| 3 | F     | 5  | 4  |
| 4 | T     | 2  | 2  |
| 5 | F     | 4  | 2  |
| 6 | F     | 3  | 2  |

**STEP 4** (Process vertex 6 - smallest unknown distance = 3):
- Mark v6 as known = T
- Adjacent to vertex 6: v1 (weight 2), v2 (already known)
- v1: 3 + 2 = 5 → Update dv=5, pv=6

| v | known | dv | pv |
|---|-------|----|----|
| 1 | F     | 5  | 6  |
| 2 | T     | 0  | 0  |
| 3 | F     | 5  | 4  |
| 4 | T     | 2  | 2  |
| 5 | F     | 4  | 2  |
| 6 | T     | 3  | 2  |

**STEP 5** (Process vertex 5 - smallest unknown distance = 4):
- Mark v5 as known = T
- Adjacent to vertex 5: v3 (weight 1), v1 (weight 2), v2 (already known)
- v3: 4 + 1 = 5, same as current distance, no change
- v1: 4 + 2 = 6 > 5, no change

| v | known | dv | pv |
|---|-------|----|----|
| 1 | F     | 5  | 6  |
| 2 | T     | 0  | 0  |
| 3 | F     | 5  | 4  |
| 4 | T     | 2  | 2  |
| 5 | T     | 4  | 2  |
| 6 | T     | 3  | 2  |

**STEP 6** (Process vertex 1 or 3 - both distance = 5, choose v1):
- Mark v1 as known = T
- Adjacent to vertex 1: v5 (already known), v6 (already known)
- No updates needed

| v | known | dv | pv |
|---|-------|----|----|
| 1 | T     | 5  | 6  |
| 2 | T     | 0  | 0  |
| 3 | F     | 5  | 4  |
| 4 | T     | 2  | 2  |
| 5 | T     | 4  | 2  |
| 6 | T     | 3  | 2  |

**STEP 7** (Process vertex 3 - distance = 5):
- Mark v3 as known = T
- All vertices processed

**FINAL DISTANCES FROM VERTEX 2:**
- To vertex 1: **5** (path: 2→6→1)
- To vertex 3: **5** (path: 2→4→3)
- To vertex 4: **2** (path: 2→4)
- To vertex 5: **4** (path: 2→5)
- To vertex 6: **3** (path: 2→6)

## Key Exam Points

1. **Read the graph exactly as given**
2. **Trace adjacencies carefully**
3. **Show all work in table format**
4. **Always pick smallest unknown distance**
5. **Update both dv AND pv when distance improves**