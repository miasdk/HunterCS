# Unit 9 - Session 1 - Standard Problems
## Tree Traversal and Manipulation

This session contains standard tree traversal and manipulation problems focused on basic tree operations, level-order traversal, and fundamental tree algorithms.

---

## Problem 1: Merging Cookie Orders 🍪

**Problem Description:**
You run a local bakery and are given the roots of two binary trees order1 and order2 where each node represents the number of a certain cookie type the customer has ordered. To maximize efficiency, you want to bake enough of each type of cookie for both orders together.

Given order1 and order2, merge the orders together into one tree and return the root of the merged tree. When two nodes overlap, sum their values; otherwise, use the non-None node.

**Function Signature:**
```python
def merge_orders(order1, order2):
    """
    Merge two binary trees representing cookie orders.
    
    Args:
        order1: Root of first binary tree representing cookie order
        order2: Root of second binary tree representing cookie order
        
    Returns:
        Root of the merged tree where overlapping nodes are summed
    """
```

**Example:**
```
     1             2         
    /  \         /   \       
   3    2       1     3   
 /               \      \   
5                 4      7   

Result:
     3
    /  \      
  4     5  
 / \      \
5   4      7
```

**Key Concepts:**
- Recursive tree merging
- Handling None nodes
- Tree structure preservation

---

## Problem 2: Croquembouche 🍰

**Problem Description:**
You are designing a delicious croquembouche (a French dessert composed of a cone-shaped tower of cream puffs), for a couple's wedding. They want the cream puffs to have a variety of flavors. You've finished your design and want to send it to the couple for review.

Given a root of a binary tree design where each node represents a cream puff, print a list of the flavors in level order (left to right, level by level).

**Function Signature:**
```python
def print_design(design):
    """
    Print cream puff flavors in level order (left to right, level by level).
    
    Args:
        design: Root of binary tree representing cream puffs
        
    Returns:
        List of flavors in level order traversal
    """
```

**Example:**
```
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  

Result: ['Vanilla', 'Chocolate', 'Strawberry', 'Vanilla', 'Matcha']
```

**Key Concepts:**
- Level-order traversal (Breadth-First Search)
- Queue-based approach
- Tree level processing

---

## Problem 3: Maximum Tiers in Cake 🎂

**Problem Description:**
You have entered your bakery into a cake baking competition and for your entry have decided build a complicated pyramid shape cake, where different sections have different numbers of tiers. Given the root of a binary tree cake where each node represents a different section of your cake, return the maximum number of tiers in your cake.

**Function Signature:**
```python
def max_tiers(cake):
    """
    Find the maximum number of tiers (height) in the cake.
    
    Args:
        cake: Root of binary tree representing cake sections
        
    Returns:
        Maximum number of tiers (height of the tree)
    """
```

**Example:**
```
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee

Result: 3
```

**Key Concepts:**
- Tree height calculation
- Depth-first search
- Recursive traversal

---

## Problem 4: Maximum Tiers in Cake II 🎂

**Problem Description:**
If you solved max_tiers() in the previous problem using a depth first search approach, reimplement your solution using a breadth first search approach. If you implemented it using a breadth first search approach, use a depth first search approach.

**Function Signature:**
```python
def max_tiers_alt(cake):
    """
    Find the maximum number of tiers using alternative approach (BFS if DFS was used before, vice versa).
    
    Args:
        cake: Root of binary tree representing cake sections
        
    Returns:
        Maximum number of tiers (height of the tree)
    """
```

**Key Concepts:**
- Alternative traversal methods
- BFS vs DFS for height calculation
- Level tracking in BFS

---

## Problem 5: Can Fulfill Order 📋

**Problem Description:**
At your bakery, you organize your current stock of baked goods in a binary tree with root inventory where each node represents the quantity of a baked good. A customer comes in wanting a random assortment of baked goods of quantity order_size. Return True if you can fulfill the order and False otherwise.

**Function Signature:**
```python
def can_fulfill_order(inventory, order_size):
    """
    Check if there's a root-to-leaf path that sums to the order size.
    
    Args:
        inventory: Root of binary tree representing baked goods inventory
        order_size: Integer representing the required order size
        
    Returns:
        True if order can be fulfilled, False otherwise
    """
```

**Example:**
```
             5
           /   \
          4     8
        /      /  \
       11     13   4
      /  \          \
     7   2           1   

can_fulfill_order(baked_goods, 22) → True  (5 + 4 + 11 + 2 = 22)
can_fulfill_order(baked_goods, 2) → False
```

**Key Concepts:**
- Path sum calculation
- Root-to-leaf path finding
- Recursive backtracking

---

## Problem 6: Icing Cupcakes in Zigzag Order 🧁

**Problem Description:**
You have rows of cupcakes represented as a binary tree where each node represents a cupcake. To ice them efficiently, you are icing cupcakes one row (level) at a time, in zigzag order (left to right, then right to left for the next row and alternate between).

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

1. **Tree Merging**: Use recursive approach, handle None nodes carefully
2. **Level-Order Traversal**: Use a queue to process nodes level by level
3. **Height Calculation**: Use DFS for recursive approach, BFS for iterative
4. **Path Sum**: Use recursive backtracking with sum tracking
5. **Zigzag Traversal**: Track level numbers and reverse lists for odd levels

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
- Basic tree traversal techniques
- Tree merging algorithms
- Height calculation methods
- Path sum problems
- Level-order traversal variations
- Alternative traversal approaches

Good luck with your tree traversal adventures! 🌳✨ 