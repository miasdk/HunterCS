//Written and short answer problems from homework 6
6.1 Can both insert and `findMin` be implemented in constant time? 

6.2 
a. Show the result of inserting 10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, and 2,
one at a time, into an initially empty binary heap.
b. Show the result of using the linear-time algorithm to build a binary heap using
the same input.

6.3 Show the result of performing three deleteMin operations in the heap of the previous exercise.

6.4 A complete binary tree of N elements uses array positions 1 to N. Suppose we try
to use an array representation of a binary tree that is not complete. Determine how large the array must be for the following:

a. a binary tree that has two extra levels (that is, it is very slightly unbalanced)
b. a binary tree that has a deepest node at depth 2 logN
c. a binary tree that has a deepest node at depth 4.1 logN
d. the worst-case binary tree

6.5 Rewrite the BinaryHeap insert routine by placing a copy of the inserted item in position 0

6.6 How many nodes are in the large heap in Figure 6.13?

6.7 a. Prove that for binary heaps, buildHeap does at most 2N−2 comparisons between
elements.