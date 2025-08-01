# Quick Complexity Cheat Sheet
*One-Page Reference for Technical Interviews*

## 🎯 **Big-O Growth Rates** (Best to Worst)
```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

---

## 📊 **Data Structure Operations**

### **Arrays/Vectors**
| Operation | Time | Notes |
|-----------|------|-------|
| Access by index | O(1) | Direct memory access |
| Search unsorted | O(n) | Must check each element |
| Insert at end | O(1) amortized | May need reallocation |
| Insert at position | O(n) | Must shift elements |
| Delete at end | O(1) | Just update size |
| Delete at position | O(n) | Must shift elements |

### **Hash Tables (unordered_map/set)**
| Operation | Average | Worst | Notes |
|-----------|---------|-------|-------|
| Insert | O(1) | O(n) | Worst case: all collisions |
| Search | O(1) | O(n) | Depends on hash quality |
| Delete | O(1) | O(n) | Same as search + removal |

### **Balanced Trees (map/set)**
| Operation | Time | Notes |
|-----------|------|-------|
| Insert | O(log n) | Always guaranteed |
| Search | O(log n) | Binary search in tree |
| Delete | O(log n) | May need rebalancing |
| Min/Max | O(log n) | Traverse to leftmost/rightmost |

### **Binary Heaps (priority_queue)**
| Operation | Time | Notes |
|-----------|------|-------|
| Insert | O(log n) | Bubble up |
| Extract min/max | O(log n) | Bubble down |
| Peek min/max | O(1) | Root element |
| Build heap | O(n) | **Not O(n log n)!** |

---

## 🔄 **Algorithm Complexities**

### **Sorting Algorithms**
| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|---------|
| **Quicksort** | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| **Mergesort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| **Heapsort** | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| **Introsort** | O(n log n) | O(n log n) | O(n log n) | O(log n) | No |

### **Search Algorithms**
| Algorithm | Time | Space | Prerequisites |
|-----------|------|-------|---------------|
| **Linear search** | O(n) | O(1) | None |
| **Binary search** | O(log n) | O(1) | Sorted array |
| **Hash table lookup** | O(1) avg | O(1) | Good hash function |

### **Graph Algorithms**
| Algorithm | Time | Space | Use Case |
|-----------|------|-------|----------|
| **BFS** | O(V + E) | O(V) | Shortest path (unweighted) |
| **DFS** | O(V + E) | O(V) | Cycle detection, topological sort |
| **Dijkstra** | O((V+E) log V) | O(V) | Shortest path (weighted, no negative) |
| **Prim's MST** | O(E log V) | O(V) | Minimum spanning tree |
| **Kruskal's MST** | O(E log V) | O(V) | Minimum spanning tree |

---

## ⚡ **Quick Pattern Recognition**

### **When to Use Each Complexity**

#### **O(1) - Constant Time**
- Hash table operations
- Array access by index
- Stack/queue push/pop

#### **O(log n) - Logarithmic**
- Binary search in sorted array
- Balanced tree operations (insert/search/delete)
- Heap operations

#### **O(n) - Linear**
- Single pass through array
- Counting elements
- Building hash table
- **Build heap from array**

#### **O(n log n) - Linearithmic**
- Efficient sorting algorithms
- Divide-and-conquer algorithms
- Graph algorithms with heaps

#### **O(n²) - Quadratic**
- Nested loops over same data
- Bubble sort, selection sort
- Naive closest pair algorithms

---

## 🚨 **Common Interview Traps**

### **1. Build Heap is O(n), NOT O(n log n)**
```cpp
// This is O(n), not O(n log n)!
std::make_heap(vec.begin(), vec.end());
```

### **2. Hash Table Worst Case is O(n)**
- All elements hash to same bucket
- Becomes linked list traversal

### **3. Array vs Linked List**
| Operation | Array | Linked List |
|-----------|-------|-------------|
| Access by index | O(1) | O(n) |
| Insert at beginning | O(n) | O(1) |
| Insert at end | O(1) | O(1) or O(n) |

### **4. Space Complexity Gotchas**
- **Recursion**: O(depth) space for call stack
- **Iterative**: Often O(1) space
- **Memoization**: O(state space) additional memory

---

## 🎯 **Interview Quick Checks**

### **Before Implementing**
1. **What's the input size?** (n = ?)
2. **What complexity is expected?** 
3. **Is there a sorted property I can exploit?**
4. **Can I use a hash table for O(1) lookup?**
5. **Is this a known pattern?** (Two pointers, sliding window, etc.)

### **After Implementing**
1. **What's my time complexity?**
2. **What's my space complexity?**
3. **Can I do better?**
4. **What are the edge cases?**
5. **How does this scale?**

---

**💡 Pro Tip**: When in doubt during interviews, state your assumptions about complexity and ask if that's acceptable before diving into implementation! 