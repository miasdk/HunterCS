# Exam Cram Cheatsheet

---

## 🧮 Arithmetic Series
- **Sum of first n terms:**
  \[
  S_n = \frac{n}{2} (2a_1 + (n-1)d)
  \]
- **Sum of first n integers:**
  \[
  1 + 2 + \ldots + n = \frac{n(n+1)}{2}
  \]
- **General linear sum:**
  \[
  \sum_{k=0}^{n} (a k + b) = a \frac{n(n+1)}{2} + b(n+1)
  \]

---

## 🔢 Euclidean Algorithm for GCD
- **Process:**
  1. Divide a by b, get remainder r
  2. Replace a with b, b with r
  3. Repeat until r = 0
  4. Last nonzero remainder is the GCD
- **Formula:**
  \[
  \gcd(a, b) = \gcd(b, a \bmod b)
  \]
- **Example:**
  \(
  \gcd(114, 256) = \gcd(256, 114) = \gcd(114, 28) = \gcd(28, 2) = \gcd(2, 0) = 2
  \)

---

## 🧩 Modular Arithmetic
- **a mod n = remainder when a is divided by n**
- **Properties:**
  - (a + b) mod n = [(a mod n) + (b mod n)] mod n
  - (a × b) mod n = [(a mod n) × (b mod n)] mod n
- **Negative numbers:**
  - (-a) mod n = (n - (a mod n)) mod n
- **Example:**
  - 57 mod 14 = 1

---

## 🌳 BST Deletion (Node with Two Children)
1. Find inorder successor (smallest in right subtree) **or** predecessor (largest in left)
2. Replace node's value with that value
3. Recursively delete the successor/predecessor

---

## 🌲 AVL Rotations Table
| Node BF | Child BF | Rotation | What to do                |
|---------|----------|----------|---------------------------|
| +2      | +1/0     | RR       | Right at node             |
| +2      | -1       | LR       | Left at child, right at node |
| -2      | -1/0     | LL       | Left at node              |
| -2      | +1       | RL       | Right at child, left at node  |
- **BF = Height(Left) - Height(Right)**
- **+ = left-heavy, - = right-heavy**

---

## 🏷️ Big-O, Big-Omega, Big-Theta
- **Big-O (O):** Upper bound (worst case)
- **Big-Omega (Ω):** Lower bound (best case or at least this fast)
- **Big-Theta (Θ):** Tight bound (both upper and lower)
- **Example:** Linear search: O(n) worst, Ω(1) best

---

## 💻 C++ Copy Assignment Example
```cpp
class MyArray {
    int* data;
    int size;
public:
    MyArray& operator=(const MyArray& other) {
        if (this != &other) {
            delete[] data;
            size = other.size;
            data = new int[size];
            for (int i = 0; i < size; ++i)
                data[i] = other.data[i];
        }
        return *this;
    }
};
```
- **Key:** Self-assignment check, cleanup, deep copy, return *this

---

## 🔍 Vector Search (Linear Search)
```cpp
bool findValue(const std::vector<int>& v, int x) {
    for (int val : v) {
        if (val == x) return true;
    }
    return false;
}
```
- **Worst case:** O(n)
- **Best case:** Ω(1)

---

## ⭐ Exam Tips
- Show all work, even for "easy" math
- Draw diagrams for trees and rotations
- For AVL, check balance factors after every operation
- For BST deletion, use successor or predecessor
- For copy assignment, always check for self-assignment
- For Big-O/Big-Omega, state what case you mean (best/worst)

---

## 🍀 GOOD LUCK ON YOUR EXAM! 🍀
You've got this! Stay calm, read each question carefully, and trust your preparation. If you get stuck, write what you know and move on—then come back. You're ready to ace it! 