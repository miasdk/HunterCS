# Unit 9 - Session 1 - Advanced Problems
## Tree Traversal and Manipulation

This session contains advanced tree traversal and manipulation problems focused on level-order traversal, zigzag traversal, tree modification, and complex tree operations.

---

## Problem 1: Croquembouche II 🍰

**Problem Description:**
You are designing a delicious croquembouche (a French dessert composed of a cone-shaped tower of cream puffs), for a couple's wedding. They want the cream puffs to have a variety of flavors. You've finished your design and want to send it to the couple for review.

Given a root of a binary tree design where each node in the tree represents a cream puff in the croquembouche, traverse the croquembouche in tier order (i.e., level by level, left to right).

**Function Signature:**
```python
def listify_design(design):
    """
    Traverse the croquembouche in tier order (level by level, left to right).
    
    Args:
        design: Root of binary tree representing cream puffs
        
    Returns:
        List of lists where each inner list represents a tier (level) of the croquembouche
        and contains the flavors of each cream puff on that tier from left to right
    """
```

**Example:**
```
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  

Result: [['Vanilla'], ['Chocolate', 'Strawberry'], ['Vanilla', 'Matcha']]
```

**Key Concepts:**
- Level-order traversal (Breadth-First Search)
- Queue-based approach
- Tree level identification

---

## Problem 2: Icing Cupcakes in Zigzag Order 🧁

**Problem Description:**
You have rows of cupcakes represented as a binary tree where each node represents a cupcake. To ice them efficiently, you are icing cupcakes one row (level) at a time, in zigzag order (i.e., from left to right, then right to left for the next row and alternate between).

**Function Signature:**
```python
def zigzag_icing_order(cupcakes):
    """
    Ice cupcakes in zigzag order (left to right, then right to left alternating).
    
    Args:
        cupcakes: Root of binary tree representing cupcakes
        
    Returns:
        List of cupcake values in the order they were iced
    """
```

**Example:**
```
            Chocolate
           /         \
        Vanilla       Lemon
       /              /    \
    Strawberry   Hazelnut   Red Velvet   

Result: ['Chocolate', 'Lemon', 'Vanilla', 'Strawberry', 'Hazelnut', 'Red Velvet']
```

**Key Concepts:**
- Level-order traversal with direction alternation
- Level tracking
- List reversal for alternating levels

---

## Problem 3: Larger Order Tree 📊

**Problem Description:**
You have the root of a binary search tree orders, where each node represents an order and each node's value represents the number of cupcakes the customer ordered. Convert the tree to a 'larger order tree' such that the value of each node is equal to its original value plus the sum of all node values greater than it.

**Function Signature:**
```python
def larger_order_tree(orders):
    """
    Convert BST to 'larger order tree' where each node's value equals its original value
    plus the sum of all node values greater than it.
    
    Args:
        orders: Root of binary search tree representing orders
        
    Returns:
        Root of the modified tree
    """
```

**Example:**
```
Original:          Modified:
     4                 30
   /   \             /   \
  1     6           36    21
 / \   / \         / \   / \
0   2 5   7       36 35 26 15
     \     \           \     \
      3     8           33     8
```

**Key Concepts:**
- Inorder traversal (for BST properties)
- Running sum calculation
- Tree modification

---

## Problem 4: Find Next Order to Fulfill Today 📋

**Problem Description:**
You store each customer order at your bakery in a binary tree where each node represents a different order. Each level of the tree represents a different day's orders. Given the root of a binary tree order_tree and a TreeNode object order representing the order you are currently fulfilling, return the next order to fulfill that day.

**Function Signature:**
```python
def next_order_to_fulfill(order_tree, order):
    """
    Find the next order to fulfill on the same level as the given order.
    
    Args:
        order_tree: Root of binary tree representing orders
        order: TreeNode object representing current order being fulfilled
        
    Returns:
        Next order to fulfill on the same level, or None if order is the last of the day
    """
```

**Example:**
```
        Cupcakes
       /       \ 
   Macaron     Cookies      
        \      /      \
      Cake   Eclair   Croissant

next_order_to_fulfill(cupcakes, cake) → eclair
next_order_to_fulfill(cupcakes, cookies) → None
```

**Key Concepts:**
- Level-order traversal
- Node reference tracking
- Same-level node identification

---

## Problem 5: Add Row of Cupcakes to Display 🎂

**Problem Description:**
You have a cupcake display represented by a binary tree where each node represents a different cupcake. Given the root of the binary tree display, a string flavor, and an integer depth, add a row of nodes with value flavor at the given depth.

**Function Signature:**
```python
def add_row(display, flavor, depth):
    """
    Add a row of cupcakes with given flavor at the specified depth.
    
    Args:
        display: Root of binary tree representing cupcake display
        flavor: String representing the flavor of new cupcakes
        depth: Integer representing the depth where to add the row
        
    Returns:
        Root of the modified tree
    """
```

**Example:**
```
Original:              Modified:
    Chocolate              Chocolate
    /        \            /        \
Vanilla    Strawberry  Vanilla    Strawberry
            /     \     /    \     /       \
     Chocolate    Red Velvet  Mocha   Mocha  Mocha     Mocha
                         /             \
                      Chocolate       Red Velvet
```

**Key Concepts:**
- Depth-first traversal
- Tree modification at specific depth
- Subtree preservation

---

## Problem 6: Maximum Icing Difference 🍯

**Problem Description:**
In your bakery, you're planning a display of cupcakes where each cupcake is represented by a node in a binary tree. The sweetness level of the icing on each cupcake is stored in the node's value. You want to identify the maximum icing difference between any two cupcakes where one cupcake is an ancestor of the other.

**Function Signature:**
```python
def max_icing_difference(root):
    """
    Find the maximum icing difference between any ancestor-descendant pair.
    
    Args:
        root: Root of binary tree representing cupcake display
        
    Returns:
        Maximum difference between any ancestor-descendant pair
    """
```

**Example:**
```
            8
           /  \
         3     10
        / \      \
       1   6     14
          /  \    /
         4    7  13

Result: 7 (difference between root 8 and leaf 1: |8 - 1| = 7)
```

**Key Concepts:**
- Depth-first traversal
- Ancestor-descendant relationship tracking
- Global maximum tracking

---

## Complexity Analysis Requirements

For each problem, you must evaluate and document:

### Time Complexity
- Define variables (n = number of nodes, h = height of tree)
- Provide rationale for your analysis
- Assume balanced trees unless specified otherwise

### Space Complexity
- Consider both auxiliary space and recursion stack
- Account for data structures used
- Provide clear rationale

### Example Analysis Format:
```python
"""
Time Complexity: O(n)
- n = number of nodes in the tree
- We visit each node exactly once during traversal

Space Complexity: O(w)
- w = maximum width of the tree (number of nodes at the widest level)
- We store at most one level of nodes in the queue at any time
"""
```

---

## Implementation Hints

1. **Level-Order Traversal**: Use a queue (collections.deque or list) to process nodes level by level
2. **Zigzag Traversal**: Track level numbers and reverse lists for odd levels
3. **BST Operations**: Leverage inorder traversal for sorted property
4. **Tree Modification**: Be careful to preserve existing subtrees when modifying
5. **Ancestor-Descendant**: Use DFS with path tracking or global variables

---

## Testing

Run the test suite to verify your implementations:
```bash
python problems.py
```

Each problem includes comprehensive test cases covering:
- Basic functionality
- Edge cases (empty trees, single nodes)
- Complex scenarios
- Expected outputs

---

## Learning Objectives

By completing these problems, you will master:
- Advanced tree traversal techniques
- Tree modification algorithms
- Complex tree operations
- Level-order traversal variations
- BST property utilization
- Ancestor-descendant relationship handling

Good luck with your tree traversal adventures! 🌳✨ 