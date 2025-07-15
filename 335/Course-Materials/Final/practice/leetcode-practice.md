# Sample LeetCode Problems Similar to Exam Questions

Based on the exam content you've shared, here are several LeetCode-style problems that test similar concepts and would be great practice for your CSCI 33500 final exam.

## 1. Graph Algorithms

### Problem 1: Network Delay Time (Similar to Dijkstra's Algorithm)
**LeetCode #743**: https://leetcode.com/problems/network-delay-time/

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

```cpp
int networkDelayTime(vector<vector<int>>& times, int n, int k) {
    // Implement using Dijkstra's algorithm
}
```

### Problem 2: Minimum Spanning Tree (Similar to Prim's/Kruskal's)
**LeetCode #1584**: https://leetcode.com/problems/min-cost-to-connect-all-points/

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the Manhattan distance between them: |xi - xj| + |yi - yj|.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

```cpp
int minCostConnectPoints(vector<vector<int>>& points) {
    // Implement using Prim's or Kruskal's algorithm
}
```

### Problem 3: Course Schedule (Topological Sort)
**LeetCode #207**: https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

```cpp
bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
    // Implement using topological sort
}
```

## 2. Heap Operations

### Problem 4: Kth Largest Element in an Array (Heap Operations)
**LeetCode #215**: https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

```cpp
int findKthLargest(vector<int>& nums, int k) {
    // Implement using a heap
}
```

### Problem 5: Top K Frequent Elements (Heap Application)
**LeetCode #347**: https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

```cpp
vector<int> topKFrequent(vector<int>& nums, int k) {
    // Implement using hash map and heap
}
```

## 3. Binary Search Trees & AVL Trees

### Problem 6: Validate Binary Search Tree
**LeetCode #98**: https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

```cpp
bool isValidBST(TreeNode* root) {
    // Implement validation for BST properties
}
```

### Problem 7: Balance a Binary Search Tree
**LeetCode #1382**: https://leetcode.com/problems/balance-a-binary-search-tree/

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

```cpp
TreeNode* balanceBST(TreeNode* root) {
    // Convert to balanced BST (similar to AVL tree operations)
}
```

## 4. Dynamic Programming

### Problem 8: Unique Paths with Obstacles (2D DP)
**LeetCode #63**: https://leetcode.com/problems/unique-paths-ii/

You are given an m x n grid with obstacles. Each cell is either empty (0) or has an obstacle (1).

Starting from the top-left corner, you need to reach the bottom-right corner. At each step, you can either move down or right.

Return the number of unique paths to reach the bottom-right corner.

```cpp
int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
    // Implement 2D dynamic programming solution
}
```

### Problem 9: Longest Common Subsequence (2D DP)
**LeetCode #1143**: https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest common subsequence.

If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

```cpp
int longestCommonSubsequence(string text1, string text2) {
    // Implement dynamic programming solution
}
```

## 5. Hash Tables

### Problem 10: Find All Numbers Disappeared in an Array (Hash Table)
**LeetCode #448**: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

```cpp
vector<int> findDisappearedNumbers(vector<int>& nums) {
    // Implement using hash set
}
```

### Problem 11: Group Anagrams (Hash Table)
**LeetCode #49**: https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

```cpp
vector<vector<string>> groupAnagrams(vector<string>& strs) {
    // Implement using hash map
}
```

## 6. C++ STL Knowledge

### Problem 12: Implement LRU Cache
**LeetCode #146**: https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity
- int get(int key) Return the value of the key if it exists, otherwise return -1
- void put(int key, int value) Update or insert the value if the key exists; otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity, evict the least recently used key.

```cpp
class LRUCache {
public:
    // Implement using STL containers
};
```

### Problem 13: Next Greater Element Using Stack
**LeetCode #496**: https://leetcode.com/problems/next-greater-element-i/

Given an array of integers nums, return an array answer such that answer[i] is the next greater element for nums[i] in the array.

The next greater element for an element nums[i] is the first element nums[j] such that j > i and nums[j] > nums[i]. If there is no such element, the answer is -1.

```cpp
vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    // Implement using STL stack
}
```

## 7. Sorting and Selection Algorithms

### Problem 14: Sort an Array (Implementing Sorting Algorithms)
**LeetCode #912**: https://leetcode.com/problems/sort-an-array/

Given an array of integers nums, sort the array in ascending order.

```cpp
vector<int> sortArray(vector<int>& nums) {
    // Implement quicksort, mergesort, or heapsort
}
```

### Problem 15: K Closest Points to Origin (Application of QuickSelect)
**LeetCode #973**: https://leetcode.com/problems/k-closest-points-to-origin/

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)² + (y1 - y2)²).

```cpp
vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    // Implement using quickselect or heap
}
```

## Tips for Success

1. **Understand the fundamentals**: Before diving into these problems, make sure you understand the core algorithms and data structures covered in your course.

2. **Start with simpler problems**: Begin with problems that test your understanding of basic operations before moving to more complex algorithm implementations.

3. **Focus on time/space complexity**: For each solution, analyze its time and space complexity and consider if there are more efficient approaches.

4. **Test edge cases**: Consider empty inputs, single-element inputs, and other boundary cases when testing your solutions.

5. **Practice tracing algorithms**: Many exam questions require you to trace algorithms step-by-step—practice this skill by working through examples manually.

6. **Review STL containers**: Understand the operations and time complexities of std::vector, std::list, std::set, std::map, std::unordered_set, std::unordered_map, and std::priority_queue.

7. **Implement algorithms from scratch**: While STL provides many built-in algorithms, practice implementing fundamental algorithms like Dijkstra's, Prim's, Kruskal's, and quickselect from scratch.
