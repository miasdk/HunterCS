# Algorithm Patterns Quick Reference
*Essential Patterns for Technical Interview Success*

## 🎯 **Pattern Recognition Guide**

### **How to Use This Guide**
1. **Read the problem** 
2. **Identify keywords** that hint at patterns
3. **Match to pattern** and apply template
4. **Implement and optimize**

---

## 📝 **Array & Hash Table Patterns**

### **1. Two Pointers**
**When to Use**: Array is sorted, looking for pairs/triplets, palindrome checking
**Keywords**: "sorted array", "two sum", "palindrome", "remove duplicates"

```cpp
// Template: Two pointers from ends
int left = 0, right = arr.size() - 1;
while (left < right) {
    if (condition_met) {
        // Process and move both
        left++; right--;
    } else if (need_smaller) {
        right--;
    } else {
        left++;
    }
}
```

**Classic Problems**: Two Sum II, Valid Palindrome, Container With Most Water

### **2. Sliding Window**
**When to Use**: Subarray/substring problems, "contiguous", "window size k"
**Keywords**: "substring", "subarray", "consecutive", "window", "k elements"

```cpp
// Template: Fixed size window
int windowSum = 0;
for (int i = 0; i < k; i++) windowSum += arr[i];  // Initial window
int maxSum = windowSum;

for (int i = k; i < arr.size(); i++) {
    windowSum += arr[i] - arr[i-k];  // Slide window
    maxSum = max(maxSum, windowSum);
}
```

**Classic Problems**: Longest Substring Without Repeating, Maximum Sum Subarray

### **3. Hash Table Lookup**
**When to Use**: Need O(1) lookup, complement search, frequency counting
**Keywords**: "two sum", "anagram", "frequency", "count", "seen before"

```cpp
// Template: Complement search
unordered_map<int, int> seen;
for (int i = 0; i < nums.size(); i++) {
    int complement = target - nums[i];
    if (seen.find(complement) != seen.end()) {
        return {seen[complement], i};
    }
    seen[nums[i]] = i;
}
```

**Classic Problems**: Two Sum, Anagram Detection, Contains Duplicate

---

## 🌳 **Tree Patterns**

### **4. Tree Traversal (DFS)**
**When to Use**: Process all nodes, path problems, tree properties
**Keywords**: "traverse", "path sum", "depth", "validate"

```cpp
// Template: Recursive DFS
void dfs(TreeNode* node) {
    if (!node) return;  // Base case
    
    // Process current node
    process(node);
    
    // Recurse on children
    dfs(node->left);
    dfs(node->right);
}
```

**Variations**: Preorder, Inorder, Postorder, Path Sum

### **5. Tree BFS (Level Order)**
**When to Use**: Level-by-level processing, shortest path in tree
**Keywords**: "level order", "level by level", "zigzag", "width"

```cpp
// Template: BFS with queue
queue<TreeNode*> q;
q.push(root);

while (!q.empty()) {
    int levelSize = q.size();
    for (int i = 0; i < levelSize; i++) {
        TreeNode* node = q.front(); q.pop();
        process(node);
        
        if (node->left) q.push(node->left);
        if (node->right) q.push(node->right);
    }
}
```

**Classic Problems**: Level Order Traversal, Zigzag Traversal, Right Side View

---

## 📊 **Graph Patterns**

### **6. Graph DFS**
**When to Use**: Connected components, cycle detection, topological sort
**Keywords**: "connected", "islands", "cycle", "path exists"

```cpp
// Template: Graph DFS
vector<bool> visited(n, false);

void dfs(int node, vector<vector<int>>& graph) {
    visited[node] = true;
    process(node);
    
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor, graph);
        }
    }
}
```

**Classic Problems**: Number of Islands, Course Schedule (cycle detection)

### **7. Graph BFS**
**When to Use**: Shortest path, minimum steps, level-based problems
**Keywords**: "shortest path", "minimum steps", "level", "nearest"

```cpp
// Template: Graph BFS
queue<int> q;
vector<int> distance(n, -1);
q.push(start);
distance[start] = 0;

while (!q.empty()) {
    int node = q.front(); q.pop();
    
    for (int neighbor : graph[node]) {
        if (distance[neighbor] == -1) {
            distance[neighbor] = distance[node] + 1;
            q.push(neighbor);
        }
    }
}
```

**Classic Problems**: Shortest Path in Unweighted Graph, Word Ladder

---

## 🔄 **Dynamic Programming Patterns**

### **8. 1D DP**
**When to Use**: Sequence problems, optimal substructure, "maximum/minimum"
**Keywords**: "maximum sum", "climbing stairs", "house robber", "decode ways"

```cpp
// Template: 1D DP
vector<int> dp(n);
dp[0] = base_case;

for (int i = 1; i < n; i++) {
    dp[i] = max(dp[i-1] + arr[i], dp[i-2] + arr[i]);  // Example recurrence
}
```

**Classic Problems**: House Robber, Climbing Stairs, Maximum Subarray

### **9. 2D DP**
**When to Use**: Grid problems, two sequences, "unique paths"
**Keywords**: "grid", "matrix", "two strings", "paths", "edit distance"

```cpp
// Template: 2D DP
vector<vector<int>> dp(m, vector<int>(n));
// Initialize base cases
dp[0][0] = initial_value;

for (int i = 1; i < m; i++) {
    for (int j = 1; j < n; j++) {
        dp[i][j] = dp[i-1][j] + dp[i][j-1];  // Example recurrence
    }
}
```

**Classic Problems**: Unique Paths, Edit Distance, Longest Common Subsequence

---

## 🔍 **Search & Sort Patterns**

### **10. Binary Search**
**When to Use**: Sorted array, "search for target", finding boundaries
**Keywords**: "sorted", "search", "find first/last", "peak element"

```cpp
// Template: Binary search
int left = 0, right = arr.size() - 1;
while (left <= right) {
    int mid = left + (right - left) / 2;
    if (arr[mid] == target) return mid;
    else if (arr[mid] < target) left = mid + 1;
    else right = mid - 1;
}
```

**Classic Problems**: Search in Rotated Array, Find Peak Element

### **11. Quickselect**
**When to Use**: Find kth element, "kth largest/smallest"
**Keywords**: "kth largest", "kth smallest", "median"

```cpp
// Template: Quickselect
int quickselect(vector<int>& nums, int k) {
    int left = 0, right = nums.size() - 1;
    while (left < right) {
        int pivot = partition(nums, left, right);
        if (pivot == k) return nums[k];
        else if (pivot < k) left = pivot + 1;
        else right = pivot - 1;
    }
    return nums[k];
}
```

**Classic Problems**: Kth Largest Element, Top K Frequent Elements

---

## 🔄 **Backtracking Patterns**

### **12. Backtracking**
**When to Use**: Generate all possibilities, "all combinations", "permutations"
**Keywords**: "all", "generate", "combinations", "permutations", "subsets"

```cpp
// Template: Backtracking
void backtrack(vector<int>& current, vector<vector<int>>& result, /* other params */) {
    if (is_complete(current)) {
        result.push_back(current);
        return;
    }
    
    for (int choice : possible_choices) {
        current.push_back(choice);      // Make choice
        backtrack(current, result);     // Recurse
        current.pop_back();             // Undo choice
    }
}
```

**Classic Problems**: Subsets, Permutations, N-Queens

---

## 🎯 **Quick Pattern Identification**

### **Problem Keywords → Pattern**

| Keywords | Pattern | Complexity |
|----------|---------|------------|
| "two sum", "pair" + sorted | Two Pointers | O(n) |
| "substring", "subarray", "window" | Sliding Window | O(n) |
| "frequency", "anagram", "seen before" | Hash Table | O(n) |
| "path", "traverse", "depth" | Tree/Graph DFS | O(V+E) |
| "shortest", "minimum steps", "level" | BFS | O(V+E) |
| "maximum/minimum", sequence | 1D DP | O(n) |
| "grid", "two strings" | 2D DP | O(mn) |
| "sorted", "search", "find" | Binary Search | O(log n) |
| "kth largest/smallest" | Heap/Quickselect | O(n log k) |
| "all combinations", "generate" | Backtracking | O(2ⁿ) |

---

## ⚡ **Interview Strategy**

### **1. Pattern Recognition (30 seconds)**
- Read problem statement
- Identify key words/constraints
- Match to known pattern

### **2. Template Application (2 minutes)**
- Start with pattern template
- Adapt to specific problem requirements
- Consider edge cases

### **3. Optimization (if time permits)**
- Can we reduce time complexity?
- Can we reduce space complexity?
- Are there special cases to handle?

**💡 Remember**: Most interview problems are variations of these core patterns. Master the templates, then adapt them! 