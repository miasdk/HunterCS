# HunterCS-Interview-Prep-Python - Repository Template

## 🐍 Python-Optimized Interview Preparation

This template provides the complete structure for creating a Python version of the C++ interview prep repository, optimized for Python's unique strengths and idioms.

## 📁 Directory Structure Template

```
HunterCS-Interview-Prep-Python/
├── 📍 START-HERE/
│   ├── README.md                    ← Python-specific welcome
│   └── Python-User-Manual.md       ← Python daily practice guide
├── ⚡ Quick-Reference/
│   ├── python-cheat-sheet.md       ← dict, list, set operations
│   ├── builtin-functions.md        ← len, sum, max, min, sorted
│   └── algorithm-patterns-quick-ref.md
├── 🎯 Interview-Prep/
│   ├── Patterns/
│   │   ├── Hash-Table/
│   │   │   ├── README.md           ← dict, set, Counter patterns
│   │   │   └── examples.py
│   │   ├── Tree-Traversal/
│   │   │   ├── README.md           ← collections.deque, recursion
│   │   │   └── examples.py
│   │   ├── Array-TwoPointer/
│   │   │   ├── README.md           ← list operations, slicing
│   │   │   └── examples.py
│   │   ├── Dynamic-Programming/
│   │   │   ├── README.md           ← list comprehensions, memoization
│   │   │   └── examples.py
│   │   └── Graph-Algorithms/
│   │       ├── README.md           ← defaultdict, adjacency lists
│   │       └── examples.py
│   ├── Daily-Practice/
│   │   ├── README.md               ← Python practice methodology
│   │   └── practice-log.py         ← Progress tracking script
│   ├── Mock-Interviews/
│   └── Python-Stdlib/
│       ├── collections-guide.md    ← Counter, defaultdict, deque
│       ├── heapq-guide.md          ← Priority queues
│       ├── itertools-guide.md      ← combinations, permutations
│       └── bisect-guide.md         ← Binary search
├── 💻 Code-Library/
│   ├── By-Topic/
│   │   ├── Hashing/
│   │   │   ├── two_sum.py
│   │   │   ├── valid_anagram.py
│   │   │   └── group_anagrams.py
│   │   ├── Trees/
│   │   │   ├── max_depth.py
│   │   │   ├── same_tree.py
│   │   │   └── level_order.py
│   │   ├── Arrays/
│   │   │   ├── two_sum_sorted.py
│   │   │   ├── remove_duplicates.py
│   │   │   └── valid_palindrome.py
│   │   ├── DP/
│   │   │   ├── fibonacci.py
│   │   │   ├── coin_change.py
│   │   │   └── longest_subsequence.py
│   │   └── Graphs/
│   │       ├── dfs_bfs.py
│   │       ├── course_schedule.py
│   │       └── word_ladder.py
│   ├── By-Difficulty/
│   │   ├── Easy/
│   │   ├── Medium/
│   │   └── Hard/
│   └── Templates/
│       ├── hash_table_template.py
│       ├── tree_traversal_template.py
│       ├── two_pointer_template.py
│       ├── dp_template.py
│       └── graph_template.py
├── 📖 Reference/
│   ├── Python-Big-O.md            ← Time complexity in Python
│   ├── Python-DP.md               ← DP with Python optimizations
│   ├── Python-Trees.md            ← Tree algorithms in Python
│   └── Python-Graphs.md           ← Graph algorithms with collections
├── 🎓 Course-Materials/            ← Academic content (if applicable)
└── 🔧 Tools/
    ├── practice-timer.py           ← Same timer, Python version
    ├── test-runner.py              ← Automated testing
    └── profile-performance.py     ← Performance analysis
```

## 🐍 Python-Specific Content Examples

### Hash Table Pattern (Python Version)
```python
# Hash Table Pattern - Python Interview Guide

## 🎯 Pattern Recognition
**Use dictionaries and sets when you need:**
- Fast lookups (O(1) average)
- Counting frequency of elements  
- Finding pairs/complements
- Removing duplicates
- Grouping related data

## 📋 Core Templates

### Basic Frequency Counting
```python
from collections import Counter, defaultdict

# Method 1: Basic dict
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1

# Method 2: defaultdict
freq = defaultdict(int)
for item in items:
    freq[item] += 1

# Method 3: Counter (most Pythonic)
freq = Counter(items)
```

### Two Sum Pattern
```python
def two_sum(nums, target):
    """Hash table approach - O(n) time, O(n) space"""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

## 🔥 Must-Know Problems (Python)

### 1. Valid Anagram (Pythonic)
```python
def is_anagram(s, t):
    # Method 1: Counter (most readable)
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

### 2. Group Anagrams (Python Power)
```python
def group_anagrams(strs):
    from collections import defaultdict
    
    groups = defaultdict(list)
    for s in strs:
        # Sorted string as key
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())
```
```

### Tree Traversal Pattern (Python Version)
```python
# Tree Traversal Pattern - Python Interview Guide

## 📋 Core Templates

### Tree Node Definition
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### DFS Traversals (Recursive)
```python
def preorder(root):
    """Root -> Left -> Right"""
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def inorder(root):
    """Left -> Root -> Right (sorted for BST)"""
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def postorder(root):
    """Left -> Right -> Root"""
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

### BFS (Level Order) - Python Style
```python
from collections import deque

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(current_level)
    
    return result
```

## 🔥 Must-Know Problems (Python)

### Maximum Depth (Pythonic)
```python
def max_depth(root):
    # Method 1: Recursive (clean)
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
    
    # Method 2: BFS iterative
    if not root:
        return 0
    
    from collections import deque
    queue = deque([(root, 1)])
    max_depth = 0
    
    while queue:
        node, depth = queue.popleft()
        max_depth = max(max_depth, depth)
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return max_depth
```
```

### Array/Two-Pointer Pattern (Python Version)
```python
# Array & Two-Pointer Pattern - Python Interview Guide

## 📋 Core Templates

### Two-Pointer (Opposite Direction)
```python
def two_sum_sorted(numbers, target):
    """Two pointers on sorted array"""
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []
```

### Two-Pointer (Same Direction)
```python
def remove_duplicates(nums):
    """Remove duplicates in-place"""
    if not nums:
        return 0
    
    write_pos = 0
    for read_pos in range(1, len(nums)):
        if nums[read_pos] != nums[write_pos]:
            write_pos += 1
            nums[write_pos] = nums[read_pos]
    
    return write_pos + 1
```

### Sliding Window
```python
def longest_substring_without_repeating(s):
    """Sliding window with set"""
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Shrink window while duplicate exists
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

## 🔥 Must-Know Problems (Python)

### Valid Palindrome (Pythonic)
```python
def is_palindrome(s):
    # Method 1: Two pointers (space efficient)
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

    # Method 2: Pythonic (but uses O(n) space)
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
```

### Container With Most Water
```python
def max_area(height):
    """Two pointers for optimization"""
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate area
        width = right - left
        current_height = min(height[left], height[right])
        area = width * current_height
        max_water = max(max_water, area)
        
        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water
```
```

## 🐍 Python-Specific Advantages

### Why Python for Interviews?
- **Readable code** - Focus on algorithms, not syntax
- **Rich standard library** - collections, itertools, heapq
- **List comprehensions** - Concise data transformations
- **Dynamic typing** - Faster prototyping
- **Popular at many companies** - Google, Netflix, Instagram

### Python Interview Edge
- **Rapid development** - More time for optimization discussion
- **Clean syntax** - Easier to explain logic
- **Built-in functions** - sum(), max(), sorted() save time
- **Pythonic patterns** - Shows language mastery

## 🛠️ Key Implementation Differences

| Feature | C++ | Python |
|---------|-----|--------|
| **Hash Table** | `unordered_map<int,int>` | `dict` or `Counter` |
| **Set** | `unordered_set<int>` | `set()` |
| **Queue** | `queue<TreeNode*>` | `collections.deque` |
| **Priority Queue** | `priority_queue<int>` | `heapq` module |
| **2D Array** | `vector<vector<int>>` | `list[list[int]]` |
| **Sort** | `sort(nums.begin(), nums.end())` | `sorted(nums)` or `nums.sort()` |

## 📚 Python Stdlib for Interviews

### Essential Modules
```python
from collections import Counter, defaultdict, deque
import heapq
import bisect
from itertools import combinations, permutations
```

### When to Use Each
- **Counter**: Frequency counting
- **defaultdict**: Grouping, graph adjacency lists
- **deque**: BFS, sliding window optimization
- **heapq**: Priority queues, top K problems
- **bisect**: Binary search on sorted arrays

## 🚀 Quick Implementation Guide

### Step 1: Clone Structure
```bash
mkdir HunterCS-Interview-Prep-Python
cd HunterCS-Interview-Prep-Python
# Copy directory structure from template above
```

### Step 2: Convert C++ Examples
- Translate all `.cpp` files to `.py`
- Replace STL containers with Python equivalents
- Use Pythonic idioms and list comprehensions
- Add type hints for clarity

### Step 3: Python-Specific Content
- Create Python stdlib guides
- Add Pythonic solution variations
- Include performance comparison notes
- Build Python-specific templates

### Step 4: Testing & Validation
- Create test runner script
- Add performance profiling tools
- Validate all examples work correctly
- Cross-reference with C++ versions for consistency

---

**🎯 Result**: A complete Python sister repository with the same systematic approach but optimized for Python's strengths and interview expectations! 