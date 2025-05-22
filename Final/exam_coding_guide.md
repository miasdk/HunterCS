# Exam Coding Questions - Complete Implementation Guide

## 1. Hash Map Best Scores (High Priority - From Exam 2)

### Problem Pattern
Track best (lowest) score for each person from a list of score pairs.

### Template Solution
```cpp
void printBestScores(std::vector<std::pair<std::string, int>> scores) {
    std::unordered_map<std::string, int> best;
    
    for (auto x : scores) {
        // KEY: Check if element already exists
        if (best.find(x.first) == best.end()) {
            best[x.first] = x.second;  // First time seeing this person
        } else if (x.second < best[x.first]) {
            best[x.first] = x.second;  // Update if better score
        }
    }
    
    // Print results
    for (auto x : best) {
        std::cout << x.first << " " << x.second << std::endl;
    }
}
```

### Key Points:
- **MUST check if element exists** before comparing (biggest mistake)
- Use `.find() == .end()` or `.count()` to check existence
- Only update if new score is better than existing

### Alternative Approaches:
```cpp
// Using .count()
if (best.count(x.first)) {
    if (x.second < best[x.first])
        best[x.first] = x.second;
} else {
    best[x.first] = x.second;
}
```

## 2. STL Container Operations (Medium Priority)

### Asymmetric List Difference
```cpp
void printUninvited(const std::vector<std::string>& rsvped, 
                   const std::vector<std::string>& showed) {
    std::unordered_set<std::string> rsvp_set;
    
    // Put all RSVPs in hash set
    for (const auto& person : rsvped) {
        rsvp_set.insert(person);
    }
    
    // Check who showed but didn't RSVP
    for (const auto& person : showed) {
        if (rsvp_set.find(person) == rsvp_set.end()) {
            std::cout << person << std::endl;
        }
    }
}
```

### Mode of Vector (Find most frequent element)
```cpp
int modeOfVector(const std::vector<int>& nums) {
    std::unordered_map<int, int> counts;
    
    // Count frequencies
    for (int num : nums) {
        counts[num]++;
    }
    
    // Find maximum frequency
    int mode = nums[0];
    int maxCount = 0;
    for (auto& pair : counts) {
        if (pair.second > maxCount) {
            maxCount = pair.second;
            mode = pair.first;
        }
    }
    
    return mode;
}
```

## 3. Tree Traversal (Medium Priority)

### In-Order Traversal (BST)
```cpp
void printTree(BinaryNode* root) {
    if (root == nullptr) return;
    
    printTree(root->left);    // Process left subtree
    std::cout << root->element << " ";  // Process current
    printTree(root->right);   // Process right subtree
}
```

### Tree Properties Check
```cpp
// Check if tree has topological ordering
bool hasTopologicalOrdering(Graph& g) {
    // Only DAGs (Directed Acyclic Graphs) have topological orderings
    return isDirected(g) && isAcyclic(g);
}
```

## 4. Algorithm Implementation Snippets

### BuildHeap Bottom-Up
```cpp
void buildHeap(std::vector<int>& heap) {
    for (int i = heap.size() / 2; i >= 0; --i) {
        percolateDown(heap, i);
    }
}
```

### QuickSelect Implementation
```cpp
int quickSelect(std::vector<int>& nums, int low, int high, int k) {
    if (high - low < 10) {
        std::sort(nums.begin() + low, nums.begin() + high + 1);
        return nums[k];
    }
    
    auto pivot = partition(nums, low, high);
    
    if (pivot == k) {
        return nums[k];
    } else if (pivot > k) {
        return quickSelect(nums, low, pivot - 1, k);
    } else {
        return quickSelect(nums, pivot + 1, high, k);
    }
}
```

## 5. Common Exam Coding Patterns

### Pattern 1: Hash Map for Counting/Tracking
```cpp
std::unordered_map<KeyType, ValueType> tracker;
for (auto item : container) {
    if (tracker.find(item.key) == tracker.end()) {
        // First time seeing this key
        tracker[item.key] = item.value;
    } else {
        // Update existing entry
        tracker[item.key] = updateFunction(tracker[item.key], item.value);
    }
}
```

### Pattern 2: Two Data Structures for Different Access Patterns
```cpp
// For O(1) lookup AND O(log n) range queries
std::unordered_map<std::string, int> fastLookup;  // O(1) access
std::map<int, std::string> sortedByTime;          // O(log n) range queries
```

### Pattern 3: Iterator vs Range-Based Loops
```cpp
// Range-based (preferred for simplicity)
for (auto x : container) {
    // Process x
}

// Iterator (when you need more control)
for (auto it = container.begin(); it != container.end(); ++it) {
    // Process *it or it->member
}
```

## 6. Critical Syntax Points

### STL Container Methods
```cpp
// Hash containers (unordered_map, unordered_set)
.find(key) == .end()  // Check if key exists
.count(key)           // Returns 0 or 1 for existence
.insert(value)        // Add element
.erase(key)           // Remove element

// Ordered containers (map, set)
.lower_bound(key)     // First element >= key
.upper_bound(key)     // First element > key
```

### Common Mistakes to Avoid
1. **Using `map[key]` without checking existence** (creates entry with default value)
2. **Forgetting to handle empty containers**
3. **Iterator invalidation** when modifying container during iteration
4. **Wrong complexity analysis** for operations

## 7. Exam Strategy

### Before Writing Code:
1. **Understand the problem** - what data structure is most appropriate?
2. **Consider time complexity** - what operations are needed most frequently?
3. **Plan data structures** - sometimes need multiple for different access patterns

### While Writing:
1. **Start with includes** and function signature
2. **Declare data structures** first
3. **Handle edge cases** (empty input, single element)
4. **Test logic** with small examples mentally

### Key Exam Rubric Points:
- Correct data structure choice
- Proper existence checking for hash containers
- Correct iteration patterns
- Appropriate time complexity
- Proper output format