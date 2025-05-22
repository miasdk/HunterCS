# Complete Time Complexity Reference - Exam Topics Only

## Table of Contents

### **1. Quick Reference - Most Tested**
- [1.1 Must-Know Complexities](#11-must-know-complexities)
- [1.2 Common Exam Traps](#12-common-exam-traps)
- [1.3 Big O Growth Rates](#13-big-o-growth-rates)

### **2. Data Structure Operations**
- [2.1 Hash Tables (unordered_map, unordered_set)](#21-hash-tables-unordered_map-unordered_set)
- [2.2 Binary Search Trees (map, set)](#22-binary-search-trees-map-set)
- [2.3 AVL Trees (Self-Balancing BST)](#23-avl-trees-self-balancing-bst)
- [2.4 Binary Heaps](#24-binary-heaps)
- [2.5 Arrays/Vectors](#25-arraysvectors)

### **3. Sorting Algorithms**
- [3.1 Comparison-Based Sorts](#31-comparison-based-sorts)
- [3.2 Special Cases - Input Dependencies](#32-special-cases---input-dependencies)
- [3.3 Hybrid Sorting (Introsort)](#33-hybrid-sorting-introsort)

### **4. Selection Algorithms**
- [4.1 QuickSelect](#41-quickselect)
- [4.2 Median of Medians](#42-median-of-medians)

### **5. Graph Algorithms**
- [5.1 Graph Traversal (BFS/DFS)](#51-graph-traversal-bfsdfs)
- [5.2 Shortest Path Algorithms](#52-shortest-path-algorithms)
- [5.3 Minimum Spanning Tree](#53-minimum-spanning-tree)
- [5.4 Topological Sort](#54-topological-sort)
- [5.5 Sparse vs Dense Graph Impact](#55-sparse-vs-dense-graph-impact)

### **6. Tree Operations**
- [6.1 General Tree Operations](#61-general-tree-operations)
- [6.2 Splay Trees](#62-splay-trees)

### **7. Dynamic Programming**
- [7.1 Basic DP Patterns](#71-basic-dp-patterns)
- [7.2 Common DP Time Complexities](#72-common-dp-time-complexities)

### **8. Hash Table Design**
- [8.1 Collision Resolution Methods](#81-collision-resolution-methods)
- [8.2 Hash Function Impact](#82-hash-function-impact)
- [8.3 Load Factor Effects](#83-load-factor-effects)

### **9. String Algorithms**
- [9.1 String Search](#91-string-search)
- [9.2 Pattern Matching](#92-pattern-matching)

### **10. Exam Strategy**
- [10.1 Complexity Recognition Patterns](#101-complexity-recognition-patterns)
- [10.2 Quick Decision Framework](#102-quick-decision-framework)
- [10.3 Final Review Checklist](#103-final-review-checklist)

---

## 1. Quick Reference - Most Tested

### 1.1 Must-Know Complexities

**⭐ MEMORIZE THESE FOR EXAM:**

```
Hash Tables:
✅ Find key in unordered_map: O(1) average, O(n) worst
✅ Find VALUE in unordered_map: O(n) - must iterate through all elements
✅ Insert/Delete in hash table: O(1) average, O(n) worst

Binary Search Trees:
✅ Find key in ordered map (BST): O(log n) average, O(n) worst
✅ Insert/Delete in BST: O(log n) average, O(n) worst

Heaps:
✅ Insert/Delete in heap: O(log n)
✅ BuildHeap from array: O(n) ⭐ NOT O(n log n)
✅ Find min/max in heap: O(1)

Sorting:
✅ Quicksort: O(n log n) average, O(n²) worst
✅ Heapsort: O(n log n) ALWAYS (even on sorted input)
✅ Mergesort: O(n log n) ALWAYS
✅ Insertion sort on sorted array: O(n) ⭐
✅ Insertion sort on reverse sorted: O(n²)

Graphs:
✅ BFS/DFS traversal: O(|V| + |E|)
✅ Dijkstra with priority queue: O(|E| log |V|)
✅ Dijkstra simple implementation: O(|V|²)
✅ Kruskal's MST: O(|E| log |V|)
✅ Prim's MST with heap: O(|E| log |V|)
✅ Prim's MST without heap: O(|V|²)
✅ Topological sort: O(|V| + |E|)
✅ Unweighted shortest path (BFS): O(|V| + |E|)

Selection:
✅ QuickSelect: O(n) average, O(n²) worst
✅ Median of Medians: O(n) guaranteed
```

### 1.2 Common Exam Traps

| ❌ **Common Wrong Answer** | ✅ **Correct Answer** | **Why** |
|---------------------------|---------------------|---------|
| Hash table find value: O(1) | **O(n)** | Must check all key-value pairs |
| Heapsort on sorted array: O(n) | **O(n log n)** | Still builds heap and extracts |
| Building heap: O(n log n) | **O(n)** | Mathematical analysis proves O(n) |
| BST always O(log n) | **O(n) worst case** | When tree becomes linked list |
| Quicksort always O(n log n) | **O(n²) worst case** | Poor pivot choices |

### 1.3 Big O Growth Rates

| Complexity | n=100 | n=1,000 | n=10,000 | Performance |
|------------|-------|---------|----------|-------------|
| **O(1)** | 1 | 1 | 1 | Excellent |
| **O(log n)** | 7 | 10 | 13 | Excellent |
| **O(n)** | 100 | 1,000 | 10,000 | Good |
| **O(n log n)** | 700 | 10,000 | 130,000 | Acceptable |
| **O(n²)** | 10,000 | 1,000,000 | 100,000,000 | Poor |

## 2. Data Structure Operations

### 2.1 Hash Tables (unordered_map, unordered_set)

| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| **Insert** | **O(1)** | O(n) | Worst when all keys hash to same bucket |
| **Find key** | **O(1)** | O(n) | Hash directly to bucket |
| **Delete** | **O(1)** | O(n) | Find then remove |
| **Find VALUE** | **O(n)** | **O(n)** | ⭐ Must iterate through all pairs |
| **Update value** | **O(1)** | O(n) | After finding key |
| **Rehashing** | **O(n)** | O(n) | When load factor too high |

**⚠️ EXAM ALERT**: Finding a VALUE (not key) in hash map requires checking all key-value pairs = O(n)

### 2.2 Binary Search Trees (map, set)

| Operation | Average Case | Worst Case | Best Case |
|-----------|--------------|------------|-----------|
| **Insert** | **O(log n)** | O(n) | O(1) |
| **Find key** | **O(log n)** | O(n) | O(1) |
| **Delete** | **O(log n)** | O(n) | O(1) |
| **Min/Max** | **O(log n)** | O(n) | O(1) |
| **In-order traversal** | **O(n)** | O(n) | O(n) |

**Worst case**: Tree degenerates to linked list (inserting sorted data)

### 2.3 AVL Trees (Self-Balancing BST)

| Operation | Guaranteed | Notes |
|-----------|------------|-------|
| **Insert** | **O(log n)** | Max 2 rotations |
| **Find** | **O(log n)** | Height ≤ 1.44 log n |
| **Delete** | **O(log n)** | Max 1 rotation |

### 2.4 Binary Heaps

| Operation | Complexity | Implementation |
|-----------|------------|----------------|
| **Insert** | **O(log n)** | Bubble up |
| **DeleteMin/Max** | **O(log n)** | Replace root, bubble down |
| **FindMin/Max** | **O(1)** | Root element |
| **BuildHeap** | **O(n)** ⭐ | Bottom-up construction |
| **Decrease/Increase Key** | **O(log n)** | Bubble up/down |

**⚠️ EXAM ALERT**: BuildHeap is O(n), NOT O(n log n)!

### 2.5 Arrays/Vectors

| Operation | Complexity | Notes |
|-----------|------------|-------|
| **Access by index** | **O(1)** | Direct memory access |
| **Search (unsorted)** | **O(n)** | Linear scan |
| **Search (sorted)** | **O(log n)** | Binary search |
| **Insert at end** | **O(1)** amortized | May need resize |
| **Insert at position** | **O(n)** | Shift elements |
| **Delete at position** | **O(n)** | Shift elements |

## 3. Sorting Algorithms

### 3.1 Comparison-Based Sorts

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable |
|-----------|-----------|--------------|------------|-------|--------|
| **Quicksort** | **O(n log n)** | **O(n log n)** | **O(n²)** | O(log n) | No |
| **Heapsort** | **O(n log n)** | **O(n log n)** | **O(n log n)** | O(1) | No |
| **Mergesort** | **O(n log n)** | **O(n log n)** | **O(n log n)** | O(n) | Yes |
| **Insertion Sort** | **O(n)** | **O(n²)** | **O(n²)** | O(1) | Yes |
| **Selection Sort** | **O(n²)** | **O(n²)** | **O(n²)** | O(1) | No |

### 3.2 Special Cases - Input Dependencies

| Input Type | Algorithm | Complexity | Why |
|------------|-----------|------------|-----|
| **Already sorted** | Insertion Sort | **O(n)** | Only comparisons, no swaps |
| **Already sorted** | Heapsort | **O(n log n)** | Still builds heap |
| **Reverse sorted** | Insertion Sort | **O(n²)** | Maximum number of swaps |
| **All elements equal** | Quicksort | **O(n²)** | Poor pivot selection |
| **Nearly sorted** | Insertion Sort | **~O(n)** | Few inversions to fix |

**⚠️ EXAM ALERT**: Heapsort is ALWAYS O(n log n), regardless of input!

### 3.3 Hybrid Sorting (Introsort)

| Component | When Used | Complexity |
|-----------|-----------|------------|
| **Quicksort** | Main algorithm | O(n log n) average |
| **Heapsort** | Recursion depth > 2⌊log n⌋ | O(n log n) guaranteed |
| **Insertion Sort** | Subarray size ≤ 16 | O(n) for small subarrays |

**Overall**: O(n log n) worst case guaranteed

## 4. Selection Algorithms

### 4.1 QuickSelect

| Case | Complexity | Notes |
|------|------------|-------|
| **Average** | **O(n)** | Random pivot selection |
| **Worst** | **O(n²)** | Poor pivot choices |
| **Best** | **O(n)** | Good pivot selection |

### 4.2 Median of Medians

| Case | Complexity | Notes |
|------|------------|-------|
| **All cases** | **O(n)** | Guaranteed linear time |

## 5. Graph Algorithms

### 5.1 Graph Traversal (BFS/DFS)

| Algorithm | Complexity | Space | Use Case |
|-----------|------------|-------|----------|
| **BFS** | **O(\|V\| + \|E\|)** | O(\|V\|) | Shortest path (unweighted) |
| **DFS** | **O(\|V\| + \|E\|)** | O(\|V\|) | Cycle detection, topological sort |

### 5.2 Shortest Path Algorithms

| Algorithm | Complexity | Graph Type | Implementation |
|-----------|------------|------------|----------------|
| **BFS (unweighted)** | **O(\|V\| + \|E\|)** | Unweighted | Simple queue |
| **Dijkstra (priority queue)** | **O(\|E\| log \|V\|)** | Non-negative weights | Min-heap |
| **Dijkstra (simple)** | **O(\|V\|²)** | Non-negative weights | Array-based |

### 5.3 Minimum Spanning Tree

| Algorithm | Complexity | Best For | Implementation |
|-----------|------------|----------|----------------|
| **Kruskal's** | **O(\|E\| log \|V\|)** | Sparse graphs | Sort edges + Union-Find |
| **Prim's (with heap)** | **O(\|E\| log \|V\|)** | Dense graphs | Priority queue |
| **Prim's (without heap)** | **O(\|V\|²)** | Very dense graphs | Simple array |

### 5.4 Topological Sort

| Algorithm | Complexity | Notes |
|-----------|------------|-------|
| **DFS-based** | **O(\|V\| + \|E\|)** | Post-order traversal |
| **Kahn's algorithm** | **O(\|V\| + \|E\|)** | BFS with in-degree |

### 5.5 Sparse vs Dense Graph Impact

**Sparse Graphs** (\|E\| ≈ \|V\|):
- Use Kruskal's for MST
- Use Dijkstra with priority queue
- Prefer adjacency lists

**Dense Graphs** (\|E\| ≈ \|V\|²):
- Use Prim's without heap for MST
- Use simple Dijkstra
- Adjacency matrix acceptable

## 6. Tree Operations

### 6.1 General Tree Operations

| Operation | Complexity | Notes |
|-----------|------------|-------|
| **Tree traversal** (any order) | **O(n)** | Visit each node once |
| **Find height** | **O(n)** | Recursive traversal |
| **Count nodes** | **O(n)** | Full traversal required |

### 6.2 Splay Trees

| Operation | Amortized | Worst Single |
|-----------|-----------|--------------|
| **Insert** | **O(log n)** | O(n) |
| **Find** | **O(log n)** | O(n) |
| **Delete** | **O(log n)** | O(n) |

## 7. Dynamic Programming

### 7.1 Basic DP Patterns

| Pattern | Complexity | Example |
|---------|------------|---------|
| **1D DP** | **O(n)** | Fibonacci, climbing stairs |
| **2D DP** | **O(n²)** | Longest common subsequence |
| **Grid DP** | **O(nm)** | Path counting problems |

### 7.2 Common DP Time Complexities

| Problem | Complexity | Space |
|---------|------------|-------|
| **0/1 Knapsack** | **O(nW)** | O(nW) |
| **Coin Change** | **O(nA)** | O(A) |
| **Edit Distance** | **O(nm)** | O(nm) |

## 8. Hash Table Design

### 8.1 Collision Resolution Methods

| Method | Average | Worst Case | Cache Performance |
|--------|---------|------------|------------------|
| **Separate Chaining** | **O(1)** | **O(n)** | Poor |
| **Linear Probing** | **O(1)** | **O(n)** | Good |
| **Quadratic Probing** | **O(1)** | **O(n)** | Moderate |

### 8.2 Hash Function Impact

| Hash Quality | Performance | Frequency |
|--------------|-------------|-----------|
| **Good (uniform)** | O(1) | Common |
| **Poor** | O(n) | Too frequent |
| **Worst (constant)** | O(n) | Always |

### 8.3 Load Factor Effects

| Load Factor | Performance | Memory |
|-------------|-------------|--------|
| **< 0.75** | Good | Acceptable |
| **≥ 0.75** | Degrades | Efficient |
| **≥ 1.0** | Poor | Over-utilized |

## 9. String Algorithms

### 9.1 String Search

| Algorithm | Complexity | Space | Notes |
|-----------|------------|-------|-------|
| **Naive search** | **O(nm)** | O(1) | n=text, m=pattern |
| **KMP** | **O(n + m)** | O(m) | Preprocessing needed |

### 9.2 Pattern Matching

| Operation | Complexity | Notes |
|-----------|------------|-------|
| **Substring search** | **O(n + m)** | With proper algorithm |
| **Pattern counting** | **O(n + m)** | All occurrences |

## 10. Exam Strategy

### 10.1 Complexity Recognition Patterns

**O(1) Indicators:**
- Array/hash access by key
- Stack/queue operations
- Simple arithmetic

**O(log n) Indicators:**
- Binary search
- Balanced tree operations
- Heap operations

**O(n) Indicators:**
- Single loop through data
- Tree traversal
- Linear search

**O(n log n) Indicators:**
- Efficient sorting
- Divide and conquer with merge

**O(n²) Red Flags:**
- Nested loops over same data
- All pairs processing
- Poor sorting algorithms

### 10.2 Quick Decision Framework

**For sorting:**
1. Small n? → Insertion sort
2. Need O(1) space? → Heapsort
3. Need stability? → Mergesort
4. Otherwise → Quicksort

**For searching:**
1. Unsorted? → Linear O(n)
2. Sorted? → Binary O(log n)
3. Frequent searches? → Hash table O(1)

**For graphs:**
1. Unweighted shortest path? → BFS
2. Weighted shortest path? → Dijkstra
3. MST on sparse graph? → Kruskal's
4. MST on dense graph? → Prim's

### 10.3 Final Review Checklist

**30 minutes before exam:**
```
✅ Hash table: find key O(1), find value O(n)
✅ BST worst case: O(n) when unbalanced
✅ Heap: insert/delete O(log n), build O(n)
✅ Insertion sort: O(n) on sorted, O(n²) on reverse
✅ Heapsort: ALWAYS O(n log n)
✅ Quicksort: O(n log n) avg, O(n²) worst
✅ Graph traversal: O(|V| + |E|)
✅ Dijkstra: O(|E| log |V|) with heap
✅ QuickSelect: O(n) avg, O(n²) worst
```

**During exam:**
- Read carefully: best/average/worst case?
- Hash tables: key vs value operations
- BST: balanced vs unbalanced
- Graphs: sparse vs dense
- Special input cases (sorted, reverse sorted)

**⚠️ Remember**: When finding VALUES in hash maps, you must iterate = O(n)!