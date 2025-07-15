# Hash Table Pattern Guide

> **Master the most powerful interview pattern: O(1) lookups**
> 
> *Hash tables solve 40% of interview problems. Learn the patterns that matter.*

## 🎯 Why Hash Tables Dominate Interviews

### **The O(1) Advantage**
- **Speed**: Constant time lookups vs O(n) linear search
- **Flexibility**: Key-value mapping for complex relationships
- **Memory**: Trade space for time - classic interview optimization

### **Interview Reality Check**
```
Without Hash Table: "Let me iterate through the array to find..." → O(n²)
With Hash Table: "I'll store it in a map for instant lookup" → O(n)
```

**Result**: Turn impossible problems into easy solutions!

---

## 🚀 The 5 Core Hash Table Patterns

### **Pattern 1: Frequency Counting**
**When to use:** Count occurrences, find duplicates, character analysis
**Key insight:** Use map[key]++ for elegant counting

```cpp
#include <unordered_map>

// Basic frequency counting
std::unordered_map<char, int> charFreq;
for (char c : str) {
    charFreq[c]++;  // Automatically handles new keys
}

// Find most frequent character
char mostFrequent;
int maxCount = 0;
for (const auto& [ch, count] : charFreq) {
    if (count > maxCount) {
        maxCount = count;
        mostFrequent = ch;
    }
}
```

**LeetCode Examples:**
- Valid Anagram (242)
- First Unique Character (387)
- Majority Element (169)

### **Pattern 2: Complement Search (Two Sum Family)**
**When to use:** Find pairs that sum to target, complement relationships
**Key insight:** Store what you need to find, not what you've seen

```cpp
// Two Sum - Store complement
std::unordered_map<int, int> needed;  // value -> index
for (int i = 0; i < nums.size(); i++) {
    int complement = target - nums[i];
    
    if (needed.find(complement) != needed.end()) {
        return {needed[complement], i};
    }
    
    needed[nums[i]] = i;  // Store current for future complements
}

// Three Sum - Use Two Sum as subroutine
std::sort(nums.begin(), nums.end());
for (int i = 0; i < nums.size() - 2; i++) {
    int target2 = -nums[i];
    // Use two-pointer or hash table for remaining two numbers
}
```

**LeetCode Examples:**
- Two Sum (1)
- Three Sum (15)
- Four Sum (18)

### **Pattern 3: Grouping and Classification**
**When to use:** Group anagrams, classify by properties, partition data
**Key insight:** Use computed key to group related items

```cpp
// Group Anagrams
std::unordered_map<std::string, std::vector<std::string>> groups;
for (const std::string& word : words) {
    std::string key = word;
    std::sort(key.begin(), key.end());  // Sorted word as key
    groups[key].push_back(word);
}

// Group by custom property
std::unordered_map<int, std::vector<int>> lengthGroups;
for (const std::string& word : words) {
    lengthGroups[word.length()].push_back(word);
}
```

**LeetCode Examples:**
- Group Anagrams (49)
- Group Shifted Strings (249)
- Partition Labels (763)

### **Pattern 4: Seen/Visited Tracking**
**When to use:** Detect cycles, track visited nodes, avoid duplicates
**Key insight:** Use set for existence checking, map for additional data

```cpp
// Detect cycle in linked list
std::unordered_set<ListNode*> visited;
ListNode* current = head;
while (current) {
    if (visited.count(current)) {
        return true;  // Cycle detected
    }
    visited.insert(current);
    current = current->next;
}

// Track visited with additional data
std::unordered_map<TreeNode*, int> depths;
void dfs(TreeNode* node, int depth) {
    if (!node || depths.count(node)) return;
    depths[node] = depth;
    dfs(node->left, depth + 1);
    dfs(node->right, depth + 1);
}
```

**LeetCode Examples:**
- Linked List Cycle (141)
- Contains Duplicate (217)
- Happy Number (202)

### **Pattern 5: Prefix/Suffix Mapping**
**When to use:** Subarray problems, prefix sums, running calculations
**Key insight:** Store cumulative results for O(1) range queries

```cpp
// Subarray Sum Equals K
std::unordered_map<int, int> prefixSums;  // sum -> count
prefixSums[0] = 1;  // Important: empty prefix
int currentSum = 0;
int result = 0;

for (int num : nums) {
    currentSum += num;
    int needed = currentSum - k;
    
    if (prefixSums.count(needed)) {
        result += prefixSums[needed];
    }
    
    prefixSums[currentSum]++;
}

// Longest Subarray with Equal 0s and 1s
std::unordered_map<int, int> firstOccurrence;  // balance -> index
firstOccurrence[0] = -1;  // Important: before array starts
int balance = 0;
int maxLength = 0;

for (int i = 0; i < nums.size(); i++) {
    balance += (nums[i] == 1) ? 1 : -1;
    
    if (firstOccurrence.count(balance)) {
        maxLength = std::max(maxLength, i - firstOccurrence[balance]);
    } else {
        firstOccurrence[balance] = i;
    }
}
```

**LeetCode Examples:**
- Subarray Sum Equals K (560)
- Continuous Subarray Sum (523)
- Longest Subarray Equal 0s and 1s (525)

---

## 🎯 Hash Table Container Decision Tree

### **std::unordered_map vs std::unordered_set**
```cpp
// Use unordered_set when you only need existence checking
std::unordered_set<int> seen;
if (seen.count(num)) { /* exists */ }

// Use unordered_map when you need to store additional data
std::unordered_map<int, int> valueToIndex;
std::unordered_map<char, int> charFrequency;
```

### **std::unordered_map vs std::map**
```cpp
// Use unordered_map (hash table) for O(1) operations
std::unordered_map<int, int> fast;  // O(1) average

// Use map (red-black tree) when you need sorted order
std::map<int, int> sorted;  // O(log n) but ordered iteration
for (auto& [key, value] : sorted) { /* keys in sorted order */ }
```

### **Custom Hash Functions**
```cpp
// For pairs
struct PairHash {
    size_t operator()(const std::pair<int, int>& p) const {
        return std::hash<int>{}(p.first) ^ (std::hash<int>{}(p.second) << 1);
    }
};
std::unordered_set<std::pair<int, int>, PairHash> pairSet;

// For strings (custom key)
std::unordered_map<std::string, int> customMap;
// STL automatically uses std::hash<std::string>
```

---

## 🎯 Advanced Hash Table Techniques

### **Technique 1: Rolling Hash**
**When to use:** Substring matching, sliding window with strings

```cpp
class RollingHash {
private:
    static const int BASE = 31;
    static const int MOD = 1e9 + 7;
    
public:
    long long computeHash(const std::string& s) {
        long long hash = 0;
        long long power = 1;
        
        for (char c : s) {
            hash = (hash + (c - 'a' + 1) * power) % MOD;
            power = (power * BASE) % MOD;
        }
        
        return hash;
    }
};

// Use for O(1) substring comparisons in sliding window
```

### **Technique 2: Bloom Filters (Advanced)**
**When to use:** Memory-efficient existence checking, can have false positives

```cpp
// Conceptual - typically use library implementation
class BloomFilter {
private:
    std::vector<bool> bits;
    std::vector<std::function<size_t(const std::string&)>> hashFunctions;
    
public:
    void insert(const std::string& item) {
        for (auto& hash : hashFunctions) {
            bits[hash(item) % bits.size()] = true;
        }
    }
    
    bool mightContain(const std::string& item) {
        for (auto& hash : hashFunctions) {
            if (!bits[hash(item) % bits.size()]) {
                return false;  // Definitely not present
            }
        }
        return true;  // Might be present (could be false positive)
    }
};
```

### **Technique 3: Consistent Hashing**
**When to use:** Distributed systems, load balancing (system design interviews)

---

## 💡 Interview Communication Tips

### **Explaining Hash Table Choice**
```
❌ "I'll use a hash map"
✅ "I'll use an unordered_map to get O(1) average lookups, which reduces 
   the overall complexity from O(n²) to O(n)"
```

### **Handling Edge Cases**
```cpp
// Always check for empty containers
if (map.empty()) return {};

// Handle hash collisions in explanation
"In the worst case, all elements hash to the same bucket, giving O(n) 
operations, but average case is O(1)"

// Consider load factor
"STL unordered_map automatically rehashes when load factor exceeds threshold"
```

### **Space-Time Tradeoffs**
```
"We're trading O(n) extra space for the hash table to achieve O(1) lookups 
instead of O(n) search time. This is generally worth it for better time complexity."
```

---

## 🚨 Common Hash Table Pitfalls

### **1. Iterator Invalidation**
```cpp
// ❌ Dangerous - modifying while iterating
for (auto it = map.begin(); it != map.end(); ++it) {
    if (condition) {
        map.erase(it);  // Invalidates iterator!
    }
}

// ✅ Safe approach
for (auto it = map.begin(); it != map.end();) {
    if (condition) {
        it = map.erase(it);  // Returns valid iterator
    } else {
        ++it;
    }
}
```

### **2. Default Value Assumptions**
```cpp
// ❌ Creates entry even if key doesn't exist
if (map[key] > 0) { /* ... */ }

// ✅ Check existence first
if (map.count(key) && map[key] > 0) { /* ... */ }
// or
auto it = map.find(key);
if (it != map.end() && it->second > 0) { /* ... */ }
```

### **3. Hash Function Performance**
```cpp
// Consider hash function quality for custom types
// Poor hash function → many collisions → O(n) operations
```

---

## 🎯 Practice Progression

### **Week 1: Master Basic Patterns**
**Day 1-2:** Frequency counting problems
- Valid Anagram (242)
- First Unique Character (387)
- Majority Element (169)

**Day 3-4:** Two Sum family
- Two Sum (1)
- Two Sum II - Sorted Array (167)
- Two Sum III - Data Structure Design (170)

**Day 5-7:** Grouping problems
- Group Anagrams (49)
- Find All Anagrams (438)

### **Week 2: Advanced Patterns**
**Day 1-3:** Prefix sum patterns
- Subarray Sum Equals K (560)
- Continuous Subarray Sum (523)

**Day 4-5:** Cycle detection
- Linked List Cycle (141)
- Happy Number (202)

**Day 6-7:** Complex mappings
- LRU Cache (146)
- Design Twitter (355)

---

## 📊 Complexity Analysis Summary

| Pattern | Time | Space | Use Case |
|---------|------|-------|----------|
| **Frequency Counting** | O(n) | O(k) | k = unique elements |
| **Complement Search** | O(n) | O(n) | Pair finding |
| **Grouping** | O(n) | O(n) | Classification |
| **Visited Tracking** | O(n) | O(n) | Cycle detection |
| **Prefix Mapping** | O(n) | O(n) | Subarray problems |

**Key Insight**: Hash tables consistently provide O(n) time solutions to problems that would otherwise be O(n²)

---

## 🎯 Next Steps

1. **Master these 5 patterns** with 20+ problems
2. **Practice explaining** your hash table choice clearly
3. **Move to Tree Traversal** pattern next
4. **Combine patterns** for complex problems

---

**💡 Pro Tip**: When stuck on any array/string problem, ask yourself: "What if I could look up any value in O(1) time?"

---

**🎯 Ready to practice?** Check out `../../../Code-Library/By-Topic/Hashing/` for complete implementations! 