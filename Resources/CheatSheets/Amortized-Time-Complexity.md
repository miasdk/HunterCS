# Amortized Time Complexity Cheat Sheet

## Overview
Amortized time complexity is the **average time per operation** over a sequence of operations, even if some individual operations are expensive. This is particularly useful for understanding the performance of dynamic data structures.

---

## Table of Amortized Time Complexities

### **Dynamic Array (`std::vector`)**
| Operation          | Amortized Time Complexity |
|--------------------|---------------------------|
| `push_back`        | O(1)                      |
| `pop_back`         | O(1)                      |
| `insert` (middle)  | O(n)                      |
| `erase` (middle)   | O(n)                      |

---

### **Hash Table (`std::unordered_map`, `std::unordered_set`)**
| Operation | Amortized Time Complexity |
|-----------|---------------------------|
| Insertion | O(1)                      |
| Deletion  | O(1)                      |
| Lookup    | O(1)                      |

---

### **Disjoint Set Union (Union-Find)**
| Operation | Amortized Time Complexity |
|-----------|---------------------------|
| Union     | O(α(n))                   |
| Find      | O(α(n))                   |

---

### **Trees**
#### **Splay Tree**
| Operation | Amortized Time Complexity |
|-----------|---------------------------|
| Insertion | O(log n)                  |
| Deletion  | O(log n)                  |
| Search    | O(log n)                  |

#### **AVL Tree**
| Operation | Amortized Time Complexity |
|-----------|---------------------------|
| Insertion | O(log n)                  |
| Deletion  | O(log n)                  |
| Search    | O(log n)                  |

#### **Red-Black Tree**
| Operation | Amortized Time Complexity |
|-----------|---------------------------|
| Insertion | O(log n)                  |
| Deletion  | O(log n)                  |
| Search    | O(log n)                  |

#### **B-Tree**
| Operation | Amortized Time Complexity |
|-----------|---------------------------|
| Insertion | O(log n)                  |
| Deletion  | O(log n)                  |
| Search    | O(log n)                  |

---

### **Fibonacci Heap**
| Operation    | Amortized Time Complexity |
|--------------|---------------------------|
| Insert       | O(1)                      |
| Extract-Min  | O(log n)                  |
| Decrease-Key | O(1)                      |
| Merge        | O(1)                      |

---

### **Priority Queue (`std::priority_queue`)**
| Operation | Amortized Time Complexity |
|-----------|---------------------------|
| Push      | O(log n)                  |
| Pop       | O(log n)                  |
| Top       | O(1)                      |

---

### **Deque (`std::deque`)**
| Operation    | Amortized Time Complexity |
|--------------|---------------------------|
| `push_back`  | O(1)                      |
| `push_front` | O(1)                      |
| `pop_back`   | O(1)                      |
| `pop_front`  | O(1)                      |

---

### **Stack (`std::stack`)**
| Operation | Amortized Time Complexity |
|-----------|---------------------------|
| Push      | O(1)                      |
| Pop       | O(1)                      |
| Top       | O(1)                      |

---

### **Queue (`std::queue`)**
| Operation | Amortized Time Complexity |
|-----------|---------------------------|
| Push      | O(1)                      |
| Pop       | O(1)                      |
| Front     | O(1)                      |

---

## References
- [Introduction to Algorithms (CLRS)](https://mitpress.mit.edu/books/introduction-algorithms)
- [GeeksforGeeks: Amortized Analysis](https://www.geeksforgeeks.org/amortized-analysis/)