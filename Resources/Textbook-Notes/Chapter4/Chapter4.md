# **Chapter 4: Trees and Binary Search Trees**

## **4.1 Basic Concepts**
A **tree** is a collection of nodes, with one node designated as the **root**. Each node has zero or more child nodes, and nodes with no children are called **leaves**.

### **Terminology**
- **Root**: The topmost node.
- **Leaf**: A node with no children.
- **Siblings**: Nodes with the same parent.
- **Depth**: Length of the path from the root to the node.
- **Height**: Length of the longest path from the node to a leaf.
- **Path**: Sequence of nodes from one node to another.
- **Ancestor/Descendant**: If there is a path from node A to node B, A is an ancestor of B, and B is a descendant of A.

---

## **4.2 Binary Trees**
A **binary tree** is a tree where each node has **at most two children**.

### **Properties**
- The **average depth** of a binary tree is **O(N)**.
- For a **binary search tree (BST)**, the **average depth** is **O(log N)**.
- **Expression Trees**: Used to represent mathematical expressions, where:
  - **Leaves** are operands (numbers/variables).
  - **Internal nodes** are operators (+, −, *, /).

---

## **4.3 Tree Traversals**
Tree traversal refers to visiting all nodes of a tree systematically. There are three common types:

### **Example Tree**

`    A
   / \
  B   C
 / \   \
D   E   F
`

 ### **1. Inorder Traversal (Left, Root, Right)**
- Visit the **left subtree**.
- Visit the **root**.
- Visit the **right subtree**.

#### **Inorder Example**
D → B → E → A → C → F

**Used in**: BST traversal to get elements in sorted order.

---

### **2. Preorder Traversal (Root, Left, Right)**
- Visit the **root**.
- Visit the **left subtree**.
- Visit the **right subtree**.

#### **Preorder Example**
A → B → D → E → C → F

**Used in**: Copying a tree, evaluating expression trees.

---

### **3. Postorder Traversal (Left, Right, Root)**
- Visit the **left subtree**.
- Visit the **right subtree**.
- Visit the **root**.

#### **Postorder Example**
D → E → B → F → C → A

**Used in**: Deleting trees, postfix expression evaluation.

---

### **4. Level Order Traversal (Breadth-First Search)**
- Visit nodes **level by level** (left to right).

#### **Level Order Example**
A → B → C → D → E → F

 **Used in**: Finding shortest paths in graphs, printing tree structures.

---

## **4.4 Binary Search Trees (BSTs)**
A **BST** follows this rule:
- **Left subtree** contains values **smaller** than the node.
- **Right subtree** contains values **greater** than the node.

### **Operations in BSTs**
| Operation | Average Time Complexity | Worst-Case Time Complexity (Unbalanced) |
|-----------|------------------------|---------------------------------|
| **Search** | **O(log N)** | **O(N)** |
| **Insert** | **O(log N)** | **O(N)** |
| **Delete** | **O(log N)** | **O(N)** |

---

### **Insertion in a BST**
1. Start at the **root**.
2. If the tree is empty, insert the new node as the **root**.
3. Otherwise, compare the new value with the **current node**:
   - If **smaller**, go to the **left** subtree.
   - If **larger**, go to the **right** subtree.
4. Repeat until an empty spot is found, then insert the node.

---

### **Deletion in a BST**
1. **Case 1**: Node has **no children** → Simply remove the node.
2. **Case 2**: Node has **one child** → Replace the node with its child.
3. **Case 3**: Node has **two children** →
   - Find the **inorder successor** (smallest node in the right subtree).
   - Replace the node with the **inorder successor**.
   - Delete the **inorder successor** from the right subtree.

---

## **4.5 AVL Trees**
An **AVL tree** is a **self-balancing BST**, where the height of two child subtrees differs by **at most 1**.

### **Balancing Methods**
- **Single Rotation**: Fixes **left-left (LL)** or **right-right (RR)** imbalance.
- **Double Rotation**: Fixes **left-right (LR)** or **right-left (RL)** imbalance.

### **Operations in AVL Trees**
| Operation | Time Complexity |
|-----------|---------------|
| **Search** | **O(log N)** |
| **Insert** | **O(log N)** |
| **Delete** | **O(log N)** |

### **Insertion & Deletion in AVL Trees**
1. **Perform BST insertion/deletion**.
2. **Update the heights** along the affected path.
3. **Check balance factors**:
   - If **balance factor = ±2**, perform **rotations** to restore balance.

---

## **4.6 Splay Trees**
A **splay tree** is a **self-adjusting BST** that moves accessed nodes to the **root** using **splaying**.

### **What is Splaying?**
**Splaying** moves a recently accessed node **to the root** using **rotations**.
- **Improves locality**: Frequently accessed nodes stay near the root.
- **Maintains balance dynamically**.
- **Ensures amortized O(log N) time** for operations.

### **Splaying Techniques**
1. **Zig (Single Rotation)** → When the node is a **child of the root**.
2. **Zig-Zig (Double Rotation - Same Direction)** → The node and parent are both left or both right children.
3. **Zig-Zag (Double Rotation - Opposite Direction)** → The node is a **left child of a right parent** or **right child of a left parent**.

### **Operations in Splay Trees**
| Operation | Amortized Time Complexity |
|-----------|--------------------------|
| **Search** | **O(log N)** |
| **Insert** | **O(log N)** |
| **Delete** | **O(log N)** |

### **Insertion in Splay Trees**
1. Insert like a **BST**.
2. **Splay** the inserted node to the **root**.

### **Deletion in Splay Trees**
1. Perform **BST deletion**.
2. **Splay the parent** of the deleted node to the root.

---

## **4.7 B-Trees**
A **B-tree** is a **balanced M-way tree**, optimized for **disk storage and large datasets**.

### **Properties**
- Each node has between **M/2** and **M** children.
- All leaves are at the **same depth**.

### **Operations in B-Trees**
| Operation | Time Complexity |
|-----------|---------------|
| **Search** | **O(log N)** |
| **Insert** | **O(log N)** |
| **Delete** | **O(log N)** |

### **Insertion in B-Trees**
1. Start at the **root** and traverse to the appropriate **leaf**.
2. Insert the key into the leaf.
3. If the leaf **overflows** (more than **M-1** keys):
   - **Split the leaf** and promote the middle key to the **parent**.
   - Recursively split and promote up if needed.

### **Deletion in B-Trees**
1. Locate and remove the key.
2. If the node **underflows** (fewer than **M/2** keys):
   - **Borrow a key from a sibling**, or
   - **Merge with a sibling**.
