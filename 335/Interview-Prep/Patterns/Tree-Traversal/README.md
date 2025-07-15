# Tree Traversal Pattern - Interview Guide

## 🎯 Pattern Recognition
**Use tree traversals when you need:**
- Visit all nodes in specific order
- Search/find elements in tree
- Validate tree properties
- Calculate tree statistics
- Transform tree structure

## 📋 Core Templates

### Basic Tree Node
```cpp
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
```

### DFS Traversals
```cpp
// Preorder: Root -> Left -> Right
void preorder(TreeNode* root, vector<int>& result) {
    if (!root) return;
    result.push_back(root->val);    // Process root
    preorder(root->left, result);   // Process left
    preorder(root->right, result);  // Process right
}

// Inorder: Left -> Root -> Right (sorted order for BST)
void inorder(TreeNode* root, vector<int>& result) {
    if (!root) return;
    inorder(root->left, result);    // Process left
    result.push_back(root->val);    // Process root
    inorder(root->right, result);   // Process right
}

// Postorder: Left -> Right -> Root
void postorder(TreeNode* root, vector<int>& result) {
    if (!root) return;
    postorder(root->left, result);  // Process left
    postorder(root->right, result); // Process right
    result.push_back(root->val);    // Process root
}
```

### BFS Traversal (Level Order)
```cpp
vector<vector<int>> levelOrder(TreeNode* root) {
    if (!root) return {};
    
    vector<vector<int>> result;
    queue<TreeNode*> q;
    q.push(root);
    
    while (!q.empty()) {
        int levelSize = q.size();
        vector<int> currentLevel;
        
        for (int i = 0; i < levelSize; i++) {
            TreeNode* node = q.front();
            q.pop();
            currentLevel.push_back(node->val);
            
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        result.push_back(currentLevel);
    }
    return result;
}
```

## 🔥 Must-Know Problems

### 1. Maximum Depth (Easy) ⭐⭐⭐
```cpp
int maxDepth(TreeNode* root) {
    if (!root) return 0;
    return 1 + max(maxDepth(root->left), maxDepth(root->right));
}
```

### 2. Same Tree (Easy) ⭐⭐⭐
```cpp
bool isSameTree(TreeNode* p, TreeNode* q) {
    if (!p && !q) return true;
    if (!p || !q) return false;
    return (p->val == q->val) && 
           isSameTree(p->left, q->left) && 
           isSameTree(p->right, q->right);
}
```

### 3. Symmetric Tree (Easy) ⭐⭐
```cpp
bool isSymmetric(TreeNode* root) {
    return isMirror(root, root);
}

bool isMirror(TreeNode* t1, TreeNode* t2) {
    if (!t1 && !t2) return true;
    if (!t1 || !t2) return false;
    return (t1->val == t2->val) && 
           isMirror(t1->right, t2->left) && 
           isMirror(t1->left, t2->right);
}
```

### 4. Path Sum (Easy) ⭐⭐
```cpp
bool hasPathSum(TreeNode* root, int targetSum) {
    if (!root) return false;
    if (!root->left && !root->right) {
        return root->val == targetSum;
    }
    return hasPathSum(root->left, targetSum - root->val) ||
           hasPathSum(root->right, targetSum - root->val);
}
```

### 5. Validate BST (Medium) ⭐⭐⭐
```cpp
bool isValidBST(TreeNode* root) {
    return validate(root, LONG_MIN, LONG_MAX);
}

bool validate(TreeNode* node, long minVal, long maxVal) {
    if (!node) return true;
    if (node->val <= minVal || node->val >= maxVal) return false;
    return validate(node->left, minVal, node->val) &&
           validate(node->right, node->val, maxVal);
}
```

## 💡 Key Patterns

### Pattern 1: Recursive DFS
**When**: Need to process entire tree, calculate properties
**Template**: Base case + recursive calls
```cpp
int dfs(TreeNode* root) {
    if (!root) return base_case;
    int left = dfs(root->left);
    int right = dfs(root->right);
    return combine(root->val, left, right);
}
```

### Pattern 2: Level Order BFS
**When**: Process by levels, find shortest path
**Template**: Queue + level-by-level processing

### Pattern 3: BST Properties
**When**: Binary search tree problems
**Template**: Use inorder traversal or validation with bounds

### Pattern 4: Path Problems
**When**: Find paths from root to leaf
**Template**: DFS with running sum/path

## ⚡ Interview Tips

### Time/Space Complexity
- **DFS**: O(n) time, O(h) space (h = height)
- **BFS**: O(n) time, O(w) space (w = max width)

### When to Use Each Traversal
- **Preorder**: Copy tree, expression parsing
- **Inorder**: BST sorted output, validation
- **Postorder**: Delete tree, calculate size/height
- **Level order**: Print by levels, shortest path

### Common Mistakes
- Forgetting null checks
- Wrong base case in recursion
- Not handling single node trees
- Confusing left/right in symmetric problems

### Interview Tips
- Always ask about tree properties (BST? complete? balanced?)
- Draw examples for complex problems
- Consider both recursive and iterative solutions
- Handle edge cases (null, single node, skewed tree)

## 🎪 Practice Progression

### Week 1: Master These (Easy)
1. Maximum Depth ⭐⭐⭐
2. Same Tree ⭐⭐⭐  
3. Invert Binary Tree ⭐⭐
4. Path Sum ⭐⭐

### Week 2: Add These (Easy-Medium)
1. Symmetric Tree ⭐⭐
2. Level Order Traversal ⭐⭐
3. Minimum Depth ⭐⭐
4. Sum of Left Leaves ⭐⭐

### Week 3: Challenge (Medium)
1. Validate BST ⭐⭐⭐
2. Path Sum II ⭐⭐⭐
3. Lowest Common Ancestor ⭐⭐⭐
4. Binary Tree Right Side View ⭐⭐

## 📚 Related Files
- **Code Examples**: `../../../Code-Library/By-Topic/Trees/`
- **Theory**: `../../../Reference/Trees.md`
- **Templates**: `../../../Code-Library/Templates/tree_traversal_template.cpp` 