(Due to technical issues, the search service is temporarily unavailable.)

### AVL Trees

An **AVL tree** (named after its inventors Adelson-Velsky and Landis) is a self-balancing binary search tree (BST). In an AVL tree, the heights of the two child subtrees of any node differ by at most one. If at any point this balance condition is violated, the tree performs rotations to restore balance.

#### Key Properties of AVL Trees:

1\. **Balanced**: The height difference (balance factor) between the left and right subtrees of any node is at most 1.

2\. **Efficient Operations**: Due to its balanced nature, AVL trees guarantee \(O(\log n)\) time complexity for search, insert, and delete operations.

3\. **Balance Factor**: For any node, the balance factor is calculated as:

   \[

   \text{Balance Factor} = \text{Height of Left Subtree} - \text{Height of Right Subtree}

   \]

   The balance factor must be \(-1\), \(0\), or \(1\).

---

### Types of AVL Rotations

When an insertion or deletion causes the AVL tree to become unbalanced, rotations are performed to restore balance. There are four types of rotations:

#### 1. **Left Rotation (LL Rotation)**

   - **Scenario**: The tree is unbalanced due to a node in the **right subtree of the right child**.

   - **Action**: Rotate the unbalanced node to the left.

   - **Example**:

     ```

     Unbalanced Tree:

           A

             B

               C

     After Left Rotation:

           B

          /

         A   C

     ```

#### 2. **Right Rotation (RR Rotation)**

   - **Scenario**: The tree is unbalanced due to a node in the **left subtree of the left child**.

   - **Action**: Rotate the unbalanced node to the right.

   - **Example**:

     ```

     Unbalanced Tree:

           C

          /

         B

        /

       A

     After Right Rotation:

           B

          /

         A   C

     ```

#### 3. **Left-Right Rotation (LR Rotation)**

   - **Scenario**: The tree is unbalanced due to a node in the **right subtree of the left child**.

   - **Action**: First, perform a left rotation on the left child, then a right rotation on the unbalanced node.

   - **Example**:

     ```

     Unbalanced Tree:

           C

          /

         A

           B

     After Left Rotation on A:

           C

          /

         B

        /

       A

     After Right Rotation on C:

           B

          /

         A   C

     ```

#### 4. **Right-Left Rotation (RL Rotation)**

   - **Scenario**: The tree is unbalanced due to a node in the **left subtree of the right child**.

   - **Action**: First, perform a right rotation on the right child, then a left rotation on the unbalanced node.

   - **Example**:

     ```

     Unbalanced Tree:

         A

           C

          /

         B

     After Right Rotation on C:

         A

           B

             C

     After Left Rotation on A:

           B

          /

         A   C

     ```

---

### Summary of Rotations

| **Rotation Type** | **Unbalance Scenario**               | **Action**                                                                 |

|--------------------|--------------------------------------|----------------------------------------------------------------------------|

| **LL Rotation**    | Right subtree of the right child     | Single left rotation on the unbalanced node                                |

| **RR Rotation**    | Left subtree of the left child       | Single right rotation on the unbalanced node                               |

| **LR Rotation**    | Right subtree of the left child      | Left rotation on the left child, then right rotation on the unbalanced node|

| **RL Rotation**    | Left subtree of the right child      | Right rotation on the right child, then left rotation on the unbalanced node|

---

### Why Rotations Are Important

Rotations ensure that the AVL tree remains balanced after insertions and deletions, maintaining the \(O(\log n)\) time complexity for operations. Without rotations, the tree could degenerate into a linked list, resulting in \(O(n)\) time complexity for operations.

Let me know if you'd like further clarification or examples!