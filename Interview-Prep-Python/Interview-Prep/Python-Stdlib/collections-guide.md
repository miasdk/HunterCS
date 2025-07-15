# Python Collections Module - Interview Guide

## 🎯 Why Collections Matter in Interviews

The `collections` module provides **interview superpowers**:
- **Cleaner code** - Less boilerplate, more algorithm focus
- **Optimal performance** - Specialized data structures for common patterns
- **Pythonic solutions** - Shows language mastery to interviewers

## 📋 Core Collection Types

### Counter - Frequency Analysis Powerhouse

#### Basic Usage
```python
from collections import Counter

# Create from iterable
counter = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
# Counter({'a': 3, 'b': 2, 'c': 1})

# Create from dictionary
counter = Counter({'a': 3, 'b': 2})

# Create from keyword arguments
counter = Counter(a=3, b=2, c=1)
```

#### Interview-Critical Methods
```python
# Most common elements
counter.most_common()          # [('a', 3), ('b', 2), ('c', 1)]
counter.most_common(2)         # [('a', 3), ('b', 2)]

# Access counts (returns 0 for missing keys)
counter['a']                   # 3
counter['z']                   # 0 (not KeyError!)

# Update counts
counter.update(['a', 'b'])     # Add more items
counter.subtract(['a'])        # Subtract counts

# Arithmetic operations
c1 + c2                        # Add counts
c1 - c2                        # Subtract (keep positive only)
c1 & c2                        # Intersection (minimum counts)
c1 | c2                        # Union (maximum counts)
```

#### Interview Problems Perfect for Counter
```python
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """LeetCode 347 - Counter makes this trivial"""
    counter = Counter(nums)
    return [num for num, count in counter.most_common(k)]

def is_anagram(s: str, t: str) -> bool:
    """LeetCode 242 - One-liner with Counter"""
    return Counter(s) == Counter(t)

def first_unique_char(s: str) -> int:
    """LeetCode 387 - Find first non-repeating character"""
    counter = Counter(s)
    for i, char in enumerate(s):
        if counter[char] == 1:
            return i
    return -1
```

### defaultdict - Auto-initialization Magic

#### Basic Usage
```python
from collections import defaultdict

# Integer default (for counting)
count = defaultdict(int)
for item in items:
    count[item] += 1  # No KeyError, starts at 0

# List default (for grouping)
groups = defaultdict(list)
for item in items:
    key = compute_key(item)
    groups[key].append(item)  # No KeyError, starts with []

# Set default (for unique collections)
adjacency = defaultdict(set)
for edge in edges:
    adjacency[edge[0]].add(edge[1])
```

#### Interview Powerhouse Patterns
```python
def group_anagrams(strs: list[str]) -> list[list[str]]:
    """LeetCode 49 - Perfect defaultdict use case"""
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))  # Anagram signature
        groups[key].append(s)
    return list(groups.values())

def build_graph(edges: list[list[int]]) -> dict[int, list[int]]:
    """Graph construction with defaultdict"""
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # Undirected graph
    return graph

def word_pattern(pattern: str, s: str) -> bool:
    """LeetCode 290 - Bidirectional mapping"""
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    char_to_word = defaultdict(str)
    word_to_char = defaultdict(str)
    
    for char, word in zip(pattern, words):
        if char_to_word[char] and char_to_word[char] != word:
            return False
        if word_to_char[word] and word_to_char[word] != char:
            return False
        char_to_word[char] = word
        word_to_char[word] = char
    
    return True
```

### deque - Double-Ended Queue Efficiency

#### Basic Operations (All O(1))
```python
from collections import deque

# Creation
dq = deque([1, 2, 3])
dq = deque(maxlen=3)  # Fixed-size circular buffer

# Adding elements
dq.append(4)           # Add to right
dq.appendleft(0)       # Add to left

# Removing elements  
dq.pop()               # Remove from right
dq.popleft()           # Remove from left

# Other operations
dq.extend([5, 6])      # Extend right
dq.extendleft([7, 8])  # Extend left (reversed order)
dq.rotate(1)           # Rotate right
dq.rotate(-1)          # Rotate left
```

#### Interview Patterns with deque

##### 1. BFS Tree/Graph Traversal
```python
def level_order(root: TreeNode) -> list[list[int]]:
    """BFS with deque - classic pattern"""
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

##### 2. Sliding Window Maximum
```python
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """LeetCode 239 - Monotonic deque"""
    dq = deque()  # Store indices
    result = []
    
    for i, num in enumerate(nums):
        # Remove indices outside window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove smaller elements (maintain decreasing order)
        while dq and nums[dq[-1]] <= num:
            dq.pop()
        
        dq.append(i)
        
        # Add to result when window is full
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result
```

##### 3. Palindrome Checking
```python
def is_palindrome_deque(s: str) -> bool:
    """Alternative palindrome check using deque"""
    chars = deque(c.lower() for c in s if c.isalnum())
    
    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return False
    
    return True
```

### OrderedDict - Insertion Order Preservation

#### When to Use
```python
from collections import OrderedDict

# Before Python 3.7: Use when order matters
# Python 3.7+: Regular dict preserves order, but OrderedDict has extra methods

# LRU Cache implementation
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        if key in self.cache:
            # Move to end (most recently used)
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # Remove least recently used (first item)
            self.cache.popitem(last=False)
        
        self.cache[key] = value
```

### namedtuple - Lightweight Objects

#### Creating Structured Data
```python
from collections import namedtuple

# Define structure
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age email')  # Space-separated also works

# Create instances
p1 = Point(1, 2)
p2 = Point(x=3, y=4)

# Access fields
print(p1.x, p1.y)  # 1 2
print(p1[0], p1[1])  # Also works like tuple

# Interview use case: Clean coordinate handling
def manhattan_distance(p1: Point, p2: Point) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

# Convert from tuple
coords = [(1, 2), (3, 4), (5, 6)]
points = [Point(*coord) for coord in coords]
```

## 🔥 Interview Power Combinations

### Pattern Matching with Multiple Collections
```python
def find_anagram_groups(words: list[str]) -> list[list[str]]:
    """Combine defaultdict + Counter for powerful grouping"""
    groups = defaultdict(list)
    
    for word in words:
        # Use Counter as signature for anagrams
        signature = Counter(word)
        # Convert to frozenset for hashing
        key = frozenset(signature.items())
        groups[key].append(word)
    
    return [group for group in groups.values() if len(group) > 1]

def sliding_window_frequency(s: str, k: int) -> list[dict]:
    """Sliding window with Counter tracking"""
    result = []
    window_counter = Counter()
    
    for i, char in enumerate(s):
        # Add current character
        window_counter[char] += 1
        
        # Remove character outside window
        if i >= k:
            old_char = s[i - k]
            window_counter[old_char] -= 1
            if window_counter[old_char] == 0:
                del window_counter[old_char]
        
        # Record window state
        if i >= k - 1:
            result.append(dict(window_counter))
    
    return result
```

### Memory-Efficient Processing
```python
def process_large_dataset(data_stream):
    """Use deque with maxlen for fixed-size window"""
    window = deque(maxlen=1000)  # Keep only last 1000 items
    stats = Counter()
    
    for item in data_stream:
        # Add to window
        window.append(item)
        stats[item] += 1
        
        # If window is full, we automatically drop oldest
        # But need to update stats manually
        if len(window) == 1000 and item != window[0]:
            # Note: This is simplified - real implementation needs tracking
            pass
        
        # Process current window
        yield analyze_window(window, stats)
```

## 🎯 Interview Tips

### When to Show Collections Knowledge
1. **Counter**: Any frequency/counting problem
2. **defaultdict**: Grouping, graph adjacency lists, building mappings
3. **deque**: BFS, sliding window, palindromes
4. **OrderedDict**: LRU cache, maintaining insertion order pre-Python 3.7
5. **namedtuple**: Clean coordinate/point handling, structured data

### Performance Benefits to Mention
- **deque**: O(1) operations at both ends vs O(n) for list
- **Counter**: Optimized counting vs manual dict management
- **defaultdict**: Eliminates need for `if key in dict` checks

### Code Quality Improvements
```python
# Instead of verbose manual counting
freq = {}
for item in items:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

# Use Counter for clarity
from collections import Counter
freq = Counter(items)
```

---

**🎯 Collections mastery = Cleaner code + Better performance + Pythonic thinking!** 