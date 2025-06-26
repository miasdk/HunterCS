# AVL Trees: Complete Study Guide

## 📋 Table of Contents
- [Overview](#overview)
- [Key Properties](#key-properties)
- [Balance Factor](#balance-factor)
- [Rotation Types](#rotation-types)
- [Insertion Algorithm](#insertion-algorithm)
- [Deletion Algorithm](#deletion-algorithm)
- [Practice Examples](#practice-examples)
- [Time Complexity](#time-complexity)
- [Quick Reference](#quick-reference)

---

## Overview

**AVL trees** (named after Adelson-Velsky and Landis) are **self-balancing binary search trees** that maintain balance by ensuring the height difference between left and right subtrees of any node is at most 1.

### Why AVL Trees?
- **Guaranteed O(log n)** time complexity for all operations
- **Automatic balancing** prevents degeneration into linked lists
- **Efficient** for dynamic data that changes frequently

---

## Key Properties

### 1. **Balance Condition**
- Height difference between left and right subtrees ≤ 1
- Applies to **every node** in the tree

### 2. **Binary Search Tree Property**
- Left subtree contains values < node value
- Right subtree contains values > node value

### 3. **Height Balance**
- Tree height is always O(log n)
- Operations remain efficient regardless of insertion order

---

## Balance Factor

### Definition
The **balance factor (BF)** of a node is:
```
BF = Height(Left Subtree) - Height(Right Subtree)
```

### Valid Balance Factors
- **BF = -1**: Right subtree is 1 level higher
- **BF = 0**: Both subtrees have equal height
- **BF = +1**: Left subtree is 1 level higher

### Examples
```
Node A: Left height = 2, Right height = 1
BF = 2 - 1 = +1 ✓ (Valid)

Node B: Left height = 1, Right height = 3  
BF = 1 - 3 = -2 ✗ (Invalid - needs rebalancing)
```

---

## Rotation Types

When a node has |BF| > 1, we need rotations to restore balance.

### 1. **Left Rotation (LL Case)**

**When to use:** Node has BF = -2 (right-heavy) and right child has BF ≤ 0

**Visual Example:**
```
Before (Unbalanced):
    A (BF = -2)
     \
      B (BF = -1)
       \
        C

After Left Rotation:
      B (BF = 0)
     / \
    A   C
```

**Code Pattern:**
```cpp
Node* leftRotate(Node* A) {
    Node* B = A->right;
    A->right = B->left;
    B->left = A;
    return B;
}
```

### 2. **Right Rotation (RR Case)**

**When to use:** Node has BF = +2 (left-heavy) and left child has BF ≥ 0

**Visual Example:**
```
Before (Unbalanced):
        C (BF = +2)
       /
      B (BF = +1)
     /
    A

After Right Rotation:
      B (BF = 0)
     / \
    A   C
```

**Code Pattern:**
```cpp
Node* rightRotate(Node* C) {
    Node* B = C->left;
    C->left = B->right;
    B->right = C;
    return B;
}
```

### 3. **Left-Right Rotation (LR Case)**

**When to use:** Node has BF = +2 (left-heavy) and left child has BF = -1

**Two-Step Process:**
1. **Left rotation** on left child
2. **Right rotation** on original node

**Visual Example:**
```
Step 1 - Left Rotation on A:
    C (BF = +2)          C (BF = +2)
   /                     /
  A (BF = -1)    →      B (BF = +1)
   \                   /
    B                 A

Step 2 - Right Rotation on C:
      B (BF = 0)
     / \
    A   C
```

### 4. **Right-Left Rotation (RL Case)**

**When to use:** Node has BF = -2 (right-heavy) and right child has BF = +1

**Two-Step Process:**
1. **Right rotation** on right child
2. **Left rotation** on original node

**Visual Example:**
```
Step 1 - Right Rotation on C:
A (BF = -2)          A (BF = -2)
 \                    \
  C (BF = +1)   →      B (BF = -1)
 /                      \
B                        C

Step 2 - Left Rotation on A:
      B (BF = 0)
     / \
    A   C
```

---

## Insertion Algorithm

### Step-by-Step Process

1. **Insert** the new node as in a regular BST
2. **Update heights** of all affected nodes
3. **Check balance factors** starting from the insertion point up to root
4. **Perform rotations** if |BF| > 1

### Example: Insert 15 into AVL tree

```
Initial Tree:
     10
    /  \
   5    20
  / \
 3   7

Step 1: Insert 15 as right child of 10
     10
    /  \
   5    20
  / \  /
 3   7 15

Step 2: Check balance factors
- Node 15: BF = 0 (leaf)
- Node 20: BF = +1 (left child only)
- Node 10: BF = -1 (right subtree 1 level higher) ✓
- Node 5: BF = 0 ✓
- Node 3: BF = 0 ✓
- Node 7: BF = 0 ✓

Result: Tree is balanced, no rotations needed
```

### Example: Insert 25 (requires rotation)

```
After inserting 25:
     10
    /  \
   5    20
  / \  / \
 3   7 15  25

Check balance factors:
- Node 10: BF = -2 (right subtree 2 levels higher) ✗
- Node 20: BF = 0 ✓

Since 10 has BF = -2 and 20 has BF = 0, this is an LL case.
Perform left rotation on node 10:

Result:
     20
    /  \
   10   25
  /  \
 5    15
 / \
3   7
```

---

## Deletion Algorithm

### Step-by-Step Process

1. **Delete** the node as in a regular BST
2. **Update heights** of all affected nodes
3. **Check balance factors** starting from the deletion point up to root
4. **Perform rotations** if |BF| > 1

### Example: Delete 5 from AVL tree

```
Initial Tree:
     20
    /  \
   10   25
  /  \
 5    15
 / \
3   7

Step 1: Delete 5 (replace with inorder successor 7)
     20
    /  \
   10   25
  /  \
 7    15
 /
3

Step 2: Check balance factors
- Node 3: BF = 0 ✓
- Node 7: BF = +1 ✓
- Node 10: BF = +1 ✓
- Node 15: BF = 0 ✓
- Node 20: BF = 0 ✓
- Node 25: BF = 0 ✓

Result: Tree remains balanced
```

---

## Practice Examples

### Example 1: Build AVL Tree
Insert the following values: 30, 20, 40, 10, 25, 35, 50

**Solution:**
```
Step-by-step insertion:

1. Insert 30:    30

2. Insert 20:    30
                /
               20

3. Insert 40:    30
                /  \
               20   40

4. Insert 10:    30
                /  \
               20   40
              /
             10

5. Insert 25:    30
                /  \
               20   40
              /  \
             10   25

6. Insert 35:    30
                /  \
               20   40
              /  \  /
             10   25 35

7. Insert 50:    30
                /  \
               20   40
              /  \  /  \
             10   25 35  50
```

### Example 2: Identify Rotation Type
Given an unbalanced node with BF = +2 and its left child has BF = -1:

**Answer:** This is an **LR (Left-Right) case**
- Node has BF = +2 (left-heavy)
- Left child has BF = -1 (right-heavy)
- Requires left rotation on left child, then right rotation on original node

---

## Time Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Search** | O(log n) | O(1) |
| **Insert** | O(log n) | O(log n) |
| **Delete** | O(log n) | O(log n) |
| **Height** | O(log n) | O(1) |

### Why O(log n)?
- Tree height is always ≤ 1.44 × log₂(n+2)
- Each operation visits at most log n nodes
- Rotations are O(1) operations

---

## Quick Reference

### Balance Factor Rules
```
|BF| ≤ 1: Tree is balanced
|BF| > 1: Tree needs rebalancing
```

### Rotation Decision Table
| Node BF | Child BF | Rotation Type |
|---------|----------|---------------|
| +2 | +1 or 0 | RR (Right) |
| +2 | -1 | LR (Left-Right) |
| -2 | -1 or 0 | LL (Left) |
| -2 | +1 | RL (Right-Left) |

### Common Patterns
- **LL**: Right-heavy node with right-heavy child
- **RR**: Left-heavy node with left-heavy child  
- **LR**: Left-heavy node with right-heavy left child
- **RL**: Right-heavy node with left-heavy right child

### Height Calculation
```cpp
int height(Node* node) {
    if (node == nullptr) return -1;
    return 1 + max(height(node->left), height(node->right));
}
```

### Balance Factor Calculation
```cpp
int balanceFactor(Node* node) {
    if (node == nullptr) return 0;
    return height(node->left) - height(node->right);
}
```

---

## 🎯 Exam Tips

1. **Always check balance factors** after insertion/deletion
2. **Remember the rotation patterns** - practice drawing them
3. **Start from the insertion/deletion point** and work up to root
4. **Verify your answer** by checking all balance factors
5. **Use the decision table** to quickly identify rotation type

### Common Mistakes to Avoid
- Forgetting to update heights after rotations
- Not checking balance factors of all affected nodes
- Confusing LR and RL cases
- Stopping too early in the rebalancing process

---

*This guide covers all essential AVL tree concepts for your exam. Practice drawing rotations and calculating balance factors until they become second nature!* 