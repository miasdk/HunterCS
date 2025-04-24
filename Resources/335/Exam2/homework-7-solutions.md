# Homework 7: Sorting Algorithms - Solutions and Explanations

## Part A: Textbook Questions

### 7.1 Insertion Sort

**Question:** Sort the sequence 3, 1, 4, 1, 5, 9, 2, 6, 5 using insertion sort.

**Solution:**

Insertion sort processes one element at a time, inserting each element into its correct position among the previously sorted elements.

| Step | Current Element | Current Array |
|------|---------------|---------------|
| 1 | 3 | [3] |
| 2 | 1 | [1, 3] |
| 3 | 4 | [1, 3, 4] |
| 4 | 1 | [1, 1, 3, 4] |
| 5 | 5 | [1, 1, 3, 4, 5] |
| 6 | 9 | [1, 1, 3, 4, 5, 9] |
| 7 | 2 | [1, 1, 2, 3, 4, 5, 9] |
| 8 | 6 | [1, 1, 2, 3, 4, 5, 6, 9] |
| 9 | 5 | [1, 1, 2, 3, 4, 5, 5, 6, 9] |

**Final sorted array:** [1, 1, 2, 3, 4, 5, 5, 6, 9]

**Explanation:**
- Take each element and compare it with the previous elements
- Shift larger elements to the right to make space for the current element
- Insert the current element in its correct position
- Continue until all elements are processed

### 7.2 Insertion Sort Running Time for Equal Elements

**Question:** What is the running time of insertion sort if all elements are equal?

**Answer:** O(n)

**Explanation:**
- If all elements are equal, the inner loop of insertion sort never executes
- This is because each new element is never smaller than any previously sorted element
- The algorithm still needs to scan through all n elements once
- Thus, the time complexity reduces to O(n) linear time
- This represents the best-case scenario for insertion sort

### 7.11 Heapsort Process

**Question:** Show how heapsort processes the input 142, 543, 123, 65, 453, 879, 572, 434, 111, 242, 811, 102.

**Solution:**

**Step 1:** Build a max heap from the input array.
- Starting array: [142, 543, 123, 65, 453, 879, 572, 434, 111, 242, 811, 102]
- After buildHeap: [879, 543, 811, 434, 453, 572, 142, 65, 111, 242, 123, 102]

**Step 2:** Repeatedly extract the maximum element and place it at the end.

| Iteration | Max Element | Array After Swap | Array After Heapify |
|-----------|-------------|-----------------|---------------------|
| 1 | 879 | [102, 543, 811, 434, 453, 572, 142, 65, 111, 242, 123, 879] | [811, 543, 572, 434, 453, 123, 142, 65, 111, 242, 102, 879] |
| 2 | 811 | [102, 543, 572, 434, 453, 123, 142, 65, 111, 242, 811, 879] | [572, 543, 142, 434, 453, 123, 102, 65, 111, 242, 811, 879] |
| 3 | 572 | [242, 543, 142, 434, 453, 123, 102, 65, 111, 572, 811, 879] | [543, 453, 142, 434, 242, 123, 102, 65, 111, 572, 811, 879] |
| 4 | 543 | [111, 453, 142, 434, 242, 123, 102, 65, 543, 572, 811, 879] | [453, 434, 142, 111, 242, 123, 102, 65, 543, 572, 811, 879] |
| 5 | 453 | [65, 434, 142, 111, 242, 123, 102, 453, 543, 572, 811, 879] | [434, 242, 142, 111, 65, 123, 102, 453, 543, 572, 811, 879] |
| 6 | 434 | [102, 242, 142, 111, 65, 123, 434, 453, 543, 572, 811, 879] | [242, 111, 142, 102, 65, 123, 434, 453, 543, 572, 811, 879] |
| 7 | 242 | [123, 111, 142, 102, 65, 242, 434, 453, 543, 572, 811, 879] | [142, 111, 123, 102, 65, 242, 434, 453, 543, 572, 811, 879] |
| 8 | 142 | [65, 111, 123, 102, 142, 242, 434, 453, 543, 572, 811, 879] | [123, 111, 65, 102, 142, 242, 434, 453, 543, 572, 811, 879] |
| 9 | 123 | [102, 111, 65, 123, 142, 242, 434, 453, 543, 572, 811, 879] | [111, 102, 65, 123, 142, 242, 434, 453, 543, 572, 811, 879] |
| 10 | 111 | [65, 102, 111, 123, 142, 242, 434, 453, 543, 572, 811, 879] | [102, 65, 111, 123, 142, 242, 434, 453, 543, 572, 811, 879] |
| 11 | 102 | [65, 102, 111, 123, 142, 242, 434, 453, 543, 572, 811, 879] | [65, 102, 111, 123, 142, 242, 434, 453, 543, 572, 811, 879] |

**Final sorted array:** [65, 102, 111, 123, 142, 242, 434, 453, 543, 572, 811, 879]

### 7.12 Heapsort Running Time for Presorted Input

**Question:** What is the running time of heapsort for presorted input?

**Answer:** O(n log n)

**Explanation:**
- Unlike quicksort, heapsort doesn't have a better time complexity for presorted input
- The buildHeap phase still requires O(n) time
- The n deleteMax operations still require O(log n) time each
- Therefore, the total time complexity remains O(n log n)
- The constant factors might be slightly better in practice for nearly sorted inputs, but the asymptotic complexity is unchanged

### 7.15 Mergesort

**Question:** Sort 3, 1, 4, 1, 5, 9, 2, 6 using mergesort.

**Solution:**

Mergesort recursively divides the array into halves, sorts each half, and then merges the sorted halves.

**Step 1:** Divide the array into halves
- Left half: [3, 1, 4, 1]
- Right half: [5, 9, 2, 6]

**Step 2:** Recursively sort each half

Left half:
- Divide: [3, 1] and [4, 1]
- Sort [3, 1]:
  - Divide: [3] and [1]
  - Merge: [1, 3]
- Sort [4, 1]:
  - Divide: [4] and [1]
  - Merge: [1, 4]
- Merge [1, 3] and [1, 4]: [1, 1, 3, 4]

Right half:
- Divide: [5, 9] and [2, 6]
- Sort [5, 9]:
  - Divide: [5] and [9]
  - Merge: [5, 9]
- Sort [2, 6]:
  - Divide: [2] and [6]
  - Merge: [2, 6]
- Merge [5, 9] and [2, 6]: [2, 5, 6, 9]

**Step 3:** Merge the sorted halves
- Merge [1, 1, 3, 4] and [2, 5, 6, 9]
- Result: [1, 1, 2, 3, 4, 5, 6, 9]

**Final sorted array:** [1, 1, 2, 3, 4, 5, 6, 9]

### 7.17 Mergesort Running Time

**Question:** Determine the running time of mergesort for:
a. Sorted input
b. Reverse-ordered input
c. Random input

**Answer:** O(n log n) for all cases

**Explanation:**
- Mergesort has the same time complexity regardless of the input distribution
- The divide step always creates two equal halves, resulting in log n levels
- The merge step at each level requires O(n) time in total
- The recursion tree has log n levels, each costing O(n) time
- Therefore, the total time complexity is O(n log n) in all cases
- This is a key advantage of mergesort: guaranteed O(n log n) performance

### 7.19 Quicksort with Median-of-Three and Cutoff

**Question:** Sort 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5 using quicksort with median-of-three partitioning and a cutoff of 3.

**Solution:**

**Step 1:** Choose pivot using median-of-three
- First element: 3
- Middle element: 9
- Last element: 5
- Median is 5, pivot = 5

**Step 2:** Partition the array around 5
- After partitioning: [3, 1, 4, 1, 2, 3] [5] [9, 6, 5, 5]

**Step 3:** Recursively sort the subarrays

Left subarray [3, 1, 4, 1, 2, 3]:
- Size > 3, continue with quicksort
- Median of (3, 4, 3) is 3
- After partitioning: [1, 1, 2] [3] [4, 3]
- Left subarray size = 3 (equals cutoff), use insertion sort: [1, 1, 2]
- Right subarray size = 2 (< cutoff), use insertion sort: [3, 4]
- Result: [1, 1, 2, 3, 3, 4]

Right subarray [9, 6, 5, 5]:
- Size > 3, continue with quicksort
- Median of (9, 5, 5) is 5
- After partitioning: [] [5] [9, 6, 5]
- Left subarray is empty
- Right subarray size = 3 (equals cutoff), use insertion sort: [5, 6, 9]
- Result: [5, 5, 6, 9]

**Step 4:** Combine the results
- Result: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

**Final sorted array:** [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

### 7.20 Quicksort Running Time

**Question:** Determine the running time of quicksort for:
a. Sorted input
b. Reverse-ordered input
c. Random input

**Answer:**
a. Sorted input: O(n²)
b. Reverse-ordered input: O(n²)
c. Random input: O(n log n) on average

**Explanation:**
- With the classic quicksort implementation that chooses the first element as pivot:
  - For sorted or reverse-sorted input, each partition creates one empty subarray and one with n-1 elements
  - This leads to n levels of recursion instead of log n, resulting in O(n²) time
  - For random input, the partitions are more balanced on average, yielding O(n log n) time
- The quadratic worst-case behavior for sorted/reverse-sorted input is a major drawback of naive quicksort implementations
- This is why advanced pivot selection strategies like median-of-three are important

### 7.21 Quicksort with Different Pivot Selection

**Question:** Repeat Exercise 7.20 when the pivot is chosen as:
a. The first element
b. The larger of the first two distinct elements
c. A random element
d. The average of all elements in the set

**Answer:**

a. First element:
- Sorted input: O(n²)
- Reverse-ordered input: O(n²)
- Random input: O(n log n) on average

b. Larger of first two distinct elements:
- Sorted input: O(n²) (the larger element is always the second, creating highly imbalanced partitions)
- Reverse-ordered input: O(n²) (similar issue)
- Random input: O(n log n) on average

c. Random element:
- Sorted input: O(n log n) with high probability
- Reverse-ordered input: O(n log n) with high probability
- Random input: O(n log n) on average
- This is the most robust strategy for avoiding worst-case behavior

d. Average of all elements:
- This is typically not used in practice due to the O(n) cost of computing the average
- Sorted input: Potentially O(n log n) if the average creates balanced partitions
- Reverse-ordered input: Potentially O(n log n) for similar reasons
- Random input: O(n log n) on average
- However, this approach may not work well for discrete values or when many duplicates exist

### 7.24 Bad Permutation for Quicksort

**Question:** Construct a permutation of 20 elements that is as bad as possible for quicksort using median-of-three partitioning and a cutoff of 3.

**Answer:**
A particularly bad permutation would be:
[10, 1, 20, 2, 19, 3, 18, 4, 17, 5, 16, 6, 15, 7, 14, 8, 13, 9, 12, 11]

**Explanation:**
- This permutation is designed to make median-of-three consistently choose poor pivots
- The pattern alternates high and low values
- When taking the first, middle, and last elements for median-of-three, the middle element is often a poor choice
- The sequence is constructed so that after partitioning, we still get imbalanced subarrays
- With the cutoff of 3, we don't get the benefit of insertion sort until very late in the recursion
- This pattern can lead to a recursion depth approaching n, resulting in near-quadratic performance

## Part B: Quicksort with Incorrect Pivot Selection

**Question:** If you write quicksort with median-of-3 partitioning, and accidentally select the minimum of the 3 numbers instead of the median, what would happen, in terms of correctness and efficiency of your sort?

**Answer:**

**Correctness:** The algorithm would still correctly sort the array. Quicksort works correctly regardless of the pivot selection strategy, as long as the partitioning is done correctly.

**Efficiency:** The algorithm would be significantly less efficient:
- Consistently selecting the minimum element as pivot leads to highly imbalanced partitions
- For sorted or nearly-sorted data, one partition would be empty, and the other would have n-1 elements
- This creates a recursion depth of O(n) instead of O(log n)
- The time complexity degrades to O(n²) in the worst case
- This negates the key benefit of median-of-three, which is designed to avoid such imbalanced partitions

The behavior would be similar to always choosing the first element in a sorted array, which is known to be a worst-case scenario for quicksort.

## Part C: Implementing Heapsort with STL

**Question:** Implement myHeapSort using make_heap and pop_heap functions from the C++ STL.

**Solution:**

```cpp
// Takes a reference to a (typically unsorted) vector and sorts that vector using heapsort.
void myHeapSort(std::vector<int> & nums) {
    // Step 1: Transform the array into a max heap
    std::make_heap(nums.begin(), nums.end());
    
    // Step 2: Repeatedly "pop" the largest element to the end
    for (int i = nums.size() - 1; i > 0; i--) {
        // Move the largest element (at the front) to position i
        std::pop_heap(nums.begin(), nums.begin() + i + 1);
        // After pop_heap, the largest element is now at position i
        // and the remaining elements form a valid heap
    }
    
    // The array is now sorted in ascending order
}
```

**Explanation:**
- `make_heap` transforms the entire vector into a max heap in O(n) time
- `pop_heap` does three things in one operation:
  1. Swaps the first element (largest) with the last element in the specified range
  2. Reduces the heap size by 1
  3. Reestablishes the heap property for the reduced heap
- By repeatedly calling `pop_heap` with a decreasing range, we place each maximum element at the end of the array
- After n-1 operations, the entire array is sorted in ascending order
- This implementation has O(n log n) time complexity, just like a manually coded heapsort

**Advantages of using STL functions:**
1. Concise and readable code
2. Less prone to bugs than manual implementation
3. Often optimized for performance
4. Maintains the same algorithmic complexity
