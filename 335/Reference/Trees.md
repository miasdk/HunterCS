# Comprehensive Guide to Trees in C++

## Table of Contents

1. [Introduction to Trees](#introduction-to-trees)
2. [Tree Terminology](#tree-terminology)
3. [Types of Trees](#types-of-trees)
   - [Binary Trees](#binary-trees)
   - [Binary Search Trees](#binary-search-trees)
   - [AVL Trees](#avl-trees)
   - [Red-Black Trees](#red-black-trees)
   - [B-Trees](#b-trees)
   - [Tries](#tries)
4. [Tree Implementations in C++](#tree-implementations-in-c)
   - [Custom Tree Implementation](#custom-tree-implementation)
   - [C++ Standard Library Tree Containers](#c-standard-library-tree-containers)
     - [std::set](#stdset)
     - [std::map](#stdmap)
     - [std::multiset](#stdmultiset)
     - [std::multimap](#stdmultimap)
5. [Tree Traversal Algorithms](#tree-traversal-algorithms)
   - [Depth-First Traversals](#depth-first-traversals)
   - [Breadth-First Traversal](#breadth-first-traversal)
6. [Time Complexity Analysis](#time-complexity-analysis)
7. [Practice Problems](#practice-problems)
8. [Advanced Tree Concepts](#advanced-tree-concepts)
9. [References](#references)

## Introduction to Trees

A tree is a non-linear hierarchical data structure that consists of nodes connected by edges. Unlike linear data structures such as arrays, linked lists, stacks, and queues which store data sequentially, trees store data in a hierarchical manner.

Key characteristics of trees:
- Each node can have zero or more child nodes
- There is exactly one path between any two nodes
- Trees have a single root node (the top node with no parent)
- Trees cannot contain cycles

Trees are used in various applications:
- File systems (directories and files)
- Database indexing
- Syntax trees in compilers
- Network routing algorithms
- DOM (Document Object Model) in HTML

## Tree Terminology

- **Node**: Basic element of a tree, which may contain data and references to other nodes
- **Root**: The topmost node of a tree, which has no parent
- **Parent**: A node that has one or more child nodes
- **Child**: A node that has a parent node
- **Leaf/External Node**: A node with no children
- **Internal Node**: A node with at least one child
- **Edge**: Connection between two nodes
- **Sibling**: Nodes that share the same parent
- **Depth of a Node**: Length of the path from the root to the node
- **Height of a Node**: Length of the longest path from the node to a leaf
- **Height of a Tree**: Height of the root node
- **Level**: Set of nodes at the same depth
- **Subtree**: A tree consisting of a node and all its descendants

## Types of Trees

### Binary Trees

A binary tree is a tree in which each node has at most two children, referred to as the left child and the right child.

#### Types of Binary Trees:

1. **Full Binary Tree**: Every node has either 0 or 2 children (no node has exactly 1 child)
2. **Complete Binary Tree**: All levels are filled except possibly the last one, which is filled from left to right
3. **Perfect Binary Tree**: All internal nodes have exactly 2 children and all leaf nodes are at the same level
4. **Balanced Binary Tree**: The height of the left and right subtrees of any node differ by at most 1
5. **Degenerate/Pathological Tree**: Every parent node has only one child (essentially a linked list)

#### Basic Binary Tree Node Implementation:

```cpp
template <typename T>
struct TreeNode {
    T data;
    TreeNode* left;
    TreeNode* right;
    
    TreeNode(const T& value) : data(value), left(nullptr), right(nullptr) {}
};
```

### Binary Search Trees

A Binary Search Tree (BST) is a binary tree with the following properties:
- The left subtree of a node contains only nodes with keys less than the node's key
- The right subtree of a node contains only nodes with keys greater than the node's key
- Both the left and right subtrees are also binary search trees

#### Operations on BST:

1. **Search**: Find if a key exists in the BST
2. **Insert**: Add a new node to the BST
3. **Delete**: Remove a node from the BST
4. **Find Min/Max**: Find the minimum/maximum key in the BST
5. **Successor/Predecessor**: Find the next/previous node in an in-order traversal

#### BST Implementation:

```cpp
template <typename T>
class BinarySearchTree {
private:
    struct Node {
        T key;
        Node* left;
        Node* right;
        
        Node(const T& value) : key(value), left(nullptr), right(nullptr) {}
    };
    
    Node* root;
    
    // Helper functions (implementation details omitted for brevity)
    Node* insertRecursive(Node* node, const T& key);
    Node* searchRecursive(Node* node, const T& key);
    Node* deleteRecursive(Node* node, const T& key);
    Node* findMin(Node* node);
    void inorderTraversal(Node* node);
    void destroyTree(Node* node);

public:
    BinarySearchTree() : root(nullptr) {}
    ~BinarySearchTree() { destroyTree(root); }
    
    void insert(const T& key) { root = insertRecursive(root, key); }
    bool search(const T& key) { return searchRecursive(root, key) != nullptr; }
    void remove(const T& key) { root = deleteRecursive(root, key); }
    void inorder() { inorderTraversal(root); }
};
```

### AVL Trees

AVL trees are self-balancing binary search trees. In an AVL tree, the heights of the two child subtrees of any node differ by at most one. If at any time they differ by more than one, rebalancing is done to restore this property.

#### Balancing Operations:

1. **Left Rotation**: Used when the right subtree is heavier
2. **Right Rotation**: Used when the left subtree is heavier
3. **Left-Right Rotation**: Left rotation on the left child followed by a right rotation on the node
4. **Right-Left Rotation**: Right rotation on the right child followed by a left rotation on the node

#### AVL Tree Time Complexity:
- Search: O(log n)
- Insert: O(log n)
- Delete: O(log n)

### Red-Black Trees

Red-Black trees are another type of self-balancing binary search tree. Each node in a Red-Black tree has an extra attribute representing its color (either red or black), which is used to ensure that the tree remains balanced during insertions and deletions.

#### Properties of Red-Black Trees:

1. Every node is either red or black
2. The root is black
3. Every leaf (NIL) is black
4. If a node is red, then both its children are black
5. For each node, all paths from the node to descendant leaves contain the same number of black nodes

Red-Black trees are used in the implementation of associative containers in many programming language standard libraries, including C++'s `std::map`, `std::set`, `std::multimap`, and `std::multiset`.

#### Red-Black Tree Time Complexity:
- Search: O(log n)
- Insert: O(log n)
- Delete: O(log n)

### B-Trees

B-Trees are self-balancing search trees designed to work efficiently with disk-based storage systems. Unlike binary trees, a B-Tree node can have more than two children. They are commonly used in databases and file systems.

#### Properties of B-Trees:

1. Every node has at most m children (m is the order of the B-Tree)
2. Every non-leaf node (except root) has at least ⌈m/2⌉ children
3. The root has at least 2 children if it is not a leaf node
4. A non-leaf node with k children contains k-1 keys
5. All leaf nodes appear at the same level

### Tries

A Trie (pronounced "try") is a special type of tree used to store strings. Each node in a trie represents a single character of a string. The root is typically an empty node, and each path from the root to a marked node represents a word or string.

#### Features of Tries:

1. Fast retrieval of data, especially for prefix matching
2. Space-efficient for storing strings with common prefixes
3. Used in autocomplete features, spell checkers, and IP routing tables

## Tree Implementations in C++

### Custom Tree Implementation

For general-purpose trees with any number of children per node, a common approach is to use a vector or list to store child pointers:

```cpp
template <typename T>
class Tree {
private:
    struct Node {
        T data;
        std::vector<Node*> children;
        
        Node(const T& value) : data(value) {}
        ~Node() {
            for (Node* child : children) {
                delete child;
            }
        }
    };
    
    Node* root;
    
    // Helper functions (implementation details omitted for brevity)
    void destroyTree(Node* node);

public:
    Tree() : root(nullptr) {}
    Tree(const T& rootData) : root(new Node(rootData)) {}
    ~Tree() { destroyTree(root); }
    
    // Tree operations (add child, remove, find, etc.)
    void addChild(const T& parentData, const T& childData);
    void removeNode(const T& data);
    bool findNode(const T& data);
    // Traversal methods
    void depthFirstTraversal();
    void breadthFirstTraversal();
};
```

### C++ Standard Library Tree Containers

The C++ Standard Library doesn't provide a direct tree implementation, but it offers several tree-based associative containers that are typically implemented as balanced binary search trees (usually Red-Black trees).

#### std::set

`std::set` is an ordered container that contains unique elements. Elements are sorted in ascending order according to a comparison function.

```cpp
#include <set>
#include <iostream>

int main() {
    std::set<int> mySet;
    
    // Insert elements
    mySet.insert(10);
    mySet.insert(20);
    mySet.insert(30);
    mySet.insert(10); // Duplicate, won't be inserted
    
    // Check if an element exists
    if (mySet.find(20) != mySet.end()) {
        std::cout << "Found 20" << std::endl;
    }
    
    // Remove an element
    mySet.erase(20);
    
    // Iterate through the set
    for (const auto& element : mySet) {
        std::cout << element << " ";
    }
    // Output: 10 30
    
    return 0;
}
```

##### Member Functions:

| Function | Description | Time Complexity |
|----------|-------------|----------------|
| `insert(value)` | Inserts an element | O(log n) |
| `erase(value)` | Removes an element | O(log n) |
| `find(value)` | Returns iterator to element | O(log n) |
| `count(value)` | Returns count of elements (0 or 1) | O(log n) |
| `lower_bound(value)` | Returns iterator to first element not less than value | O(log n) |
| `upper_bound(value)` | Returns iterator to first element greater than value | O(log n) |
| `size()` | Returns number of elements | O(1) |
| `empty()` | Checks if container is empty | O(1) |
| `clear()` | Removes all elements | O(n) |

#### std::map

`std::map` is an ordered container that stores key-value pairs with unique keys. Elements are sorted by key in ascending order.

```cpp
#include <map>
#include <string>
#include <iostream>

int main() {
    std::map<int, std::string> myMap;
    
    // Insert elements
    myMap[1] = "One";
    myMap[2] = "Two";
    myMap.insert({3, "Three"});
    
    // Access elements
    std::cout << "myMap[2] = " << myMap[2] << std::endl;
    
    // Modify elements
    myMap[2] = "Modified Two";
    
    // Check if a key exists
    if (myMap.find(3) != myMap.end()) {
        std::cout << "Key 3 exists with value: " << myMap[3] << std::endl;
    }
    
    // Remove an element
    myMap.erase(2);
    
    // Iterate through the map
    for (const auto& pair : myMap) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }
    // Output:
    // 1: One
    // 3: Three
    
    return 0;
}
```

##### Member Functions:

| Function | Description | Time Complexity |
|----------|-------------|----------------|
| `operator[key]` | Access or insert element | O(log n) |
| `at(key)` | Access element with bounds checking | O(log n) |
| `insert({key, value})` | Inserts a key-value pair | O(log n) |
| `erase(key)` | Removes element with specified key | O(log n) |
| `find(key)` | Returns iterator to element with key | O(log n) |
| `count(key)` | Returns count of elements with key (0 or 1) | O(log n) |
| `lower_bound(key)` | Returns iterator to first element not less than key | O(log n) |
| `upper_bound(key)` | Returns iterator to first element greater than key | O(log n) |
| `size()` | Returns number of elements | O(1) |
| `empty()` | Checks if container is empty | O(1) |
| `clear()` | Removes all elements | O(n) |

#### std::multiset

`std::multiset` is similar to `std::set` but allows duplicate elements.

```cpp
#include <set>
#include <iostream>

int main() {
    std::multiset<int> myMultiset;
    
    // Insert elements
    myMultiset.insert(10);
    myMultiset.insert(20);
    myMultiset.insert(10); // Duplicate, will be inserted
    
    // Count occurrences of an element
    std::cout << "Count of 10: " << myMultiset.count(10) << std::endl; // Output: 2
    
    // Erase one occurrence of an element
    myMultiset.erase(myMultiset.find(10));
    
    // Erase all occurrences of an element
    myMultiset.erase(10);
    
    return 0;
}
```

#### std::multimap

`std::multimap` is similar to `std::map` but allows duplicate keys.

```cpp
#include <map>
#include <string>
#include <iostream>

int main() {
    std::multimap<int, std::string> myMultimap;
    
    // Insert elements
    myMultimap.insert({1, "One"});
    myMultimap.insert({2, "Two"});
    myMultimap.insert({1, "Another One"}); // Duplicate key, will be inserted
    
    // Count occurrences of a key
    std::cout << "Count of key 1: " << myMultimap.count(1) << std::endl; // Output: 2
    
    // Find all values associated with a key
    auto range = myMultimap.equal_range(1);
    for (auto it = range.first; it != range.second; ++it) {
        std::cout << it->first << ": " << it->second << std::endl;
    }
    
    return 0;
}
```

## Tree Traversal Algorithms

Tree traversal refers to the process of visiting each node in a tree exactly once. There are two main categories of traversal algorithms:

### Depth-First Traversals

Depth-first traversals explore as far as possible along each branch before backtracking.

#### In-order Traversal (Left-Root-Right)

```cpp
template <typename T>
void inorderTraversal(TreeNode<T>* node) {
    if (node == nullptr) return;
    
    inorderTraversal(node->left);  // Visit left subtree
    std::cout << node->data << " "; // Visit root
    inorderTraversal(node->right); // Visit right subtree
}
```

- Time Complexity: O(n)
- Space Complexity: O(h) where h is the height of the tree
- For a BST, in-order traversal gives nodes in ascending order

#### Pre-order Traversal (Root-Left-Right)

```cpp
template <typename T>
void preorderTraversal(TreeNode<T>* node) {
    if (node == nullptr) return;
    
    std::cout << node->data << " "; // Visit root
    preorderTraversal(node->left);  // Visit left subtree
    preorderTraversal(node->right); // Visit right subtree
}
```

- Time Complexity: O(n)
- Space Complexity: O(h)
- Used for creating a copy of a tree or getting prefix expression of an expression tree

#### Post-order Traversal (Left-Right-Root)

```cpp
template <typename T>
void postorderTraversal(TreeNode<T>* node) {
    if (node == nullptr) return;
    
    postorderTraversal(node->left);  // Visit left subtree
    postorderTraversal(node->right); // Visit right subtree
    std::cout << node->data << " ";  // Visit root
}
```

- Time Complexity: O(n)
- Space Complexity: O(h)
- Used for deleting a tree or getting postfix expression of an expression tree

### Breadth-First Traversal

Breadth-first traversal (also known as level-order traversal) visits all nodes at the same depth before moving to nodes at the next depth level.

```cpp
template <typename T>
void levelOrderTraversal(TreeNode<T>* root) {
    if (root == nullptr) return;
    
    std::queue<TreeNode<T>*> q;
    q.push(root);
    
    while (!q.empty()) {
        TreeNode<T>* node = q.front();
        q.pop();
        
        std::cout << node->data << " ";
        
        if (node->left != nullptr) q.push(node->left);
        if (node->right != nullptr) q.push(node->right);
    }
}
```

- Time Complexity: O(n)
- Space Complexity: O(w) where w is the maximum width of the tree
- Used for finding the shortest path or creating a level-order traversal

## Time Complexity Analysis

Here's a summary of time complexities for common operations on different types of trees:

| Operation | Binary Search Tree (Average) | Binary Search Tree (Worst) | AVL Tree | Red-Black Tree | B-Tree |
|-----------|------------------------------|----------------------------|----------|----------------|--------|
| Search    | O(log n)                     | O(n)                       | O(log n) | O(log n)       | O(log n) |
| Insert    | O(log n)                     | O(n)                       | O(log n) | O(log n)       | O(log n) |
| Delete    | O(log n)                     | O(n)                       | O(log n) | O(log n)       | O(log n) |
| Find Min  | O(log n)                     | O(n)                       | O(log n) | O(log n)       | O(log n) |
| Find Max  | O(log n)                     | O(n)                       | O(log n) | O(log n)       | O(log n) |

For C++ Standard Library containers:

| Operation | std::set / std::map | std::unordered_set / std::unordered_map |
|-----------|---------------------|----------------------------------------|
| Insert    | O(log n)            | O(1) average, O(n) worst               |
| Delete    | O(log n)            | O(1) average, O(n) worst               |
| Search    | O(log n)            | O(1) average, O(n) worst               |

## Practice Problems

Here are some common tree-related problems for practice, ranging from easy to hard:

### Easy:
1. **Binary Tree Traversal**: Implement in-order, pre-order, and post-order traversals.
2. **Maximum Depth of Binary Tree**: Find the maximum depth (height) of a binary tree.
3. **Path Sum**: Given a sum, determine if the tree has a root-to-leaf path that adds up to this sum.
4. **Invert Binary Tree**: Invert a binary tree (mirror it).

### Medium:
1. **Validate Binary Search Tree**: Determine if a binary tree is a valid BST.
2. **Lowest Common Ancestor**: Find the lowest common ancestor of two nodes in a binary tree.
3. **Binary Tree Level Order Traversal**: Return the level order traversal of nodes' values.
4. **Construct Binary Tree from Preorder and Inorder Traversal**: Rebuild a tree from traversal results.

### Hard:
1. **Serialize and Deserialize Binary Tree**: Design an algorithm to serialize and deserialize a binary tree.
2. **Binary Tree Maximum Path Sum**: Find the maximum path sum in a binary tree.
3. **Recover Binary Search Tree**: Recover a BST where two nodes have been swapped.
4. **Binary Tree Cameras**: Place cameras to monitor all nodes with minimum number of cameras.

## Advanced Tree Concepts

### Segment Trees
Segment trees are a tree data structure used for storing information about intervals, or segments. They allow querying which of the stored segments contain a given point, and are used for range queries (e.g., find the minimum/maximum element in a range).

### Fenwick Trees (Binary Indexed Trees)
Fenwick trees provide a way to represent an array of numbers in an array, allowing prefix sums to be computed efficiently. They are used for dynamic cumulative frequency tables.

### Splay Trees
Splay trees are self-adjusting binary search trees with the additional property that recently accessed elements are quick to access again. They perform basic operations such as insertion, look-up, and removal in O(log n) amortized time.

## References

- [C++ Reference - std::map](https://cplusplus.com/reference/map/map/)
- [C++ Reference - std::set](https://cplusplus.com/reference/set/set/)
- [Introduction to Tree Data Structure](https://www.geeksforgeeks.org/introduction-to-tree-data-structure/)
- [Binary Search Tree](https://www.programiz.com/dsa/binary-search-tree)
- [AVL Tree](https://www.programiz.com/dsa/avl-tree)
- [Red-Black Tree](https://www.programiz.com/dsa/red-black-tree)
- [B-Tree](https://www.programiz.com/dsa/b-tree)
