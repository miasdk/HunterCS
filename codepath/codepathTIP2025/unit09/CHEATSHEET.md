# Unit 9 Cheatsheet

## Overview
Here is a helpful cheatsheet outlining common syntax and concepts that will help you in your problem solving journey! Use this as reference as you solve the breakout problems for Unit 9. This is not an exhaustive list of all data structures, algorithmic techniques, and syntax you may encounter; it only covers the most critical concepts needed to ace Unit 9. In addition to the material below, you will be expected to know any required concepts from previous units.

---

## Standard Concepts

### Breadth First Search
Breadth First Search (BFS), also known as Level Order Traversal, is a method for visiting all the nodes in a tree. In a breadth first search approach, we visit nodes level by level. We begin by traversing the tree's root node, then traversing the root's direct children from left to right, followed by the root's grandchildren, etc.

In the diagram above, nodes that are outlined in pink have been added to the queue. Nodes shaded in pink have been visited and removed from the queue. The root node, at level 1, is visited first. Then the root node's children at level 2, nodes 7 and 25, are visited. The pattern continues until the nodes have been explored in the following order: [19, 7, 25, 5, 22, 71, 6, 30, 96].

BFS is typically implemented iteratively using a queue. The pseudocode for a Breadth First Search is as follows:

```
If the tree is empty:
    return an empty list

Create an empty queue
Create an empty list to store visited nodes

Add the root into the queue

While the queue is not empty:
    Pop the next node off the queue 
    Add the popped node to the list of visited nodes

    Add the popped node's left child to the queue
    Add the popped node's right child to the queue
```

**Example Implementation:**
```python
from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def breadth_first_search(root):
    # If the tree is empty, return an empty list
    if root is None:
        return []
    
    # Create an empty queue and result list
    queue = deque([root])
    visited = []
    
    # While the queue is not empty
    while queue:
        # Pop the next node off the queue
        current = queue.popleft()
        
        # Add the popped node to the list of visited nodes
        visited.append(current.value)
        
        # Add the popped node's left child to the queue
        if current.left:
            queue.append(current.left)
        
        # Add the popped node's right child to the queue
        if current.right:
            queue.append(current.right)
    
    return visited
```

BFS can also be implemented recursively, but an iterative, queue-based implementation is generally preferred because the order in which BFS visits nodes in a tree matches the FIFO insertion/removal order of a queue.

#### Level Order Traversal
BFS naturally visits nodes level by level, making it perfect for level order traversal problems.

**Example Implementation:**
```python
def level_order_traversal(root):
    if root is None:
        return []
    
    queue = deque([root])
    levels = []
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        # Process all nodes at the current level
        for _ in range(level_size):
            current = queue.popleft()
            current_level.append(current.value)
            
            # Add children to queue for next level
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        levels.append(current_level)
    
    return levels
```

### How to Pick a Traversal Method
There are four standard traversal algorithms for a binary tree. The first three - preorder, inorder, and postorder - are all depth first search traversals. The final algorithm is a breadth first search traversal.

For many problems, any traversal algorithm will lead to a solution. However, there are certain cases where a particular algorithm is preferred.

#### Depth First Search
In general, depth first search algorithms are preferred when the solution is expected to be deeper within the tree since the algorithm follows one branch as far as possible before backtracking and exploring other paths. In these scenarios, a breadth first approach may still find a solution, but more slowly since it traverses nodes closest to the root first.

**Inorder**
- Given a binary search tree, inorder will traverse the nodes in sorted ascending order.
- Inorder traversals are commonly used for binary search tree tasks or converting a binary search tree to a sorted list.

**Preorder**
- Given a binary tree, preorder will process the root of the tree before either subtree. It also processes nodes in the order they were inserted into the tree.
- Preorder traversals are commonly used for tree copying, expression tree evaluation, and serializing a tree.

**Postorder**
- Given a binary tree, postorder will process the subtrees before the root.
- Postorder traversals are commonly used for deleting a tree and expression tree evaluation.

#### Breadth First Search
Given a binary tree, breadth first search traverses nodes higher up in the tree (closest to the root) first. It is preferred when you expect the solution to be closer to the root. It also explores nodes level by level, from left to right.

Breadth first search is commonly used for problems that require traversing by level.

---

## Advanced Concepts

### Queue Data Structure
BFS relies heavily on the queue data structure. A queue follows FIFO (First In, First Out) principle, which is perfect for BFS since we want to process nodes in the order they were discovered.

**Queue Operations:**
- `enqueue()` or `append()`: Add element to the back
- `dequeue()` or `popleft()`: Remove element from the front
- `peek()` or `queue[0]`: View front element without removing

### Time and Space Complexity
- **Time Complexity**: O(n) where n is the number of nodes
- **Space Complexity**: O(w) where w is the maximum width of the tree
- In the worst case (complete binary tree), space complexity is O(n/2) ≈ O(n)

### Common BFS Applications
1. **Level order traversal** - Visit nodes level by level
2. **Shortest path problems** - Find minimum steps to reach target
3. **Tree serialization** - Convert tree to string representation
4. **Tree deserialization** - Reconstruct tree from string
5. **Connectivity problems** - Find all reachable nodes
6. **Level-based operations** - Process nodes at specific depths

### BFS vs DFS Comparison

| Aspect | BFS | DFS |
|--------|-----|-----|
| **Order** | Level by level | Branch by branch |
| **Memory** | O(w) - width of tree | O(h) - height of tree |
| **Best for** | Shallow solutions | Deep solutions |
| **Implementation** | Queue-based | Stack-based (recursive) |
| **Use cases** | Level order, shortest path | Tree traversal, backtracking |

---

## Bonus Concepts & Syntax

### Collections Module
The `collections` module provides the `deque` class, which is an efficient double-ended queue implementation.

```python
from collections import deque

# Create a queue
queue = deque()

# Add elements
queue.append(1)
queue.append(2)

# Remove elements (FIFO)
first = queue.popleft()  # Returns 1
```

### Queue Implementation with List
While `deque` is preferred, you can also use a regular list for simple queue operations:

```python
# Using list as queue (less efficient)
queue = []
queue.append(1)  # enqueue
if queue:
    item = queue.pop(0)  # dequeue (O(n) operation)
```

### Level Order with Null Values
Some problems require handling null/None values in level order traversal:

```python
def level_order_with_nulls(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        level = []
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            
            if node is None:
                level.append(None)
            else:
                level.append(node.value)
                queue.append(node.left)
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

---

## Key Takeaways
- **BFS** visits nodes level by level, left to right
- **Queue** is the natural data structure for BFS
- **Level order traversal** is a common BFS application
- **BFS vs DFS** choice depends on problem requirements
- **Time complexity** is O(n), space complexity is O(w)
- **Use BFS** when solution is likely near the root
- **Use BFS** for level-based problems and shortest path

--- 