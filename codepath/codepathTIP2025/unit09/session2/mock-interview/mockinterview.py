"""
100. Same Tree - Interview Solution and Explanation

Problem: Given two binary trees, check if they are identical (same structure and values).

Interview Approach:
1. Recursive DFS (Depth-First Search)
2. Base cases first
3. Recursive case: check current nodes, then left and right subtrees
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
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
        # Both left subtrees must be identical AND both right subtrees must be identical
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Interview Demonstration Code
def demonstrate_solution():
    """
    Interview Demo: "Let me show you how this works with an example..."
    """
    print("=== Same Tree Problem - Interview Demo ===\n")
    
    # Example 1: Identical trees
    print("Example 1: Identical Trees")
    # Tree 1:    1          Tree 2:    1
    #           / \                    / \
    #          2   3                  2   3
    
    tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
    tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
    
    solution = Solution()
    result = solution.isSameTree(tree1, tree2)
    print(f"Trees are identical: {result}")  # Expected: True
    
    # Example 2: Different values
    print("\nExample 2: Different Values")
    # Tree 1:    1          Tree 2:    1
    #           / \                    / \
    #          2   3                  2   4
    
    tree3 = TreeNode(1, TreeNode(2), TreeNode(3))
    tree4 = TreeNode(1, TreeNode(2), TreeNode(4))
    
    result = solution.isSameTree(tree3, tree4)
    print(f"Trees are identical: {result}")  # Expected: False
    
    # Example 3: Different structure
    print("\nExample 3: Different Structure")
    # Tree 1:    1          Tree 2:    1
    #           / \                      \
    #          2   3                      3
    
    tree5 = TreeNode(1, TreeNode(2), TreeNode(3))
    tree6 = TreeNode(1, None, TreeNode(3))
    
    result = solution.isSameTree(tree5, tree6)
    print(f"Trees are identical: {result}")  # Expected: False

def interview_explanation():
    """
    Complete Interview Script:
    """
    print("\n" + "="*60)
    print("INTERVIEW EXPLANATION SCRIPT")
    print("="*60)
    
    print("""
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
     * Both null → return True (empty trees are identical)
     * One null, one not → return False (different structure)
     * Different values → return False (different content)
   - Recursive case:
     * Check current nodes are equal
     * Recursively check left subtrees
     * Recursively check right subtrees
     * Both must be True for overall result

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
""")

if __name__ == "__main__":
    demonstrate_solution()
    interview_explanation()
