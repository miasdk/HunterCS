# Python Interview Cheat Sheet

## 🐍 Essential Python for Technical Interviews

### Core Data Structures

#### Lists (Dynamic Arrays)
```python
# Creation and basic operations
nums = [1, 2, 3]
nums.append(4)              # O(1) amortized
nums.insert(0, 0)           # O(n) - inserts at index
nums.pop()                  # O(1) - removes last
nums.pop(0)                 # O(n) - removes first
nums.remove(2)              # O(n) - removes first occurrence
len(nums)                   # O(1) - length

# Slicing
nums[1:3]                   # [2, 3] - slice
nums[::-1]                  # Reverse list
nums[::2]                   # Every 2nd element

# List comprehensions
squares = [x**2 for x in range(5)]
filtered = [x for x in nums if x > 0]
```

#### Dictionaries (Hash Tables)
```python
# Creation and operations
d = {}
d = {'a': 1, 'b': 2}
d['c'] = 3                  # O(1) average insertion
d.get('a', 0)               # O(1) safe access with default
'a' in d                    # O(1) membership test
d.pop('a', None)            # O(1) remove with default

# Iteration
for key in d:               # Keys
for value in d.values():    # Values  
for k, v in d.items():      # Key-value pairs

# Common patterns
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1
```

#### Sets
```python
# Creation and operations
s = set()
s = {1, 2, 3}
s.add(4)                    # O(1) average
s.remove(2)                 # O(1) average, KeyError if missing
s.discard(2)                # O(1) average, no error if missing
1 in s                      # O(1) membership

# Set operations
s1 | s2                     # Union
s1 & s2                     # Intersection
s1 - s2                     # Difference
s1 ^ s2                     # Symmetric difference
```

### Built-in Functions for Interviews

#### Essential Functions
```python
# Sequence operations
len(seq)                    # Length
sum(nums)                   # Sum of numbers
max(nums)                   # Maximum value
min(nums)                   # Minimum value
sorted(seq)                 # Returns new sorted list
seq.sort()                  # In-place sort

# Iteration helpers
enumerate(seq)              # (index, value) pairs
zip(seq1, seq2)            # Pair elements from sequences
range(start, stop, step)    # Generate number sequence

# Type conversions
list(seq)                   # Convert to list
set(seq)                    # Convert to set
str(obj)                    # Convert to string
int(s)                      # String to integer
```

#### String Operations
```python
s = "hello world"
s.split()                   # Split by whitespace -> ['hello', 'world']
s.split(',')                # Split by delimiter
s.strip()                   # Remove leading/trailing whitespace
s.replace('l', 'x')         # Replace substring
s.upper() / s.lower()       # Case conversion
s.isalnum()                 # Check if alphanumeric
''.join(list_of_strings)    # Join strings
```

### Collections Module (Interview Gold)

#### Counter - Frequency Counting
```python
from collections import Counter

# Most common use case
counter = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
counter.most_common(2)      # [('a', 3), ('b', 2)]
counter['a']                # 3 - frequency of 'a'

# Arithmetic operations
c1 + c2                     # Add counts
c1 - c2                     # Subtract counts
c1 & c2                     # Intersection (min counts)
c1 | c2                     # Union (max counts)
```

#### defaultdict - Auto-initialization
```python
from collections import defaultdict

# Group items
groups = defaultdict(list)
for item in items:
    key = compute_key(item)
    groups[key].append(item)

# Count with defaultdict
count = defaultdict(int)
for item in items:
    count[item] += 1
```

#### deque - Double-ended Queue
```python
from collections import deque

# BFS and sliding window
queue = deque([1, 2, 3])
queue.append(4)             # Add to right
queue.appendleft(0)         # Add to left
queue.pop()                 # Remove from right
queue.popleft()             # Remove from left

# All operations are O(1)
```

### Algorithms and Patterns

#### Sorting and Searching
```python
# Custom sorting
nums.sort(key=lambda x: abs(x))           # Sort by absolute value
words.sort(key=len)                       # Sort by length
tuples.sort(key=lambda x: (x[1], x[0]))  # Sort by second, then first

# Binary search
import bisect
pos = bisect.bisect_left(sorted_list, target)  # Insert position
```

#### Common Interview Patterns
```python
# Two pointers
left, right = 0, len(arr) - 1
while left < right:
    if condition:
        # Process
        left += 1
        right -= 1
    elif need_increase:
        left += 1
    else:
        right -= 1

# Sliding window
left = 0
for right in range(len(arr)):
    # Expand window
    while window_invalid:
        # Shrink window
        left += 1
    # Update result

# Frequency counting
from collections import Counter
freq = Counter(items)
```

### Input/Output for Coding Problems

#### Reading Input
```python
# Single values
n = int(input())
s = input().strip()

# Multiple values on one line
a, b, c = map(int, input().split())
nums = list(map(int, input().split()))

# Multiple lines
lines = []
for _ in range(n):
    lines.append(input().strip())
```

#### Useful Conversions
```python
# String to character list
chars = list(s)

# Integer to string
s = str(num)

# String to integer (with error handling)
try:
    num = int(s)
except ValueError:
    # Handle invalid input
    pass
```

### Advanced Python Features

#### List Comprehensions and Generators
```python
# List comprehension
squares = [x**2 for x in range(10) if x % 2 == 0]

# Dictionary comprehension
word_lengths = {word: len(word) for word in words}

# Generator (memory efficient)
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

#### Lambda Functions
```python
# Sorting with lambda
students.sort(key=lambda x: x.grade)

# Filtering
evens = list(filter(lambda x: x % 2 == 0, nums))

# Mapping
doubled = list(map(lambda x: x * 2, nums))
```

#### Multiple Assignment
```python
# Swapping
a, b = b, a

# Multiple return values
def min_max(arr):
    return min(arr), max(arr)

min_val, max_val = min_max(numbers)
```

### Performance Tips

#### Time Complexity Quick Reference
```python
# O(1) operations
dict[key], set.add(), list.append(), deque operations

# O(log n) operations  
bisect operations, heap operations

# O(n) operations
list iteration, dict.items(), set operations, sum(), max(), min()

# O(n log n) operations
sorted(), list.sort()

# O(n²) operations (avoid in interviews)
Nested loops, list.remove() in loop
```

#### Memory Optimization
```python
# Use generators for large sequences
def large_sequence():
    for i in range(1000000):
        yield expensive_computation(i)

# Use slots for memory-efficient classes
class Point:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x, self.y = x, y
```

### Common Interview Mistakes to Avoid

#### Python-Specific Pitfalls
```python
# Mutable default arguments (BAD)
def bad_function(arr=[]):
    arr.append(1)
    return arr

# Correct way
def good_function(arr=None):
    if arr is None:
        arr = []
    arr.append(1)
    return arr

# Integer division in Python 3
5 // 2  # 2 (floor division)
5 / 2   # 2.5 (true division)

# List modification during iteration (BAD)
for item in items:
    if condition:
        items.remove(item)  # Don't do this

# Correct way
items = [item for item in items if not condition]
```

### Interview Best Practices

#### Code Style
```python
# Use type hints for clarity
def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Meaningful variable names
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    # Clear variable names make intent obvious
```

#### Explanation Templates
```python
# Always explain your approach
"""
1. Use hash table for O(1) lookups
2. For each number, check if complement exists
3. Store number -> index mapping
4. Return indices when complement found

Time: O(n), Space: O(n)
"""
```

---

**🎯 Master these fundamentals and you'll handle 90% of Python interview problems efficiently!** 