# C++ STL Mastery for Technical Interviews

> **Master the containers and algorithms that power 90% of interview solutions**
> 
> *Strategic STL knowledge to solve problems faster and impress interviewers*

## 🎯 Why STL Dominates Interviews

### **The Interview Advantage**
- **Speed**: Write solutions 3x faster than implementing from scratch
- **Correctness**: Battle-tested implementations, fewer bugs
- **Impression**: Shows professional C++ knowledge
- **Performance**: Optimized implementations, better complexity

### **Real Interview Impact**
```cpp
// Naive approach (5+ minutes to implement)
class HashTable {
    // ... 50+ lines of hash table implementation
};

// STL approach (30 seconds)
std::unordered_map<int, int> freq;
```

---

## 🚀 The Big 5 (Interview Essential)

### **1. std::unordered_map - Hash Tables**
**When to use:** Frequency counting, caching, lookups
**Interview power:** O(1) operations

```cpp
#include <unordered_map>

// Frequency counting pattern
std::unordered_map<char, int> freq;
for (char c : str) freq[c]++;

// Two Sum pattern
std::unordered_map<int, int> seen;
for (int i = 0; i < nums.size(); i++) {
    int complement = target - nums[i];
    if (seen.find(complement) != seen.end()) {
        return {seen[complement], i};
    }
    seen[nums[i]] = i;
}

// Common operations
freq[key]++;                    // Insert/increment
auto it = freq.find(key);       // O(1) lookup
if (freq.count(key)) { ... }    // Check existence
freq.erase(key);                // Remove
```

### **2. std::vector - Dynamic Arrays**
**When to use:** Most problems, dynamic sizing, random access
**Interview power:** Versatile, efficient

```cpp
#include <vector>

// Initialization patterns
std::vector<int> nums = {1, 2, 3};
std::vector<int> dp(n, 0);              // n elements, all 0
std::vector<std::vector<int>> matrix(m, std::vector<int>(n, 0));

// Essential operations
nums.push_back(x);              // O(1) amortized
nums.pop_back();                // O(1)
nums.insert(nums.begin(), x);   // O(n) - insert at beginning
nums.erase(nums.begin());       // O(n) - remove first
int size = nums.size();         // O(1)
bool empty = nums.empty();      // O(1)

// Modern iteration
for (const auto& num : nums) { /* process */ }
for (auto& num : nums) { num *= 2; }    // modify elements
```

### **3. std::queue - BFS and FIFO**
**When to use:** Level-order traversal, BFS, scheduling
**Interview power:** Clean BFS implementation

```cpp
#include <queue>

// BFS pattern
std::queue<TreeNode*> q;
q.push(root);
while (!q.empty()) {
    int level_size = q.size();
    for (int i = 0; i < level_size; i++) {
        TreeNode* node = q.front();
        q.pop();
        
        // Process node
        if (node->left) q.push(node->left);
        if (node->right) q.push(node->right);
    }
}

// FIFO operations
q.push(item);           // Add to back
auto front = q.front(); // Access front
q.pop();                // Remove front
bool empty = q.empty(); // Check if empty
```

### **4. std::stack - DFS and LIFO**
**When to use:** DFS traversal, parentheses matching, undo operations
**Interview power:** Iterative DFS, expression evaluation

```cpp
#include <stack>

// DFS pattern
std::stack<TreeNode*> stk;
stk.push(root);
while (!stk.empty()) {
    TreeNode* node = stk.top();
    stk.pop();
    
    // Process node
    if (node->right) stk.push(node->right);  // Right first
    if (node->left) stk.push(node->left);    // Left second
}

// Parentheses matching
std::stack<char> brackets;
for (char c : s) {
    if (c == '(' || c == '[' || c == '{') {
        brackets.push(c);
    } else {
        if (brackets.empty()) return false;
        char top = brackets.top();
        brackets.pop();
        if (!isMatching(top, c)) return false;
    }
}
```

### **5. std::priority_queue - Heaps**
**When to use:** Top K problems, Dijkstra, merge K lists
**Interview power:** O(log n) insert/delete, O(1) access to min/max

```cpp
#include <queue>

// Max heap (default)
std::priority_queue<int> maxHeap;
maxHeap.push(3);
maxHeap.push(1);
maxHeap.push(4);
int max_val = maxHeap.top();  // 4

// Min heap
std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;

// Custom comparator for pairs
auto cmp = [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
    return a.second > b.second;  // Min heap by second element
};
std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, decltype(cmp)> pq(cmp);

// Top K pattern
std::priority_queue<int> heap;
for (int num : nums) {
    heap.push(num);
    if (heap.size() > k) heap.pop();
}
```

---

## 🎯 The Supporting Cast (Interview Helpers)

### **std::set/map - When Order Matters**
**When to use:** Sorted data, range queries, balanced search

```cpp
#include <set>
#include <map>

// Maintain sorted unique elements
std::set<int> sorted_set;
sorted_set.insert(3);  // O(log n)
sorted_set.insert(1);
sorted_set.insert(4);
// Set contents: {1, 3, 4}

// Range operations
auto it = sorted_set.lower_bound(2);  // First >= 2
auto it2 = sorted_set.upper_bound(3); // First > 3

// Map for sorted key-value pairs
std::map<std::string, int> ordered_map;
ordered_map["apple"] = 5;
ordered_map["banana"] = 3;
// Iteration gives keys in alphabetical order
```

### **std::deque - Double-Ended Queue**
**When to use:** Sliding window, both ends access

```cpp
#include <deque>

// Sliding window maximum
std::deque<int> dq;  // Store indices
for (int i = 0; i < nums.size(); i++) {
    // Remove elements outside window
    while (!dq.empty() && dq.front() <= i - k) {
        dq.pop_front();
    }
    
    // Remove smaller elements
    while (!dq.empty() && nums[dq.back()] <= nums[i]) {
        dq.pop_back();
    }
    
    dq.push_back(i);
    if (i >= k - 1) {
        result.push_back(nums[dq.front()]);
    }
}
```

---

## ⚡ Essential STL Algorithms

### **Sorting and Searching**
```cpp
#include <algorithm>

// Sorting
std::sort(nums.begin(), nums.end());                    // O(n log n)
std::sort(nums.begin(), nums.end(), std::greater<int>()); // Descending

// Custom comparator
std::sort(words.begin(), words.end(), [](const std::string& a, const std::string& b) {
    return a.length() < b.length();
});

// Binary search (requires sorted array)
bool found = std::binary_search(nums.begin(), nums.end(), target);
auto it = std::lower_bound(nums.begin(), nums.end(), target);  // First >= target
auto it2 = std::upper_bound(nums.begin(), nums.end(), target); // First > target

// Finding elements
auto it = std::find(nums.begin(), nums.end(), target);
auto it2 = std::find_if(nums.begin(), nums.end(), [](int x) { return x > 5; });
```

### **Transformations and Aggregations**
```cpp
// Counting
int count = std::count(nums.begin(), nums.end(), target);
int count_if = std::count_if(nums.begin(), nums.end(), [](int x) { return x % 2 == 0; });

// Min/Max
auto min_it = std::min_element(nums.begin(), nums.end());
auto max_it = std::max_element(nums.begin(), nums.end());
int min_val = std::min({a, b, c});  // Min of multiple values

// Accumulate
int sum = std::accumulate(nums.begin(), nums.end(), 0);
int product = std::accumulate(nums.begin(), nums.end(), 1, std::multiplies<int>());

// Transform
std::transform(nums.begin(), nums.end(), nums.begin(), [](int x) { return x * 2; });
```

### **Useful Utilities**
```cpp
// Reverse
std::reverse(nums.begin(), nums.end());

// Rotate
std::rotate(nums.begin(), nums.begin() + k, nums.end());  // Rotate by k positions

// Unique (requires sorted array)
std::sort(nums.begin(), nums.end());
auto end = std::unique(nums.begin(), nums.end());
nums.erase(end, nums.end());

// Partition
auto it = std::partition(nums.begin(), nums.end(), [](int x) { return x % 2 == 0; });
// Even numbers before it, odd numbers after
```

---

## 🎯 Interview Pattern Recognition

### **Pattern: Frequency Counting**
```cpp
// Character frequency
std::unordered_map<char, int> freq;
for (char c : s) freq[c]++;

// Most frequent element
int max_freq = 0;
char most_frequent;
for (const auto& [ch, count] : freq) {
    if (count > max_freq) {
        max_freq = count;
        most_frequent = ch;
    }
}
```

### **Pattern: Sliding Window**
```cpp
// Fixed window
std::unordered_map<char, int> window;
for (int i = 0; i < s.length(); i++) {
    window[s[i]]++;
    
    if (i >= k - 1) {  // Window size reached
        // Process window
        
        // Shrink window
        window[s[i - k + 1]]--;
        if (window[s[i - k + 1]] == 0) {
            window.erase(s[i - k + 1]);
        }
    }
}
```

### **Pattern: Two Pointers**
```cpp
// Two sum on sorted array
int left = 0, right = nums.size() - 1;
while (left < right) {
    int sum = nums[left] + nums[right];
    if (sum == target) return {left, right};
    else if (sum < target) left++;
    else right--;
}
```

### **Pattern: Merge K Sorted Lists**
```cpp
auto cmp = [](ListNode* a, ListNode* b) { return a->val > b->val; };
std::priority_queue<ListNode*, std::vector<ListNode*>, decltype(cmp)> pq(cmp);

// Add all list heads
for (ListNode* list : lists) {
    if (list) pq.push(list);
}

// Merge process
while (!pq.empty()) {
    ListNode* node = pq.top();
    pq.pop();
    
    // Add to result
    if (node->next) pq.push(node->next);
}
```

---

## 💡 Pro Interview Tips

### **1. Always Explain Your Container Choice**
```
❌ "I'll use a map"
✅ "I'll use an unordered_map for O(1) average lookups, which is better than 
   map's O(log n) since we don't need sorted order"
```

### **2. Mention Time Complexity Benefits**
```cpp
// Always mention the advantage
std::unordered_set<int> seen;  // "This gives us O(1) lookups instead of O(n)"
```

### **3. Use Modern C++ Features**
```cpp
// Shows C++11+ knowledge
for (const auto& [key, value] : map) { /* structured binding */ }
auto result = std::make_pair(i, j);
```

### **4. Know When NOT to Use STL**
- **Custom requirements**: Need specific behavior
- **Performance critical**: Custom optimization needed
- **Educational**: Interviewer wants you to implement data structure

---

## 📊 Complexity Quick Reference

| Container | Access | Insert | Delete | Search | Space |
|-----------|--------|--------|--------|--------|-------|
| **vector** | O(1) | O(n) | O(n) | O(n) | O(n) |
| **unordered_map** | O(1)* | O(1)* | O(1)* | O(1)* | O(n) |
| **map** | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| **priority_queue** | O(1) | O(log n) | O(log n) | O(n) | O(n) |
| **set** | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |

*Average case for hash-based containers

| Algorithm | Time Complexity | Space | Notes |
|-----------|----------------|-------|-------|
| **sort** | O(n log n) | O(log n) | Introsort (quicksort + heapsort) |
| **binary_search** | O(log n) | O(1) | Requires sorted input |
| **find** | O(n) | O(1) | Linear search |
| **lower_bound** | O(log n) | O(1) | Requires sorted input |

---

## 🎯 Practice Strategy

### **Week 1: Master the Big 5**
- Solve 20 problems using only unordered_map, vector, queue, stack, priority_queue
- Focus on basic operations and patterns

### **Week 2: Algorithm Integration**
- Combine containers with STL algorithms
- Practice sort + binary_search combinations

### **Week 3: Advanced Patterns**
- Custom comparators and lambda functions
- Complex data structures (map of vectors, etc.)

### **Week 4: Speed and Polish**
- Timed problem solving
- Interview communication practice

---

**🎯 Next Step**: Practice with `../Patterns/Hash-Table/README.md` to master your first interview pattern!

---

*Master these containers and you'll solve 90% of interview problems with confidence!* 