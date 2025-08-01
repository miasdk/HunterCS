/**
 * Tree Traversal Templates for Interview Success
 * All essential tree patterns and traversal techniques
 */

#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <climits>
using namespace std;

// Tree Node Definition
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// ========================================
// DFS TRAVERSALS (RECURSIVE)
// ========================================

// Preorder: Root -> Left -> Right
void preorderRecursive(TreeNode* root, vector<int>& result) {
    if (!root) return;
    result.push_back(root->val);        // Process root
    preorderRecursive(root->left, result);   // Process left subtree
    preorderRecursive(root->right, result);  // Process right subtree
}

// Inorder: Left -> Root -> Right (sorted for BST)
void inorderRecursive(TreeNode* root, vector<int>& result) {
    if (!root) return;
    inorderRecursive(root->left, result);    // Process left subtree
    result.push_back(root->val);        // Process root
    inorderRecursive(root->right, result);   // Process right subtree
}

// Postorder: Left -> Right -> Root
void postorderRecursive(TreeNode* root, vector<int>& result) {
    if (!root) return;
    postorderRecursive(root->left, result);  // Process left subtree
    postorderRecursive(root->right, result); // Process right subtree
    result.push_back(root->val);        // Process root
}

// ========================================
// DFS TRAVERSALS (ITERATIVE)
// ========================================

vector<int> preorderIterative(TreeNode* root) {
    vector<int> result;
    if (!root) return result;
    
    stack<TreeNode*> stk;
    stk.push(root);
    
    while (!stk.empty()) {
        TreeNode* node = stk.top();
        stk.pop();
        result.push_back(node->val);
        
        // Push right first (stack is LIFO)
        if (node->right) stk.push(node->right);
        if (node->left) stk.push(node->left);
    }
    return result;
}

vector<int> inorderIterative(TreeNode* root) {
    vector<int> result;
    stack<TreeNode*> stk;
    TreeNode* current = root;
    
    while (current || !stk.empty()) {
        // Go to leftmost node
        while (current) {
            stk.push(current);
            current = current->left;
        }
        
        // Process current node
        current = stk.top();
        stk.pop();
        result.push_back(current->val);
        
        // Go to right subtree
        current = current->right;
    }
    return result;
}

// ========================================
// BFS TRAVERSAL (LEVEL ORDER)
// ========================================

vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result;
    if (!root) return result;
    
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

// ========================================
// COMMON TREE PROBLEMS
// ========================================

// Maximum depth of binary tree
int maxDepth(TreeNode* root) {
    if (!root) return 0;
    return 1 + max(maxDepth(root->left), maxDepth(root->right));
}

// Check if two trees are identical
bool isSameTree(TreeNode* p, TreeNode* q) {
    if (!p && !q) return true;
    if (!p || !q) return false;
    return (p->val == q->val) && 
           isSameTree(p->left, q->left) && 
           isSameTree(p->right, q->right);
}

// Check if tree is symmetric
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

// Path sum from root to leaf
bool hasPathSum(TreeNode* root, int targetSum) {
    if (!root) return false;
    if (!root->left && !root->right) {
        return root->val == targetSum;
    }
    return hasPathSum(root->left, targetSum - root->val) ||
           hasPathSum(root->right, targetSum - root->val);
}

// Validate binary search tree
bool isValidBST(TreeNode* root) {
    return validateBST(root, LONG_MIN, LONG_MAX);
}

bool validateBST(TreeNode* node, long minVal, long maxVal) {
    if (!node) return true;
    if (node->val <= minVal || node->val >= maxVal) return false;
    return validateBST(node->left, minVal, node->val) &&
           validateBST(node->right, node->val, maxVal);
}

// Invert binary tree
TreeNode* invertTree(TreeNode* root) {
    if (!root) return nullptr;
    
    swap(root->left, root->right);
    invertTree(root->left);
    invertTree(root->right);
    
    return root;
}

// ========================================
// UTILITY FUNCTIONS
// ========================================

// Create tree from level order array (null = -1)
TreeNode* createTree(vector<int>& vals, int index = 0) {
    if (index >= vals.size() || vals[index] == -1) return nullptr;
    
    TreeNode* root = new TreeNode(vals[index]);
    root->left = createTree(vals, 2 * index + 1);
    root->right = createTree(vals, 2 * index + 2);
    return root;
}

// Print tree in level order
void printTree(TreeNode* root) {
    if (!root) {
        cout << "Empty tree\n";
        return;
    }
    
    queue<TreeNode*> q;
    q.push(root);
    
    while (!q.empty()) {
        int levelSize = q.size();
        for (int i = 0; i < levelSize; i++) {
            TreeNode* node = q.front();
            q.pop();
            
            if (node) {
                cout << node->val << " ";
                q.push(node->left);
                q.push(node->right);
            } else {
                cout << "null ";
            }
        }
        cout << "\n";
    }
}

// ========================================
// QUICK REFERENCE
// ========================================
/*
TREE TRAVERSAL PATTERNS:

1. PREORDER (Root->Left->Right):
   - Use when: copying tree, expression parsing
   - Template: process root, then recurse left, then right

2. INORDER (Left->Root->Right):
   - Use when: BST sorted output, validation
   - Template: recurse left, process root, recurse right

3. POSTORDER (Left->Right->Root):
   - Use when: deleting tree, calculating height/size
   - Template: recurse left, recurse right, process root

4. LEVEL ORDER (BFS):
   - Use when: level-by-level processing, shortest path
   - Template: queue with level-size tracking

COMMON PATTERNS:
- Tree validation: Use bounds checking
- Path problems: DFS with running sum
- Level problems: BFS with level tracking
- BST problems: Use inorder properties

COMPLEXITY:
- Time: O(n) for all traversals
- Space: O(h) for DFS, O(w) for BFS (h=height, w=width)

INTERVIEW TIPS:
- Always check for null nodes
- Ask about tree properties (BST? balanced? complete?)
- Consider both recursive and iterative solutions
- Draw examples for complex problems
*/ 