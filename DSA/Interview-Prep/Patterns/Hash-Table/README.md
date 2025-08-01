# Hash Table Pattern - Interview Guide

## 🎯 Pattern Recognition
**Use hash tables when you need:**
- Fast lookups (O(1) average)
- Counting frequency of elements
- Finding pairs/complements
- Removing duplicates
- Grouping related data

## 📋 Core Template
```cpp
#include <unordered_map>
#include <unordered_set>

// Basic frequency counting
unordered_map<int, int> freq;
for (int num : nums) {
    freq[num]++;
}

// Two-pointer complement pattern
unordered_set<int> seen;
for (int num : nums) {
    if (seen.count(target - num)) {
        // Found pair: num and target-num
    }
    seen.insert(num);
}
```

## 🔥 Must-Know Problems

### 1. Two Sum (Easy) ⭐⭐⭐
```cpp
// Hash table approach - O(n) time, O(n) space
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> map;
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (map.count(complement)) {
            return {map[complement], i};
        }
        map[nums[i]] = i;
    }
    return {};
}
```

### 2. Valid Anagram (Easy) ⭐⭐
```cpp
bool isAnagram(string s, string t) {
    if (s.length() != t.length()) return false;
    
    unordered_map<char, int> count;
    for (char c : s) count[c]++;
    for (char c : t) count[c]--;
    
    for (auto& p : count) {
        if (p.second != 0) return false;
    }
    return true;
}
```

### 3. Contains Duplicate II (Medium) ⭐⭐
```cpp
bool containsNearbyDuplicate(vector<int>& nums, int k) {
    unordered_map<int, int> map;
    for (int i = 0; i < nums.size(); i++) {
        if (map.count(nums[i]) && i - map[nums[i]] <= k) {
            return true;
        }
        map[nums[i]] = i;
    }
    return false;
}
```

## 💡 Key Patterns

### Pattern 1: Complement Search
**Problem**: Find pairs that sum to target
**Template**: Store seen elements, check if complement exists

### Pattern 2: Frequency Counting  
**Problem**: Count occurrences of elements
**Template**: `unordered_map<element, count>`

### Pattern 3: Sliding Window with Hash
**Problem**: Find subarray/substring with constraints
**Template**: Use hash to track window contents

### Pattern 4: Grouping/Bucketing
**Problem**: Group elements by some property
**Template**: `unordered_map<property, vector<elements>>`

## ⚡ Interview Tips

### Time Complexity
- **Insert/Delete/Search**: O(1) average, O(n) worst case
- **Space**: O(n) for n elements

### When to Use
✅ Need fast lookups  
✅ Counting/frequency problems  
✅ Finding complements/pairs  
✅ Removing duplicates  

### When NOT to Use
❌ Need ordered traversal  
❌ Range queries  
❌ Memory is very limited  

### Common Mistakes
- Forgetting to check if key exists before accessing
- Using wrong hash container (map vs unordered_map)
- Not handling duplicate keys properly

## 🎪 Practice Progression

### Week 1: Master These
1. Two Sum ⭐⭐⭐
2. Valid Anagram ⭐⭐
3. Contains Duplicate ⭐

### Week 2: Add These  
1. Contains Duplicate II ⭐⭐
2. Group Anagrams ⭐⭐
3. Top K Frequent Elements ⭐⭐

### Week 3: Challenge
1. Longest Substring Without Repeating ⭐⭐⭐
2. 4Sum ⭐⭐⭐
3. Substring with Concatenation ⭐⭐⭐

## 📚 Related Files
- **Code Examples**: `../../../Code-Library/By-Topic/Hashing/`
- **STL Reference**: `../STL/std::unordered_map.md`
- **Quick Reference**: `../../../Quick-Reference/` 