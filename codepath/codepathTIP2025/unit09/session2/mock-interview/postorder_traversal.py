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

# Alternative iterative solution using stack
class SolutionIterative(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        
        result = []
        stack = []
        current = root
        last_visited = None
        
        while stack or current:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Check the top of stack
            current = stack[-1]
            
            # If right child exists and hasn't been visited
            if current.right and current.right != last_visited:
                current = current.right
            else:
                # Visit the current node
                result.append(current.val)
                last_visited = current
                stack.pop()
                current = None
        
        return result

# Interview demonstration and explanation
def demonstrate_postorder():
    """
    Interview Demo: "Let me show you how postorder traversal works with examples..."
    """
    print("=== Binary Tree Postorder Traversal - Interview Demo ===\n")
    
    # Create TreeNode class for demonstration
    class TreeNode(object):
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
    # Example 1: [1,null,2,3]
    print("Example 1: root = [1,null,2,3]")
    # Tree structure:
    #     1
    #      \
    #       2
    #      /
    #     3
    
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    
    solution = Solution()
    result1 = solution.postorderTraversal(root1)
    print(f"Postorder traversal: {result1}")  # Expected: [3,2,1]
    
    # Example 2: [1,2,3,4,5,null,8,null,null,6,7,9]
    print("\nExample 2: root = [1,2,3,4,5,null,8,null,null,6,7,9]")
    # Tree structure:
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   8
    #       / \
    #      6   7
    #           \
    #            9
    
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.right = TreeNode(8)
    root2.left.right.left = TreeNode(6)
    root2.left.right.right = TreeNode(7)
    root2.left.right.right.right = TreeNode(9)
    
    result2 = solution.postorderTraversal(root2)
    print(f"Postorder traversal: {result2}")  # Expected: [4,6,7,5,2,9,8,3,1]

def interview_explanation():
    """
    Complete Interview Script for Postorder Traversal
    """
    print("\n" + "="*60)
    print("INTERVIEW EXPLANATION SCRIPT")
    print("="*60)
    
    print("""
1. PROBLEM UNDERSTANDING:
   - I need to perform a postorder traversal of a binary tree
   - Postorder means: Left subtree → Right subtree → Root
   - I need to return the values in postorder sequence as a list
   - The order is: visit left child, then right child, then current node

2. APPROACH SELECTION:
   - I'll use recursive DFS (Depth-First Search)
   - Why? Because tree traversal problems are naturally recursive
   - Recursion makes the postorder logic very clear and simple
   - Alternative: iterative approach using stack (more complex)

3. ALGORITHM DESIGN:
   - Base case: if node is null, return (do nothing)
   - Recursive case:
     * Recursively traverse left subtree
     * Recursively traverse right subtree  
     * Visit current node (add to result)
   - The key insight: we visit the root AFTER visiting both children

4. TIME & SPACE COMPLEXITY:
   - Time: O(n) where n is the number of nodes
   - Space: O(h) where h is the height of the tree
   - In worst case (skewed tree): O(n) space for recursion stack

5. EDGE CASES HANDLED:
   - Empty tree (null root) → return empty list
   - Single node tree → return [root.val]
   - Skewed trees (left or right only)
   - Balanced trees

6. ALTERNATIVE APPROACHES:
   - Iterative using stack (more complex but avoids recursion)
   - Morris traversal (O(1) space but complex)
   - Using two stacks approach

7. KEY DIFFERENCES FROM OTHER TRAVERSALS:
   - Preorder: Root → Left → Right
   - Inorder: Left → Root → Right  
   - Postorder: Left → Right → Root
   - Level-order: Level by level (BFS)

8. PRACTICAL APPLICATIONS:
   - Deleting a tree (delete children before parent)
   - Expression tree evaluation
   - File system operations
   - Memory cleanup in garbage collection
""")

if __name__ == "__main__":
    demonstrate_postorder()
    interview_explanation() 