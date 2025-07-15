# TIP102 Unit 1 Version A (Standard) - Practice Problems

## Table of Contents

### [Coding Problems](#coding-problems)
- [Problem 1: Unique Characters](#problem-1-unique-characters)
- [Problem 2: Needle in Haystack](#problem-2-needle-in-haystack)
- [Problem 3: Can Place Flowers](#problem-3-can-place-flowers)
- [Problem 7: Find the Bug - Reverse List](#problem-7-find-the-bug---reverse-list)

### [Multiple Choice Problems](#multiple-choice-problems)
- [Problem 4: String Immutability](#problem-4-string-immutability)
- [Problem 5: Adjacent Characters Count](#problem-5-adjacent-characters-count)
- [Problem 6: Threshold Sum](#problem-6-threshold-sum)

---

## Coding Problems

### Problem 1: Unique Characters
Check if every character in a string is unique.

**Function Signature:**
```python
def has_all_unique_characters(s):
    pass
```

**Problem Description:**
Given a string `s`, return `True` if every character in the string is unique. Return `False` if any characters in `s` are repeated.

**Example Usage:**
```python
print(has_all_unique_characters("abcdef"))  # Returns: True
print(has_all_unique_characters("aabbcc"))  # Returns: False
print(has_all_unique_characters(""))       # Returns: True
```

**Key Concept:** Set-based duplicate detection

---

### Problem 2: Needle in Haystack
Find the first occurrence of a substring in a string.

**Function Signature:**
```python
def find_needle(haystack, needle):
    pass
```

**Problem Description:**
Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or -1 if `needle` is not part of `haystack`.

**Example Usage:**
```python
print(find_needle("sadbutsad", "sad"))    # Returns: 0
print(find_needle("leetcode", "leeto"))   # Returns: -1
print(find_needle("mad", "madden"))       # Returns: -1 (needle longer than haystack)
```

**Key Concept:** String searching and indexing

---

### Problem 3: Can Place Flowers
Determine if flowers can be planted without violating adjacency rules.

**Function Signature:**
```python
def can_place_flowers(flowerbed, n):
    pass
```

**Problem Description:**
You have a flowerbed where some plots are planted (1) and some are empty (0). Flowers cannot be planted directly adjacent to another flower. Given an integer array `flowerbed` and an integer `n`, return `True` if `n` new flowers can be planted without violating the no-adjacent-flowers rule.

**Example Usage:**
```python
print(can_place_flowers([1,0,0,0,1], 1))  # Returns: True
print(can_place_flowers([1,0,0,0,1], 2))  # Returns: False
```

**Key Concept:** Array traversal with adjacency constraints

**Hint:** Focus on each plot and check its neighboring plots. Consider edge cases for the first and last positions.

---

### Problem 7: Find the Bug - Reverse List
Debug and fix a broken list reversal function.

**Function Signature:**
```python
def reverse_lst(lst):
    pass
```

**Problem Description:**
The provided code incorrectly implements a function that should reverse a list in-place. Identify and fix the bugs.

**Buggy Code:**
```python
def reverse_lst(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left] = lst[right]    # Bug: No temporary variable
        lst[right] = lst[left]    # Bug: Data already overwritten
        left -= 1                 # Bug: Wrong direction
        right += 1                # Bug: Wrong direction
    return lst
```

**Example Usage:**
```python
print(reverse_lst([1, 2, 3, 4, 5]))  # Should return: [5, 4, 3, 2, 1]
print(reverse_lst([10, 20, 30, 40])) # Should return: [40, 30, 20, 10]
```

**Key Concept:** Two-pointer technique with proper swapping

---

## Multiple Choice Problems

### Problem 4: String Immutability
**Question:** What is the output of the following code snippet?

```python
name = "codepath"
name[0] = "C"
print(name)
```

**Options:**
- a) Codepath
- b) Ccodepath  
- c) C
- d) Throws an error because strings are immutable and characters cannot be changed once the string is created.

**Answer:** d) Throws an error because strings are immutable

**Key Concept:** String immutability in Python

---

### Problem 5: Adjacent Characters Count
**Question:** What is the output of the following code snippet?

```python
def mystery_function(s):
    count = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
    return count

result = mystery_function("AABBAB")
print(result)
```

**Options:**
- a) 1
- b) 2
- c) 3
- d) 4

**Answer:** b) 2

**Explanation:** The function counts adjacent identical characters. In "AABBAB":
- Position 1: A == A (count = 1)
- Position 2: A != B 
- Position 3: B == B (count = 2)
- Position 4: B != A
- Position 5: A != B
Result: 2

**Key Concept:** String iteration and comparison

---

### Problem 6: Threshold Sum
**Question:** What is the output of the following code snippet?

```python
def mystery_function(lst, threshold):
    total = 0
    i = 0
    while i < len(lst) and total + lst[i] <= threshold:
        total += lst[i]
        i += 1
    return total

result = mystery_function([1, 2, 3, 4, 5], 7)
print(result)
```

**Options:**
- a) 3
- b) 6
- c) 7
- d) 10

**Answer:** b) 6

**Explanation:** The function sums elements while the total stays within the threshold:
- total = 0, add 1: total = 1 (≤ 7) ✓
- total = 1, add 2: total = 3 (≤ 7) ✓  
- total = 3, add 3: total = 6 (≤ 7) ✓
- total = 6, add 4: would be 10 (> 7) ✗ Stop
Result: 6

**Key Concept:** While loop with cumulative conditions

---

## Practice Notes

**Important Reminders:**
- Practice implementing these problems from scratch
- Focus on understanding the underlying algorithms and data structures
- Test your solutions with multiple edge cases
- Consider time and space complexity

**Key Topics Covered:**
- String manipulation and properties
- Array traversal and modification
- Set-based operations
- Two-pointer techniques
- Debugging and code analysis