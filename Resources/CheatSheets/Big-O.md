# Big-O Cheat Sheet

## Common Time Complexities
- **O(1)**: Constant time (e.g., accessing an array element).
- **O(log n)**: Logarithmic time (e.g., binary search).
- **O(n)**: Linear time (e.g., iterating through an array).
- **O(n log n)**: Linearithmic time (e.g., merge sort, quick sort).
- **O(n^2)**: Quadratic time (e.g., bubble sort, nested loops).
- **O(2^n)**: Exponential time (e.g., recursive Fibonacci).
- **O(n!)**: Factorial time (e.g., traveling salesman problem).

## Data Structure Complexities
| Operation          | Array | Linked List | Stack/Queue | Hash Table | Binary Search Tree (BST) | AVL Tree |
|--------------------|-------|-------------|-------------|------------|--------------------------|----------|
| Access            | O(1)  | O(n)        | O(n)        | O(1)       | O(log n)                 | O(log n) |
| Search            | O(n)  | O(n)        | O(n)        | O(1)       | O(log n)                 | O(log n) |
| Insertion         | O(n)  | O(1)        | O(1)        | O(1)       | O(log n)                 | O(log n) |
| Deletion          | O(n)  | O(1)        | O(1)        | O(1)       | O(log n)                 | O(log n) |

## Sorting Algorithm Complexities
| Algorithm         | Best Case | Average Case | Worst Case | Space Complexity |
|-------------------|-----------|--------------|------------|------------------|
| Bubble Sort       | O(n)      | O(n^2)       | O(n^2)     | O(1)             |
| Merge Sort        | O(n log n)| O(n log n)   | O(n log n) | O(n)             |
| Quick Sort        | O(n log n)| O(n log n)   | O(n^2)     | O(log n)         |
| Heap Sort         | O(n log n)| O(n log n)   | O(n log n) | O(1)             |
| Insertion Sort    | O(n)      | O(n^2)       | O(n^2)     | O(1)             |