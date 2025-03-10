# Chapter 4: Trees and Binary Search Trees

## 4.1 Basic Concepts
### Tree Definition
A **tree** is a collection of nodes with one node designated as the **root**. Each node has zero or more child nodes, and nodes with no children are called **leaves**.

### Terminology
- **Root**: The topmost node.
- **Leaf**: A node with no children.
- **Siblings**: Nodes with the same parent.
- **Depth**: Length of the path from the root to the node.
- **Height**: Length of the longest path from the node to a leaf.
- **Path**: Sequence of nodes from one node to another.
- **Ancestor/Descendant**: If there is a path from node A to node B, A is an ancestor of B, and B is a descendant of A.

## 4.2 Binary Trees
A **binary tree** is a tree where each node has at most two children.

### Properties
- The **average depth** of a binary tree is \(O(N)\).
- For a **binary search tree (BST)**, the **average depth** is \(O(\log N)\).

### Expression Trees
Used to represent expressions, with leaves as **operands** and internal nodes as **operators**.

## 4.3 Binary Search Trees (BST)
### BST Property
For every node:
- All elements in the **left subtree** are **smaller**.
- All elements in the **right subtree** are **larger**.

### Operations
| Operation | Average Time Complexity | Worst-case Time Complexity (Unbalanced Tree) |
|-----------|-------------------------|----------------------------------|
| **Search** | \(O(\log N)\) | \(O(N)\) |
| **Insert** | \(O(\log N)\) | \(O(N)\) |
| **Delete** | \(O(\log N)\) | \(O(N)\) |

### Insertion in BST
1. Start at the **root**.
2. If the tree is empty, insert the new node as the **root**.
3. Otherwise, compare the new value with the **current node**:
   - If **smaller**, go to the **left subtree**.
   - If **larger**, go to the **right subtree**.
4. Repeat until an empty spot is found, then insert the new node.

### Deletion in BST
- **Case 1**: Node has **no children** → Simply remove the node.
- **Case 2**: Node has **one child** → Replace the node with its child.
- **Case 3**: Node has **two children** →
  - Find the **inorder successor** (smallest node in the right subtree).
  - Replace the node with the inorder successor.
  - Delete the inorder successor from the right subtree.

## 4.4 AVL Trees
An **AVL tree** is a self-balancing BST where the heights of the two child subtrees of any node differ by at most **one**.

### Balancing
- **Single Rotation**: Fixes imbalances on the outside (**left-left** or **right-right**).
- **Double Rotation**: Fixes imbalances on the inside (**left-right** or **right-left**).

### Operations
| Operation | Time Complexity |
|-----------|----------------|
| **Search** | \(O(\log N)\) |
| **Insert** | \(O(\log N)\) |
| **Delete** | \(O(\log N)\) |

### Insertion in AVL Trees
1. Perform a **standard BST insertion**.
2. Update the **heights** of the nodes along the insertion path.
3. Check the **balance factor** of each node:
   - If balance factor becomes \(+2\) or \(-2\), perform **rotations** to restore balance.

### Deletion in AVL Trees
1. Perform a **standard BST deletion**.
2. Update the **heights** of the nodes along the deletion path.
3. Check the **balance factor** of each node:
   - If balance factor becomes \(+2\) or \(-2\), perform **rotations** to restore balance.

## 4.5 Splay Trees
A **splay tree** is a self-adjusting BST with **amortized** \(O(\log N)\) time per operation.

### Amortized Analysis
Any sequence of **M** operations takes \(O(M \log N)\) time.

### Operations
| Operation | Amortized Time Complexity |
|-----------|---------------------------|
| **Search** | \(O(\log N)\) |
| **Insert** | \(O(\log N)\) |
| **Delete** | \(O(\log N)\) |

### Insertion in Splay Trees
1. Perform a **standard BST insertion**.
2. **Splay** the newly inserted node to the **root**.

### Deletion in Splay Trees
1. Perform a **standard BST deletion**.
2. **Splay** the parent of the deleted node to the **root**.

## 4.6 B-Trees
A **B-tree** is a **balanced M-way tree**, suitable for **disk storage**.

### Properties
- Each node has between \(\frac{M}{2}\) and \(M\) children.
- All **leaves** are at the same depth.

### Operations
| Operation | Time Complexity |
|-----------|----------------|
| **Search** | \(O(\log N)\) |
| **Insert** | \(O(\log N)\) |
| **Delete** | \(O(\log N)\) |

### Insertion in B-Trees
1. Start at the **root** and traverse to the appropriate **leaf**.
2. Insert the **new key** into the leaf.
3. If the **leaf overflows** (more than \(M-1\) keys):
   - **Split** the leaf and promote the **middle key** to the parent.
   - Repeat the process **recursively** up the tree if necessary.

### Deletion in B-Trees
1. Start at the **root** and traverse to the appropriate **leaf**.
2. Delete the key from the **leaf**.
3. If the **leaf underflows** (fewer than \(\frac{M}{2}\) keys):
   - **Borrow a key** from a sibling or **merge** with a sibling.
   - Repeat the process **recursively** up the tree if necessary.

## Summary
- **BSTs** provide efficient search, insert, and delete operations with \(O(\log N)\) average time.
- **AVL Trees** and **Splay Trees** ensure balanced trees, preventing worst-case \(O(N)\) behavior.
- **B-Trees** are optimized for **disk storage** and **large datasets**.

## Essential Practice Problems
1. **Tree Properties**: Prove that the number of full nodes plus one equals the number of leaves in a binary tree.
2. **Tree Traversal**: Give the prefix, infix, and postfix expressions for a given binary tree.
3. **Tree Operations**: Write functions to compute the number of **nodes, leaves, and full nodes** in a binary tree.

## Exam Preparation Tips
### Focus on:
- **BST operations** (insert, delete, search).
- **AVL tree rotations** (single and double).
- **Understanding tree properties** (depth, height, balance).

### Practice:
- **Drawing trees** and performing operations.
- **Analyzing time complexity** of tree operations.
- **Implementing tree algorithms in code**.

