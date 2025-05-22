# Comprehensive Sorting Algorithms Reference

## Table of Contents
1. [Insertion Sort](#insertion-sort)
2. [Mergesort](#mergesort)
3. [Quicksort](#quicksort)
4. [Quickselect](#quickselect)
5. [Theoretical Foundations](#theoretical-foundations)

---

## Insertion Sort

### Algorithm Overview
Insertion sort is one of the simplest sorting algorithms, consisting of N-1 passes. For each pass p (from 1 to N-1), it ensures elements in positions 0 through p are in sorted order.

### How It Works
- **Strategy**: Move the element in position p left until its correct place is found among the first p+1 elements
- **Implementation**: Uses a temporary variable to avoid explicit swaps
- **Key Insight**: Leverages the fact that elements in positions 0 through p-1 are already sorted

### Time Complexity Analysis
- **Worst Case**: O(N²) - occurs with reverse-sorted input
- **Best Case**: O(N) - occurs with already sorted input
- **Average Case**: Θ(N²)
- **Space Complexity**: O(1) - in-place sorting

### Performance Characteristics
- **When to Use**: Excellent for small datasets or nearly sorted arrays
- **Advantage**: Linear time performance on nearly sorted data
- **Connection to Inversions**: Running time is O(I + N) where I is the number of inversions

### STL Implementation Considerations
- Uses iterators instead of array indexing
- Requires `decltype` for template type deduction in C++11
- Function objects for custom comparison operations

---

## Mergesort

### Algorithm Overview
Mergesort is a divide-and-conquer algorithm that guarantees O(N log N) worst-case performance with nearly optimal number of comparisons.

### How It Works
1. **Divide**: Split array into two halves
2. **Conquer**: Recursively sort each half
3. **Combine**: Merge the two sorted halves

### Recurrence Relation
```
T(1) = 1
T(N) = 2T(N/2) + N
```

### Time Complexity Analysis
- **All Cases**: Θ(N log N) - consistent performance regardless of input
- **Space Complexity**: O(N) - requires temporary array for merging

### Key Advantages
- **Stable**: Maintains relative order of equal elements
- **Predictable**: Consistent performance across all input types
- **Optimal Comparisons**: Uses nearly the minimum number of comparisons possible

### Implementation Notes
- Uses a temporary array that can be reused across recursive calls
- The merge operation is the fundamental building block
- Excellent for external sorting (large datasets that don't fit in memory)

---

## Quicksort

### Algorithm Overview
Historically the fastest generic sorting algorithm in practice with average O(N log N) performance, though it has O(N²) worst-case behavior.

### Core Algorithm Steps
1. **Base Case**: If array has 0 or 1 elements, return
2. **Choose Pivot**: Select any element v as the pivot
3. **Partition**: Split remaining elements into:
   - S₁ = {x | x ≤ v}
   - S₂ = {x | x ≥ v}
4. **Recurse**: Return quicksort(S₁) + v + quicksort(S₂)

### Pivot Selection Strategies

#### Random Pivot
- **Safety**: Eliminates worst-case scenarios in practice
- **Performance**: Makes O(N²) behavior exponentially unlikely

#### Median-of-Three Partitioning
- **Method**: Use median of left, right, and center elements
- **Benefits**: 
  - Eliminates worst case for sorted input
  - Reduces comparisons by 14%
  - More predictable than random selection

### Critical Partitioning Implementation

#### The Duplicate Elements Problem
When partitioning, there are four strategies for handling elements equal to the pivot:

1. **Both pointers stop** ✅ **RECOMMENDED**
2. **Only i stops**
3. **Only j stops** 
4. **Neither pointer stops**

#### Why Strategy 1 is Optimal
- **Balanced Partitions**: Creates roughly equal-sized partitions
- **Handles Duplicates**: Critical for arrays with many identical elements
- **Performance**: Maintains O(N log N) even with all identical elements
- **Trade-off**: Performs "unnecessary" swaps but ensures balance

#### The All-Identical Test Case
This reveals why the implementation choice matters:
- **Strategy 1**: Many swaps, but balanced partitions → O(N log N)
- **Strategy 4**: No swaps, but extremely unbalanced partitions → O(N²)

### Time Complexity
- **Average Case**: O(N log N)
- **Best Case**: O(N log N)
- **Worst Case**: O(N²) - can be made exponentially unlikely
- **Space Complexity**: O(log N) average (recursion stack)

### When to Use Quicksort
- **Best for**: General-purpose sorting with good average performance
- **Advantages**: Very tight inner loop, cache-friendly
- **Considerations**: Not stable, worst-case can be problematic

---

## Quickselect

### Algorithm Overview
A modification of quicksort that finds the kth smallest element in expected linear time.

### Key Differences from Quicksort
- **Single Recursion**: Makes only one recursive call instead of two
- **Targeted Search**: Only recurses on the partition containing the target element

### Algorithm Steps
1. **Base Case**: If |S| = 1, return the element
2. **Choose Pivot**: Select pivot element v
3. **Partition**: Split into S₁ and S₂ as in quicksort
4. **Selective Recursion**:
   - If k ≤ |S₁|: recurse on S₁
   - If k = 1 + |S₁|: pivot is the answer
   - Otherwise: recurse on S₂ for (k - |S₁| - 1)st element

### Time Complexity
- **Average Case**: O(N) - linear expected time
- **Worst Case**: O(N²) - same as quicksort
- **Space Complexity**: O(log N) average

### Applications
- Finding medians in linear time
- Order statistics problems
- Top-k problems with better performance than sorting

---

## Theoretical Foundations

### Inversions and Sorting
**Definition**: An inversion is an ordered pair (i,j) where i < j but a[i] > a[j]

**Key Theorems**:

#### Theorem 7.1: Average Inversions
The average number of inversions in an array of N distinct elements is N(N-1)/4.

**Proof Insight**: Consider any array and its reverse - exactly one contains each possible inversion.

#### Theorem 7.2: Lower Bound for Adjacent Swaps
Any algorithm that sorts by exchanging only adjacent elements requires Ω(N²) time.

### Practical Implications
- **Insertion Sort Performance**: O(I + N) where I = number of inversions
- **Nearly Sorted Data**: Insertion sort becomes linear for small numbers of inversions
- **Algorithm Selection**: Understanding inversions helps choose appropriate algorithms

### Comparison Summary

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable | Notes |
|-----------|-----------|--------------|------------|-------|--------|-------|
| Insertion Sort | O(N) | Θ(N²) | O(N²) | O(1) | Yes | Great for small/nearly sorted |
| Mergesort | Θ(N log N) | Θ(N log N) | Θ(N log N) | O(N) | Yes | Consistent performance |
| Quicksort | O(N log N) | O(N log N) | O(N²) | O(log N) | No | Fastest in practice |
| Quickselect | O(N) | O(N) | O(N²) | O(log N) | N/A | Selection only |

### Algorithm Selection Guidelines

**Use Insertion Sort when**:
- Small datasets (< 50 elements)
- Nearly sorted data
- Stability is required and simplicity is valued

**Use Mergesort when**:
- Guaranteed O(N log N) performance is needed
- Stability is required
- Working with linked lists
- External sorting scenarios

**Use Quicksort when**:
- General-purpose sorting with best average performance
- Memory usage should be minimized
- Stability is not required

**Use Quickselect when**:
- Only need the kth smallest element
- Don't need the entire array sorted
- Linear expected time is acceptable