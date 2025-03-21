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
    A
   / \
  B   C
 / \   \
 D   E   F


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

### **4.5 AVL Trees**
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

### **4.6 Splay Trees**
A **splay tree** is a **self-adjusting BST** that moves accessed nodes to the **root** using **splaying**.

## **What is Splaying?**
**Splaying** moves a recently accessed node **to the root** using **rotations**.
- **Improves locality**: Frequently accessed nodes stay near the root.
- **Maintains balance dynamically**.
- **Ensures amortized O(log N) time** for operations.

## **Splaying Techniques**
1. **Zig (Single Rotation)** → When the node is a **child of the root**.
2. **Zig-Zig (Double Rotation - Same Direction)** → The node and parent are both left or both right children.
3. **Zig-Zag (Double Rotation - Opposite Direction)** → The node is a **left child of a right parent** or **right child of a left parent**.

## **Operations in Splay Trees**
| Operation | Amortized Time Complexity |
|-----------|--------------------------|
| **Search** | **O(log N)** |
| **Insert** | **O(log N)** |
| **Delete** | **O(log N)** |

## **Insertion in Splay Trees**
1. Insert like a **BST**.
2. **Splay** the inserted node to the **root**.

## **Deletion in Splay Trees**
1. Perform **BST deletion**.
2. **Splay the parent** of the deleted node to the root.

---

## **4.7 B-Trees**
A **B-tree** is a **balanced M-way tree**, optimized for **disk storage and large datasets**.

## **Properties**
- Each node has between **M/2** and **M** children.
- All leaves are at the **same depth**.

## **Operations in B-Trees**
| Operation | Time Complexity |
|-----------|---------------|
| **Search** | **O(log N)** |
| **Insert** | **O(log N)** |
| **Delete** | **O(log N)** |

## **Insertion in B-Trees**
1. Start at the **root** and traverse to the appropriate **leaf**.
2. Insert the key into the leaf.
3. If the leaf **overflows** (more than **M-1** keys):
   - **Split the leaf** and promote the middle key to the **parent**.
   - Recursively split and promote up if needed.

## **Deletion in B-Trees**
1. Locate and remove the key.
2. If the node **underflows** (fewer than **M/2** keys):
   - **Borrow a key from a sibling**, or
   - **Merge with a sibling**.

### **Tree Traversals (Revisited)**

inorder traversal: process the left subtree
first, then perform processing at the current node, and finally process the right subtree
total running time
is O(N).

postorder traversal: process both subtrees first before we can process a node
total running time is
O(N), because constant work is performed at each node.

preorder traversal: node is processed before the children

level-order traversal: all nodes at depth d are processed before any node at depth d + 1.
`
/**
* Print the tree contents in sorted order. 
*/
void printTree( ostream & out = cout ) const 
{ 
   if( isEmpty())
      out << "Empty tree" << endl;
   else
      printTree( root, out);
}

/**
* Internal method to print a subtree rooted at t in sorted order.
*/
void printTree(BinaryNode *t, ostream & out) const 
{
   if ( t != nullptr )
   {
      printTree(t->left, out); 
      out << t->element << endl; 
      printTree(t->right, out);
   }
}

/**
* Internal method to compute the height of a subtree rooted at t. 
*/ 
int height( BinaryNode *t)
{
   if (t == nullptr )
      return -1; 
   else
      return 1 + max( height(t->left), height(t->right));
}

### **4.7 B-Trees** 
An M-ary search tree allows M-way branching
As branching increases,the depth decreases. Whereas a complete binary tree has height that is roughly log2 N, a
complete M-ary tree has height that is roughly **logM N**.

- In an M-ary search tree, we need M − 1 keys to decide which branch to take.
- In principle, a B-tree
guarantees only a few disk accesses.

A B-tree of order M is an M-ary tree with the following properties:
1. The data items are stored at leaves.
2. The nonleaf nodes store up to M − 1 keys to guide the searching; key i represents the
smallest key in subtree i + 1.
3. The root is either a leaf or has between two and M children.
4. All nonleaf nodes (except the root) have between  M/2  and M children.
5. All leaves are at the same depth and have between  L/2  and L data items, for some L
(the determination of L is described shortly).

### **4.8 Sets and Maps in the STL**

### 4.8.1 Sets 
The set is an ordered container that does not allow duplicates.

nested in the set are
iterator and const_iterator types that allow traversal of the set, and several methods
from vector and list are identically named in set, including begin, end, size, and empty.

Also included: find and insert 
The STL defines a class template called pair that is little more than a struct with
members first and second to access the two items in the pair. There are two different
insert routines:
pair<iterator,bool> insert( const Object & x );
pair<iterator,bool> insert( iterator hint, const Object & x );

### 4.8.2 Maps
A map is used to store a collection of ordered entries that consists of keys and their values.
Keys must be unique, but several keys can map to the same values.

### **4.8.3 Implementation of set and map**

//Accessing values in a map 
`
map<string, double> salariesl 

salaries[ "Pat" ] << endl; 
cout << salaries[ "Pat" ] << endl; 
cout << salaries[ "Jan" ] << endl; 

map<string, double>::const_iterator itr; 
itr = salaries.find( "Chris" ); 
if ( itr == salaries.end()) 
   cout << "Not an employee of this company!" << endl;
else 
   cout << itr->second << endl; 
`

A final note: By inserting elements into a search tree and then performing an inorder
traversal, we obtain the elements in sorted order. This gives an O(N logN) algorithm to
sort, which is a worst-case bound if any sophisticated search tree is used.
