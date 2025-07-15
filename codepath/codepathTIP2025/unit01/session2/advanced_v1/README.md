# Advanced Problem Sets

## Table of Contents

### [Version 1 Advanced Set](#version-1-advanced-set)
- [Problem 1: Transpose Matrix](#problem-1-transpose-matrix)
- [Problem 2: Two-Pointer Reverse List](#problem-2-two-pointer-reverse-list)
- [Problem 3: Remove Duplicates](#problem-3-remove-duplicates)
- [Problem 4: Sort Array by Parity](#problem-4-sort-array-by-parity)
- [Problem 5: Container with Most Honey](#problem-5-container-with-most-honey)
- [Problem 6: Merge Intervals](#problem-6-merge-intervals)

### [Version 2 Advanced Set](#version-2-advanced-set)
- [Problem 1: Matrix Addition](#problem-1-matrix-addition)
- [Problem 2: Two-Pointer Palindrome](#problem-2-two-pointer-palindrome)
- [Problem 3: Squash Spaces](#problem-3-squash-spaces)
- [Problem 4: Two-Pointer Two Sum](#problem-4-two-pointer-two-sum)
- [Problem 5: Three Sum](#problem-5-three-sum)
- [Problem 6: Insert Interval](#problem-6-insert-interval)

---

## Version 1 Advanced Set

### Problem 1: Transpose Matrix

Write a function `transpose()` that accepts a 2D integer array `matrix` and returns the transpose of `matrix`. The transpose of a matrix is the matrix flipped over its main diagonal, swapping the rows and columns.

```python
def transpose(matrix):
    pass
```

**Example Usage:**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose(matrix)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transpose(matrix)  # Output: [[1, 4], [2, 5], [3, 6]]
```

**✨ AI Hint:** Nested Lists  
**✨ AI Hint:** Nested Loops

---

### Problem 2: Two-Pointer Reverse List

Write a function `reverse_list()` that takes in a list `lst` and returns elements of the list in reverse order. The list should be reversed in-place without using list slicing (e.g. `lst[::-1]`).

Instead, use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.

```python
def reverse_list(lst):
    pass
```

**Example Usage:**
```python
lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
reverse_list(lst)  # Output: ["eeyore", "roo", "piglet", "christopher robin", "pooh"]
```

**💡 Hint:** While Loops

---

### Problem 3: Remove Duplicates

Write a function `remove_dupes()` that accepts a sorted array `items`, and removes the duplicates in-place such that each element appears only once. Return the length of the modified array. You may not create another array; your implementation must modify the original input array `items`.

```python
def remove_dupes(items):
    pass
```

**Example Usage:**
```python
items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
remove_dupes(items)  # Output: 4

items = ["extract of malt", "haycorns", "honey", "thistle"]
remove_dupes(items)  # Output: 4
```

**💡 Hint:** Two Pointer Technique

---

### Problem 4: Sort Array by Parity

Given an integer array `nums`, write a function `sort_by_parity()` that moves all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

```python
def sort_by_parity(nums):
    pass
```

**Example Usage:**
```python
nums = [3, 1, 2, 4]
sort_by_parity(nums)  # Output: [2, 4, 3, 1]

nums = [0]
sort_by_parity(nums)  # Output: [0]
```

**💡 Hint:** Remainders with Modulus Division

---

### Problem 5: Container with Most Honey

Christopher Robin is helping Pooh construct the biggest hunny jar possible. Help his write a function that accepts an integer array `height` of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most honey.

Return the maximum amount of honey a container can store.

Notice that you may not slant the container.

```python
def most_honey(height):
    pass
```

**Example Usage:**
```python
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
most_honey(height)  # Output: 49

height = [1, 1]
most_honey(height)  # Output: 1
```

---

### Problem 6: Merge Intervals

Write a function `merge_intervals()` that accepts an array of intervals where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

```python
def merge_intervals(intervals):
    pass
```

**Example Usage:**
```python
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals)  # Output: [[1, 6], [8, 10], [15, 18]]

intervals = [[1, 4], [4, 5]]
merge_intervals(intervals)  # Output: [[1, 5]]
```

**💡 Hint:** Sorting Lists

---

## Version 2 Advanced Set

### Problem 1: Matrix Addition

Write a function `add_matrices()` that accepts to n x m matrices `matrix1` and `matrix2`. The function should return an n x m matrix `sum_matrix` that is the sum of the given matrices such that each value in `sum_matrix` is the sum of values of corresponding elements in `matrix1` and `matrix2`.

```python
def add_matrices(matrix1, matrix2):
    pass
```

**Example Usage:**
```python
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

add_matrices(matrix1, matrix2)  # Output: [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
```

**✨ AI Hint:** Nested Lists  
**✨ AI Hint:** Nested Loops

---

### Problem 2: Two-Pointer Palindrome

Write a function `is_palindrome()` that takes in a string `s` as a parameter and returns `True` if the string is a palindrome and `False` otherwise. You may assume the string contains only lowercase alphabetic characters.

The function must use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.

```python
def is_palindrome(s):
    pass
```

**Example Usage:**
```python
s = "madam"
is_palindrome(s)  # Output: True

s = "madamweb"
is_palindrome(s)  # Output: False
```

**💡 Hint:** While Loops  
**💡 Hint:** Two Pointer Technique

---

### Problem 3: Squash Spaces

Write a function `squash_spaces()` that takes in a string `s` as a parameter and returns a new string with each substring with consecutive spaces reduced to a single space. Assume `s` can contain leading or trailing spaces, but in the result should be trimmed. Do not use any of the built-in trim methods.

```python
def squash_spaces(s):
    pass
```

**Example Usage:**
```python
s = "   Up,     up,   and  away! "
squash_spaces(s)  # Output: "Up, up, and away!"

s = "With great power comes great responsibility."
squash_spaces(s)  # Output: "With great power comes great responsibility."
```

---

### Problem 4: Two-Pointer Two Sum

Use the two pointer approach to implement a function `two_sum()` that takes in a sorted list of integers `nums` and an integer `target` as parameters and returns the indices of the two numbers that add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the indices in any order.

```python
def two_sum(nums, target):
    pass
```

**Example Usage:**
```python
nums = [2, 7, 11, 15]
target = 9
two_sum(nums, target)  # Output: [0, 1]

nums = [2, 7, 11, 15]
target = 18
two_sum(nums, target)  # Output: [1, 2]
```

---

### Problem 5: Three Sum

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

```python
def three_sum(nums):
    pass
```

**Example Usage:**
```python
nums = [-1, 0, 1, 2, -1, -4]
three_sum(nums)  # Output: [[-1, -1, 2], [-1, 0, 1]]

nums = [0, 1, 1]
three_sum(nums)  # Output: []

nums = [0, 0, 0]
three_sum(nums)  # Output: [[0, 0, 0]]
```

**💡 Hint:** Sorting Lists

---

### Problem 6: Insert Interval

Implement a function `insert_interval()` that accepts an array of non-overlapping intervals `intervals` where `intervals[i] = [starti, endi]` represent the start and the end of the ith interval and `intervals` is sorted in ascending order by `starti`. The function also accepts an interval `new_interval = [start, end]` that represents the start and end of another interval.

Insert `new_interval` into `intervals` such that `intervals` is still sorted in ascending order by `starti` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` after the insertion.

You don't need to modify `intervals` in-place. You can make a new array and return it.

```python
def insert_interval(intervals, new_interval):
    pass
```

**Example Usage:**
```python
intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
insert_interval(intervals, new_interval)  # Output: [[1, 5], [6, 9]]

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval = [4, 8]
insert_interval(intervals, new_interval)  # Output: [[1, 2], [3, 10], [12, 16]]
```