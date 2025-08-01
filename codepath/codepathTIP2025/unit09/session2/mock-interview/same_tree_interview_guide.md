# 100. Same Tree - Complete Interview Guide

## Problem Statement
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

## Interview Presentation Script

### 1. Problem Understanding (30 seconds)
*"Let me make sure I understand the problem correctly. I need to check if two binary trees are identical, which means they must have the same structure and the same values at each corresponding node. For example, if one tree has a node with value 5 and the other tree has a different value at the same position, they're not identical."*

### 2. Approach Selection (1 minute)
*"For this problem, I'll use a recursive approach with Depth-First Search (DFS). This is a natural choice because:
- Tree problems often benefit from recursion
- Recursion naturally handles the tree structure
- We can compare nodes at the same positions in both trees
- The recursive approach is clean and easy to understand"*

### 3. Algorithm Design (2 minutes)
*"Let me break down my approach:

**Base Cases (always start with these in recursion):**
1. If both trees are null → return true (empty trees are identical)
2. If one tree is null and the other isn't → return false (different structure)
3. If the values at current nodes are different → return false (different content)

**Recursive Case:**
- Check if current nodes have the same value
- Recursively check left subtrees
- Recursively check right subtrees
- Both left and right subtrees must be identical for overall result to be true"*

### 4. Code Implementation (3 minutes)

#### Python Solution:
```python
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    # Base Case 1: Both trees are null (empty) - they're identical
    if not p and not q:
        return True
    
    # Base Case 2: One tree is null, the other isn't - they're different
    if not p or not q:
        return False
    
    # Base Case 3: Values at current nodes are different
    if p.val != q.val:
        return False
    
    # Recursive Case: Check left and right subtrees
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

#### C++ Solution:
```cpp
bool isSameTree(TreeNode* p, TreeNode* q) {
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
    return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
}
```

### 5. Walkthrough Example (2 minutes)
*"Let me walk through an example to show how this works:

**Example:**
```
Tree 1:    1          Tree 2:    1
          / \                    / \
         2   3                  2   3
```

**Step-by-step execution:**
1. Start at root: both have value 1 → continue
2. Check left subtree: both have value 2 → continue
3. Check right subtree: both have value 3 → continue
4. All nodes match → return true

**Another example:**
```
Tree 1:    1          Tree 2:    1
          / \                    / \
         2   3                  2   4
```

**Step-by-step execution:**
1. Start at root: both have value 1 → continue
2. Check left subtree: both have value 2 → continue
3. Check right subtree: 3 ≠ 4 → return false"*

### 6. Time & Space Complexity (1 minute)
*"**Time Complexity:** O(min(n,m)) where n and m are the number of nodes in each tree. We visit each node at most once, and we stop as soon as we find a difference.

**Space Complexity:** O(min(h1,h2)) where h1 and h2 are the heights of the trees. This is due to the recursion stack. In the worst case (skewed trees), this becomes O(n).

The complexity is optimal because we need to visit every node in the worst case to determine if trees are identical."*

### 7. Edge Cases & Testing (1 minute)
*"I should test these edge cases:
1. **Empty trees** (both null) → should return true
2. **One empty, one non-empty** → should return false
3. **Trees with different sizes** → should return false
4. **Trees with same structure but different values** → should return false
5. **Trees with different structure but same values** → should return false
6. **Large trees** → should handle efficiently"*

### 8. Alternative Approaches (if asked)
*"There are other approaches I could consider:

1. **Iterative DFS using stacks:** More complex but avoids recursion stack
2. **BFS using queues:** Level-by-level comparison
3. **Serialization:** Convert trees to strings and compare (less efficient)
4. **Hash-based approach:** Create hash of tree structure and values

However, the recursive approach is the most elegant and efficient for this problem."*

## Complete Interview Checklist

### Before Starting:
- [ ] Clarify the problem statement
- [ ] Ask about input constraints
- [ ] Confirm TreeNode structure

### During Implementation:
- [ ] Start with base cases
- [ ] Explain each step as you code
- [ ] Use clear variable names
- [ ] Handle edge cases

### After Implementation:
- [ ] Walk through an example
- [ ] Discuss time/space complexity
- [ ] Mention edge cases handled
- [ ] Be ready for follow-up questions

## Common Follow-up Questions

1. **"What if the trees are very large?"**
   - Answer: The recursive approach might cause stack overflow. Consider iterative approach.

2. **"Can you optimize this further?"**
   - Answer: The current solution is already optimal. Early termination on first difference.

3. **"What if TreeNode values are not integers?"**
   - Answer: The logic remains the same, just compare the actual values.

4. **"How would you test this function?"**
   - Answer: Unit tests with various tree structures, edge cases, and performance tests.

## Key Points to Remember

1. **Always start with base cases in recursion**
2. **Explain your thought process clearly**
3. **Walk through examples step-by-step**
4. **Discuss complexity analysis**
5. **Mention edge cases you're handling**
6. **Be prepared for follow-up questions**

## Practice Questions to Master This Pattern

- 101. Symmetric Tree
- 104. Maximum Depth of Binary Tree
- 110. Balanced Binary Tree
- 226. Invert Binary Tree
- 572. Subtree of Another Tree

This recursive tree traversal pattern is fundamental and appears in many tree-related problems! 