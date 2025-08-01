# Unit 8 Cheatsheet

## Overview
Here is a helpful cheatsheet outlining common syntax and concepts that will help you in your problem solving journey! Use this as reference as you solve the breakout problems for Unit 8. This is not an exhaustive list of all data structures, algorithmic techniques, and syntax you may encounter; it only covers the most critical concepts needed to ace Unit 8. In addition to the material below, you will be expected to know any required concepts from previous units.

---

## Standard Concepts

### Binary Trees
Binary trees are a non-linear data structure. Similar to a linked list, trees are made up of nodes that store a piece of data as well as references to other nodes.

#### Binary Tree Structure
Each node in a binary tree can point to up to two other nodes in the tree. Each of these pointers is known as a child of the original parent node. The two children are referred to as the left and right children or pointers.

A TreeNode class for a binary tree may look like the following:

```python
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.value = value
         self.left = left
         self.right = right
```

**Example Usage:**
```python
# Creates the following tree:
#   1
#  / \
# 2   3

node_one = TreeNode(1)
node_two = TreeNode(2)
node_three = TreeNode(3)

node_one.left = node_two    # Node two is the left child of node one
node_one.right = node_three # Node three is the right child of node one
```

#### Tree Terminology
There is a lot of terminology used to discuss tree data structures. Here are some common ones!

- **root**: The top-most node in a tree.
- **leaf**: A node with no children.
- **edge**: The reference or pointer (path) between a parent and child node.
- **height**: The maximum number of edges it takes to travel from a leaf node to the root node.
- **level**: All the nodes at the same height in the tree.
- **subtree**: The tree formed by any node, its children, grandchildren, etc. that is not the root node.
- **ancestor**: A node with a greater height (closer to the root) on the path from the current node to the root node.
- **descendant**: A node in the current node's subtree(s).
- **siblings**: Two nodes that share a parent.

#### Balanced Trees
A tree is considered balanced if the height difference between the left and right subtree is at most one and both subtrees are also balanced. In this way the nodes in the tree must be spread fairly evenly.

Whether or not a tree is balanced can affect the time complexity of our algorithms. It is usually much faster to reach the bottom of a tree or find a particular node in a balanced tree than it is in an unbalanced tree!

#### Tree Traversal
Tree traversals almost always start from the root of the tree. But how do we decide which child we want to visit first? Now that we are working with a non-linear data structure, there are multiple paths that we can take to visit all the nodes of a tree. Oftentimes, the strategy you'll use will depend on the data you are trying to find or the operation you want to perform on the tree.

The most common type of traversal is a **depth first search** traversal. This means that we choose one of the root node's children to visit, then visit its grandchildren and any further descendants before ever exploring the root's second child and its descendants. In other words, we fully explore a single subtree before traversing the second subtree.

There are three standard types of depth first search tree traversals:

1. **Preorder**: Current, Left, Right
2. **Inorder**: Left, Current, Right
3. **Postorder**: Left, Right, Current

##### Preorder
A preorder traversal works as follows:
1. visit the current node
2. traverse the current node's left subtree
3. traverse the current node's right subtree

Preorder traverses nodes in the order they were added to the tree, so it is commonly used to save a copy of the tree structure to memory or send it across a network.

**Example Implementation:**
```python
def preorder_traversal(node):
    if node is None:
        return
    
    # Visit current node
    print(node.value)
    
    # Traverse left subtree
    preorder_traversal(node.left)
    
    # Traverse right subtree
    preorder_traversal(node.right)
```

##### Inorder
An inorder traversal works as follows:
1. traverse the current node's left subtree
2. visit the current node
3. traverse the current node's right subtree

Inorder begins by traversing the leftmost node and ends by traversing the rightmost node. In a binary search tree which is a specific type of binary tree that maintains nodes in a specific order, this means that nodes are processed from smallest to largest, so it can be useful to print nodes in sorted order.

**Example Implementation:**
```python
def inorder_traversal(node):
    if node is None:
        return
    
    # Traverse left subtree
    inorder_traversal(node.left)
    
    # Visit current node
    print(node.value)
    
    # Traverse right subtree
    inorder_traversal(node.right)
```

##### Postorder
A postorder traversal works as follows:
1. traverse the current node's left subtree
2. traverse the current node's right subtree
3. visit the current node

Postorder traverses all of the root node's descendants before processing the root itself. This makes it useful for deleting a binary tree.

**Example Implementation:**
```python
def postorder_traversal(node):
    if node is None:
        return
    
    # Traverse left subtree
    postorder_traversal(node.left)
    
    # Traverse right subtree
    postorder_traversal(node.right)
    
    # Visit current node
    print(node.value)
```

💡 **Why do we traverse left to right?**
This is a convention that makes tree traversals predictable and consistent. By always visiting the left child before the right child, we ensure that our traversal order is deterministic.

### Binary Search Trees
A binary search tree (BST) is a very common type of binary tree that organizes nodes in a specific way that makes searching, inserting, and deleting nodes from the tree very efficient (O(log n) time complexity).

A binary search tree maintains the following rules:
- All nodes in the left subtree of a node contain values less than the node's value
- All nodes in the right subtree of a node contain values greater than the node's value

In the tree above, we can see that all nodes in the root's right subtree are greater than 19, and all nodes in the root's left subtree are less than 19. The same properties hold for any subtree we consider. All nodes in node 25's right subtree are greater than 25, and the only node in its left subtree is less than 25.

The TreeNode class for a binary search tree often maintains an additional property key. The key is an integer used to maintain the sorted order of the tree: all nodes in the left subtree must have a smaller key and all nodes in the right subtree must have a greater key. The value is then free to be any piece of data (a string, list, another integer) irrespective of the key.

```python
class TreeNode():
     def __init__(self, key, value=0, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
```

**Example Usage:**
```python
# Creates the following tree :
# By Key:        By Value:
#     1              Yoda
#    / \            /   \
#   2   3         Luke  R2D2

z = Node(2, 'Yoda')
x = Node(1, 'Luke')
y = Node(3, 'R2D2')
```

#### Binary Search Tree Operations
We can use the properties of a binary search tree to perform insert, delete, and search operations faster.

Let's take the search operation for example. Because the nodes are maintained in sorted order, every time we visit a node we can compare the key of the node we are visiting to the key of the node we are searching for. If the node is not the node we are looking for, we can determine whether our target node will be in the current node's left or right subtree.

If our target node's key is less than the current node's key, we should look in the left subtree. If it is greater, we should look in the right subtree.

In this way, with each node we visit, we halve the amount of remaining nodes we need to look through (assuming the tree is balanced). Notice this is just like the binary search algorithm we did on sorted lists from Unit 7!

**Example Search Implementation:**
```python
class TreeNode():
     def __init__(self, key, value=0, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

def search_bst(node, key):
    # Base case: node is None or we find the key
    if node is None or node.key == key:
        return node

    # If the key to be found is less than the current node's key, search in the left subtree
    if key < node.key:
        return search_bst(node.left, key)

    # If the key to be found is greater than the current node's key, search in the right subtree
    return search_bst(node.right, key)
```

---

## Advanced Concepts

### Tree Height and Balance
The height of a tree is the maximum number of edges from the root to any leaf node. A balanced tree has a height of approximately log₂(n) where n is the number of nodes, making operations efficient.

### Time Complexity Analysis
- **Balanced BST**: O(log n) for search, insert, delete
- **Unbalanced BST**: O(n) in worst case (degenerates to linked list)
- **Tree Traversal**: O(n) time and O(h) space where h is height

### Common Tree Problems
1. **Height calculation**
2. **Balanced tree checking**
3. **Tree serialization/deserialization**
4. **Path finding**
5. **Subtree operations**

---

## Bonus Concepts & Syntax
The following concepts are nice to know and may improve your code readability or help you solve certain problems more easily and efficiently. However, they are not required to solve any of the problems in this unit. These concepts are not in scope for either the Standard or Advanced Unit 8 assessments, and you do not need to memorize them!

### Throwaway Variable
Used to ignore values. Commonly used when a function returns multiple values but the user is only interested in one or when the loop variable is not needed inside the body of the for loop.

**Example:**
```python
# Ignoring the second return value
result, _ = some_function()

# Ignoring loop variable
for _ in range(5):
    print("Hello")
```

### Inner Functions
Specialized Python syntax often used to create helper functions.

**Example:**
```python
def outer_function(x):
    def inner_function(y):
        return y * 2
    
    return inner_function(x) + 1
```

---

## Key Takeaways
- **Binary trees** are hierarchical data structures with at most two children per node
- **Tree traversals** (preorder, inorder, postorder) visit nodes in different orders
- **Binary search trees** maintain sorted order for efficient operations
- **Balanced trees** provide optimal O(log n) performance
- **Recursive algorithms** are natural for tree operations
- **Tree terminology** helps communicate tree concepts clearly

--- 