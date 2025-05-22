# Complete Time Complexity Reference - All Exam Topics

## 1. Data Structure Operations

### Hash Tables (unordered_map, unordered_set)
| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Insert | **O(1)** | O(n) |
| **Find key in unordered_map** | **O(1)** | O(n) |
| Delete | **O(1)** | O(n) |
| **Find VALUE in unordered_map** | **O(n)** | **O(n)** |
| Update hash value | **O(1)** | O(n) |
| Rehashing | **O(n)** | O(n) |

### Binary Search Trees (map, set)
| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Insert | **O(log n)** | O(n) |
| **Find key in ordered map** | **O(log n)** | O(n) |
| Delete | **O(log n)** | O(n) |
| In-order traversal | **O(n)** | O(n) |

### AVL Trees (Self-Balancing BST)
| Operation | Always |
|-----------|--------|
| Insert | **O(log n)** |
| Find | **O(log n)** |
| Delete | **O(log n)** |

### Binary Heaps
| Operation | Complexity |
|-----------|------------|
| Insert | **O(log n)** |
| DeleteMin/Max | **O(log n)** |
| FindMin/Max | **O(1)** |
| BuildHeap | **O(n)** ⭐ |
| Decrease/Increase Key | **O(log n)** |

### Arrays/Vectors
| Operation | Complexity |
|-----------|------------|
| Access by index | **O(1)** |
| Search (unsorted) | **O(n)** |
| Search (sorted) | **O(log n)** |
| Insert at end | **O(1)** amortized |
| Insert at position | **O(n)** |

## 2. Sorting Algorithms

### Comparison-Based Sorts
| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| **Quicksort** | **O(n log n)** | **O(n log n)** | **O(n²)** | O(log n) |
| **Heapsort** | **O(n log n)** | **O(n log n)** | **O(n log n)** | O(1) |
| **Mergesort** | **O(n log n)** | **O(n log n)** | **O(n log n)** | O(n) |
| **Insertion Sort** | **O(n)** | **O(n²)** | **O(n²)** | O(1) |
| **Selection Sort** | **O(n²)** | **O(n²)** | **O(n²)** | O(1) |

### Special Cases
- **Insertion sort on sorted array**: **O(n)** ⭐
- **Insertion sort on reverse sorted array**: **O(n²)**
- **Quicksort with median-of-3**: Avoids O(n²) in practice
- **Heapsort on sorted array**: Still **O(n log n)**

## 3. Graph Algorithms

### Shortest Path Algorithms
| Algorithm | Complexity | Notes |
|-----------|------------|-------|
| **Dijkstra's (priority queue)** | **O(\|E\| log \|V\|)** | Most common implementation |
| **Dijkstra's (simple)** | **O(\|V\|²)** | Without heap |
| **Unweighted shortest path** | **O(\|V\| + \|E\|)** | BFS-based |

### Minimum Spanning Tree
| Algorithm | Complexity | Notes |
|-----------|------------|-------|
| **Kruskal's** | **O(\|E\| log \|V\|)** | or O(\|E\| log \|E\|) |
| **Prim's (with heaps)** | **O(\|E\| log \|V\|)** | Better for dense graphs |
| **Prim's (without heaps)** | **O(\|V\|²)** | Better for sparse graphs |

### Graph Traversal
| Algorithm | Complexity |
|-----------|------------|
| **BFS** | **O(\|V\| + \|E\|)** |
| **DFS** | **O(\|V\| + \|E\|)** |
| **Topological Sort** | **O(\|V\| + \|E\|)** |

## 4. Selection Algorithms

| Algorithm | Average Case | Worst Case |
|-----------|--------------|------------|
| **QuickSelect** | **O(n)** | **O(n²)** |
| **Median of Medians** | **O(n)** | **O(n)** |

## 5. Tree Operations

### General Tree Operations
| Operation | Complexity |
|-----------|------------|
| **Tree traversal** (any order) | **O(n)** |
| **Find height** | **O(n)** |
| **Count nodes** | **O(n)** |

### Splay Trees
| Operation | Amortized |
|-----------|-----------|
| **Insert** | **O(log n)** |
| **Find** | **O(log n)** |
| **Delete** | **O(log n)** |
| **Worst case single operation** | **O(n)** |

## 6. Advanced Topics

### Dynamic Programming
| Problem Type | Typical Complexity |
|--------------|-------------------|
| **1D DP** | **O(n)** |
| **2D DP** | **O(n²)** |
| **Grid path counting** | **O(nm)** |

### String Algorithms
| Algorithm | Complexity |
|-----------|------------|
| **String search (naive)** | **O(nm)** |
| **String search (KMP)** | **O(n + m)** |

## 7. Hash Table Design Complexities

### Hash Operations by Design
| Design Choice | Impact |
|---------------|---------|
| **Good hash function** | Maintains O(1) average |
| **Poor hash function** | Degrades to O(n) operations |
| **Load factor too high** | More collisions, worse performance |
| **Load factor too low** | Wastes space, frequent rehashing |

### Collision Resolution
| Method | Average Case | Worst Case |
|--------|--------------|------------|
| **Separate Chaining** | **O(1)** | **O(n)** |
| **Linear Probing** | **O(1)** | **O(n)** |
| **Quadratic Probing** | **O(1)** | **O(n)** |
| **Double Hashing** | **O(1)** | **O(n)** |

## 8. Hybrid Algorithms

### Introsort (Hybrid Sorting)
| Component | When Used | Complexity |
|-----------|-----------|------------|
| **Quicksort** | Main algorithm | **O(n log n)** average |
| **Heapsort** | When recursion too deep | **O(n log n)** guaranteed |
| **Insertion Sort** | Small subarrays (< 16 elements) | **O(n)** for small n |

### Overall Introsort Complexity: **O(n log n)** worst case

## 9. Algorithm Analysis by Input Size

### Small Input (n < 50)
- **Insertion Sort**: Often fastest due to low overhead
- **Linear search**: Acceptable performance
- **Simple algorithms**: Usually preferred

### Medium Input (50 < n < 10,000)
- **Quicksort**: Usually optimal
- **Hash tables**: Start showing benefits
- **Binary search**: Much better than linear

### Large Input (n > 10,000)
- **Merge/Heapsort**: Consistent performance
- **Hash tables**: Essential for fast lookups
- **Graph algorithms**: Need efficient implementations

## 10. Memory Hierarchy Impact

### Cache-Friendly vs Cache-Hostile
| Algorithm | Cache Behavior | Real Performance |
|-----------|----------------|------------------|
| **Array traversal** | Cache-friendly | Often faster than O(n log n) alternatives |
| **Linked list traversal** | Cache-hostile | Slower than theoretical complexity |
| **Binary search** | Moderately friendly | Good in practice |
| **Hash tables** | Variable | Depends on implementation |

## 11. Practical Complexity Considerations

### Constants Matter
- **O(n)** with large constant vs **O(n log n)** with small constant
- **Example**: Simple O(n²) may beat O(n log n) for small n

### Real-World Factors
| Factor | Impact |
|--------|--------|
| **Memory allocation** | Can dominate for small inputs |
| **Cache misses** | Can make O(n) slower than O(log n) |
| **Branch prediction** | Affects loop performance |

## 12. Quick Exam Reference

### Most Commonly Tested Complexities
```
Find key in unordered_map: O(1) average, O(n) worst
Find value in unordered_map: O(n) - requires iterating through map
Find key in ordered map: O(log n)
Hash table operations: O(1) average, O(n) worst
BST operations: O(log n) average, O(n) worst
Heap operations: O(log n), BuildHeap: O(n)
Insertion sort on sorted array: O(n)
Insertion sort on reverse sorted: O(n²)
Heapsort on sorted array: O(n log n)
Partition around pivot: O(n)
Dijkstra's: O(|E| log |V|)
Prim's with heaps: O(|E| log |V|)
Prim's without heaps: O(|V|²)
Kruskal's: O(|E| log |V|)
Graph traversal: O(|V| + |E|)
Topological sort: O(|V| + |E|)
Unweighted single-source shortest path: O(|V| + |E|)
Quicksort average: O(n log n)
Quicksort worst: O(n²)
Heapsort: O(n log n) always
QuickSelect average: O(n)
QuickSelect worst: O(n²)
```

### When Graphs Are Sparse vs Dense
- **Sparse**: |E| ≈ |V|
  - Use Prim's with heaps
  - Adjacency lists
- **Dense**: |E| ≈ |V|²
  - Use Prim's without heaps
  - Adjacency matrices acceptable

## 13. Red Flags for Higher Complexity

### O(n²) Indicators
- Processing all pairs of elements
- Nested loops over same data
- Bubble sort, selection sort
- Matrix multiplication

### O(n³) Indicators
- Triple nested loops
- All-pairs shortest paths (Floyd-Warshall)
- Some dynamic programming problems

### O(2ⁿ) Indicators
- Generating all subsets
- Brute force solutions to NP problems
- Recursive solutions without memoization

## 14. Optimization Strategies

### From O(n²) to O(n log n)
- **Sorting first** then processing
- **Using heaps** instead of linear search
- **Divide and conquer** approaches

### From O(n log n) to O(n)
- **Hash tables** for constant-time lookups
- **Counting sort** for limited range integers
- **Two-pointer** techniques

### From O(n) to O(1)
- **Preprocessing** with additional space
- **Mathematical formulas** instead of iteration
- **Amortized analysis** with smart data structures