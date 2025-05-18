### Problem 7: Counting Bloom Filter for Multisets
**Subtopic**: Bloom Filters

**Problem Statement**:
Implement a Counting Bloom Filter that extends the standard Bloom Filter to support item removal operations. Use it to implement a multiset (a set that can contain multiple occurrences of the same element).

**Example**:
```cpp
CountingBloomFilter<std::string> cbf(1000, 3);  // 1000 counters, 3 hash functions
cbf.add("apple");
cbf.add("apple");  // Add twice
cbf.add("banana");

cbf.contains("apple");    // Returns true
cbf.count("apple");       // Returns 2
cbf.count("banana");      // Returns 1
cbf.count("cherry");      // Returns 0

cbf.remove("apple");      // Remove one occurrence
cbf.count("apple");       // Returns 1
```

**Step-by-Step Solution Approach**:
1. Replace the bit array with an array of small counters
2. Increment counters during insertion
3. Decrement counters during deletion
4. Check counters for presence test

**Code Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <functional>
#include <limits>
#include <unordered_map>

template<typename T>
class CountingBloomFilter {
private:
    std::vector<uint8_t> counters;  // Use 8-bit counters
    size_t numHashFunctions;
    size_t size;  // Size of counter array
    
    // Hash functions using std::hash with different seeds
    size_t hash(const T& item, size_t seed) const {
        std::hash<T> hasher;
        size_t hashValue = hasher(item);
        // Combine with seed
        hashValue ^= seed + 0x9e3779b9 + (hashValue << 6) + (hashValue >> 2);
        return hashValue % size;
    }
    
public:
    CountingBloomFilter(size_t m = 1000, size_t k = 3) 
        : counters(m, 0), numHashFunctions(k), size(m) {}
    
    // Add an element
    void add(const T& item) {
        for (size_t i = 0; i < numHashFunctions; i++) {
            size_t pos = hash(item, i);
            if (counters[pos] < std::numeric_limits<uint8_t>::max()) {
                counters[pos]++;
            }
        }
    }
    
    // Remove an element
    bool remove(const T& item) {
        // Check if the item might be in the filter
        if (!contains(item)) {
            return false;
        }
        
        // Verify the counters are positive before decrementing
        for (size_t i = 0; i < numHashFunctions; i++) {
            size_t pos = hash(item, i);
            if (counters[pos] == 0) {
                return false;  // Unexpected state
            }
        }
        
        // Decrement counters
        for (size_t i = 0; i < numHashFunctions; i++) {
            size_t pos = hash(item, i);
            counters[pos]--;
        }
        
        return true;
    }
    
    // Check if an element might be in the filter
    bool contains(const T& item) const {
        for (size_t i = 0; i < numHashFunctions; i++) {
            size_t pos = hash(item, i);
            if (counters[pos] == 0) {
                return false;  // Definitely not in the filter
            }
        }
        return true;  // Might be in the filter
    }
    
    // Estimate the count of an element
    uint8_t count(const T& item) const {
        if (!contains(item)) {
            return 0;
        }
        
        // Return the minimum counter value as an estimate
        uint8_t minCount = std::numeric_limits<uint8_t>::max();
        for (size_t i = 0; i < numHashFunctions; i++) {
            size_t pos = hash(item, i);
            minCount = std::min(minCount, counters[pos]);
        }
        
        return minCount;
    }
    
    // Clear the filter
    void clear() {
        std::fill(counters.begin(), counters.end(), 0);
    }
};

// Multiset implementation using Counting Bloom Filter
template<typename T>
class BloomMultiset {
private:
    CountingBloomFilter<T> cbf;
    std::unordered_map<T, size_t> backupCounts;  // For exact counts
    
public:
    BloomMultiset(size_t m = 10000, size_t k = 5) 
        : cbf(m, k) {}
    
    // Add an element
    void add(const T& item) {
        cbf.add(item);
        backupCounts[item]++;
    }
    
    // Remove an element
    bool remove(const T& item) {
        auto it = backupCounts.find(item);
        if (it == backupCounts.end() || it->second == 0) {
            return false;
        }
        
        cbf.remove(item);
        it->second--;
        
        if (it->second == 0) {
            backupCounts.erase(it);
        }
        
        return true;
    }
    
    // Check if an element is in the multiset
    bool contains(const T& item) const {
        return backupCounts.find(item) != backupCounts.end();
    }
    
    // Get the exact count of an element
    size_t count(const T& item) const {
        auto it = backupCounts.find(item);
        return (it == backupCounts.end()) ? 0 : it->second;
    }
    
    // Get the total number of elements
    size_t size() const {
        size_t total = 0;
        for (const auto& pair : backupCounts) {
            total += pair.second;
        }
        return total;
    }
    
    // Get the number of unique elements
    size_t uniqueSize() const {
        return backupCounts.size();
    }
};
```

**Complexity Analysis**:
- Time Complexity:
  - Add/Remove: O(k) where k is the number of hash functions
  - Contains: O(1) with the backup hash map
  - Count: O(1) with the backup hash map
- Space Complexity: O(m + n) where m is the size of the counter array and n is the number of unique elements

**Edge Cases and Pitfalls**:
- Counter overflow (limited to 8 bits in this implementation)
- False positives in the contains operation
- Need for a backup data structure for exact counts
- Counter underflow during removal of non-existent items
- Multiple hash functions increase overhead

### Problem 8: Cryptographic Hash Function for Password Storage
**Subtopic**: Cryptographic Hashing

**Problem Statement**:
Implement a secure password storage system using cryptographic hash functions with salt. The system should allow for password verification without storing the actual passwords.

**Example**:
```cpp
PasswordManager pm;
pm.registerUser("user1", "password123");
pm.registerUser("user2", "securePassword");

bool isValid1 = pm.verifyPassword("user1", "password123");    // Returns true
bool isValid2 = pm.verifyPassword("user1", "wrongPassword");  // Returns false
```

**Step-by-Step Solution Approach**:
1. Generate a random salt for each user
2. Combine the password with the salt
3. Apply a cryptographic hash function (e.g., SHA-256)
4. Store the salt and hash value
5. For verification, rehash the provided password with the stored salt

**Code Implementation**:
```cpp
#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
#include <random>
#include <iomanip>
#include <sstream>
#include <openssl/sha.h>  // Requires OpenSSL library

class PasswordManager {
private:
    struct PasswordData {
        std::string salt;
        std::string hash;
    };
    
    std::unordered_map<std::string, PasswordData> users;
    
    // Generate a random salt
    std::string generateSalt(size_t length = 16) {
        static const char alphanumeric[] =
            "0123456789"
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "abcdefghijklmnopqrstuvwxyz";
        
        std::random_device rd;
        std::mt19937 generator(rd());
        std::uniform_int_distribution<int> distribution(0, sizeof(alphanumeric) - 2);
        
        std::string salt;
        salt.reserve(length);
        
        for (size_t i = 0; i < length; ++i) {
            salt += alphanumeric[distribution(generator)];
        }
        
        return salt;
    }
    
    // Compute SHA-256 hash
    std::string computeHash(const std::string& input) {
        unsigned char hash[SHA256_DIGEST_LENGTH];
        SHA256_CTX sha256;
        SHA256_Init(&sha256);
        SHA256_Update(&sha256, input.c_str(), input.size());
        SHA256_Final(hash, &sha256);
        
        std::stringstream ss;
        for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
            ss << std::hex << std::setw(2) << std::setfill('0') << static_cast<int>(hash[i]);
        }
        
        return ss.str();
    }
    
public:
    // Register a new user
    bool registerUser(const std::string& username, const std::string& password) {
        if (users.find(username) != users.end()) {
            return false;  // User already exists
        }
        
        PasswordData data;
        data.salt = generateSalt();
        data.hash = computeHash(password + data.salt);
        
        users[username] = data;
        return true;
    }
    
    // Verify a user's password
    bool verifyPassword(const std::string& username, const std::string& password) {
        auto it = users.find(username);
        if (it == users.end()) {
            return false;  // User not found
        }
        
        const PasswordData& data = it->second;
        std::string computedHash = computeHash(password + data.salt);
        
        return computedHash == data.hash;
    }
    
    // Change a user's password
    bool changePassword(const std::string& username, const std::string& oldPassword, 
                        const std::string& newPassword) {
        if (!verifyPassword(username, oldPassword)) {
            return false;  // Old password is incorrect
        }
        
        PasswordData& data = users[username];
        data.salt = generateSalt();  // Generate new salt
        data.hash = computeHash(newPassword + data.salt);
        
        return true;
    }
    
    // Remove a user
    bool removeUser(const std::string& username) {
        return users.erase(username) > 0;
    }
};
```

**Complexity Analysis**:
- Time Complexity:
  - Registration: O(1) average case for hash map operations
  - Verification: O(1) average case
- Space Complexity: O(n) where n is the number of users

**Edge Cases and Pitfalls**:
- Salt length should be sufficient (at least 16 bytes)
- Use a cryptographic hash function (not a general-purpose hash function)
- Store salts separately from hashes
- Consider using a more specialized password hashing function (e.g., bcrypt, Argon2)
- Potential timing attacks if comparison is not time-constant

### Problem 9: LRU Cache Implementation
**Subtopic**: Hash Table Applications

**Problem Statement**:
Implement a Least Recently Used (LRU) cache with a specified capacity that evicts the least recently used item when the cache is full. The cache should support get and put operations in O(1) time.

**Example**:
```cpp
LRUCache<int, std::string> cache(2);  // Capacity of 2
cache.put(1, "one");
cache.put(2, "two");
cache.get(1);          // Returns "one"
cache.put(3, "three");  // Evicts key 2
cache.get(2);          // Returns std::nullopt (not found)
cache.get(3);          // Returns "three"
```

**Step-by-Step Solution Approach**:
1. Use a hash map for O(1) lookups
2. Use a doubly linked list to track usage order
3. Move items to the front on access
4. Evict items from the back when capacity is exceeded

**Code Implementation**:
```cpp
#include <iostream>
#include <unordered_map>
#include <list>
#include <optional>

template<typename K, typename V>
class LRUCache {
private:
    // Doubly linked list node type
    struct Node {
        K key;
        V value;
        Node(K k, V v) : key(k), value(v) {}
    };
    
    size_t capacity;
    std::list<Node> items;  // Doubly linked list to track usage order
    std::unordered_map<K, typename std::list<Node>::iterator> cache;  // Map from key to list iterator
    
public:
    explicit LRUCache(size_t capacity) : capacity(capacity) {}
    
    // Get value by key
    std::optional<V> get(const K& key) {
        auto it = cache.find(key);
        if (it == cache.end()) {
            return std::nullopt;  // Key not found
        }
        
        // Move the accessed item to the front (most recently used)
        items.splice(items.begin(), items, it->second);
        return it->second->value;
    }
    
    // Insert or update key-value pair
    void put(const K& key, const V& value) {
        auto it = cache.find(key);
        
        if (it != cache.end()) {
            // Key exists, update value and move to front
            it->second->value = value;
            items.splice(items.begin(), items, it->second);
            return;
        }
        
        // Check if cache is full
        if (cache.size() >= capacity) {
            // Remove the least recently used item (back of the list)
            K oldKey = items.back().key;
            items.pop_back();
            cache.erase(oldKey);
        }
        
        // Insert new item at the front
        items.emplace_front(key, value);
        cache[key] = items.begin();
    }
    
    // Get the number of items in the cache
    size_t size() const {
        return cache.size();
    }
    
    // Check if the cache is empty
    bool empty() const {
        return cache.empty();
    }
    
    // Clear the cache
    void clear() {
        items.clear();
        cache.clear();
    }
};
```

**Complexity Analysis**:
- Time Complexity:
  - Get: O(1) on average
  - Put: O(1) on average
- Space Complexity: O(capacity) for storing up to capacity items

**Edge Cases and Pitfalls**:
- Zero capacity cache
- Updating existing keys
- Memory overhead of doubly linked list
- Thread safety (the current implementation is not thread-safe)
- Handling multiple accesses to the same key

### Problem 10: Cuckoo Hashing Implementation
**Subtopic**: Advanced Collision Resolution

**Problem Statement**:
Implement a hash table using Cuckoo hashing, which uses two hash functions and guarantees O(1) worst-case lookup time. When a collision occurs, the existing key is displaced, and this process continues until all keys find a place or a cycle is detected (requiring rehashing).

**Example**:
```cpp
CuckooHashTable<int, std::string> cht(10);
cht.insert(5, "apple");
cht.insert(15, "banana");  // Will use the second hash function
cht.insert(25, "cherry");  // Will trigger displacement
cht.lookup(15);            // Returns "banana"
cht.remove(15);
cht.lookup(15);            // Returns std::nullopt
```

**Step-by-Step Solution Approach**:
1. Implement two different hash functions
2. On insert, try the first hash function location
3. If occupied, displace the existing key to its alternate location
4. Continue until all keys find a place or a loop is detected
5. If a loop is detected, rehash with larger tables

**Code Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <optional>
#include <functional>
#include <utility>
#include <algorithm>
#include <stdexcept>

template<typename K, typename V>
class CuckooHashTable {
private:
    struct Slot {
        K key;
        V value;
        bool occupied;
        
        Slot() : occupied(false) {}
    };
    
    std::vector<Slot> table1;
    std::vector<Slot> table2;
    size_t size;
    size_t capacity;
    static constexpr size_t MAX_LOOP = 100;  // Maximum displacement loops
    static constexpr double LOAD_FACTOR_THRESHOLD = 0.4;  // Lower for Cuckoo hashing
    
    // Two different hash functions
    size_t hash1(const K& key) const {
        return std::hash<K>{}(key) % capacity;
    }
    
    size_t hash2(const K& key) const {
        // Use a different seed for the second hash function
        return (std::hash<K>{}(key) ^ 0x5555555555555555ULL) % capacity;
    }
    
    void rehash() {
        size_t newCapacity = capacity * 2;
        CuckooHashTable<K, V> newTable(newCapacity);
        
        // Reinsert all elements
        for (const auto& slot : table1) {
            if (slot.occupied) {
                newTable.insert(slot.key, slot.value);
            }
        }
        
        for (const auto& slot : table2) {
            if (slot.occupied) {
                newTable.insert(slot.key, slot.value);
            }
        }
        
        // Swap the tables
        table1 = std::move(newTable.table1);
        table2 = std::move(newTable.table2);
        capacity = newCapacity;
    }
    
public:
    explicit CuckooHashTable(size_t initialCapacity = 16) 
        : table1(initialCapacity), table2(initialCapacity), 
          size(0), capacity(initialCapacity) {}
    
    bool insert(const K& key, const V& value) {
        // Check if key already exists
        auto result = lookup(key);
        if (result.has_value()) {
            // Update the value
            size_t pos1 = hash1(key);
            size_t pos2 = hash2(key);
            
            if (table1[pos1].occupied && table1[pos1].key == key) {
                table1[pos1].value = value;
            } else {
                table2[pos2].value = value;
            }
            
            return true;
        }
        
        // Check if load factor threshold is exceeded
        if (static_cast<double>(size + 1) / (2 * capacity) >= LOAD_FACTOR_THRESHOLD) {
            rehash();
        }
        
        // Try to insert
        K currentKey = key;
        V currentValue = value;
        bool useTable1 = true;
        
        for (size_t loop = 0; loop < MAX_LOOP; loop++) {
            if (useTable1) {
                size_t pos = hash1(currentKey);
                
                if (!table1[pos].occupied) {
                    // Found an empty slot
                    table1[pos].key = currentKey;
                    table1[pos].value = currentValue;
                    table1[pos].occupied = true;
                    size++;
                    return true;
                }
                
                // Displace the existing key
                std::swap(currentKey, table1[pos].key);
                std::swap(currentValue, table1[pos].value);
                useTable1 = false;
            } else {
                size_t pos = hash2(currentKey);
                
                if (!table2[pos].occupied) {
                    // Found an empty slot
                    table2[pos].key = currentKey;
                    table2[pos].value = currentValue;
                    table2[pos].occupied = true;
                    size++;
                    return true;
                }
                
                // Displace the existing key
                std::swap(currentKey, table2[pos].key);
                std::swap(currentValue, table2[pos].value);
                useTable1 = true;
            }
        }
        
        // If we get here, we've detected a cycle
        rehash();
        return insert(currentKey, currentValue);  // Try again with the last displaced key
    }
    
    std::optional<V> lookup(const K& key) const {
        size_t pos1 = hash1(key);
        if (table1[pos1].occupied && table1[pos1].key == key) {
            return table1[pos1].value;
        }
        
        size_t pos2 = hash2(key);
        if (table2[pos2].occupied && table2[pos2].key == key) {
            return table2[pos2].value;
        }
        
        return std::nullopt;  // Not found
    }
    
    bool remove(const K& key) {
        size_t pos1 = hash1(key);
        if (table1[pos1].occupied && table1[pos1].key == key) {
            table1[pos1].occupied = false;
            size--;
            return true;
        }
        
        size_t pos2 = hash2(key);
        if (table2[pos2].occupied && table2[pos2].key == key) {
            table2[pos2].occupied = false;
            size--;
            return true;
        }
        
        return false;  // Not found
    }
    
    size_t getSize() const {
        return size;
    }
    
    bool empty() const {
        return size == 0;
    }
};
```

**Complexity Analysis**:
- Time Complexity:
  - Lookup: O(1) worst case
  - Insert: O(1) amortized but can be O(n) if rehashing is needed
  - Remove: O(1) worst case
- Space Complexity: O(n) where n is the number of elements

**Edge Cases and Pitfalls**:
- Infinite loops during insertion (addressed with MAX_LOOP)
- Low load factor threshold required
- Two different hash functions must be truly independent
- Rehashing overhead when cycles are detected
- Memory overhead due to two tables

## Implementation Best Practices

### Hash Function Design
1. **Distribution**: Aim for uniform distribution of hash values
2. **Speed**: Hash functions should be computationally efficient
3. **Avalanche Effect**: Small changes in input should cause significant changes in output
4. **Independence**: Multiple hash functions should be independent of each other
5. **Seed Variation**: Use different seeds or salt values for different instances

### Collision Resolution
1. **Separate Chaining**:
   - Use more sophisticated data structures for chains (balanced BSTs instead of linked lists)
   - Keep load factor below 0.7 for optimal performance
   - Consider rehashing when chains grow too long

2. **Open Addressing**:
   - Keep load factor below 0.5-0.6 to minimize clustering
   - Use quadratic probing or double hashing instead of linear probing
   - Handle deletions carefully with tombstone markers

### Performance Optimization
1. **Resizing Strategy**:
   - Grow by a factor of 2 when load factor exceeds threshold
   - Consider shrinking when load factor falls below a lower threshold
   - Rehash incrementally for large tables to prevent pauses

2. **Memory Management**:
   - Choose appropriate initial capacity to minimize resizing
   - Consider memory alignment and cache efficiency
   - For small keys and values, consider using inline storage

3. **Thread Safety**:
   - Use fine-grained locking for concurrent access
   - Consider lock-free implementations for high-contention scenarios
   - Use thread-local storage for temporary operations

### Testing and Validation
1. **Correctness Testing**:
   - Test edge cases: empty tables, single elements, duplicates
   - Test with colliding keys to verify collision resolution
   - Test deletion and rehashing behavior

2. **Performance Testing**:
   - Measure lookup, insert, and delete times for various loads
   - Test with realistic data distributions
   - Profile memory usage and cache behavior

3. **Hash Function Quality**:
   - Test uniformity of distribution
   - Check for patterns or clusters
   - Use statistical tests (chi-squared test) for validation

## Advanced Topics and Further Resources

### Advanced Hashing Techniques
1. **Extendible Hashing**: Dynamic technique for external storage where the directory size doubles but not all buckets need to split.
2. **Linear Hashing**: Incremental growth technique that splits buckets in a predetermined order.
3. **Robin Hood Hashing**: Variant of open addressing that reduces variance in probe sequence lengths.
4. **Hopscotch Hashing**: Combines elements of cuckoo hashing and linear probing with a neighborhood concept.
5. **Locality-Sensitive Hashing (LSH)**: Hash similar items to the same buckets, used for approximate nearest neighbor search.

### Specialized Hash Tables
1. **Concurrent Hash Maps**: Designed for high-performance parallel access.
2. **Distributed Hash Tables (DHTs)**: Spread across multiple machines for peer-to-peer networks.
3. **Persistent Hash Tables**: Maintain state across program executions.
4. **Cache-Oblivious Hash Tables**: Optimized for modern memory hierarchies.
5. **GP-GPU Hash Tables**: Designed for execution on graphics processing units.

### Further Reading
1. "Introduction to Algorithms" by Cormen, Leiserson, Rivest, and Stein
2. "The Art of Computer Programming, Volume 3: Sorting and Searching" by Donald Knuth
3. "Algorithms in C++, Parts 1-4" by Robert Sedgewick
4. "Algorithms" by Sanjoy Dasgupta, Christos Papadimitriou, and Umesh Vazirani
5. "The Algorithm Design Manual" by Steven Skiena

### Online Resources
1. [Hash Table - Wikipedia](https://en.wikipedia.org/wiki/Hash_table)
2. [Bloom Filters - Brilliant](https://brilliant.org/wiki/bloom-filter/)
3. [Cuckoo Hashing - Carnegie Mellon University](https://www.cs.cmu.edu/~dga/papers/cuckoo-conext2014.pdf)
4. [Consistent Hashing - Toptal Engineering Blog](https://www.toptal.com/big-data/consistent-hashing)
5. [Perfect Hashing - MIT OpenCourseWare](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2015/lecture-notes/MIT6_046JS15_lec10.pdf)

This guide has covered the essential concepts, techniques, and applications of hashing, from basic hash tables to advanced specialized data structures. By working through the practice problems and understanding the theoretical foundations, you'll be well-equipped to apply hashing effectively in a wide range of computing scenarios.# Comprehensive Hashing Mastery Guide

## Table of Contents
1. [Introduction to Hashing](#introduction-to-hashing)
2. [Theoretical Foundations](#theoretical-foundations)
   - [Hash Functions](#hash-functions)
   - [Collision Resolution](#collision-resolution)
   - [Load Factor and Dynamic Resizing](#load-factor-and-dynamic-resizing)
3. [Key Hashing Subtopics](#key-hashing-subtopics)
   - [Basic Hash Tables](#basic-hash-tables)
   - [Open Addressing](#open-addressing)
   - [Separate Chaining](#separate-chaining)
   - [Consistent Hashing](#consistent-hashing)
   - [Perfect Hashing](#perfect-hashing)
   - [Bloom Filters](#bloom-filters)
   - [Cryptographic Hashing](#cryptographic-hashing)
4. [Learning Progression Strategy](#learning-progression-strategy)
5. [Practice Problems](#practice-problems)
6. [Implementation Best Practices](#implementation-best-practices)
7. [Advanced Topics and Further Resources](#advanced-topics-and-further-resources)

## Introduction to Hashing

Hashing is a fundamental technique in computer science that transforms data of arbitrary size into fixed-size values, typically for efficient data retrieval and storage. At its core, hashing provides O(1) average-case time complexity for insertions, deletions, and lookups, making it one of the most efficient data structures for these operations.

### When to Use Hashing
- Fast lookups, insertions, and deletions
- Removing duplicates from a collection
- Caching and memorization
- Implementing sets and dictionaries
- Database indexing
- Cryptography and data integrity

### Core Properties of Hashing
- **Deterministic**: Same input always produces the same hash value
- **Fast Computation**: Hashing should be computationally efficient
- **Uniform Distribution**: Hash values should spread evenly across the available space
- **Collision Handling**: Must deal with different inputs producing the same hash value
- **Avalanche Effect**: Small changes in input should produce significantly different hash values (particularly important for cryptographic hashing)

## Theoretical Foundations

### Hash Functions

A hash function is an algorithm that maps data of arbitrary size to fixed-size values. An ideal hash function should:

1. **Be Deterministic**: Same input always yields the same output
2. **Be Uniform**: Distribute outputs uniformly across the hash table
3. **Have Low Collision Probability**: Different inputs rarely produce the same output
4. **Be Efficient**: Compute hash values quickly

#### Common Hash Functions:

1. **Division Method**: h(k) = k mod m
   - Simple but can lead to patterns if m is poorly chosen
   - Works best when m is a prime number not close to a power of 2 or 10

2. **Multiplication Method**: h(k) = ⌊m(kA mod 1)⌋
   - Where A is a constant between 0 and 1
   - The value A = (√5-1)/2 ≈ 0.618 often works well

3. **Universal Hashing**: Choose a hash function randomly from a family of hash functions
   - Prevents adversarial worst-case scenarios
   - Provides mathematical guarantees on collision probability

4. **Polynomial Hash**: h(s) = s[0] + s[1]·p + s[2]·p² + ... + s[n-1]·p^(n-1) mod m
   - Particularly useful for strings
   - The prime p is typically 31 or 33 for ASCII strings

### Collision Resolution

When two different keys hash to the same value, we have a collision. There are several strategies to handle collisions:

#### 1. Separate Chaining
- Each bucket contains a linked list, array, or other data structure
- All elements that hash to the same value are stored in the corresponding bucket
- Performance degrades as chains grow longer
- Time complexity: O(1 + α) where α is the load factor

#### 2. Open Addressing
- All elements are stored in the hash table itself
- When a collision occurs, probe according to a deterministic sequence until an empty slot is found
- Requires load factor < 1.0
- Common probing methods:
  - **Linear Probing**: h(k, i) = (h'(k) + i) mod m
  - **Quadratic Probing**: h(k, i) = (h'(k) + c₁i + c₂i²) mod m
  - **Double Hashing**: h(k, i) = (h₁(k) + i·h₂(k)) mod m

### Load Factor and Dynamic Resizing

The load factor (α) of a hash table is defined as n/m, where:
- n is the number of entries occupied in the hash table
- m is the size of the hash table

As the load factor increases, the performance of a hash table degrades. To maintain performance:

1. **Resize Trigger**: Typically when α exceeds 0.7 or 0.75
2. **Resizing Strategy**: Create a new table with 2-3 times the capacity
3. **Rehashing**: Recompute the hash for each element and insert into the new table

Amortized cost analysis shows that with proper resizing, operations remain O(1) on average.

## Key Hashing Subtopics

### Basic Hash Tables

Hash tables are the most common application of hashing. They store key-value pairs and allow for efficient retrieval based on keys.

**Key Operations**:
- **Insert**: Add a key-value pair
- **Search**: Find a value associated with a key
- **Delete**: Remove a key-value pair

**Performance**:
- Average case: O(1) for all operations
- Worst case: O(n) (when many collisions occur)

### Open Addressing

In open addressing, all elements are stored in the hash table array itself, and collisions are resolved by finding an alternative slot.

**Advantages**:
- Better cache performance (data locality)
- No pointers/overhead of linked structures
- Can achieve higher space efficiency

**Disadvantages**:
- Performance degrades rapidly as the table fills up
- Deletions are more complex (may require tombstones)
- Clustering can develop, especially with linear probing

### Separate Chaining

In separate chaining, each slot in the hash table points to a data structure (typically a linked list) that holds all elements that hash to that slot.

**Advantages**:
- Simple implementation
- Handles high load factors well
- Easy deletion

**Disadvantages**:
- Extra memory overhead for pointers
- Worse cache performance
- May require dynamic memory allocation

### Consistent Hashing

Consistent hashing minimizes the reshuffling of keys when the hash table changes size, particularly useful in distributed systems.

**Key Properties**:
- When adding or removing a node, only K/n keys need to be remapped (where K is total keys, n is number of nodes)
- Keys are distributed relatively uniformly
- Often implemented using a virtual ring with multiple virtual nodes per physical node

**Applications**:
- Distributed caches (e.g., Memcached)
- Distributed databases
- Content delivery networks

### Perfect Hashing

Perfect hashing guarantees no collisions, achieving O(1) worst-case lookup time.

**Types**:
- **Static Perfect Hashing**: No collisions for a fixed set of keys known in advance
- **Minimal Perfect Hashing**: Uses exactly n slots for n keys (100% space efficiency)
- **Dynamic Perfect Hashing**: Allows insertions and deletions while maintaining perfect hashing

**Approach**:
- Often implemented using two-level hash tables
- First level maps to small secondary tables
- Secondary tables use carefully chosen hash functions

### Bloom Filters

Bloom filters are probabilistic data structures that test whether an element is a member of a set.

**Key Properties**:
- Space-efficient
- No false negatives (if it says an element is not in the set, it's definitely not)
- Allows false positives (may incorrectly report that an absent element is present)
- Does not store the elements themselves

**Operations**:
- **Insert**: Hash with k hash functions and set corresponding bits
- **Query**: Check if all k bits are set
- **Delete**: Not directly supported (requires extensions like Counting Bloom Filters)

### Cryptographic Hashing

Cryptographic hash functions are designed for security applications and have additional properties beyond regular hash functions.

**Key Properties**:
- **Pre-image Resistance**: Given a hash h, it's computationally infeasible to find any input x such that hash(x) = h
- **Second Pre-image Resistance**: Given input x₁, it's computationally infeasible to find a different input x₂ such that hash(x₁) = hash(x₂)
- **Collision Resistance**: It's computationally infeasible to find any two different inputs x₁ and x₂ such that hash(x₁) = hash(x₂)

**Common Algorithms**:
- SHA-256, SHA-3
- Blake2, Blake3
- MD5, SHA-1 (no longer considered secure)

## Learning Progression Strategy

To master hashing, follow this recommended learning path:

1. **Foundational Understanding**:
   - Basic hash table operations and implementations
   - Common hash functions
   - Analysis of collision probabilities

2. **Collision Resolution Techniques**:
   - Separate chaining implementation
   - Linear probing and analysis
   - Quadratic probing and double hashing

3. **Performance Optimization**:
   - Load factor analysis
   - Dynamic resizing strategies
   - Cache-efficient implementations

4. **Specialized Hashing Techniques**:
   - Bloom filters
   - Perfect hashing
   - Consistent hashing

5. **Advanced Applications**:
   - Cryptographic hashing
   - Distributed hash tables
   - Locality-sensitive hashing

### Prerequisite Knowledge:
- Basic data structures (arrays, linked lists)
- Algorithm analysis (Big O notation)
- Probability theory basics
- Modular arithmetic

## Practice Problems

### Problem 1: Basic Hash Table Implementation
**Subtopic**: Basic Hash Tables

**Problem Statement**:
Implement a hash table with separate chaining using linked lists. Your implementation should support the following operations:
- `put(key, value)`: Insert or update a key-value pair
- `get(key)`: Retrieve the value associated with a key
- `remove(key)`: Remove a key-value pair
- `contains(key)`: Check if a key exists in the hash table

**Example**:
```cpp
HashTable<string, int> ht(10);
ht.put("apple", 5);
ht.put("banana", 8);
ht.get("apple");  // Returns 5
ht.contains("cherry");  // Returns false
ht.remove("apple");
ht.contains("apple");  // Returns false
```

**Step-by-Step Solution Approach**:

1. **Naive Solution**: Start with a simple array of linked lists
2. **Hash Function**: Implement a hash function for various key types
3. **Collision Resolution**: Implement separate chaining using linked lists
4. **Table Operations**: Implement put, get, remove, and contains operations
5. **Edge Cases**: Handle null values, resizing, and other edge cases

**Code Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <optional>
#include <functional>

template<typename K, typename V>
class HashTable {
private:
    struct Node {
        K key;
        V value;
        Node* next;
        
        Node(const K& k, const V& v) : key(k), value(v), next(nullptr) {}
    };
    
    std::vector<Node*> buckets;
    size_t size;
    static constexpr double LOAD_FACTOR_THRESHOLD = 0.75;
    
    size_t hash(const K& key) const {
        return std::hash<K>{}(key) % buckets.size();
    }
    
    void resize() {
        size_t newCapacity = buckets.size() * 2;
        std::vector<Node*> newBuckets(newCapacity, nullptr);
        
        for (auto current : buckets) {
            while (current != nullptr) {
                Node* next = current->next;
                
                // Rehash and insert into new buckets
                size_t newIndex = std::hash<K>{}(current->key) % newCapacity;
                current->next = newBuckets[newIndex];
                newBuckets[newIndex] = current;
                
                current = next;
            }
        }
        
        buckets = std::move(newBuckets);
    }
    
public:
    explicit HashTable(size_t capacity = 16) : buckets(capacity, nullptr), size(0) {}
    
    ~HashTable() {
        for (auto bucket : buckets) {
            Node* current = bucket;
            while (current != nullptr) {
                Node* next = current->next;
                delete current;
                current = next;
            }
        }
    }
    
    void put(const K& key, const V& value) {
        if (size >= buckets.size() * LOAD_FACTOR_THRESHOLD) {
            resize();
        }
        
        size_t index = hash(key);
        Node* current = buckets[index];
        
        // Check if key already exists
        while (current != nullptr) {
            if (current->key == key) {
                current->value = value;
                return;
            }
            current = current->next;
        }
        
        // Key doesn't exist, add new node
        Node* newNode = new Node(key, value);
        newNode->next = buckets[index];
        buckets[index] = newNode;
        size++;
    }
    
    std::optional<V> get(const K& key) const {
        size_t index = hash(key);
        Node* current = buckets[index];
        
        while (current != nullptr) {
            if (current->key == key) {
                return current->value;
            }
            current = current->next;
        }
        
        return std::nullopt;
    }
    
    bool contains(const K& key) const {
        size_t index = hash(key);
        Node* current = buckets[index];
        
        while (current != nullptr) {
            if (current->key == key) {
                return true;
            }
            current = current->next;
        }
        
        return false;
    }
    
    std::optional<V> remove(const K& key) {
        size_t index = hash(key);
        Node* current = buckets[index];
        Node* prev = nullptr;
        
        while (current != nullptr) {
            if (current->key == key) {
                if (prev == nullptr) {
                    // Removing head node
                    buckets[index] = current->next;
                } else {
                    prev->next = current->next;
                }
                
                V value = current->value;
                delete current;
                size--;
                
                return value;
            }
            
            prev = current;
            current = current->next;
        }
        
        return std::nullopt;
    }
    
    size_t getSize() const {
        return size;
    }
};
```

**Complexity Analysis**:
- Time Complexity:
  - Average case: O(1) for put, get, contains, remove
  - Worst case: O(n) when all keys hash to the same bucket
- Space Complexity: O(n + m) where n is the number of elements and m is the number of buckets

**Edge Cases and Pitfalls**:
- Empty buckets
- Collisions (handled with chaining)
- Resizing the hash table
- Key equality comparison
- Memory management (delete nodes properly)

### Problem 2: Open Addressing with Linear Probing
**Subtopic**: Open Addressing

**Problem Statement**:
Implement a hash table using open addressing with linear probing for collision resolution. Your implementation should support the following operations:
- `insert(key, value)`: Insert a key-value pair
- `get(key)`: Retrieve the value associated with a key
- `remove(key)`: Remove a key-value pair
- `contains(key)`: Check if a key exists

**Example**:
```cpp
LinearProbingHashTable<int, string> lpt(10);
lpt.insert(5, "apple");
lpt.insert(15, "banana");  // Same hash as 5 (assuming hash function is h(k) = k % 10)
lpt.insert(25, "cherry");  // Same hash as 5 and 15
lpt.get(15);               // Returns "banana"
lpt.remove(15);
lpt.get(25);               // Returns "cherry"
lpt.contains(15);          // Returns false
```

**Step-by-Step Solution Approach**:
1. Create a hash table with slots for key-value pairs and status (EMPTY, OCCUPIED, DELETED)
2. Implement linear probing for collision resolution
3. Handle the "tombstone" problem for deletions
4. Implement dynamic resizing

**Code Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <optional>
#include <functional>

template<typename K, typename V>
class LinearProbingHashTable {
private:
    enum SlotStatus { EMPTY, OCCUPIED, DELETED };
    
    struct Slot {
        K key;
        V value;
        SlotStatus status;
        
        Slot() : status(EMPTY) {}
    };
    
    std::vector<Slot> table;
    size_t size;
    size_t capacity;
    static constexpr double LOAD_FACTOR_THRESHOLD = 0.6;  // Lower for open addressing
    
    size_t hash(const K& key) const {
        return std::hash<K>{}(key) % capacity;
    }
    
    size_t findSlot(const K& key) const {
        size_t index = hash(key);
        size_t originalIndex = index;
        bool firstIteration = true;
        
        do {
            if (table[index].status == EMPTY) {
                return capacity;  // Not found
            }
            
            if (table[index].status == OCCUPIED && table[index].key == key) {
                return index;  // Found
            }
            
            // Linear probing
            index = (index + 1) % capacity;
            firstIteration = false;
        } while (index != originalIndex);
        
        return capacity;  // Table is full of OCCUPIED or DELETED and key not found
    }
    
    void resize() {
        size_t oldCapacity = capacity;
        capacity = capacity * 2;
        std::vector<Slot> newTable(capacity);
        
        for (size_t i = 0; i < oldCapacity; i++) {
            if (table[i].status == OCCUPIED) {
                size_t newIndex = hash(table[i].key);
                
                // Find next empty slot
                while (newTable[newIndex].status == OCCUPIED) {
                    newIndex = (newIndex + 1) % capacity;
                }
                
                newTable[newIndex].key = table[i].key;
                newTable[newIndex].value = table[i].value;
                newTable[newIndex].status = OCCUPIED;
            }
        }
        
        table = std::move(newTable);
    }
    
public:
    explicit LinearProbingHashTable(size_t initialCapacity = 16) 
        : table(initialCapacity), size(0), capacity(initialCapacity) {}
    
    void insert(const K& key, const V& value) {
        if (static_cast<double>(size) / capacity >= LOAD_FACTOR_THRESHOLD) {
            resize();
        }
        
        size_t index = hash(key);
        
        // Find the next available slot using linear probing
        while (table[index].status == OCCUPIED && table[index].key != key) {
            index = (index + 1) % capacity;
        }
        
        // If this key already exists, update its value
        if (table[index].status == OCCUPIED) {
            table[index].value = value;
            return;
        }
        
        // Insert new key-value pair
        table[index].key = key;
        table[index].value = value;
        table[index].status = OCCUPIED;
        size++;
    }
    
    std::optional<V> get(const K& key) const {
        size_t index = findSlot(key);
        
        if (index < capacity) {
            return table[index].value;
        }
        
        return std::nullopt;
    }
    
    bool contains(const K& key) const {
        return findSlot(key) < capacity;
    }
    
    std::optional<V> remove(const K& key) {
        size_t index = findSlot(key);
        
        if (index < capacity) {
            table[index].status = DELETED;
            size--;
            return table[index].value;
        }
        
        return std::nullopt;
    }
    
    size_t getSize() const {
        return size;
    }
};
```

**Complexity Analysis**:
- Time Complexity:
  - Average case: O(1) for insert, get, contains, remove
  - Worst case: O(n) when there are many collisions
- Space Complexity: O(m) where m is the capacity of the table

**Edge Cases and Pitfalls**:
- Handling deleted slots during lookups
- Maintaining a low load factor to prevent clustering
- Infinite loops during linear probing if the table becomes full
- Primary clustering: keys tend to cluster together leading to longer search times

### Problem 3: Implementing a Set with Bloom Filter
**Subtopic**: Bloom Filters

**Problem Statement**:
Implement a Bloom filter to efficiently test whether an element might be in a set. Then use it to implement a memory-efficient set data structure that can handle false positives but no false negatives.

**Example**:
```cpp
BloomFilter<string> filter(1000, 3);  // 1000 bits, 3 hash functions
filter.insert("apple");
filter.insert("banana");
filter.mightContain("apple");   // Returns true
filter.mightContain("cherry");  // Probably returns false, but could be a false positive
```

**Step-by-Step Solution Approach**:
1. Implement multiple independent hash functions
2. Create a bit array of fixed size
3. Insert elements by setting bits corresponding to hash values
4. Check for presence by verifying all relevant bits are set

**Code Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <functional>
#include <bitset>
#include <array>

template<typename T, size_t M = 1000>
class BloomFilter {
private:
    std::bitset<M> bits;
    size_t numHashFunctions;
    
    // Hash functions using std::hash with different seeds
    size_t hash(const T& item, size_t seed) const {
        std::hash<T> hasher;
        size_t hashValue = hasher(item);
        // Combine with seed using a simple mixing function
        hashValue ^= seed + 0x9e3779b9 + (hashValue << 6) + (hashValue >> 2);
        return hashValue % M;
    }
    
public:
    explicit BloomFilter(size_t k = 3) : numHashFunctions(k) {}
    
    void insert(const T& item) {
        for (size_t i = 0; i < numHashFunctions; i++) {
            bits.set(hash(item, i));
        }
    }
    
    bool mightContain(const T& item) const {
        for (size_t i = 0; i < numHashFunctions; i++) {
            if (!bits.test(hash(item, i))) {
                return false;  // Definitely not in the set
            }
        }
        return true;  // Might be in the set (could be a false positive)
    }
    
    void clear() {
        bits.reset();
    }
    
    // Calculate the current false positive probability
    double falsePositiveProbability(size_t numItems) const {
        // p = (1 - e^(-kn/m))^k
        // Where:
        // k = number of hash functions
        // n = number of items
        // m = size of the bit array
        double m = static_cast<double>(M);
        double k = static_cast<double>(numHashFunctions);
        double n = static_cast<double>(numItems);
        
        double e = 2.71828182845904;  // Base of natural logarithm
        double innerTerm = 1.0 - std::pow(e, -k * n / m);
        return std::pow(innerTerm, k);
    }
};

// A memory-efficient set using BloomFilter with backup for verification
template<typename T>
class BloomFilterSet {
private:
    BloomFilter<T, 10000> filter;
    std::vector<T> backupSet;  // For verification to eliminate false positives
    
public:
    BloomFilterSet() : filter(5) {}  // 5 hash functions for lower false positive rate
    
    void insert(const T& item) {
        if (!contains(item)) {  // Avoid duplicates
            filter.insert(item);
            backupSet.push_back(item);
        }
    }
    
    bool contains(const T& item) const {
        // First use the bloom filter for efficient negative checks
        if (!filter.mightContain(item)) {
            return false;  // Definitely not in the set
        }
        
        // If bloom filter indicates it might be present, check the backup
        for (const auto& element : backupSet) {
            if (element == item) {
                return true;
            }
        }
        
        return false;  // False positive in the bloom filter
    }
    
    size_t size() const {
        return backupSet.size();
    }
};
```

**Complexity Analysis**:
- Time Complexity:
  - Insert: O(k) where k is the number of hash functions
  - Lookup: O(k) in the average case when the element is not present, O(n) in the worst case to verify positives
- Space Complexity: O(m + n) where m is the size of the bit array and n is the number of elements stored

**Edge Cases and Pitfalls**:
- False positives (handled with backup validation)
- Choosing optimal number of hash functions
- Selecting appropriate bit array size
- Cannot remove elements from standard Bloom filters
- Performance degradation as the filter fills up

### Problem 4: Hash Map with Double Hashing
**Subtopic**: Open Addressing

**Problem Statement**:
Implement a hash map using open addressing with double hashing for collision resolution. Double hashing uses a secondary hash function to determine the step size when a collision occurs.

**Example**:
```cpp
DoubleHashMap<int, string> map(11);  // Size 11 (prime number)
map.put(5, "apple");
map.put(16, "banana");  // Collision with 5, use double hashing
map.put(27, "cherry");  // Another collision, use double hashing
map.get(16);            // Returns "banana"
map.contains(27);       // Returns true
map.remove(16);
map.contains(16);       // Returns false
```

**Step-by-Step Solution Approach**:
1. Implement primary hash function h₁(k)
2. Implement secondary hash function h₂(k) (must never return 0)
3. Calculate probe sequence as h(k, i) = (h₁(k) + i·h₂(k)) mod m
4. Handle deletions with tombstone markers
5. Implement dynamic resizing

**Code Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <optional>
#include <functional>

template<typename K, typename V>
class DoubleHashMap {
private:
    enum SlotStatus { EMPTY, OCCUPIED, DELETED };
    
    struct Entry {
        K key;
        V value;
        SlotStatus status;
        
        Entry() : status(EMPTY) {}
    };
    
    std::vector<Entry> table;
    size_t size;
    size_t capacity;
    static constexpr double LOAD_FACTOR_THRESHOLD = 0.5;  // Lower for open addressing
    
    // Primary hash function
    size_t hash1(const K& key) const {
        return std::hash<K>{}(key) % capacity;
    }
    
    // Secondary hash function - must never return 0
    size_t hash2(const K& key) const {
        // Using a different seed/salt for the second hash
        size_t h2 = (std::hash<K>{}(key) ^ 0x5555555555555555ULL) % (capacity - 1);
        return h2 + 1;  // Ensure it's never 0
    }
    
    size_t findSlot(const K& key) const {
        size_t h1 = hash1(key);
        size_t h2 = hash2(key);
        size_t i = 0;
        size_t slot;
        
        do {
            slot = (h1 + i * h2) % capacity;
            
            if (table[slot].status == EMPTY) {
                return capacity;  // Not found
            }
            
            if (table[slot].status == OCCUPIED && table[slot].key == key) {
                return slot;  // Found
            }
            
            i++;
        } while (i < capacity);  // Avoid infinite loop
        
        return capacity;  // Table is full and key not found
    }
    
    bool isPrime(size_t n) const {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        
        for (size_t i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        
        return true;
    }
    
    size_t nextPrime(size_t n) const {
        if (n <= 1) return 2;
        
        size_t prime = n;
        bool found = false;
        
        while (!found) {
            prime++;
            if (isPrime(prime)) found = true;
        }
        
        return prime;
    }
    
    void resize() {
        size_t oldCapacity = capacity;
        capacity = nextPrime(capacity * 2);
        std::vector<Entry> newTable(capacity);
        
        for (size_t i = 0; i < oldCapacity; i++) {
            if (table[i].status == OCCUPIED) {
                K key = table[i].key;
                V value = table[i].value;
                
                // Insert into new table
                size_t h1 = std::hash<K>{}(key) % capacity;
                size_t h2 = (std::hash<K>{}(key) ^ 0x5555555555555555ULL) % (capacity - 1) + 1;
                size_t j = 0;
                size_t slot;
                
                do {
                    slot = (h1 + j * h2) % capacity;
                    j++;
                } while (newTable[slot].status == OCCUPIED);
                
                newTable[slot].key = key;
                newTable[slot].value = value;
                newTable[slot].status = OCCUPIED;
            }
        }
        
        table = std::move(newTable);
    }
    
public:
    explicit DoubleHashMap(size_t initialCapacity = 17) 
        : size(0) {
        // Ensure capacity is prime for better double hashing
        capacity = isPrime(initialCapacity) ? initialCapacity : nextPrime(initialCapacity);
        table.resize(capacity);
    }
    
    void put(const K& key, const V& value) {
        if (static_cast<double>(size) / capacity >= LOAD_FACTOR_THRESHOLD) {
            resize();
        }
        
        size_t h1 = hash1(key);
        size_t h2 = hash2(key);
        size_t i = 0;
        size_t slot;
        
        do {
            slot = (h1 + i * h2) % capacity;
            
            if (table[slot].status != OCCUPIED || table[slot].key == key) {
                break;
            }
            
            i++;
        } while (i < capacity);
        
        // If this key already exists, update its value
        if (table[slot].status == OCCUPIED && table[slot].key == key) {
            table[slot].value = value;
            return;
        }
        
        // Insert new key-value pair
        table[slot].key = key;
        table[slot].value = value;
        table[slot].status = OCCUPIED;
        size++;
    }
    
    std::optional<V> get(const K& key) const {
        size_t slot = findSlot(key);
        
        if (slot < capacity) {
            return table[slot].value;
        }
        
        return std::nullopt;
    }
    
    bool contains(const K& key) const {
        return findSlot(key) < capacity;
    }
    
    std::optional<V> remove(const K& key) {
        size_t slot = findSlot(key);
        
        if (slot < capacity) {
            table[slot].status = DELETED;
            size--;
            return table[slot].value;
        }
        
        return std::nullopt;
    }
    
    size_t getSize() const {
        return size;
    }
};
```

**Complexity Analysis**:
- Time Complexity:
  - Average case: O(1) for put, get, contains, remove
  - Worst case: O(n) when there are many collisions
- Space Complexity: O(m) where m is the capacity of the table

**Edge Cases and Pitfalls**:
- Ensure the secondary hash function never returns 0
- Use prime number table sizes for better distribution
- Handle tombstone markers correctly
- Infinite loop if the table becomes full without proper safeguards
- Choose appropriate load factor threshold