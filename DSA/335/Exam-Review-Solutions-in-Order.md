# Exam Review Solutions (In Practice Exam Order)

---

## 1. Series Sum
**Question:** Calculate \( \sum_{i=0}^{32} (5i + 7) \)

**Solution:**
- \( \sum_{i=0}^{32} (5i + 7) = 5 \sum_{i=0}^{32} i + 7 \times 33 \)
- \( \sum_{i=0}^{32} i = \frac{32 \times 33}{2} = 528 \)
- \( 5 \times 528 + 231 = 2640 + 231 = 2871 \)
- **General formula:**
  \[
  \sum_{k=0}^{n} (a k + b) = a \frac{n(n+1)}{2} + b(n+1)
  \]

---

## 2. Copy Assignment vs Copy Constructor
**Question:** What do you do in copy assignment that you don't do in copy constructor?

**Answer:**
- **Copy assignment:**
  - Check for self-assignment
  - Clean up existing resources
  - Return *this
- **Copy constructor:**
  - No self-assignment check (no existing object)
  - No cleanup needed
  - No return value

---

## 3. Modular Arithmetic
**Question:** Calculate \( 57 \bmod 14 \)

**Solution:**
- \( 57 \div 14 = 4 \) remainder 1
- **Answer:** \( 57 \bmod 14 = 1 \)

---

## 4. Binary Search Tree Operations
**Question:** Given BST with root 27, perform requested operations (e.g., insert, delete, traverse).

**Key Steps:**
- Insert values as per BST rules (left < root < right)
- For deletion:
  - If node has two children: replace with inorder successor (smallest in right subtree), then delete successor
- For traversal: use inorder for sorted order

---

## 5. Greatest Common Divisor (GCD)
**Question:** Calculate \( \gcd(114, 256) \)

**Solution (Euclidean Algorithm):**
- \( 256 \div 114 = 2 \) remainder 28 → \( \gcd(256, 114) = \gcd(114, 28) \)
- \( 114 \div 28 = 4 \) remainder 2 → \( \gcd(114, 28) = \gcd(28, 2) \)
- \( 28 \div 2 = 14 \) remainder 0 → \( \gcd(28, 2) = \gcd(2, 0) \)
- **Final answer:** \( \gcd(114, 256) = 2 \)
- **Formula:**
  \[
  \gcd(a, b) = \gcd(b, a \bmod b)\text{; repeat until } b = 0
  \]

---

## 6. Initialization Lists
**Question:** Name two cases where you must use initialization lists

**Answer:**
1. **Const member variables** (must be initialized at creation)
2. **Reference member variables** (must be bound at creation)
3. (Also: member objects without default constructors, base class constructors)

---

## 7. AVL Tree RR Rotation
**Question:** Explain and diagram an RR (Right-Right) rotation

**Answer:**
- **When:** Node has BF = +2 (left-heavy), left child has BF = +1 or 0
- **How:**
  - Left child becomes new root
  - Original node becomes right child
  - Left child's right subtree becomes original node's left subtree
- **Diagram:**
  ```
      X (+2)
     /
    Y (+1)
   /
  Z
  // After RR rotation:
    Y
   / \
  Z   X
  ```

---

## 8. Big-O Notation
**Question:** What is Big-Omega (Ω) notation and provide an example

**Answer:**
- **Big-Omega (Ω):** Lower bound for an algorithm's running time
- **Example:** Linear search best case: Ω(1) (find in first position)
- **Definition:**
  \[
  f(n) = \Omega(g(n)) \text{ if } \exists c > 0, n_0 \text{ s.t. } f(n) \geq c g(n) \forall n \geq n_0
  \]

---

## 9. BST Node Deletion (Two Children)
**Question:** Explain how to remove a node with two children from BST

**Answer:**
1. Find inorder successor (smallest in right subtree) or predecessor (largest in left)
2. Replace node's value with successor/predecessor
3. Recursively delete successor/predecessor

---

## Coding Problem 1: AVL Tree Operations
**1.1 Insert 30:**
- Insert as root
**1.2 Delete 35:**
- Remove 35, rebalance if needed (check BFs, perform rotation if |BF| > 1)
**1.3 Balance Factors:**
- For each node: BF = height(left) - height(right)
**1.4 Rotations Needed:**
- Use AVL rotation table:
  - +2/+1 or 0: RR
  - +2/-1: LR
  - -2/-1 or 0: LL
  - -2/+1: RL

---

## Coding Problem 2: Vector Search Function
**2.1 Implementation:**
```cpp
#include <vector>
bool findValue(const std::vector<int>& v, int x) {
    for (int val : v) {
        if (val == x) return true;
    }
    return false;
}
```
**2.2 Time Complexity:**
- Worst case (O): O(n)
- Best case (Ω): Ω(1)
- Average case: O(n)

---

## Key Formulas to Memorize
- **Arithmetic series:**
  \[
  S_n = \frac{n}{2} (2a_1 + (n-1)d)\text{ or }S_n = \frac{n}{2}(a_1 + a_n)
  \]
- **Sum of first n integers:**
  \[
  1 + 2 + \ldots + n = \frac{n(n+1)}{2}
  \]
- **Euclidean GCD:**
  \[
  \gcd(a, b) = \gcd(b, a \bmod b)
  \]
- **Big-Omega definition:**
  \[
  f(n) = \Omega(g(n)) \text{ if } \exists c > 0, n_0 \text{ s.t. } f(n) \geq c g(n) \forall n \geq n_0
  \]
- **AVL Rotation Table:**
  | Node BF | Child BF | Rotation |
  |---------|----------|----------|
  | +2      | +1/0     | RR       |
  | +2      | -1       | LR       |
  | -2      | -1/0     | LL       |
  | -2      | +1       | RL       | 