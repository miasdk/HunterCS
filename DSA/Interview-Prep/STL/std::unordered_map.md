# std::unordered_map Complete Reference
*Essential C++ Hash Table Container for Technical Interviews*

## 📋 Quick Reference

### **Time Complexities**
| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| `insert()` | O(1) | O(n) |
| `find()` | O(1) | O(n) |
| `erase()` | O(1) | O(n) |
| `operator[]` | O(1) | O(n) |
| `count()` | O(1) | O(n) |

### **Essential Methods**
```cpp
#include <unordered_map>

std::unordered_map<int, int> map;

// Insertion
map[key] = value;           // Insert or update
map.insert({key, value});   // Insert if key doesn't exist
map.emplace(key, value);    // Construct in-place

// Lookup
auto it = map.find(key);    // Returns iterator (preferred)
int val = map[key];         // Direct access (creates if missing!)
bool exists = map.count(key); // Check existence (returns 0 or 1)

// Deletion  
map.erase(key);            // Remove by key
map.erase(it);             // Remove by iterator
```

---

## 🎯 **Core Interview Patterns**

### **Pattern 1: Two Sum / Complement Search**
**Problem**: Find two numbers that add up to target
```cpp
std::vector<int> twoSum(std::vector<int>& nums, int target) {
    std::unordered_map<int, int> seen; // value -> index
    
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        
        // Check if complement exists
        if (seen.find(complement) != seen.end()) {
            return {seen[complement], i};
        }
        
        // Store current number
        seen[nums[i]] = i;
    }
    return {};
}
```

**Key Insights**:
- Use map to store "what we've seen so far"
- Look for complement instead of brute force checking
- **Always use `find()` for existence checks** (safer than `operator[]`)

### **Pattern 2: Frequency Counting**
**Problem**: Count occurrences of elements
```cpp
std::unordered_map<char, int> charFrequency(const std::string& s) {
    std::unordered_map<char, int> freq;
    
    for (char c : s) {
        freq[c]++;  // Creates entry with 0 if doesn't exist, then increments
    }
    return freq;
}

// Alternative: More explicit
for (char c : s) {
    if (freq.find(c) != freq.end()) {
        freq[c]++;
    } else {
        freq[c] = 1;
    }
}
```

### **Pattern 3: Seen Before / Duplicate Detection**
**Problem**: Check if we've encountered something before
```cpp
bool hasDuplicate(const std::vector<int>& nums) {
    std::unordered_set<int> seen;  // Often use unordered_set for this pattern
    
    for (int num : nums) {
        if (seen.count(num)) {
            return true;
        }
        seen.insert(num);
    }
    return false;
}
```

### **Pattern 4: Lookup Table / Memoization**
**Problem**: Cache expensive computations
```cpp
std::unordered_map<int, int> memo;

int fibonacci(int n) {
    if (n <= 1) return n;
    
    // Check if already computed
    if (memo.find(n) != memo.end()) {
        return memo[n];
    }
    
    // Compute and store
    memo[n] = fibonacci(n-1) + fibonacci(n-2);
    return memo[n];
}
```

---

## ⚠️ **Critical Interview Gotchas**

### **1. `operator[]` vs `find()` vs `at()`**
```cpp
std::unordered_map<std::string, int> map;

// DANGER: Creates entry if key doesn't exist!
if (map["nonexistent"] == 0) { /* This created an entry! */ }

// SAFE: Check existence first
if (map.find("key") != map.end()) {
    int value = map["key"];  // Now safe to use operator[]
}

// ALTERNATIVE: Use at() for bounds checking
try {
    int value = map.at("key");  // Throws exception if key doesn't exist
} catch (const std::out_of_range&) {
    // Handle missing key
}
```

### **2. Iterator Invalidation**
```cpp
// DANGER: Don't modify map while iterating
for (auto it = map.begin(); it != map.end(); ++it) {
    if (some_condition) {
        map.erase(it);  // This invalidates the iterator!
        // ++it will now crash
    }
}

// SAFE: Use erase's return value
for (auto it = map.begin(); it != map.end(); ) {
    if (some_condition) {
        it = map.erase(it);  // erase returns next valid iterator
    } else {
        ++it;
    }
}
```

### **3. Custom Key Types**
```cpp
// For custom types, need hash function and equality operator
struct Point {
    int x, y;
    bool operator==(const Point& other) const {
        return x == other.x && y == other.y;
    }
};

// Custom hash function
struct PointHash {
    std::size_t operator()(const Point& p) const {
        return std::hash<int>()(p.x) ^ (std::hash<int>()(p.y) << 1);
    }
};

std::unordered_map<Point, int, PointHash> pointMap;
```

---

## 🚀 **Advanced Techniques**

### **1. Emplace vs Insert**
```cpp
// Construct object in-place (more efficient)
map.emplace(key, value);

// For complex objects
map.emplace(std::piecewise_construct,
           std::forward_as_tuple(key),
           std::forward_as_tuple(constructor_args...));
```

### **2. Reserve for Performance**
```cpp
// If you know approximate size, reserve space
map.reserve(expected_size);  // Reduces rehashing
```

### **3. Load Factor Management**
```cpp
// Monitor performance
std::cout << "Load factor: " << map.load_factor() << std::endl;
std::cout << "Max load factor: " << map.max_load_factor() << std::endl;

// Adjust if needed
map.max_load_factor(0.5);  // Lower = faster lookups, more memory
```

---

## 📝 **Common Interview Questions**

### **Question**: "When would you use `unordered_map` vs `map`?"

**Answer**: 
- **`unordered_map`**: When you need **O(1) average** lookup/insertion and don't care about key ordering
- **`map`**: When you need **guaranteed O(log n)** operations or **sorted key iteration**

### **Question**: "What happens if hash function has many collisions?"

**Answer**:
- Performance degrades to **O(n)** for all operations
- Hash table becomes essentially a linked list
- Can be mitigated with better hash function or lower load factor

### **Question**: "How do you handle thread safety?"

**Answer**:
- `unordered_map` is **not thread-safe** by default
- Multiple readers OK, but any writer needs synchronization
- Use `std::shared_mutex` for reader-writer scenarios

---

## 🔗 **Related Topics in This Repository**

- **Hash Functions**: `335/STL/std::hash.md`
- **Sets**: `335/STL/std::unordered_set.md` 
- **Complexity Analysis**: `335/Reference/Big-O-Improved.md`
- **Hash Table Theory**: `335/Reference/Hashing.md`
- **Implementation Examples**: `335/Exam02/code/two_sum.cpp`

---

## ✅ **Practice Checklist**

- [ ] Implement Two Sum from memory using unordered_map
- [ ] Build frequency counter for string anagram detection
- [ ] Create lookup table for dynamic programming problem
- [ ] Handle edge cases (empty input, single element, duplicates)
- [ ] Optimize hash function for custom key type
- [ ] Explain time complexity trade-offs in interview setting
