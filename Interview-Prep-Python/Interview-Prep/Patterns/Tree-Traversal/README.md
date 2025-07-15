# Tree Traversal Pattern - Python Interview Guide

## 🎯 Pattern Recognition
**Use tree traversals when you need:**
- Visit all nodes in specific order
- Search/find elements in tree
- Validate tree properties
- Calculate tree statistics
- Transform tree structure

## 📋 Core Templates

### Basic Tree Node
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.val})"
```

### DFS Traversals (Recursive)
```python
def preorder(root: TreeNode) -> list[int]:
    """Root -> Left -> Right"""
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def inorder(root: TreeNode) -> list[int]:
    """Left -> Root -> Right (sorted for BST)"""
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def postorder(root: TreeNode) -> list[int]:
    """Left -> Right -> Root"""
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

### BFS (Level Order) - Python Style
```python
from collections import deque

def level_order(root: TreeNode) -> list[list[int]]:
    """BFS level order traversal"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(current_level)
    
    return result
```

### DFS Traversals (Iterative)
```python
def preorder_iterative(root: TreeNode) -> list[int]:
    """Iterative preorder using stack"""
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Push right first (stack is LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result

def inorder_iterative(root: TreeNode) -> list[int]:
    """Iterative inorder using stack"""
    result = []
    stack = []
    current = root
    
    while current or stack:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Process current node
        current = stack.pop()
        result.append(current.val)
        
        # Go to right subtree
        current = current.right
    
    return result
```

## 🔥 Must-Know Problems

### 1. Maximum Depth (Easy) ⭐⭐⭐
```python
def max_depth(root: TreeNode) -> int:
    """Recursive approach - most elegant"""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# Alternative: BFS approach
def max_depth_bfs(root: TreeNode) -> int:
    """BFS level-by-level"""
    if not root:
        return 0
    
    depth = 0
    queue = deque([root])
    
    while queue:
        depth += 1
        # Process entire level
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return depth
```

### 2. Same Tree (Easy) ⭐⭐⭐
```python
def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    """Check if two trees are identical"""
    # Both empty
    if not p and not q:
        return True
    
    # One empty, one not
    if not p or not q:
        return False
    
    # Both non-empty: check value and subtrees
    return (p.val == q.val and 
            is_same_tree(p.left, q.left) and 
            is_same_tree(p.right, q.right))
```

### 3. Symmetric Tree (Easy) ⭐⭐
```python
def is_symmetric(root: TreeNode) -> bool:
    """Check if tree is mirror of itself"""
    def is_mirror(t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val and 
                is_mirror(t1.right, t2.left) and 
                is_mirror(t1.left, t2.right))
    
    return is_mirror(root, root) if root else True
```

### 4. Path Sum (Easy) ⭐⭐
```python
def has_path_sum(root: TreeNode, target_sum: int) -> bool:
    """Check if root-to-leaf path exists with given sum"""
    if not root:
        return False
    
    # Leaf node
    if not root.left and not root.right:
        return root.val == target_sum
    
    # Recurse with reduced target
    return (has_path_sum(root.left, target_sum - root.val) or
            has_path_sum(root.right, target_sum - root.val))

# Alternative: Path tracking
def path_sum_with_paths(root: TreeNode, target_sum: int) -> list[list[int]]:
    """Return all root-to-leaf paths that sum to target"""
    def dfs(node, remaining, path, all_paths):
        if not node:
            return
        
        # Add current node to path
        path.append(node.val)
        
        # Check if leaf and target reached
        if not node.left and not node.right and remaining == node.val:
            all_paths.append(path[:])  # Copy current path
        else:
            # Continue search
            dfs(node.left, remaining - node.val, path, all_paths)
            dfs(node.right, remaining - node.val, path, all_paths)
        
        # Backtrack
        path.pop()
    
    result = []
    dfs(root, target_sum, [], result)
    return result
```

### 5. Validate BST (Medium) ⭐⭐⭐
```python
def is_valid_bst(root: TreeNode) -> bool:
    """Validate binary search tree using bounds"""
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))

# Alternative: Inorder traversal approach
def is_valid_bst_inorder(root: TreeNode) -> bool:
    """BST inorder traversal should be sorted"""
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)
    
    values = inorder(root)
    for i in range(1, len(values)):
        if values[i] <= values[i-1]:
            return False
    return True
```

## 💡 Key Python Patterns

### Pattern 1: Recursive Template
```python
def dfs_template(root):
    # Base case
    if not root:
        return base_value
    
    # Recursive case
    left_result = dfs_template(root.left)
    right_result = dfs_template(root.right)
    
    # Combine results
    return combine(root.val, left_result, right_result)
```

### Pattern 2: Level Order Template
```python
def level_order_template(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(process(node))
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result
```

### Pattern 3: Path Tracking
```python
def path_template(root, target):
    def dfs(node, path, all_paths):
        if not node:
            return
        
        path.append(node.val)
        
        if is_target(node, target):
            all_paths.append(path[:])  # Make copy
        
        dfs(node.left, path, all_paths)
        dfs(node.right, path, all_paths)
        
        path.pop()  # Backtrack
    
    result = []
    dfs(root, [], result)
    return result
```

## ⚡ Python Interview Tips

### Pythonic Advantages
- **collections.deque** for efficient queue operations
- **List concatenation** for simple recursive solutions
- **None checks** with `not node` syntax
- **Multiple return values** for complex calculations

### Performance Notes
- **Recursive DFS**: O(n) time, O(h) space (h = height)
- **Iterative BFS**: O(n) time, O(w) space (w = max width)
- **Python recursion limit**: ~1000 levels (use iterative for deep trees)

### Common Mistakes
- Forgetting to check `if not root` in base case
- Not handling single node trees correctly
- Confusing left/right in symmetric problems
- Forgetting to copy paths when backtracking

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

## 🔥 Python Power Moves

### Show Pythonic Tree Creation
```python
def create_tree_from_list(values: list) -> TreeNode:
    """Create tree from level-order list (None for missing nodes)"""
    if not values:
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
```

### Generator for Memory Efficiency
```python
def inorder_generator(root: TreeNode):
    """Memory-efficient inorder traversal"""
    def dfs(node):
        if node:
            yield from dfs(node.left)
            yield node.val
            yield from dfs(node.right)
    
    return dfs(root)

# Usage: for val in inorder_generator(root): ...
```

## 📚 Related Files
- **Code Examples**: `../../../Code-Library/By-Topic/Trees/`
- **Python Features**: `../Python-Stdlib/collections-guide.md`
- **Templates**: `../../../Code-Library/Templates/tree_traversal_template.py`

---

**🎯 Tree mastery unlocks many advanced algorithms!** Once comfortable with basic traversals, you can tackle complex problems like serialization, LCA, and tree DP. 