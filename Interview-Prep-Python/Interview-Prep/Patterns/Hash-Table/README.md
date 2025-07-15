# Hash Table Pattern - Python Interview Guide

## 🎯 Pattern Recognition
**Use dictionaries and sets when you need:**
- Fast lookups (O(1) average)
- Counting frequency of elements
- Finding pairs/complements
- Removing duplicates
- Grouping related data

## 📋 Core Templates

### Basic Dictionary Operations
```python
# Method 1: Basic dict with get()
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1

# Method 2: Using dict.setdefault()
freq = {}
for item in items:
    freq.setdefault(item, 0)
    freq[item] += 1

# Method 3: defaultdict (cleanest)
from collections import defaultdict
freq = defaultdict(int)
for item in items:
    freq[item] += 1

# Method 4: Counter (most Pythonic)
from collections import Counter
freq = Counter(items)
```

### Two Sum Pattern
```python
def two_sum(nums: list[int], target: int) -> list[int]:
    """Hash table approach - O(n) time, O(n) space"""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

## 🔥 Must-Know Problems

### 1. Two Sum (Easy) ⭐⭐⭐
```python
def two_sum(nums: list[int], target: int) -> list[int]:
    """Most important interview problem"""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Alternative: More explicit
def two_sum_explicit(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if seen.get(complement) is not None:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### 2. Valid Anagram (Easy) ⭐⭐
```python
def is_anagram(s: str, t: str) -> bool:
    """Multiple Pythonic approaches"""
    
    # Method 1: Counter (most readable)
    from collections import Counter
    return Counter(s) == Counter(t)
    
    # Method 2: Sorting (space efficient)
    return sorted(s) == sorted(t)
    
    # Method 3: Manual counting (interview version)
    if len(s) != len(t):
        return False
    
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        count[char] = count.get(char, 0) - 1
        
    return all(v == 0 for v in count.values())
```

### 3. Contains Duplicate (Easy) ⭐
```python
def contains_duplicate(nums: list[int]) -> bool:
    """Set-based solution"""
    return len(nums) != len(set(nums))

# Alternative: Early termination
def contains_duplicate_early(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

### 4. Group Anagrams (Medium) ⭐⭐
```python
def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Python's power with defaultdict"""
    from collections import defaultdict
    
    groups = defaultdict(list)
    for s in strs:
        # Sorted string as key
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())

# Alternative: Using tuple as key
def group_anagrams_tuple(strs: list[str]) -> list[list[str]]:
    from collections import defaultdict
    
    groups = defaultdict(list)
    for s in strs:
        # Character count as key
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        groups[tuple(count)].append(s)
    
    return list(groups.values())
```

### 5. Top K Frequent Elements (Medium) ⭐⭐
```python
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Counter + heap solution"""
    from collections import Counter
    import heapq
    
    # Count frequencies
    count = Counter(nums)
    
    # Use heap to get top k
    return heapq.nlargest(k, count.keys(), key=count.get)

# Alternative: Bucket sort approach
def top_k_frequent_bucket(nums: list[int], k: int) -> list[int]:
    from collections import Counter
    
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    
    # Put numbers in frequency buckets
    for num, freq in count.items():
        buckets[freq].append(num)
    
    # Collect top k from highest frequency
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    
    return result
```

## 💡 Key Python Patterns

### Pattern 1: Frequency Counting
```python
# Basic pattern
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1

# Pythonic pattern
from collections import Counter
freq = Counter(items)
```

### Pattern 2: Complement Search
```python
# Template for Two Sum variants
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        # Found pair
        return [seen[complement], i]
    seen[num] = i
```

### Pattern 3: Grouping/Bucketing
```python
# Template for grouping problems
from collections import defaultdict
groups = defaultdict(list)
for item in items:
    key = generate_key(item)  # Define your key function
    groups[key].append(item)
return list(groups.values())
```

### Pattern 4: Set Operations
```python
# Union, intersection, difference
set1 = set(list1)
set2 = set(list2)

union = set1 | set2
intersection = set1 & set2
difference = set1 - set2
```

## ⚡ Python Interview Tips

### Pythonic Advantages
- **dict.get()** for safe access with defaults
- **Counter** for frequency counting
- **defaultdict** for automatic initialization
- **set operations** for mathematical set problems

### Performance Notes
- **dict lookup**: O(1) average, O(n) worst case
- **set operations**: O(1) for add/remove/contains
- **Counter most_common()**: O(n log k) for top k elements

### Common Mistakes
- Forgetting to handle empty inputs
- Using `dict[key]` instead of `dict.get(key, default)`
- Not considering hash collision edge cases
- Overcomplicating when Counter would work

## 🎪 Practice Progression

### Week 1: Master These (Easy)
1. Two Sum ⭐⭐⭐
2. Valid Anagram ⭐⭐
3. Contains Duplicate ⭐

### Week 2: Add These (Medium)
1. Group Anagrams ⭐⭐
2. Top K Frequent Elements ⭐⭐
3. Longest Substring Without Repeating ⭐⭐

### Week 3: Challenge (Medium-Hard)
1. 4Sum II ⭐⭐⭐
2. Substring with Concatenation ⭐⭐⭐
3. Design HashSet ⭐⭐

## 🔥 Interview Power Moves

### Show Python Mastery
```python
# Instead of manual loops
freq = {}
for item in items:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

# Use Counter
from collections import Counter
freq = Counter(items)
```

### Type Hints for Clarity
```python
def two_sum(nums: list[int], target: int) -> list[int]:
    """Type hints show professionalism"""
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

## 📚 Related Files
- **Code Examples**: `../../../Code-Library/By-Topic/Hashing/`
- **Python Stdlib**: `../Python-Stdlib/collections-guide.md`
- **Quick Reference**: `../../../Quick-Reference/`

---

**🎯 Master this pattern first!** Hash tables are the foundation of efficient algorithms and the most tested pattern in interviews. 