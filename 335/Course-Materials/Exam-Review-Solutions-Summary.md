# Exam Review Solutions Summary

## 1. AVL Tree Insertion Example (with Balance Factors)

**Insert [30, 20, 40, 10, 25, 35, 50, 5] into an empty AVL tree:**

### Step-by-Step Insertions

1. Insert 30
```
30 (BF = 0)
```
2. Insert 20
```
  30 (BF = 1)
 /
20 (BF = 0)
```
3. Insert 40
```
  30 (BF = 0)
 /  \
20   40
(BF=0) (BF=0)
```
4. Insert 10
```
    30 (BF = 1)
   /  \
 20   40 (BF=0)
(BF=1)
 /
10 (BF=0)
```
5. Insert 25
```
    30 (BF = 1)
   /  \
 20   40 (BF=0)
(BF=0)
 / \
10 25
(BF=0) (BF=0)
```
6. Insert 35
```
    30 (BF = -1)
   /  \
 20   40 (BF=1)
(BF=0) / \
10 25 35
(BF=0) (BF=0)
```
7. Insert 50
```
    30 (BF = 0)
   /  \
 20   40 (BF=0)
(BF=0) / \
10 25 35 50
(BF=0) (BF=0)
```
8. Insert 5
```
      30 (BF = 1)
     /  \
   20   40 (BF=0)
  (BF=1) / \
10 25 35 50
(BF=1) (BF=0) (BF=0)
/
5 (BF=0)
```
- **After each insertion, compute BF for the inserted node and all ancestors up to the root.**
- **A node is unbalanced if |BF| > 1.**
- **In this sequence, no rotation is needed.**

---

## 2. AVL Rotation Decision Table (Memorize!)

| Node BF | Child BF | Rotation | Pattern | What to do                |
|---------|----------|----------|---------|---------------------------|
| +2      | +1 or 0  | RR       | ↙↙      | Right at node             |
| +2      | –1       | LR       | ↙↘      | Left at child, right at node |
| –2      | –1 or 0  | LL       | ↘↘      | Left at node              |
| –2      | +1       | RL       | ↘↙      | Right at child, left at node  |

- **+2 = left-heavy node**
- **–2 = right-heavy node**
- **Child BF tells you if the child is heavy on its left (positive) or right (negative)**
- **Same direction = single rotation; different = double rotation**

---

## 3. Euclidean Algorithm for GCD (Memorize!)

> For any integers a and b (a > b):
> 
> \[
> \gcd(a, b) = \gcd(b, a \bmod b)
> \]
> Repeat until b = 0. Then, \( \gcd(a, 0) = a \).

**Example:**
\(
\gcd(114, 256) = \gcd(256, 114) = \gcd(114, 28) = \gcd(28, 2) = \gcd(2, 0) = 2
\)

---

## 4. Arithmetic Series Formula (Memorize!)

- **Sum of first n terms (first term a₁, common difference d):**
  \[
  S_n = \frac{n}{2} (2a_1 + (n-1)d)
  \]
- **Or, if you know the last term aₙ:**
  \[
  S_n = \frac{n}{2} (a_1 + a_n)
  \]
- **Sum of first n positive integers:**
  \[
  1 + 2 + 3 + \ldots + n = \frac{n(n+1)}{2}
  \]

---

## 5. Vector Search Coding Problem (with Complexity)

**C++ Linear Search Function:**
```cpp
#include <vector>
bool findValue(const std::vector<int>& v, int x) {
    for (int val : v) {
        if (val == x) return true;
    }
    return false;
}
```

**Time Complexity:**
- **Worst case (Big-O):** O(n) — must check every element
- **Best case (Big-Omega):** Ω(1) — find it in the first position
- **Average case:** O(n)

**Explanation:**
- In the best case, the value is at the first position.
- In the worst case, it's not present or at the end, so every element is checked.

---

## 6. Big-O, Big-Omega, Big-Theta (Quick Reference)

| Notation | Meaning      | Bound Type | Example (Linear Search) |
|----------|-------------|------------|-------------------------|
| O        | Upper bound | Worst-case | O(n)                    |
| Ω        | Lower bound | Best-case  | Ω(1)                    |
| Θ        | Tight bound | Both       | Θ(n)                    |

---

**Good luck! Review this summary and you'll be ready for your test!** 