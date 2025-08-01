/**
 * 100. Same Tree - C++ Interview Solution
 * 
 * Problem: Given two binary trees, check if they are identical.
 * 
 * Interview Approach:
 * 1. Recursive DFS (Depth-First Search)
 * 2. Base cases first
 * 3. Recursive case: check current nodes, then left and right subtrees
 */

#include <iostream>
using namespace std;

/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        /*
         * INTERVIEW PRESENTATION SCRIPT:
         * 
         * "For this problem, I'll use a recursive approach with DFS. 
         * The key insight is that two trees are identical if:
         * 1. Their root values are equal
         * 2. Their left subtrees are identical  
         * 3. Their right subtrees are identical
         * 
         * Let me walk through my solution step by step..."
         */
        
        // Base Case 1: Both trees are null (empty) - they're identical
        if (!p && !q) {
            return true;
        }
        
        // Base Case 2: One tree is null, the other isn't - they're different
        if (!p || !q) {
            return false;
        }
        
        // Base Case 3: Values at current nodes are different
        if (p->val != q->val) {
            return false;
        }
        
        // Recursive Case: Check left and right subtrees
        // Both left subtrees must be identical AND both right subtrees must be identical
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};

// Helper function to create a tree node
TreeNode* createNode(int val) {
    return new TreeNode(val);
}

// Helper function to create a tree with children
TreeNode* createNode(int val, TreeNode* left, TreeNode* right) {
    return new TreeNode(val, left, right);
}

// Interview demonstration function
void demonstrate_solution() {
    cout << "=== Same Tree Problem - Interview Demo ===" << endl << endl;
    
    // Example 1: Identical trees
    cout << "Example 1: Identical Trees" << endl;
    // Tree 1:    1          Tree 2:    1
    //           / \                    / \
    //          2   3                  2   3
    
    TreeNode* tree1 = createNode(1, createNode(2), createNode(3));
    TreeNode* tree2 = createNode(1, createNode(2), createNode(3));
    
    Solution solution;
    bool result = solution.isSameTree(tree1, tree2);
    cout << "Trees are identical: " << (result ? "True" : "False") << endl;  // Expected: True
    
    // Example 2: Different values
    cout << "\nExample 2: Different Values" << endl;
    // Tree 1:    1          Tree 2:    1
    //           / \                    / \
    //          2   3                  2   4
    
    TreeNode* tree3 = createNode(1, createNode(2), createNode(3));
    TreeNode* tree4 = createNode(1, createNode(2), createNode(4));
    
    result = solution.isSameTree(tree3, tree4);
    cout << "Trees are identical: " << (result ? "True" : "False") << endl;  // Expected: False
    
    // Example 3: Different structure
    cout << "\nExample 3: Different Structure" << endl;
    // Tree 1:    1          Tree 2:    1
    //           / \                      \
    //          2   3                      3
    
    TreeNode* tree5 = createNode(1, createNode(2), createNode(3));
    TreeNode* tree6 = createNode(1, nullptr, createNode(3));
    
    result = solution.isSameTree(tree5, tree6);
    cout << "Trees are identical: " << (result ? "True" : "False") << endl;  // Expected: False
    
    // Clean up memory
    delete tree1; delete tree2; delete tree3; delete tree4; delete tree5; delete tree6;
}

void interview_explanation() {
    cout << "\n" << string(60, '=') << endl;
    cout << "INTERVIEW EXPLANATION SCRIPT" << endl;
    cout << string(60, '=') << endl;
    
    cout << R"(
1. PROBLEM UNDERSTANDING:
   - I need to check if two binary trees are identical
   - Identical means: same structure AND same values at each node
   - I can assume the TreeNode structure is given

2. APPROACH SELECTION:
   - I'll use recursive DFS (Depth-First Search)
   - Why? Because tree problems often benefit from recursion
   - Recursion naturally handles the tree structure

3. ALGORITHM DESIGN:
   - Base cases first (always start with base cases in recursion):
     * Both null → return true (empty trees are identical)
     * One null, one not → return false (different structure)
     * Different values → return false (different content)
   - Recursive case:
     * Check current nodes are equal
     * Recursively check left subtrees
     * Recursively check right subtrees
     * Both must be true for overall result

4. TIME & SPACE COMPLEXITY:
   - Time: O(min(n,m)) where n,m are number of nodes
   - Space: O(min(h1,h2)) where h1,h2 are tree heights
   - In worst case: O(n) time, O(n) space for skewed trees

5. EDGE CASES HANDLED:
   - Empty trees (both null)
   - Trees of different sizes
   - Trees with same structure but different values
   - Trees with different structure but same values

6. TESTING STRATEGY:
   - Test with identical trees
   - Test with trees having different values
   - Test with trees having different structure
   - Test with empty trees
   - Test with one empty, one non-empty

7. ALTERNATIVE APPROACHES:
   - Iterative approach using stacks/queues (more complex)
   - BFS approach (level by level comparison)
   - Serialization approach (convert to string and compare)
)" << endl;
}

int main() {
    demonstrate_solution();
    interview_explanation();
    return 0;
} 