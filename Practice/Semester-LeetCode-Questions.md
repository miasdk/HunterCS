# Complete List of LeetCode Problems from Course Assignments

## Table of Contents
- [Array and String Problems](#array-and-string-problems)
- [Hash Table Problems](#hash-table-problems)
- [Heap/Priority Queue Problems](#heappriority-queue-problems)
- [Dynamic Programming Problems](#dynamic-programming-problems)
- [Graph Problems](#graph-problems)

---

## Array and String Problems

### 1. Remove Element
- **URL**: [LeetCode #27 - Remove Element](https://leetcode.com/problems/remove-element/description/)
- **Difficulty**: Easy
- **Assigned**: Homework 2
- **Topic**: Array manipulation, in-place operations
- **Key Concepts**: 
  - Two-pointer technique
  - In-place array modification
  - Iterator usage in C++
- **Implementation Notes**:
  - Implemented in two ways: 
    1. Naive approach with one-by-one deletion
    2. Optimized approach using two iterators to avoid repeated shifting
  - Focused on using STL methods and iterators
  - Tests understanding of vector operations and their complexity

### 2. Remove Duplicates from Sorted Array
- **URL**: [LeetCode #26 - Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)
- **Difficulty**: Easy
- **Assigned**: Homework 3
- **Topic**: Array manipulation, in-place operations
- **Key Concepts**:
  - Two-pointer technique
  - Working with sorted arrays
  - In-place array modification
- **Implementation Notes**:
  - Implemented using only iterators (no array indices)
  - Required both naive and efficient approaches
  - Builds on previous problem with additional constraint of sorted input

---

## Hash Table Problems

### 3. Contains Duplicate II
- **URL**: [LeetCode #219 - Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/description/)
- **Difficulty**: Easy
- **Assigned**: Homework 5
- **Topic**: Hash tables, sliding window
- **Key Concepts**:
  - Hash map operations
  - Tracking elements within a fixed-size window
- **Implementation Notes**:
  - Uses unordered_map to track indices of numbers
  - Tests understanding of hash-based containers
  - Focuses on efficient lookup operations

### 4. Repeated DNA Sequences
- **URL**: [LeetCode #187 - Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/description/)
- **Difficulty**: Medium
- **Assigned**: Homework 5
- **Topic**: Hash tables, string manipulation, sliding window
- **Key Concepts**:
  - Hashing substrings
  - Frequency counting
- **Implementation Notes**:
  - Use unordered_map to track frequency of sequences
  - String substring operations
  - Handling frequency counting with hash maps
  - Complexity analysis comparison between ordered and unordered maps

### 5. Contains Duplicate III
- **URL**: [LeetCode #220 - Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/description/)
- **Difficulty**: Medium
- **Assigned**: Homework 4
- **Topic**: Ordered sets, sliding window, range search
- **Key Concepts**:
  - Ordered set operations
  - Range queries with lower_bound
  - Sliding window technique
- **Implementation Notes**:
  - Uses std::set (balanced BST) for efficient range searches
  - Maintaining a window of k elements
  - Complexity analysis for ordered container operations

---

## Heap/Priority Queue Problems

### 6. Kth Largest Element in a Stream
- **URL**: [LeetCode #703 - Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
- **Difficulty**: Easy
- **Assigned**: Homework 6
- **Topic**: Heap, priority queue
- **Key Concepts**:
  - Min heap operations
  - Tracking k largest elements
  - Stream processing
- **Implementation Notes**:
  - Implementation using STL priority_queue
  - Maintaining a fixed-size min heap
  - Efficient insertion and retrieval operations
  - Suggested optimization by directly manipulating the underlying vector

---

## Dynamic Programming Problems

### 7. Pascal's Triangle
- **URL**: [LeetCode #118 - Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/description/)
- **Difficulty**: Easy
- **Assigned**: Homework 8
- **Topic**: Dynamic Programming (1D array)
- **Key Concepts**:
  - Building results using previous computations
  - Triangular structure in dynamic programming
- **Implementation Notes**:
  - Simple introduction to DP concepts
  - Building each row based on the previous row

### 8. Perfect Squares
- **URL**: [LeetCode #279 - Perfect Squares](https://leetcode.com/problems/perfect-squares/description/)
- **Difficulty**: Medium
- **Assigned**: Homework 8
- **Topic**: Dynamic Programming (1D array)
- **Key Concepts**:
  - Bottom-up DP approach
  - Minimization problem
- **Implementation Notes**:
  - Building optimal solutions from smaller subproblems
  - Finding the minimum number of squares that sum to n

### 9. Count Square Submatrices with All Ones (Optional)
- **URL**: [LeetCode #1277 - Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/)
- **Difficulty**: Medium
- **Assigned**: Homework 8 (Optional)
- **Topic**: Dynamic Programming (2D array)
- **Key Concepts**:
  - 2D dynamic programming
  - Matrix processing
- **Implementation Notes**:
  - Overwriting the original matrix to track square sizes
  - Building solutions based on adjacent cells
  - Hint provided to overwrite each 1 with the size of the largest square

### 10. Minimum Cost for Tickets (Optional)
- **URL**: [LeetCode #983 - Minimum Cost for Tickets](https://leetcode.com/problems/minimum-cost-for-tickets/description/)
- **Difficulty**: Medium
- **Assigned**: Homework 8 (Optional)
- **Topic**: Dynamic Programming (1D array)
- **Key Concepts**:
  - Minimization problem
  - Decision-making at each step
- **Implementation Notes**:
  - Finding optimal purchase strategy
  - Tracking costs over a timeline

---

## Graph Problems

### 11. Find Minimum Time to Reach Last Room I (Not to be solved - for discussion)
- **URL**: [LeetCode - Find Minimum Time to Reach Last Room I](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/description/)
- **Difficulty**: Medium/Hard
- **Assigned**: Homework 8 (Discussion only)
- **Topic**: Graph algorithms
- **Key Concepts**:
  - Understanding when dynamic programming is not applicable
  - Alternative graph traversal approaches
- **Implementation Notes**:
  - Used as an example of when DP is not suitable
  - Discussed alternative approaches (e.g., Dijkstra's algorithm)

---

## Learning Progression and Patterns

### Technique Development Path
1. **Basic Array Manipulation** (HW2, HW3)
   - In-place operations
   - Two-pointer techniques
   - Iterator usage

2. **Hash Tables and Set Operations** (HW4, HW5)
   - Simple lookup operations
   - Range queries
   - Frequency counting

3. **Priority Queues and Heaps** (HW6)
   - Maintaining k largest/smallest elements
   - Stream processing

4. **Dynamic Programming** (HW8)
   - 1D arrays (Pascal's Triangle, Perfect Squares)
   - 2D arrays (Count Square Submatrices)
   - Recognizing DP vs. non-DP problems

### Key Patterns to Master
1. **Two-pointer technique** for array problems
2. **Sliding window** combined with hash tables
3. **Range queries** using ordered sets
4. **Min/max heap** for maintaining k elements
5. **Bottom-up dynamic programming** for optimization problems

### Exam Preparation Focus
Based on the LeetCode problems assigned, focus your practice on:

1. **Graph algorithms** - While few LeetCode problems directly focused on these, they're a major part of the course and exam
2. **Dynamic programming implementation** - Especially 1D and 2D array approaches
3. **Array manipulation techniques** - Two-pointer patterns appear frequently
4. **Hash table applications** - Both ordered and unordered map/set usage
5. **Heap operations** - Especially for k-element tracking problems

Remember that many exam questions will require combining these techniques, particularly for algorithm design questions that make up a significant portion of your final.
