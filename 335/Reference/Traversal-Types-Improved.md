# Tree and Graph Traversal: Complete Guide

## 📋 Table of Contents
- [Overview](#overview)
- [Tree Traversals](#tree-traversals)
- [Graph Traversals](#graph-traversals)
- [Implementation Examples](#implementation-examples)
- [Traversal Applications](#traversal-applications)
- [Performance Comparison](#performance-comparison)
- [Practice Problems](#practice-problems)
- [Quick Reference](#quick-reference)

---

## Overview

**Traversal** is the process of visiting all nodes in a data structure (tree or graph) in a systematic way. Different traversal orders serve different purposes and have different applications.

### **Key Concepts**
- **Visit Order**: The sequence in which nodes are processed
- **Recursive vs Iterative**: Implementation approaches
- **Space Complexity**: Memory usage during traversal
- **Time Complexity**: Always O(n) where n is number of nodes

---

## Tree Traversals

### **Binary Tree Node Structure**
```cpp
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
```

### **1. Inorder Traversal (Left → Root → Right)**
**Order**: Left subtree → Current node → Right subtree
**Applications**: Binary search trees (gives sorted order)

```cpp
// Recursive implementation
void inorderTraversal(TreeNode* root) {
    if (root == nullptr) return;
    
    inorderTraversal(root->left);   // Visit left subtree
    cout << root->val << " ";       // Visit current node
    inorderTraversal(root->right);  // Visit right subtree
}

// Iterative implementation using stack
vector<int> inorderTraversalIterative(TreeNode* root) {
    vector<int> result;
    stack<TreeNode*> st;
    TreeNode* current = root;
    
    while (current != nullptr || !st.empty()) {
        // Go to leftmost node
        while (current != nullptr) {
            st.push(current);
            current = current->left;
        }
        
        // Process current node
        current = st.top();
        st.pop();
        result.push_back(current->val);
        
        // Go to right subtree
        current = current->right;
    }
    
    return result;
}
```

**Example Tree**:
```
       1
      / \
     2   3
    / \
   4   5
```
**Inorder Result**: 4 → 2 → 5 → 1 → 3

### **2. Preorder Traversal (Root → Left → Right)**
**Order**: Current node → Left subtree → Right subtree
**Applications**: Copying trees, prefix expressions

```cpp
// Recursive implementation
void preorderTraversal(TreeNode* root) {
    if (root == nullptr) return;
    
    cout << root->val << " ";       // Visit current node first
    preorderTraversal(root->left);  // Visit left subtree
    preorderTraversal(root->right); // Visit right subtree
}

// Iterative implementation using stack
vector<int> preorderTraversalIterative(TreeNode* root) {
    vector<int> result;
    if (root == nullptr) return result;
    
    stack<TreeNode*> st;
    st.push(root);
    
    while (!st.empty()) {
        TreeNode* current = st.top();
        st.pop();
        
        result.push_back(current->val);
        
        // Push right child first (so left is processed first)
        if (current->right) st.push(current->right);
        if (current->left) st.push(current->left);
    }
    
    return result;
}
```

**Preorder Result**: 1 → 2 → 4 → 5 → 3

### **3. Postorder Traversal (Left → Right → Root)**
**Order**: Left subtree → Right subtree → Current node
**Applications**: Deleting trees, postfix expressions

```cpp
// Recursive implementation
void postorderTraversal(TreeNode* root) {
    if (root == nullptr) return;
    
    postorderTraversal(root->left);  // Visit left subtree
    postorderTraversal(root->right); // Visit right subtree
    cout << root->val << " ";        // Visit current node last
}

// Iterative implementation using two stacks
vector<int> postorderTraversalIterative(TreeNode* root) {
    vector<int> result;
    if (root == nullptr) return result;
    
    stack<TreeNode*> st1, st2;
    st1.push(root);
    
    while (!st1.empty()) {
        TreeNode* current = st1.top();
        st1.pop();
        st2.push(current);
        
        if (current->left) st1.push(current->left);
        if (current->right) st1.push(current->right);
    }
    
    while (!st2.empty()) {
        result.push_back(st2.top()->val);
        st2.pop();
    }
    
    return result;
}
```

**Postorder Result**: 4 → 5 → 2 → 3 → 1

### **4. Level Order Traversal (Breadth-First)**
**Order**: Level by level, left to right
**Applications**: Finding shortest paths, breadth-first search

```cpp
// Iterative implementation using queue
vector<vector<int>> levelOrderTraversal(TreeNode* root) {
    vector<vector<int>> result;
    if (root == nullptr) return result;
    
    queue<TreeNode*> q;
    q.push(root);
    
    while (!q.empty()) {
        int levelSize = q.size();
        vector<int> currentLevel;
        
        for (int i = 0; i < levelSize; i++) {
            TreeNode* current = q.front();
            q.pop();
            
            currentLevel.push_back(current->val);
            
            if (current->left) q.push(current->left);
            if (current->right) q.push(current->right);
        }
        
        result.push_back(currentLevel);
    }
    
    return result;
}
```

**Level Order Result**: [1] → [2, 3] → [4, 5]

---

## Graph Traversals

### **Graph Representation**
```cpp
// Adjacency list representation
vector<vector<int>> graph;  // graph[i] contains neighbors of node i

// Or using adjacency matrix
vector<vector<int>> adjMatrix;  // adjMatrix[i][j] = 1 if edge exists
```

### **1. Depth-First Search (DFS)**
**Strategy**: Explore as far as possible along each branch before backtracking
**Applications**: Topological sorting, connected components, cycle detection

```cpp
// Recursive DFS
void dfsRecursive(vector<vector<int>>& graph, vector<bool>& visited, int node) {
    visited[node] = true;
    cout << node << " ";
    
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            dfsRecursive(graph, visited, neighbor);
        }
    }
}

// Iterative DFS using stack
void dfsIterative(vector<vector<int>>& graph, int start) {
    vector<bool> visited(graph.size(), false);
    stack<int> st;
    
    st.push(start);
    visited[start] = true;
    
    while (!st.empty()) {
        int current = st.top();
        st.pop();
        
        cout << current << " ";
        
        for (int neighbor : graph[current]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                st.push(neighbor);
            }
        }
    }
}
```

### **2. Breadth-First Search (BFS)**
**Strategy**: Explore all neighbors at current depth before moving to next level
**Applications**: Shortest path, minimum spanning tree, level-by-level processing

```cpp
// Iterative BFS using queue
void bfs(vector<vector<int>>& graph, int start) {
    vector<bool> visited(graph.size(), false);
    queue<int> q;
    
    q.push(start);
    visited[start] = true;
    
    while (!q.empty()) {
        int current = q.front();
        q.pop();
        
        cout << current << " ";
        
        for (int neighbor : graph[current]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
}

// BFS with level tracking
vector<vector<int>> bfsWithLevels(vector<vector<int>>& graph, int start) {
    vector<vector<int>> levels;
    vector<bool> visited(graph.size(), false);
    queue<int> q;
    
    q.push(start);
    visited[start] = true;
    
    while (!q.empty()) {
        int levelSize = q.size();
        vector<int> currentLevel;
        
        for (int i = 0; i < levelSize; i++) {
            int current = q.front();
            q.pop();
            
            currentLevel.push_back(current);
            
            for (int neighbor : graph[current]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
        
        levels.push_back(currentLevel);
    }
    
    return levels;
}
```

---

## Implementation Examples

### **Complete Tree Traversal Example**
```cpp
class TreeTraversal {
public:
    // Inorder traversal
    vector<int> inorder(TreeNode* root) {
        vector<int> result;
        inorderHelper(root, result);
        return result;
    }
    
    void inorderHelper(TreeNode* root, vector<int>& result) {
        if (root == nullptr) return;
        inorderHelper(root->left, result);
        result.push_back(root->val);
        inorderHelper(root->right, result);
    }
    
    // Preorder traversal
    vector<int> preorder(TreeNode* root) {
        vector<int> result;
        preorderHelper(root, result);
        return result;
    }
    
    void preorderHelper(TreeNode* root, vector<int>& result) {
        if (root == nullptr) return;
        result.push_back(root->val);
        preorderHelper(root->left, result);
        preorderHelper(root->right, result);
    }
    
    // Postorder traversal
    vector<int> postorder(TreeNode* root) {
        vector<int> result;
        postorderHelper(root, result);
        return result;
    }
    
    void postorderHelper(TreeNode* root, vector<int>& result) {
        if (root == nullptr) return;
        postorderHelper(root->left, result);
        postorderHelper(root->right, result);
        result.push_back(root->val);
    }
    
    // Level order traversal
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (root == nullptr) return result;
        
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
            vector<int> currentLevel;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode* current = q.front();
                q.pop();
                
                currentLevel.push_back(current->val);
                
                if (current->left) q.push(current->left);
                if (current->right) q.push(current->right);
            }
            
            result.push_back(currentLevel);
        }
        
        return result;
    }
};
```

### **Complete Graph Traversal Example**
```cpp
class GraphTraversal {
public:
    // DFS traversal
    vector<int> dfs(vector<vector<int>>& graph, int start) {
        vector<int> result;
        vector<bool> visited(graph.size(), false);
        dfsHelper(graph, start, visited, result);
        return result;
    }
    
    void dfsHelper(vector<vector<int>>& graph, int node, 
                   vector<bool>& visited, vector<int>& result) {
        visited[node] = true;
        result.push_back(node);
        
        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                dfsHelper(graph, neighbor, visited, result);
            }
        }
    }
    
    // BFS traversal
    vector<int> bfs(vector<vector<int>>& graph, int start) {
        vector<int> result;
        vector<bool> visited(graph.size(), false);
        queue<int> q;
        
        q.push(start);
        visited[start] = true;
        
        while (!q.empty()) {
            int current = q.front();
            q.pop();
            result.push_back(current);
            
            for (int neighbor : graph[current]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
        
        return result;
    }
    
    // Find connected components using DFS
    vector<vector<int>> findConnectedComponents(vector<vector<int>>& graph) {
        vector<vector<int>> components;
        vector<bool> visited(graph.size(), false);
        
        for (int i = 0; i < graph.size(); i++) {
            if (!visited[i]) {
                vector<int> component;
                dfsHelper(graph, i, visited, component);
                components.push_back(component);
            }
        }
        
        return components;
    }
};
```

---

## Traversal Applications

### **Tree Applications**

| Traversal | Applications |
|-----------|--------------|
| **Inorder** | Binary search tree validation, sorted output |
| **Preorder** | Tree serialization, prefix expressions |
| **Postorder** | Tree deletion, postfix expressions |
| **Level Order** | Breadth-first processing, level-based operations |

### **Graph Applications**

| Traversal | Applications |
|-----------|--------------|
| **DFS** | Topological sorting, cycle detection, connected components |
| **BFS** | Shortest path, minimum spanning tree, level-based processing |

### **Specific Examples**

#### **1. Binary Search Tree Validation**
```cpp
bool isValidBST(TreeNode* root) {
    vector<int> inorder;
    inorderHelper(root, inorder);
    
    for (int i = 1; i < inorder.size(); i++) {
        if (inorder[i] <= inorder[i-1]) return false;
    }
    return true;
}
```

#### **2. Tree Serialization**
```cpp
string serialize(TreeNode* root) {
    if (root == nullptr) return "null";
    return to_string(root->val) + "," + 
           serialize(root->left) + "," + 
           serialize(root->right);
}
```

#### **3. Topological Sorting**
```cpp
vector<int> topologicalSort(vector<vector<int>>& graph) {
    vector<int> result;
    vector<bool> visited(graph.size(), false);
    vector<bool> recStack(graph.size(), false);
    
    for (int i = 0; i < graph.size(); i++) {
        if (!visited[i]) {
            if (dfsTopo(graph, i, visited, recStack, result)) {
                return {}; // Cycle detected
            }
        }
    }
    
    reverse(result.begin(), result.end());
    return result;
}
```

---

## Performance Comparison

### **Time and Space Complexity**

| Traversal | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| **Tree Inorder** | O(n) | O(h) | h = tree height |
| **Tree Preorder** | O(n) | O(h) | h = tree height |
| **Tree Postorder** | O(n) | O(h) | h = tree height |
| **Tree Level Order** | O(n) | O(w) | w = max width |
| **Graph DFS** | O(V + E) | O(V) | V = vertices, E = edges |
| **Graph BFS** | O(V + E) | O(V) | V = vertices, E = edges |

### **Memory Usage Comparison**

| Traversal | Recursive Stack | Iterative Stack/Queue |
|-----------|----------------|----------------------|
| **Tree Traversals** | O(h) | O(h) |
| **Graph DFS** | O(V) | O(V) |
| **Graph BFS** | O(V) | O(V) |

---

## Practice Problems

### **Problem 1: Binary Tree Inorder Traversal**
```cpp
vector<int> inorderTraversal(TreeNode* root) {
    vector<int> result;
    stack<TreeNode*> st;
    TreeNode* current = root;
    
    while (current != nullptr || !st.empty()) {
        while (current != nullptr) {
            st.push(current);
            current = current->left;
        }
        
        current = st.top();
        st.pop();
        result.push_back(current->val);
        current = current->right;
    }
    
    return result;
}
```

### **Problem 2: Level Order Traversal**
```cpp
vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result;
    if (root == nullptr) return result;
    
    queue<TreeNode*> q;
    q.push(root);
    
    while (!q.empty()) {
        int levelSize = q.size();
        vector<int> currentLevel;
        
        for (int i = 0; i < levelSize; i++) {
            TreeNode* current = q.front();
            q.pop();
            
            currentLevel.push_back(current->val);
            
            if (current->left) q.push(current->left);
            if (current->right) q.push(current->right);
        }
        
        result.push_back(currentLevel);
    }
    
    return result;
}
```

### **Problem 3: Number of Islands (DFS)**
```cpp
void dfs(vector<vector<char>>& grid, int i, int j) {
    if (i < 0 || i >= grid.size() || j < 0 || j >= grid[0].size() || grid[i][j] == '0') {
        return;
    }
    
    grid[i][j] = '0'; // Mark as visited
    
    dfs(grid, i+1, j);
    dfs(grid, i-1, j);
    dfs(grid, i, j+1);
    dfs(grid, i, j-1);
}

int numIslands(vector<vector<char>>& grid) {
    int count = 0;
    
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[0].size(); j++) {
            if (grid[i][j] == '1') {
                dfs(grid, i, j);
                count++;
            }
        }
    }
    
    return count;
}
```

---

## Quick Reference

### **Tree Traversal Orders**
- **Inorder**: Left → Root → Right
- **Preorder**: Root → Left → Right
- **Postorder**: Left → Right → Root
- **Level Order**: Level by level, left to right

### **Graph Traversal Strategies**
- **DFS**: Explore deep first, use stack/recursion
- **BFS**: Explore wide first, use queue

### **Implementation Patterns**
- **Recursive**: Simpler code, uses call stack
- **Iterative**: More control, explicit stack/queue

### **Common Applications**
- **Inorder**: BST validation, sorted output
- **Preorder**: Tree serialization, prefix expressions
- **Postorder**: Tree deletion, postfix expressions
- **Level Order**: Breadth-first processing
- **DFS**: Topological sort, cycle detection
- **BFS**: Shortest path, level-based processing

### **Exam Tips**
1. **Know the visit order** for each traversal type
2. **Understand when to use each traversal**
3. **Be able to implement both recursive and iterative versions**
4. **Remember the space complexity** (especially for deep trees)
5. **Practice drawing traversal orders** on sample trees

---

*Master these traversal techniques and you'll be able to process any tree or graph efficiently!* 