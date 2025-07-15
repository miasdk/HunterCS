# Unit 01 Session 1 - Advanced Version 1

## Overview
This problem set focuses on advanced Python concepts and problem-solving skills for Unit 01, Session 1 (Advanced, Version 1).

## Learning Objectives
- Apply advanced Python syntax and data structures
- Tackle more challenging algorithmic problems
- Develop deeper problem-solving strategies

## Problems
1. **Problem 1:** [Short description]
2. **Problem 2:** [Short description]
3. **Problem 3:** [Short description]
...

## Key Concepts
- Data Structures: List, Dict, Set
- Algorithms: Greedy, Stack, Queue
- Python Features: Lambda, comprehensions, advanced slicing

## Tips & Pitfalls
- Break down complex problems
- Test edge cases thoroughly
- Watch for performance bottlenecks

## Testing
- [ ] All problems have test cases
- [ ] Edge cases considered

---

## Table of Contents

### [Basic Problems](#basic-problems)
- [Linear Search](#linear-search)
- [Variable Operations](#variable-operations)
- [String Filtering](#string-filtering)
- [Non-decreasing Array](#non-decreasing-array)
- [Missing Range Detection](#missing-range-detection)
- [2D Matrix Counting](#2d-matrix-counting)
- [Divisible Pairs](#divisible-pairs)
- [Local Matrix Maximums](#local-matrix-maximums)

### [Advanced Problems](#advanced-problems)
- [Character Search in Words](#character-search-in-words)
- [FizzBuzz Variant](#fizzbuzz-variant)
- [String Shuffling](#string-shuffling)
- [Greedy Box Packing](#greedy-box-packing)
- [Maximum Row Sum](#maximum-row-sum)
- [Element Comparison Count](#element-comparison-count)
- [Matrix Diagonal Sum](#matrix-diagonal-sum)
- [Circular Array Decryption](#circular-array-decryption)

## Basic Problems

### Linear Search
Find the first occurrence of a target value in a list. Return -1 if not found. Do not use built-in functions.

**Function Signature:**
```python
def linear_search(lst, target):
    pass
```

**Example Usage:**
```python
items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
linear_search(items, 'hunny')  # Returns: 3

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
linear_search(items, 'red balloon')  # Returns: -1
```

**Hint:** Python Basics

### Variable Operations
Process a list of operations that increment or decrement a counter starting from 1.

- `bouncy` and `flouncy` increment by 1
- `trouncy` and `pouncy` decrement by 1

**Function Signature:**
```python
def final_value_after_operations(operations):
    pass
```

**Example Usage:**
```python
operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)  # Returns: 2

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)  # Returns: 4
```

### String Filtering
Remove specific substrings ('t', 'i', 'gg', 'er') from a word. Case insensitive.

**Function Signature:**
```python
def tiggerfy(word):
    pass
```

**Example Usage:**
```python
tiggerfy("Trigger")   # Returns: "r"
tiggerfy("eggplant")  # Returns: "eplan"
tiggerfy("Choir")     # Returns: "Chor"
```

**Hint:** String Methods

### Non-decreasing Array
Check if an array can become non-decreasing by modifying at most one element.

**Function Signature:**
```python
def non_decreasing(nums):
    pass
```

**Example Usage:**
```python
non_decreasing([4, 2, 3])  # Returns: True
non_decreasing([4, 2, 1])  # Returns: False
```

### Missing Range Detection
Find missing numbers in a range and return as sorted list of ranges.

**Function Signature:**
```python
def find_missing_clues(clues, lower, upper):
    pass
```

**Example Usage:**
```python
clues = [0, 1, 3, 50, 75]
find_missing_clues(clues, 0, 99)  # Returns: [[2, 2], [4, 49], [51, 74], [76, 99]]

clues = [-1]
find_missing_clues(clues, -1, -1)  # Returns: []
```

**Hint:** Nested Lists

### 2D Matrix Counting
Count occurrences of a specific character ('c') in a 2D matrix.

**Function Signature:**
```python
def harvest(vegetable_patch):
    pass
```

**Example Usage:**
```python
vegetable_patch = [
    ['x', 'c', 'x'],
    ['x', 'x', 'x'],
    ['x', 'c', 'c'],
    ['c', 'c', 'c']
]
harvest(vegetable_patch)  # Returns: 6
```

**Hint:** Nested Loops

### Divisible Pairs
Count pairs where `pile1[i]` is divisible by `pile2[j] * k`.

**Function Signature:**
```python
def good_pairs(pile1, pile2, k):
    pass
```

**Example Usage:**
```python
pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
good_pairs(pile1, pile2, k)  # Returns: 5

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
good_pairs(pile1, pile2, k)  # Returns: 2
```

**Hint:** Remainders with Modulus Division

### Local Matrix Maximums
Find the maximum value in every contiguous 3×3 submatrix of an n×n grid.

**Function Signature:**
```python
def local_maximums(grid):
    pass
```

**Example Usage:**
```python
grid = [
    [9, 9, 8, 1],
    [5, 6, 2, 6],
    [8, 2, 6, 4],
    [6, 2, 2, 2]
]
local_maximums(grid)  # Returns: [[9, 9], [8, 6]]

grid = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]
local_maximums(grid)  # Returns: [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
```

## Advanced Problems

### Character Search in Words
Return indices of words that contain a specific character.

**Function Signature:**
```python
def words_with_char(words, x):
    pass
```

**Example Usage:**
```python
words = ["batman", "superman"]
words_with_char(words, "a")  # Returns: [0, 1]

words = ["black panther", "hulk", "black widow", "thor"]
words_with_char(words, "a")  # Returns: [0, 2]

words = ["star-lord", "gamora", "groot", "rocket"]
words_with_char(words, "z")  # Returns: []
```

**Hint:** Python Basics

### FizzBuzz Variant
Generate a 1-indexed string array based on divisibility rules.

- Divisible by 3 and 5: "HulkSmash"
- Divisible by 3: "Hulk"
- Divisible by 5: "Smash"
- Otherwise: number as string

**Function Signature:**
```python
def hulk_smash(n):
    pass
```

**Example Usage:**
```python
hulk_smash(3)   # Returns: ["1", "2", "Hulk"]
hulk_smash(5)   # Returns: ["1", "2", "Hulk", "4", "Smash"]
hulk_smash(15)  # Returns: ["1", "2", "Hulk", "4", "Smash", "Hulk", "7", "8", "Hulk", "Smash", "11", "Hulk", "13", "14", "HulkSmash"]
```

### String Shuffling
Rearrange string characters based on index mapping. Character at position i moves to position `indices[i]`.

**Function Signature:**
```python
def shuffle(message, indices):
    pass
```

**Example Usage:**
```python
message = "evil"
indices = [3, 1, 2, 0]
shuffle(message, indices)  # Returns: "lvie"

message = "findme"
indices = [0, 1, 2, 3, 4, 5]
shuffle(message, indices)  # Returns: "findme"
```

**Hint:** String Methods

### Greedy Box Packing
Find minimum number of boxes needed to pack all meals. Meals can be split between boxes.

**Function Signature:**
```python
def minimum_boxes(meals, capacity):
    pass
```

**Example Usage:**
```python
meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
minimum_boxes(meals, capacity)  # Returns: 2

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]
minimum_boxes(meals, capacity)  # Returns: 4
```

**Hint:** Sorting Lists

### Maximum Row Sum
Find the customer with maximum wealth across all bank accounts. Return `[index, total_wealth]`.

**Function Signature:**
```python
def wealthiest_customer(accounts):
    pass
```

**Example Usage:**
```python
accounts = [
    [1, 2, 3],
    [3, 2, 1]
]
wealthiest_customer(accounts)  # Returns: [0, 6]

accounts = [
    [1, 5],
    [7, 3],
    [3, 5]
]
wealthiest_customer(accounts)  # Returns: [1, 10]

accounts = [
    [2, 8, 7],
    [7, 1, 3],
    [1, 9, 5]
]
wealthiest_customer(accounts)  # Returns: [0, 17]
```

**Hint:** Nested Lists

### Element Comparison Count
For each element, count how many other elements in the array are smaller than it.

**Function Signature:**
```python
def smaller_than_current(nums):
    pass
```

**Example Usage:**
```python
nums = [8, 1, 2, 2, 3]
smaller_than_current(nums)  # Returns: [4, 0, 1, 1, 3]

nums = [6, 5, 4, 8]
smaller_than_current(nums)  # Returns: [2, 1, 0, 3]

nums = [7, 7, 7, 7]
smaller_than_current(nums)  # Returns: [0, 0, 0, 0]
```

**Hint:** Nested Loops

### Matrix Diagonal Sum
Sum primary and secondary diagonals, avoiding double-counting the center element in odd-sized matrices.

**Function Signature:**
```python
def diagonal_sum(grid):
    pass
```

**Example Usage:**
```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
diagonal_sum(grid)  # Returns: 25

grid = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]
diagonal_sum(grid)  # Returns: 8

grid = [[5]]
diagonal_sum(grid)  # Returns: 5
```

### Circular Array Decryption
Decrypt a circular array based on key value k.

- If k > 0: replace with sum of next k numbers
- If k < 0: replace with sum of previous k numbers  
- If k = 0: replace with 0

**Function Signature:**
```python
def defuse(code, k):
    pass
```

**Example Usage:**
```python
code = [5, 7, 1, 4]
k = 3
defuse(code, k)  # Returns: [12, 10, 16, 13]

code = [1, 2, 3, 4]
k = 0
defuse(code, k)  # Returns: [0, 0, 0, 0]

code = [2, 4, 9, 3]
k = -2
defuse(code, k)  # Returns: [12, 5, 6, 13]
```