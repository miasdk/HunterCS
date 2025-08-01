# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        self.postorder_helper(root, result)
        return result
    
    def postorder_helper(self, node, result):
        """
        Helper function for recursive postorder traversal
        Postorder: Left → Right → Root
        """
        # Base case: if node is null, return
        if not node:
            return
        
        # Recursive case: Left subtree first
        self.postorder_helper(node.left, result)
        
        # Then right subtree
        self.postorder_helper(node.right, result)
        
        # Finally, visit the current node (root)
        result.append(node.val) 