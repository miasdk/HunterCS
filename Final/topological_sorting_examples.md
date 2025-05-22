# Topological Sorting - Complete Exam Examples

## Example 1: Basic Topological Sort

**Problem**: Perform a topological sort on the following directed acyclic graph (DAG).

```
Graph:
    A → B → D
    ↓   ↓   ↓
    C → E → F
        ↓
        G
```

**Adjacency List Representation**:
- A: [B, C]
- B: [D, E]
- C: [E]
- D: [F]
- E: [F, G]
- F: []
- G: []

### DFS-Based Solution:

**Algorithm**:
1. Perform DFS starting from any unvisited vertex
2. When finishing a vertex (all descendants processed), add to result
3. Reverse the result to get topological order

**Step-by-Step Execution**:

```
DFS Traversal:
Start A: A → B → D (finish D) → E → F (finish F) → G (finish G) 
         → (finish E) → (finish B) → C → E (already visited)
         → (finish C) → (finish A)

Finish Order: D, F, G, E, B, C, A
Topological Sort: A, C, B, E, G, F, D
```

**Alternative Valid Orders**:
- A, B, C, E, D, G, F
- A, B, D, C, E, F, G
- A, C, B, D, E, G, F

**Key Point**: Multiple valid topological orderings exist for most DAGs.

---

## Example 2: Kahn's Algorithm (BFS-Based)

**Problem**: Use Kahn's algorithm to find a topological ordering of the same graph.

```
Graph:
    A → B → D
    ↓   ↓   ↓
    C → E → F
        ↓
        G
```

### Step-by-Step Solution:

**Step 1**: Calculate in-degrees
- A: 0, B: 1, C: 1, D: 1, E: 2, F: 2, G: 1

**Step 2**: Initialize queue with zero in-degree vertices
- Queue: [A]

**Step 3**: Process vertices

| Step | Process | Remove Edges | Update In-degrees | Queue After | Result |
|------|---------|--------------|-------------------|-------------|--------|
| 1 | A | A→B, A→C | B:0, C:0 | [B, C] | [A] |
| 2 | B | B→D, B→E | D:0, E:1 | [C, D] | [A, B] |
| 3 | C | C→E | E:0 | [D, E] | [A, B, C] |
| 4 | D | D→F | F:1 | [E] | [A, B, C, D] |
| 5 | E | E→F, E→G | F:0, G:0 | [F, G] | [A, B, C, D, E] |
| 6 | F | (no edges) | - | [G] | [A, B, C, D, E, F] |
| 7 | G | (no edges) | - | [] | [A, B, C, D, E, F, G] |

**Final Topological Order**: A, B, C, D, E, F, G

---

## Example 3: Cycle Detection

**Question**: Explain how topological sorting can detect cycles in a directed graph. [6 pts]

### Solution:

**Key Principle**: A directed graph has a topological ordering if and only if it's a DAG (Directed Acyclic Graph).

**Cycle Detection Methods**:

1. **Using Kahn's Algorithm**:
   ```cpp
   bool hasCycle(vector<vector<int>>& adj) {
       int n = adj.size();
       vector<int> indegree(n, 0);
       
       // Calculate in-degrees
       for (int u = 0; u < n; u++) {
           for (int v : adj[u]) {
               indegree[v]++;
           }
       }
       
       queue<int> q;
       for (int i = 0; i < n; i++) {
           if (indegree[i] == 0) {
               q.push(i);
           }
       }
       
       int processed = 0;
       while (!q.empty()) {
           int u = q.front();
           q.pop();
           processed++;
           
           for (int v : adj[u]) {
               indegree[v]--;
               if (indegree[v] == 0) {
                   q.push(v);
               }
           }
       }
       
       return processed != n;  // Cycle exists if not all vertices processed
   }
   ```

2. **Using DFS with States**:
   ```cpp
   enum State { WHITE, GRAY, BLACK };
   
   bool hasCycleDFS(vector<vector<int>>& adj) {
       int n = adj.size();
       vector<State> state(n, WHITE);
       
       function<bool(int)> dfs = [&](int u) -> bool {
           state[u] = GRAY;
           
           for (int v : adj[u]) {
               if (state[v] == GRAY) return true;  // Back edge = cycle
               if (state[v] == WHITE && dfs(v)) return true;
           }
           
           state[u] = BLACK;
           return false;
       };
       
       for (int i = 0; i < n; i++) {
           if (state[i] == WHITE && dfs(i)) {
               return true;
           }
       }
       return false;
   }
   ```

**Example of Graph with Cycle**:
```
A → B → C
↑       ↓
D ← ← ← E
```
Cycle: A → B → C → E → D → A (no topological ordering exists)

---

## Example 4: Course Prerequisites Problem

**Question**: You are given n courses numbered 0 to n-1. Some courses have prerequisites. Return a valid order to take all courses, or detect if it's impossible. [12 pts]

**Input**: 
- numCourses = 4
- prerequisites = [[1,0], [2,0], [3,1], [3,2]]

**Graph Representation**:
```
0 → 1 → 3
↓       ↑
2 → → → 
```

### Complete Solution:

```cpp
class CourseSchedule {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        // Build adjacency list and calculate in-degrees
        vector<vector<int>> adj(numCourses);
        vector<int> indegree(numCourses, 0);
        
        for (auto& prereq : prerequisites) {
            int course = prereq[0];
            int prerequisite = prereq[1];
            adj[prerequisite].push_back(course);
            indegree[course]++;
        }
        
        // Kahn's algorithm
        queue<int> q;
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        
        vector<int> result;
        while (!q.empty()) {
            int course = q.front();
            q.pop();
            result.push_back(course);
            
            // Remove edges and update in-degrees
            for (int nextCourse : adj[course]) {
                indegree[nextCourse]--;
                if (indegree[nextCourse] == 0) {
                    q.push(nextCourse);
                }
            }
        }
        
        // Check if all courses can be taken
        if (result.size() != numCourses) {
            return {};  // Cycle detected - impossible to complete
        }
        
        return result;
    }
};
```

**Step-by-Step for Example**:
1. **In-degrees**: [0, 1, 1, 2]
2. **Queue**: [0]
3. **Process 0**: Remove 0→1, 0→2. In-degrees: [-, 0, 0, 2]. Queue: [1, 2]
4. **Process 1**: Remove 1→3. In-degrees: [-, -, 0, 1]. Queue: [2]
5. **Process 2**: Remove 2→3. In-degrees: [-, -, -, 0]. Queue: [3]
6. **Process 3**: No outgoing edges. Queue: []

**Result**: [0, 1, 2, 3] or [0, 2, 1, 3] (both valid)

**Time Complexity**: O(V + E)
**Space Complexity**: O(V + E)

---

## Example 5: Topological Sort Applications

**Question**: Give three real-world applications of topological sorting and explain why topological ordering is necessary. [9 pts]

### Solution:

1. **Build Systems / Dependency Resolution**:
   - **Problem**: Compile source files in correct order when files depend on others
   - **Why topological sort**: Must compile dependencies before dependents
   - **Example**: If A.cpp includes B.h, must process B.h before A.cpp
   ```
   main.cpp → utils.h → types.h
              ↓
           math.cpp
   ```
   **Order**: types.h, utils.h, math.cpp, main.cpp

2. **Task Scheduling with Dependencies**:
   - **Problem**: Schedule tasks where some tasks must complete before others start
   - **Why topological sort**: Ensures prerequisite tasks finish first
   - **Example**: Software project tasks
   ```
   Design → Code → Test → Deploy
            ↓      ↑
         Document → Review
   ```
   **Order**: Design, Code, Document, Review, Test, Deploy

3. **Course Planning / Academic Prerequisites**:
   - **Problem**: Plan course sequence respecting prerequisite requirements
   - **Why topological sort**: Can't take advanced courses before foundations
   - **Example**: Computer Science curriculum
   ```
   CS101 → CS201 → CS301
           ↓       ↑
        CS202 → CS302
   ```
   **Order**: CS101, CS201, CS202, CS301, CS302

**Additional Applications**:
- **Package Management**: Installing software packages with dependencies
- **Excel Formula Evaluation**: Calculate cells in dependency order
- **Makefile Processing**: Build targets in correct dependency order

---

## Example 6: DFS vs BFS Implementation Comparison

**Question**: Compare DFS-based and BFS-based (Kahn's) topological sorting algorithms. [8 pts]

### Detailed Comparison:

| Aspect | DFS-Based | BFS-Based (Kahn's) |
|--------|-----------|-------------------|
| **Algorithm** | Recursive DFS with finish-time ordering | Queue-based with in-degree counting |
| **Time Complexity** | O(V + E) | O(V + E) |
| **Space Complexity** | O(V) recursion stack | O(V) queue space |
| **Cycle Detection** | Natural (back edges) | Natural (remaining vertices) |
| **Implementation** | Recursive, elegant | Iterative, explicit |
| **Memory Usage** | Stack overflow risk for deep graphs | Constant extra space |
| **Output Order** | Reverse finish time | Process order |

**DFS Implementation**:
```cpp
void topologicalSortDFS(int v, vector<vector<int>>& adj, 
                       vector<bool>& visited, stack<int>& result) {
    visited[v] = true;
    
    for (int u : adj[v]) {
        if (!visited[u]) {
            topologicalSortDFS(u, adj, visited, result);
        }
    }
    
    result.push(v);  // Add after processing all descendants
}
```

**Kahn's Implementation**:
```cpp
vector<int> topologicalSortKahn(vector<vector<int>>& adj) {
    int n = adj.size();
    vector<int> indegree(n, 0);
    
    // Calculate in-degrees
    for (int u = 0; u < n; u++) {
        for (int v : adj[u]) {
            indegree[v]++;
        }
    }
    
    queue<int> q;
    for (int i = 0; i < n; i++) {
        if (indegree[i] == 0) q.push(i);
    }
    
    vector<int> result;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        result.push_back(u);
        
        for (int v : adj[u]) {
            if (--indegree[v] == 0) {
                q.push(v);
            }
        }
    }
    
    return result;
}
```

**When to Use Each**:
- **DFS**: When you need lexicographically smallest result or working with recursion-friendly problems
- **Kahn's**: When you need to detect cycles explicitly or prefer iterative solutions