# C++ STL for Technical Interviews

## 🎯 Interview-Critical STL Knowledge

The C++ Standard Template Library (STL) is **essential** for technical interviews. Mastering these containers and algorithms gives you a significant advantage.

## 📋 Must-Know Containers

### Hash Tables (Most Important)
```cpp
#include <unordered_map>
#include <unordered_set>

// Frequency counting - O(1) operations
unordered_map<int, int> freq;
unordered_set<int> seen;

// Key interview advantage: O(1) vs O(log n)
```

### Vectors & Arrays
```cpp
#include <vector>
#include <array>

// Dynamic sizing, range-based loops
vector<int> nums = {1, 2, 3};
for (auto& num : nums) { /* process */ }

// Modern C++ initialization
vector<vector<int>> matrix(m, vector<int>(n, 0));
```

### Queues & Stacks
```cpp
#include <queue>
#include <stack>

// BFS traversals
queue<TreeNode*> q;

// DFS iterative
stack<TreeNode*> stk;

// Priority queue for heaps
priority_queue<int> maxHeap;
priority_queue<int, vector<int>, greater<int>> minHeap;
```

### Ordered Containers
```cpp
#include <set>
#include <map>

// When you need sorted order
set<int> ordered;
map<int, string> keyValue;

// Interview tip: Use when problem mentions "sorted" or "range"
```

## ⚡ Essential Algorithms

### Sorting & Searching
```cpp
#include <algorithm>

// Sort any container
sort(nums.begin(), nums.end());
sort(nums.begin(), nums.end(), greater<int>()); // descending

// Binary search variations
bool found = binary_search(nums.begin(), nums.end(), target);
auto it = lower_bound(nums.begin(), nums.end(), target);
auto it2 = upper_bound(nums.begin(), nums.end(), target);
```

### Transformations
```cpp
// Modern C++ functional style
transform(nums.begin(), nums.end(), nums.begin(), 
          [](int x) { return x * 2; });

// Accumulate for reductions
int sum = accumulate(nums.begin(), nums.end(), 0);
int product = accumulate(nums.begin(), nums.end(), 1, multiplies<int>());
```

### Finding & Counting
```cpp
// Find elements
auto it = find(nums.begin(), nums.end(), target);
auto it2 = find_if(nums.begin(), nums.end(), 
                   [](int x) { return x > 5; });

// Count elements
int count = count(nums.begin(), nums.end(), target);
int countIf = count_if(nums.begin(), nums.end(), 
                       [](int x) { return x % 2 == 0; });
```

## 🔥 Interview Power Moves

### 1. Range-Based Loops (Modern C++)
```cpp
// Old style - avoid in interviews
for (int i = 0; i < nums.size(); i++) {
    cout << nums[i] << " ";
}

// Modern style - shows C++ knowledge
for (const auto& num : nums) {
    cout << num << " ";
}
```

### 2. Auto Keyword
```cpp
// Shows modern C++ understanding
auto freq = unordered_map<string, int>{};
auto it = nums.begin();
auto result = find_if(nums.begin(), nums.end(), predicate);
```

### 3. Lambda Functions
```cpp
// Inline predicates
sort(words.begin(), words.end(), 
     [](const string& a, const string& b) {
         return a.length() < b.length();
     });
```

### 4. Emplace vs Insert
```cpp
// Shows performance awareness
map<int, string> m;
m.emplace(1, "hello");  // Constructs in place
// vs m.insert({1, "hello"});  // Creates temporary
```

## 🎯 Interview Strategy

### When to Mention STL
- **Always** explain your container choice
- **Highlight** time complexity benefits
- **Show** modern C++ knowledge

### Example Interview Dialogue
```
Interviewer: "How would you count word frequencies?"

You: "I'd use std::unordered_map for O(1) average insertions and lookups.
For each word, I'd increment map[word]++. The unordered_map automatically
handles hash collisions and gives us the frequency counting we need."
```

### Common Interview Containers by Pattern

| Pattern | Primary Container | Alternative |
|---------|------------------|-------------|
| **Hash Table** | `unordered_map/set` | `map/set` (if ordered) |
| **Tree Traversal** | `queue` (BFS), `stack` (DFS) | Recursion |
| **Two Pointer** | `vector` | `array` (fixed size) |
| **Dynamic Programming** | `vector<vector<int>>` | 1D `vector` |
| **Graph Algorithms** | `vector<vector<int>>` | Adjacency list |

## 💡 Pro Tips

### 1. Include Headers Correctly
```cpp
// Specific includes show expertise
#include <unordered_map>  // not <map>
#include <algorithm>      // for sort, find
#include <numeric>        // for accumulate
```

### 2. Handle Edge Cases
```cpp
// Check before accessing
if (map.find(key) != map.end()) {
    // Key exists
}

// Or use count() for bool check
if (map.count(key)) {
    // Key exists
}
```

### 3. Memory Efficiency
```cpp
// Reserve space when size is known
vector<int> nums;
nums.reserve(1000);  // Prevents reallocations

// Use const references to avoid copies
for (const auto& item : container) { /* ... */ }
```

## 📚 File References
- **unordered_map.md** - Complete hash table guide
- **unordered_set.md** - Set operations and usage
- **std::hash.md** - Custom hash functions

---

**🎯 Interview Success**: Master these 5 containers (unordered_map, vector, queue, stack, priority_queue) and you'll handle 90% of technical interviews!
