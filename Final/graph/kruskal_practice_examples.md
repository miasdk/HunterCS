# Kruskal's Algorithm - Exam Practice Problems

## Practice Problem 1 (6 points)
**Given the following graph, show each step of Kruskal's algorithm to find the minimum spanning tree. List each edge considered, its weight, and whether it's added or not. The algorithm should stop as soon as it completes the MST.**

```
Graph:
      A----5----B
      |\        |
      | 2       4
      |  \      |
      3   C----1-D
      |    \    |
      6     7   8
      |      \  |
      E----9---F
```

**Edge** | **Weight** | **Action**
---------|------------|------------
         |            |
         |            |
         |            |
         |            |
         |            |
         |            |
         |            |

---

## Practice Problem 2 (6 points)
**Given the following graph, show each step of Kruskal's algorithm to find the minimum spanning tree. List each edge considered, its weight, and whether it's added or not. The algorithm should stop as soon as it completes the MST.**

```
Graph:
    1----3----2
    |\        |
    | 4       3
    |  \      |
    2   5----1-6
    |    \    |
    1     2   4
    |      \  |
    3----5---4
```

**Edge** | **Weight** | **Action**
---------|------------|------------
         |            |
         |            |
         |            |
         |            |
         |            |
         |            |

---

## Practice Problem 3 (6 points)
**Given the following graph, show each step of Kruskal's algorithm to find the minimum spanning tree. List each edge considered, its weight, and whether it's added or not. The algorithm should stop as soon as it completes the MST.**

```
Graph:
     V1----6----V2----4----V3
     |\         |          |
     | 8        5          2
     |  \       |          |
     1   V4----3-V5----7----V6
     |    \     |     /
     2     9    1    6
     |      \   |   /
     V7----4---V8
```

**Edge** | **Weight** | **Action**
---------|------------|------------
         |            |
         |            |
         |            |
         |            |
         |            |
         |            |
         |            |
         |            |

---

## Practice Problem 4 (6 points)
**Given the following graph, show each step of Kruskal's algorithm to find the minimum spanning tree. List each edge considered, its weight, and whether it's added or not. The algorithm should stop as soon as it completes the MST.**

```
Graph:
    A----3----B----2----C
    |         |         |
    4         1         5
    |         |         |
    D----6----E----3----F
    |         |         |
    2         4         1
    |         |         |
    G----5----H----7----I
```

**Edge** | **Weight** | **Action**
---------|------------|------------
         |            |
         |            |
         |            |
         |            |
         |            |
         |            |
         |            |
         |            |
         |            |

---

## Practice Problem 5 (6 points)
**Given the following graph, show each step of Kruskal's algorithm to find the minimum spanning tree. List each edge considered, its weight, and whether it's added or not. The algorithm should stop as soon as it completes the MST.**

```
Graph:
         2
        /|\
       1 | 3
      /  |  \
     5---4---6
      \ /|\ /
       8 | 7
        \|/
         3
```

**Edge weights:**
- 2-5: 1, 2-4: 2, 2-6: 3
- 5-4: 4, 4-6: 7, 5-8: 8
- 4-8: 5, 4-3: 6, 6-3: 9
- 8-3: 10

**Edge** | **Weight** | **Action**
---------|------------|------------
         |            |
         |            |
         |            |
         |            |
         |            |
         |            |
         |            |

---

## Practice Problem 6 (6 points)
**Given the following graph, show each step of Kruskal's algorithm to find the minimum spanning tree. List each edge considered, its weight, and whether it's added or not. The algorithm should stop as soon as it completes the MST.**

```
Graph:
    X----4----Y----6----Z
    |\        |        /|
    | 3       2       5 |
    |  \      |      /  |
    7   W----1-V----8   |
    |    \    |    /    |
    8     9   3   7     4
    |      \  |  /      |
    P----2---Q----6----R
```

**Edge** | **Weight** | **Action**
---------|------------|------------
         |            |
         |            |
         |            |
         |            |
         |            |
         |            |
         |            |
         |            |
         |            |

---

# ANSWER KEY

## Problem 1 Solution:
**Edge** | **Weight** | **Action**
---------|------------|------------
C-D      | 1          | Accept
A-C      | 2          | Accept
A-D      | 3          | Reject
B-D      | 4          | Accept
A-B      | 5          | Reject
A-E      | 6          | Accept
C-F      | 7          | Accept

**Total MST Weight: 20**

---

## Problem 2 Solution:
**Edge** | **Weight** | **Action**
---------|------------|------------
5-6      | 1          | Accept
3-1      | 1          | Accept
5-4      | 2          | Accept
1-2      | 3          | Accept
2-6      | 3          | Accept

**Total MST Weight: 10**

---

## Problem 3 Solution:
**Edge** | **Weight** | **Action**
---------|------------|------------
V5-V8    | 1          | Accept
V1-V7    | 1          | Accept
V3-V6    | 2          | Accept
V1-V7    | 2          | Reject
V4-V5    | 3          | Accept
V7-V8    | 4          | Accept
V2-V5    | 5          | Accept
V1-V2    | 6          | Accept

**Total MST Weight: 18**

---

## Problem 4 Solution:
**Edge** | **Weight** | **Action**
---------|------------|------------
B-E      | 1          | Accept
F-I      | 1          | Accept
B-C      | 2          | Accept
D-G      | 2          | Accept
A-B      | 3          | Accept
E-F      | 3          | Accept
A-D      | 4          | Accept
E-H      | 4          | Reject

**Total MST Weight: 16**

---

## Problem 5 Solution:
**Edge** | **Weight** | **Action**
---------|------------|------------
2-5      | 1          | Accept
2-4      | 2          | Accept
2-6      | 3          | Accept
5-4      | 4          | Reject
4-8      | 5          | Accept
4-3      | 6          | Accept

**Total MST Weight: 17**

---

## Problem 6 Solution:
**Edge** | **Weight** | **Action**
---------|------------|------------
W-V      | 1          | Accept
P-Q      | 2          | Accept
Y-V      | 2          | Accept
X-W      | 3          | Accept
V-Q      | 3          | Accept
X-Y      | 4          | Reject
R-Z      | 4          | Accept
Z-V      | 5          | Reject

**Total MST Weight: 15**