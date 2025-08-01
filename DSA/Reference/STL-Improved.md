# C++ STL: Complete Standard Template Library Guide

## 📋 Table of Contents
- [Overview](#overview)
- [Sequence Containers](#sequence-containers)
- [Associative Containers](#associative-containers)
- [Unordered Containers](#unordered-containers)
- [Container Adapters](#container-adapters)
- [Iterators](#iterators)
- [Algorithms](#algorithms)
- [Common Patterns](#common-patterns)
- [Performance Comparison](#performance-comparison)
- [Quick Reference](#quick-reference)

---

## Overview

The **Standard Template Library (STL)** is a powerful collection of C++ template classes providing common data structures and algorithms. It's designed for efficiency and ease of use.

### **Key Benefits**
- **Generic Programming**: Works with any data type
- **Efficiency**: Optimized implementations
- **Consistency**: Uniform interface across containers
- **Safety**: Type-safe operations

---

## Sequence Containers

### **std::vector**
**Description**: Dynamic array with automatic resizing
**Best For**: Random access, frequent additions at end

```cpp
#include <vector>

std::vector<int> vec = {1, 2, 3, 4, 5};

// Common operations
vec.push_back(6);           // Add to end
vec.pop_back();             // Remove from end
vec.insert(vec.begin(), 0); // Insert at beginning
vec.erase(vec.begin());     // Remove first element
int first = vec[0];         // Random access
int size = vec.size();      // Get size
bool empty = vec.empty();   // Check if empty
```

**Time Complexities**:
- Access: O(1)
- Insert/Delete at end: O(1) amortized
- Insert/Delete at beginning/middle: O(n)
- Search: O(n)

### **std::list**
**Description**: Doubly-linked list
**Best For**: Frequent insertions/deletions at any position

```cpp
#include <list>

std::list<int> lst = {1, 2, 3, 4, 5};

// Common operations
lst.push_front(0);          // Add to front
lst.push_back(6);           // Add to back
lst.pop_front();            // Remove from front
lst.pop_back();             // Remove from back
lst.insert(lst.begin(), 0); // Insert anywhere
lst.erase(lst.begin());     // Remove anywhere
```

**Time Complexities**:
- Access: O(n)
- Insert/Delete: O(1) (with iterator)
- Search: O(n)

### **std::deque**
**Description**: Double-ended queue
**Best For**: Frequent additions/removals at both ends

```cpp
#include <deque>

std::deque<int> dq = {1, 2, 3, 4, 5};

// Common operations
dq.push_front(0);           // Add to front
dq.push_back(6);            // Add to back
dq.pop_front();             // Remove from front
dq.pop_back();              // Remove from back
int first = dq[0];          // Random access
```

**Time Complexities**:
- Access: O(1)
- Insert/Delete at ends: O(1)
- Insert/Delete in middle: O(n)

---

## Associative Containers

### **std::set**
**Description**: Ordered unique elements (typically implemented as BST)
**Best For**: Maintaining sorted unique elements

```cpp
#include <set>

std::set<int> s = {3, 1, 4, 1, 5}; // {1, 3, 4, 5}

// Common operations
s.insert(2);                // Insert element
s.erase(3);                 // Remove element
auto it = s.find(4);        // Find element
bool exists = s.count(5);   // Check existence
int size = s.size();        // Get size
```

**Time Complexities**:
- Insert/Delete/Search: O(log n)
- Iteration: O(n)

### **std::map**
**Description**: Ordered key-value pairs
**Best For**: Associative arrays with sorted keys

```cpp
#include <map>

std::map<std::string, int> m;
m["apple"] = 5;
m["banana"] = 3;
m["cherry"] = 7;

// Common operations
m.insert({"orange", 4});    // Insert pair
m.erase("banana");          // Remove by key
auto it = m.find("apple");  // Find by key
int count = m.count("cherry"); // Check existence
int value = m["apple"];     // Access value
```

**Time Complexities**:
- Insert/Delete/Search: O(log n)
- Iteration: O(n)

### **std::multiset / std::multimap**
**Description**: Allow duplicate elements/keys
**Best For**: When duplicates are needed

```cpp
#include <set>
#include <map>

std::multiset<int> ms = {1, 2, 2, 3, 3, 3}; // {1, 2, 2, 3, 3, 3}
std::multimap<std::string, int> mm;
mm.insert({"apple", 5});
mm.insert({"apple", 3}); // Multiple values for same key
```

---

## Unordered Containers

### **std::unordered_set**
**Description**: Hash-based unique elements
**Best For**: Fast lookups when order doesn't matter

```cpp
#include <unordered_set>

std::unordered_set<int> us = {3, 1, 4, 1, 5}; // {1, 3, 4, 5} (order may vary)

// Common operations
us.insert(2);               // Insert element
us.erase(3);                // Remove element
auto it = us.find(4);       // Find element
bool exists = us.count(5);  // Check existence
```

**Time Complexities**:
- Insert/Delete/Search: O(1) average, O(n) worst case
- Iteration: O(n)

### **std::unordered_map**
**Description**: Hash-based key-value pairs
**Best For**: Fast associative arrays

```cpp
#include <unordered_map>

std::unordered_map<std::string, int> um;
um["apple"] = 5;
um["banana"] = 3;

// Common operations
um.insert({"orange", 4});   // Insert pair
um.erase("banana");         // Remove by key
auto it = um.find("apple"); // Find by key
int value = um["apple"];    // Access value
```

**Time Complexities**:
- Insert/Delete/Search: O(1) average, O(n) worst case
- Iteration: O(n)

---

## Container Adapters

### **std::stack**
**Description**: LIFO (Last In, First Out) container
**Best For**: Undo operations, function call stack

```cpp
#include <stack>

std::stack<int> st;
st.push(1);                 // Push element
st.push(2);
st.push(3);

int top = st.top();         // Access top element
st.pop();                   // Remove top element
bool empty = st.empty();    // Check if empty
int size = st.size();       // Get size
```

### **std::queue**
**Description**: FIFO (First In, First Out) container
**Best For**: BFS, task scheduling

```cpp
#include <queue>

std::queue<int> q;
q.push(1);                  // Add to back
q.push(2);
q.push(3);

int front = q.front();      // Access front element
int back = q.back();        // Access back element
q.pop();                    // Remove front element
```

### **std::priority_queue**
**Description**: Max heap by default
**Best For**: Dijkstra's algorithm, task prioritization

```cpp
#include <queue>

std::priority_queue<int> pq;
pq.push(3);                 // Add element
pq.push(1);
pq.push(4);

int max = pq.top();         // Access maximum element
pq.pop();                   // Remove maximum element

// Min heap
std::priority_queue<int, std::vector<int>, std::greater<int>> min_pq;
```

---

## Iterators

### **Iterator Categories**

| Category | Description | Operations | Example Containers |
|----------|-------------|------------|-------------------|
| **Input** | Read-only, forward | `++`, `*`, `==`, `!=` | `std::istream_iterator` |
| **Output** | Write-only, forward | `++`, `*` | `std::ostream_iterator` |
| **Forward** | Read/write, forward | `++`, `*`, `==`, `!=` | `std::forward_list` |
| **Bidirectional** | Read/write, forward/backward | `++`, `--`, `*`, `==`, `!=` | `std::list`, `std::set` |
| **Random Access** | Read/write, random access | `++`, `--`, `+`, `-`, `[]`, `*`, `==`, `!=`, `<`, `>` | `std::vector`, `std::array` |

### **Common Iterator Operations**
```cpp
std::vector<int> vec = {1, 2, 3, 4, 5};

// Iterator declaration
auto it = vec.begin();
auto end = vec.end();

// Navigation
++it;                       // Next element
--it;                       // Previous element (if bidirectional)
it += 2;                    // Advance by 2 (if random access)
it -= 1;                    // Go back by 1 (if random access)

// Access
int value = *it;            // Dereference
int first = vec[0];         // Random access (if random access)

// Comparison
if (it != end) {            // Check if not at end
    // Process element
}

// Distance
int distance = std::distance(vec.begin(), it);
```

---

## Algorithms

### **Sorting Algorithms**
```cpp
#include <algorithm>

std::vector<int> vec = {3, 1, 4, 1, 5, 9, 2, 6};

// Sort in ascending order
std::sort(vec.begin(), vec.end());

// Sort in descending order
std::sort(vec.begin(), vec.end(), std::greater<int>());

// Partial sort (first 3 elements)
std::partial_sort(vec.begin(), vec.begin() + 3, vec.end());

// Stable sort (preserves relative order of equal elements)
std::stable_sort(vec.begin(), vec.end());
```

### **Searching Algorithms**
```cpp
// Binary search (requires sorted container)
bool found = std::binary_search(vec.begin(), vec.end(), 5);

// Find element
auto it = std::find(vec.begin(), vec.end(), 3);

// Find if (with predicate)
auto it2 = std::find_if(vec.begin(), vec.end(), 
    [](int x) { return x > 5; });

// Count occurrences
int count = std::count(vec.begin(), vec.end(), 1);
```

### **Modifying Algorithms**
```cpp
// Copy elements
std::vector<int> dest(8);
std::copy(vec.begin(), vec.end(), dest.begin());

// Fill with value
std::fill(vec.begin(), vec.end(), 0);

// Generate values
std::generate(vec.begin(), vec.end(), 
    []() { return rand() % 100; });

// Remove elements
auto new_end = std::remove(vec.begin(), vec.end(), 1);
vec.erase(new_end, vec.end());
```

### **Min/Max Operations**
```cpp
// Find minimum and maximum
auto min_it = std::min_element(vec.begin(), vec.end());
auto max_it = std::max_element(vec.begin(), vec.end());

// Min and max of two values
int min_val = std::min(3, 5);
int max_val = std::max(3, 5);

// Min and max of multiple values
int min_val = std::min({1, 2, 3, 4, 5});
int max_val = std::max({1, 2, 3, 4, 5});
```

---

## Common Patterns

### **Iterating Through Containers**
```cpp
// Range-based for loop (C++11)
for (const auto& element : vec) {
    std::cout << element << " ";
}

// Traditional iterator loop
for (auto it = vec.begin(); it != vec.end(); ++it) {
    std::cout << *it << " ";
}

// Index-based loop (for vectors/arrays)
for (size_t i = 0; i < vec.size(); ++i) {
    std::cout << vec[i] << " ";
}
```

### **Working with Pairs and Maps**
```cpp
std::map<std::string, int> m = {{"apple", 5}, {"banana", 3}};

// Iterate through key-value pairs
for (const auto& [key, value] : m) {
    std::cout << key << ": " << value << std::endl;
}

// Traditional way
for (const auto& pair : m) {
    std::cout << pair.first << ": " << pair.second << std::endl;
}
```

### **Custom Comparators**
```cpp
// Custom comparator for sorting
std::sort(vec.begin(), vec.end(), 
    [](int a, int b) { return a > b; });

// Custom comparator for set
std::set<int, std::greater<int>> s;

// Custom comparator for priority queue
auto cmp = [](int a, int b) { return a > b; };
std::priority_queue<int, std::vector<int>, decltype(cmp)> pq(cmp);
```

---

## Performance Comparison

### **Container Selection Guide**

| Use Case | Recommended Container | Reason |
|----------|----------------------|--------|
| **Frequent random access** | `std::vector` | O(1) access |
| **Frequent insertions at end** | `std::vector` | O(1) amortized |
| **Frequent insertions anywhere** | `std::list` | O(1) insertion |
| **Need sorted elements** | `std::set` | Automatic sorting |
| **Key-value pairs, sorted** | `std::map` | Ordered key-value |
| **Fast lookups, no order** | `std::unordered_set` | O(1) average |
| **Fast key-value, no order** | `std::unordered_map` | O(1) average |
| **LIFO operations** | `std::stack` | Specialized for LIFO |
| **FIFO operations** | `std::queue` | Specialized for FIFO |
| **Priority-based access** | `std::priority_queue` | Heap implementation |

### **Memory Considerations**
- **std::vector**: Contiguous memory, cache-friendly
- **std::list**: Non-contiguous, more memory overhead
- **std::map/set**: Tree-based, moderate overhead
- **std::unordered_map/set**: Hash-based, more memory for speed

---

## Quick Reference

### **Common Operations by Container**

| Operation | vector | list | set | map | unordered_set | unordered_map |
|-----------|--------|------|-----|-----|---------------|---------------|
| **Insert at end** | O(1) | O(1) | - | - | - | - |
| **Insert anywhere** | O(n) | O(1) | O(log n) | O(log n) | O(1) | O(1) |
| **Delete** | O(n) | O(1) | O(log n) | O(log n) | O(1) | O(1) |
| **Search** | O(n) | O(n) | O(log n) | O(log n) | O(1) | O(1) |
| **Random access** | O(1) | O(n) | O(n) | O(n) | O(n) | O(n) |

### **Algorithm Complexities**

| Algorithm | Time Complexity | Notes |
|-----------|----------------|-------|
| **std::sort** | O(n log n) | Unstable sort |
| **std::stable_sort** | O(n log n) | Stable sort |
| **std::find** | O(n) | Linear search |
| **std::binary_search** | O(log n) | Requires sorted range |
| **std::copy** | O(n) | Linear copy |
| **std::remove** | O(n) | Doesn't resize container |

### **Common Header Files**
```cpp
#include <vector>      // std::vector
#include <list>        // std::list
#include <deque>       // std::deque
#include <set>         // std::set, std::multiset
#include <map>         // std::map, std::multimap
#include <unordered_set> // std::unordered_set
#include <unordered_map> // std::unordered_map
#include <stack>       // std::stack
#include <queue>       // std::queue, std::priority_queue
#include <algorithm>   // std::sort, std::find, etc.
#include <iterator>    // std::iterator_traits
```

### **Exam Tips**
1. **Choose the right container** for your use case
2. **Understand iterator categories** and their capabilities
3. **Know when to use ordered vs unordered containers**
4. **Remember that algorithms work with iterators**, not containers directly
5. **Consider both time and space complexity** when choosing containers

---

## 🎯 Practice Problems

### **Problem 1: Container Selection**
You need to store unique integers and frequently check if a number exists. Which container should you use?
**Answer**: `std::unordered_set` - O(1) average lookup time

### **Problem 2: Iterator Usage**
What's wrong with this code?
```cpp
std::list<int> lst = {1, 2, 3};
auto it = lst.begin();
it += 2; // Error!
```
**Answer**: `std::list` iterators are bidirectional, not random access. Use `++it` twice instead.

### **Problem 3: Algorithm Complexity**
What's the time complexity of `std::sort` on a vector of n elements?
**Answer**: O(n log n) - typically uses introsort (quicksort + heapsort)

---

*Master the STL and you'll have powerful, efficient tools for any programming task!* 