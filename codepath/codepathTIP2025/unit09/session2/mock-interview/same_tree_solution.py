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