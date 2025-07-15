"""
Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along 
the longest path from the root node down to the farthest leaf node.

LeetCode: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Difficulty: Easy
Pattern: Tree Traversal / DFS
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, 
                 right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


def max_depth(root: Optional[TreeNode]) -> int:
    """
    Recursive DFS approach - Most elegant Python solution
    
    Algorithm:
    1. Base case: if no node, depth is 0
    2. Recursive case: 1 + max(left_depth, right_depth)
    
    Time: O(n) - visit each node once
    Space: O(h) - recursion stack, where h is height
    
    Args:
        root: Root of binary tree
        
    Returns:
        Maximum depth as integer
        
    Example:
        >>> tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        >>> max_depth(tree)
        3
    """
    if not root:
        return 0
    
    return 1 + max(max_depth(root.left), max_depth(root.right))


def max_depth_bfs(root: Optional[TreeNode]) -> int:
    """
    BFS level-by-level approach using collections.deque
    
    More explicit about levels, useful for follow-up questions
    
    Time: O(n) - visit each node once
    Space: O(w) - queue size, where w is maximum width
    """
    if not root:
        return 0
    
    depth = 0
    queue = deque([root])
    
    while queue:
        depth += 1
        # Process entire level
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return depth


def max_depth_iterative_dfs(root: Optional[TreeNode]) -> int:
    """
    Iterative DFS approach using stack
    
    Good when recursion depth might be too large
    
    Time: O(n) - visit each node once
    Space: O(h) - stack size in worst case
    """
    if not root:
        return 0
    
    stack = [(root, 1)]  # (node, depth)
    max_depth_seen = 0
    
    while stack:
        node, current_depth = stack.pop()
        max_depth_seen = max(max_depth_seen, current_depth)
        
        if node.left:
            stack.append((node.left, current_depth + 1))
        if node.right:
            stack.append((node.right, current_depth + 1))
    
    return max_depth_seen


def max_depth_with_path(root: Optional[TreeNode]) -> tuple[int, list[int]]:
    """
    Return both max depth and the path to deepest node
    
    Shows how to extend basic solution for follow-up questions
    
    Returns:
        Tuple of (max_depth, path_to_deepest_node)
    """
    if not root:
        return 0, []
    
    def dfs(node: Optional[TreeNode], path: list[int]) -> tuple[int, list[int]]:
        if not node:
            return 0, []
        
        path.append(node.val)
        
        if not node.left and not node.right:
            # Leaf node
            return 1, path[:]
        
        left_depth, left_path = dfs(node.left, path)
        right_depth, right_path = dfs(node.right, path)
        
        path.pop()  # Backtrack
        
        if left_depth >= right_depth:
            return 1 + left_depth, left_path
        else:
            return 1 + right_depth, right_path
    
    return dfs(root, [])


# ========================================
# UTILITY FUNCTIONS
# ========================================

def create_tree_from_list(values: list[Optional[int]]) -> Optional[TreeNode]:
    """
    Create binary tree from level-order list representation
    
    None values represent missing nodes
    
    Example:
        >>> tree = create_tree_from_list([3, 9, 20, None, None, 15, 7])
        >>> max_depth(tree)
        3
    """
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


def print_tree_levels(root: Optional[TreeNode]) -> None:
    """Pretty print tree level by level"""
    if not root:
        print("Empty tree")
        return
    
    queue = deque([root])
    level = 1
    
    while queue:
        level_size = len(queue)
        print(f"Level {level}: ", end="")
        
        for _ in range(level_size):
            node = queue.popleft()
            print(f"{node.val} ", end="")
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        print()  # New line after each level
        level += 1


# ========================================
# TEST CASES
# ========================================

def test_max_depth():
    """Comprehensive test cases"""
    
    # Test case 1: Normal tree [3,9,20,null,null,15,7]
    tree1 = create_tree_from_list([3, 9, 20, None, None, 15, 7])
    assert max_depth(tree1) == 3
    assert max_depth_bfs(tree1) == 3
    assert max_depth_iterative_dfs(tree1) == 3
    
    # Test case 2: Single node
    tree2 = TreeNode(1)
    assert max_depth(tree2) == 1
    
    # Test case 3: Empty tree
    assert max_depth(None) == 0
    
    # Test case 4: Linear tree (worst case)
    tree4 = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert max_depth(tree4) == 3
    
    # Test case 5: Only left children
    tree5 = TreeNode(1, TreeNode(2))
    assert max_depth(tree5) == 2
    
    print("All tests passed! ✅")


if __name__ == "__main__":
    # Run tests
    test_max_depth()
    
    # Interactive examples
    print("\n=== Maximum Depth Examples ===")
    
    # Example 1: Balanced tree
    print("\nExample 1: [3, 9, 20, null, null, 15, 7]")
    tree1 = create_tree_from_list([3, 9, 20, None, None, 15, 7])
    print_tree_levels(tree1)
    print(f"Max depth: {max_depth(tree1)}")
    
    depth, path = max_depth_with_path(tree1)
    print(f"Path to deepest node: {path}")
    
    # Example 2: Linear tree
    print("\nExample 2: Linear tree [1, 2, null, 3]")
    tree2 = create_tree_from_list([1, 2, None, 3])
    print_tree_levels(tree2)
    print(f"Max depth: {max_depth(tree2)}")


# ========================================
# INTERVIEW TALKING POINTS
# ========================================
"""
SOLUTION APPROACHES:
1. Recursive DFS: Most intuitive, clean code
2. BFS: Level-by-level, useful for level-specific questions
3. Iterative DFS: Avoids recursion stack overflow

OPTIMIZATION NOTES:
- Recursive is most readable and efficient for balanced trees
- BFS useful when you need level information
- Iterative DFS when dealing with very deep/unbalanced trees

EDGE CASES TO DISCUSS:
- Empty tree (None root)
- Single node tree
- Completely unbalanced tree (linear)
- Very deep tree (recursion limit considerations)

FOLLOW-UP QUESTIONS:
1. What if we need the path to the deepest node?
2. What if tree is very deep and recursion might overflow?
3. How would you find minimum depth instead?
4. What if we need all nodes at maximum depth?
5. How to handle trees with millions of nodes?

PYTHON-SPECIFIC NOTES:
- Use Optional[TreeNode] for type hints
- collections.deque for efficient queue operations
- Tuple unpacking for multiple return values
- List comprehensions for path tracking
- Generator expressions for memory efficiency

TIME/SPACE ANALYSIS:
- All approaches: O(n) time complexity
- Recursive: O(h) space (recursion stack)
- BFS: O(w) space (queue width)
- Iterative DFS: O(h) space (explicit stack)
where n = nodes, h = height, w = max width
""" 