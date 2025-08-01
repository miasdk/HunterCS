# Implementing Custom Hash Functions, Comparators, and Specialized Data Structures in C++

## Table of Contents
1. [Introduction](#introduction)
2. [Theoretical Foundations](#theoretical-foundations)
   - [Hash Functions](#hash-functions)
   - [Comparators](#comparators)
   - [Template Specialization](#template-specialization)
   - [Container Implementation Trade-offs](#container-implementation-trade-offs)
3. [Custom Hash Functions](#custom-hash-functions)
   - [The std::hash Template](#the-stdhash-template)
   - [Specializing std::hash for Custom Types](#specializing-stdhash-for-custom-types)
   - [Implementation Example](#implementation-example)
4. [Custom Comparators](#custom-comparators)
   - [Design Patterns for Multiple Comparison Criteria](#design-patterns-for-multiple-comparison-criteria)
   - [Implementing Comparison Classes](#implementing-comparison-classes)
5. [Hash-Based Data Structures](#hash-based-data-structures)
   - [std::unordered_set and std::unordered_map](#stdunordered_set-and-stdunordered_map)
   - [Implementing Custom Hash-Based Containers](#implementing-custom-hash-based-containers)
6. [Tree-Based Data Structures](#tree-based-data-structures)
   - [AVL Trees Fundamentals](#avl-trees-fundamentals)
   - [Implementing AVL Trees with Custom Comparators](#implementing-avl-trees-with-custom-comparators)
   - [Efficient Query Operations](#efficient-query-operations)
7. [Performance Analysis](#performance-analysis)
   - [Benchmarking Methodology](#benchmarking-methodology)
   - [Time Complexity Analysis](#time-complexity-analysis)
   - [Space Complexity Analysis](#space-complexity-analysis)
   - [Empirical Performance Testing](#empirical-performance-testing)
8. [Advanced Topics](#advanced-topics)
   - [Fine-tuning Hash Functions](#fine-tuning-hash-functions)
   - [Balancing in Tree-Based Structures](#balancing-in-tree-based-structures)
   - [Memory Layout Considerations](#memory-layout-considerations)
9. [Conclusion](#conclusion)
   - [When to Use Each Data Structure](#when-to-use-each-data-structure)
   - [Design Patterns for Extensible Class Hierarchies](#design-patterns-for-extensible-class-hierarchies)
10. [References](#references)

## Introduction

Modern C++ programming heavily relies on data structures that efficiently store, retrieve, and manage collections of objects. The Standard Template Library (STL) provides a rich set of containers, but many scenarios require custom behavior specific to user-defined types. This tutorial explores how to implement custom hash functions, comparators, and specialized data structures to optimize performance for specific use cases.

We'll begin with theoretical foundations, then proceed to practical implementations, and conclude with performance analyses to guide your selection of appropriate data structures for various scenarios.

## Theoretical Foundations

### Hash Functions

Hash functions transform data of arbitrary size into fixed-size values, typically integers, which serve as indices or keys in hash-based data structures. An ideal hash function has several properties:

- **Determinism**: The same input always produces the same output
- **Uniformity**: Output values are distributed evenly across the output range
- **Efficiency**: The computation is fast
- **Avalanche effect**: Small changes in input produce large changes in output

Hash functions enable O(1) average-case lookup, insertion, and deletion operations in hash tables, compared to O(log n) operations in tree-based structures or O(n) operations in linear collections.

![Hash Function Visualization](https://i.imgur.com/hash_function_diagram.png)

*Figure 1: Hash function transforming objects into hash codes*

### Comparators

Comparators define ordering relationships between objects, enabling algorithms and data structures to:

- Compare objects for equality
- Sort collections
- Search efficiently in ordered collections
- Establish ranges for queries

In C++, comparators can be:

1. **Comparison operators**: Overloaded operators like `<`, `==`, etc.
2. **Function objects (functors)**: Classes with overloaded `operator()`
3. **Lambda expressions**: Anonymous functions that capture context
4. **Function pointers**: References to standalone comparison functions

The STL uses comparators extensively, particularly in ordered containers like `std::set` and `std::map`.

### Template Specialization

Template specialization allows programmers to provide custom implementations for specific template parameter types. This mechanism is critical for:

- Optimizing performance for specific types
- Providing type-specific behavior while maintaining a generic interface
- Implementing exception handling for edge cases

The syntax for template specialization involves:

```cpp
// General template
template <typename T>
class Processor {
    // General implementation
};

// Specialization for a specific type
template <>
class Processor<MyCustomType> {
    // Specialized implementation
};
```

Template specialization is used extensively in hash function implementations, allowing the standard library to handle built-in types efficiently while enabling programmers to extend functionality for custom types.

### Container Implementation Trade-offs

Various container implementations offer different performance characteristics:

| Container Type | Lookup | Insertion | Deletion | Memory Overhead | Ordered? |
|----------------|--------|-----------|----------|----------------|----------|
| Vector | O(n) | O(1)* | O(n) | Low | No |
| List | O(n) | O(1) | O(1)** | High | No |
| Hash Table | O(1)*** | O(1)*** | O(1)*** | Medium | No |
| BST | O(log n) | O(log n) | O(log n) | Medium | Yes |
| AVL Tree | O(log n) | O(log n) | O(log n) | Medium | Yes |

\* Amortized when resizing isn't required  
\** With iterator  
\*** Average case, can degrade to O(n) in worst case  

The choice of container depends on:
- Access patterns (frequent lookups vs. frequent modifications)
- Memory constraints
- Need for ordered iteration
- Specific operation frequency

## Custom Hash Functions

### The std::hash Template

The C++ standard library defines `std::hash` as a template function object in the `<functional>` header:

```cpp
namespace std {
    template <class Key>
    struct hash;
}
```

The standard provides specializations for basic types like integers, floating-point numbers, pointers, and string types. For user-defined types, you must provide your own specialization.

### Specializing std::hash for Custom Types

To make a custom type usable with unordered containers like `std::unordered_set` or `std::unordered_map`, you must specialize `std::hash` for that type.

Steps to specialize `std::hash`:

1. Define a specialization of `std::hash` in the `std` namespace
2. Implement the `operator()` function that computes the hash
3. Make it callable with your type and return a `size_t`

The general pattern is:

```cpp
namespace std {
    template <>
    struct hash<MyType> {
        size_t operator()(const MyType& obj) const {
            // Hash computation logic here
            return result;
        }
    };
}
```

### Implementation Example

Let's look at a complete example for a custom `Item` class:

```cpp
#include <functional>
#include <string>
#include <iostream>
#include <unordered_set>

// Our custom Item class
class Item {
private:
    std::string name_;
    float weight_;
    int type_;

public:
    Item(const std::string& name, float weight, int type)
        : name_(name), weight_(weight), type_(type) {}
    
    // Accessor methods
    const std::string& getName() const { return name_; }
    float getWeight() const { return weight_; }
    int getType() const { return type_; }

    // Equality operator for hash table comparisons
    bool operator==(const Item& other) const {
        return name_ == other.name_;
    }
};

// Specializing std::hash for Item
namespace std {
    template <>
    struct hash<Item> {
        /**
         * @brief Computes a hash value for an Item based on
         * using the standard hash for strings on the Item's name
         *
         * @param i The Item to hash
         * @return Hash value for the Item
        */
        size_t operator()(const Item& i) const {
            return std::hash<std::string>()(i.getName());
        }
    };
}

int main() {
    // Now we can use Item with unordered_set
    std::unordered_set<Item> items;
    items.insert(Item("Sword", 5.2, 1));
    items.insert(Item("Shield", 8.7, 2));
    
    // Check if an item exists
    auto item = Item("Sword", 0.0, 0);  // Only name matters for hash and equality
    if (items.find(item) != items.end()) {
        std::cout << "Item found!" << std::endl;
    }
    
    return 0;
}
```

In this example, we've specialized `std::hash<Item>` to use the hash of the item's name. This works because:

1. Our equality comparison (`operator==`) is based solely on the name
2. The hash is consistent with the equality comparison
3. The name is a string, which already has a standard hash implementation

## Custom Comparators

### Design Patterns for Multiple Comparison Criteria

Objects often have multiple properties that can serve as comparison criteria. Common design patterns for handling multiple comparison criteria include:

1. **Static Comparator Classes**: Classes with static methods for different comparison operations
2. **Strategy Pattern**: Swappable comparison objects
3. **Policy-Based Design**: Template parameters that define comparison behavior
4. **Functors with Configuration**: Configurable comparison objects

Let's implement the first approach - static comparator classes:

### Implementing Comparison Classes

For our `Item` class, we'll create three comparator classes:

```cpp
// Comparator for Item names
class CompareItemName {
public:
    // Less than comparison
    static bool lessThan(const Item& a, const Item& b) {
        return a.getName() < b.getName();
    }
    
    // Equality comparison
    static bool equal(const Item& a, const Item& b) {
        return a.getName() == b.getName();
    }
    
    // Less than or equal comparison
    static bool leq(const Item& a, const Item& b) {
        return a.getName() <= b.getName();
    }
};

// Comparator for Item weights
class CompareItemWeight {
public:
    static bool lessThan(const Item& a, const Item& b) {
        return a.getWeight() < b.getWeight();
    }
    
    static bool equal(const Item& a, const Item& b) {
        return a.getWeight() == b.getWeight();
    }
    
    static bool leq(const Item& a, const Item& b) {
        return a.getWeight() <= b.getWeight();
    }
};

// Comparator for Item types
class CompareItemType {
public:
    static bool lessThan(const Item& a, const Item& b) {
        return a.getType() < b.getType();
    }
    
    static bool equal(const Item& a, const Item& b) {
        return a.getType() == b.getType();
    }
    
    static bool leq(const Item& a, const Item& b) {
        return a.getType() <= b.getType();
    }
};
```

With these comparator classes, we can now compare items in different ways:

```cpp
Item sword("Sword", 5.2, 1);
Item shield("Shield", 8.7, 2);

// Compare by name
bool nameOrder = CompareItemName::lessThan(sword, shield);  // true: "Sword" < "Shield"

// Compare by weight
bool weightOrder = CompareItemWeight::lessThan(sword, shield);  // true: 5.2 < 8.7

// Compare by type
bool typeOrder = CompareItemType::lessThan(sword, shield);  // true: 1 < 2
```

These comparator classes will be instrumental when we implement specialized container classes that need to order or query items based on different criteria.

## Hash-Based Data Structures

### std::unordered_set and std::unordered_map

The C++ Standard Library provides hash-based containers:

- `std::unordered_set`: Collection of unique keys
- `std::unordered_map`: Collection of key-value pairs

These containers use hash tables internally, offering average O(1) complexity for insertions, deletions, and lookups.

To use custom types with these containers, you need:
1. A hash function via `std::hash` specialization
2. An equality comparison via `operator==`

### Implementing Custom Hash-Based Containers

While the standard containers are suitable for most purposes, you might want to create specialized containers with additional functionality. Let's implement a custom `HashInventory` class that uses `std::unordered_set` internally:

```cpp
#include <unordered_set>
#include <string>

template <typename Comparator>
class HashInventory {
private:
    std::unordered_set<Item> items_;
    Item* equipped_;
    float weight_;
    size_t item_count_;

public:
    // Constructor
    HashInventory() : equipped_(nullptr), weight_(0), item_count_(0) {}
    
    // Destructor
    ~HashInventory() {
        if (equipped_) {
            delete equipped_;
        }
    }
    
    // Get equipped item
    Item* getEquipped() const {
        return equipped_;
    }
    
    // Equip an item
    void equip(Item* itemToEquip) {
        equipped_ = itemToEquip;
    }
    
    // Discard equipped item
    void discardEquipped() {
        if (equipped_) {
            delete equipped_;
            equipped_ = nullptr;
        }
    }
    
    // Get total weight
    float getWeight() const {
        return weight_;
    }
    
    // Get number of items
    size_t size() const {
        return item_count_;
    }
    
    // Get all items
    std::unordered_set<Item> getItems() const {
        return items_;
    }
    
    // Add an item
    bool pickup(const Item& target) {
        // Check if item with the same name already exists
        if (contains(target.getName())) {
            return false;
        }
        
        // Add item and update metadata
        auto result = items_.insert(target);
        if (result.second) {
            weight_ += target.getWeight();
            item_count_++;
            return true;
        }
        return false;
    }
    
    // Remove an item by name
    bool discard(const std::string& itemName) {
        // Find the item with the given name
        for (auto it = items_.begin(); it != items_.end(); ++it) {
            if (it->getName() == itemName) {
                weight_ -= it->getWeight();
                items_.erase(it);
                item_count_--;
                return true;
            }
        }
        return false;
    }
    
    // Check if an item exists by name
    bool contains(const std::string& itemName) const {
        for (const auto& item : items_) {
            if (item.getName() == itemName) {
                return true;
            }
        }
        return false;
    }
    
    // Query items in a range
    std::unordered_set<Item> query(const Item& start, const Item& end) const {
        std::unordered_set<Item> result;
        
        // Check if end is less than start according to the comparator
        if (Comparator::lessThan(end, start)) {
            return result;  // Empty set
        }
        
        // Iterate through all items
        for (const auto& item : items_) {
            // Include the item if it's in the specified range
            if ((Comparator::leq(start, item) && Comparator::leq(item, end))) {
                result.insert(item);
            }
        }
        
        return result;
    }
};
```

This `HashInventory` implementation:
- Stores items in a hash-based set
- Supports equipped item functionality
- Tracks inventory weight and item count
- Provides efficient item lookup by name
- Supports range-based queries using the specified comparator

The `query` method searches through all items, which is O(n) time complexity. This is unavoidable with a hash-based structure since hash tables do not maintain any ordering. For more efficient range queries, we'll need tree-based structures.

## Tree-Based Data Structures

### AVL Trees Fundamentals

AVL trees are self-balancing binary search trees where the heights of the two child subtrees of any node differ by at most one. This balancing ensures O(log n) time complexity for operations like insertion, deletion, and lookup.

Key properties of AVL trees:
- Nodes store a balance factor (difference in height between left and right subtrees)
- Insertions and deletions might require rotations to maintain balance
- The ordering is determined by a comparison function

The balancing process involves four types of rotations:
1. Left rotation
2. Right rotation
3. Left-Right rotation (double rotation)
4. Right-Left rotation (double rotation)

![AVL Tree Rotations](https://i.imgur.com/avl_tree_rotations.png)

*Figure 2: AVL tree rotations to maintain balance*

### Implementing AVL Trees with Custom Comparators

Let's implement an `ItemAVL` tree that uses our custom comparators:

```cpp
template <typename Comparator>
class ItemAVL {
private:
    struct Node {
        Item data;
        Node* left;
        Node* right;
        int height;
        
        Node(const Item& item) 
            : data(item), left(nullptr), right(nullptr), height(1) {}
    };
    
    Node* root_;
    size_t size_;
    
    // Helper function to get height of a node
    int height(Node* node) const {
        if (node == nullptr) return 0;
        return node->height;
    }
    
    // Helper function to get balance factor
    int getBalance(Node* node) const {
        if (node == nullptr) return 0;
        return height(node->left) - height(node->right);
    }
    
    // Helper function to update node height
    void updateHeight(Node* node) {
        if (node == nullptr) return;
        node->height = 1 + std::max(height(node->left), height(node->right));
    }
    
    // Right rotation
    Node* rightRotate(Node* y) {
        Node* x = y->left;
        Node* T2 = x->right;
        
        // Perform rotation
        x->right = y;
        y->left = T2;
        
        // Update heights
        updateHeight(y);
        updateHeight(x);
        
        return x;
    }
    
    // Left rotation
    Node* leftRotate(Node* x) {
        Node* y = x->right;
        Node* T2 = y->left;
        
        // Perform rotation
        y->left = x;
        x->right = T2;
        
        // Update heights
        updateHeight(x);
        updateHeight(y);
        
        return y;
    }
    
    // Helper function to insert a node
    Node* insertNode(Node* node, const Item& item) {
        // 1. Standard BST insertion
        if (node == nullptr) {
            size_++;
            return new Node(item);
        }
        
        // Check for duplicate name
        if (node->data.getName() == item.getName()) {
            return node;  // Do not insert duplicate items
        }
        
        // Recursive insertion based on comparator
        if (Comparator::lessThan(item, node->data)) {
            node->left = insertNode(node->left, item);
        } else if (Comparator::lessThan(node->data, item)) {
            node->right = insertNode(node->right, item);
        } else {
            return node;  // Equal items not inserted
        }
        
        // 2. Update height of current node
        updateHeight(node);
        
        // 3. Get balance factor
        int balance = getBalance(node);
        
        // 4. Rotations to rebalance if needed
        
        // Left Left Case
        if (balance > 1 && Comparator::lessThan(item, node->left->data)) {
            return rightRotate(node);
        }
        
        // Right Right Case
        if (balance < -1 && Comparator::lessThan(node->data, item)) {
            return leftRotate(node);
        }
        
        // Left Right Case
        if (balance > 1 && Comparator::lessThan(node->left->data, item)) {
            node->left = leftRotate(node->left);
            return rightRotate(node);
        }
        
        // Right Left Case
        if (balance < -1 && Comparator::lessThan(item, node->right->data)) {
            node->right = rightRotate(node->right);
            return leftRotate(node);
        }
        
        return node;
    }
    
    // Helper function to check if a subtree contains an item with a given name
    bool contains(const std::string& name, const Node* subroot) const {
        if (subroot == nullptr) {
            return false;
        }
        
        if (subroot->data.getName() == name) {
            return true;
        }
        
        // Since we're searching by name, we need to search both subtrees
        return contains(name, subroot->left) || contains(name, subroot->right);
    }
    
    // Helper function for range queries
    void queryHelper(const Item& start, const Item& end, const Node* root, 
                    std::unordered_set<Item>& result) const {
        if (root == nullptr) {
            return;
        }
        
        // Check if current node's item is in range
        if (Comparator::leq(start, root->data) && Comparator::leq(root->data, end)) {
            result.insert(root->data);
        }
        
        // If start is less than current item, search left subtree
        if (Comparator::lessThan(start, root->data)) {
            queryHelper(start, end, root->left, result);
        }
        
        // If end is greater than current item, search right subtree
        if (Comparator::lessThan(root->data, end)) {
            queryHelper(start, end, root->right, result);
        }
    }
    
    // Helper function to free memory
    void destroyTree(Node* node) {
        if (node) {
            destroyTree(node->left);
            destroyTree(node->right);
            delete node;
        }
    }
    
public:
    // Constructor
    ItemAVL() : root_(nullptr), size_(0) {}
    
    // Destructor
    ~ItemAVL() {
        destroyTree(root_);
    }
    
    // Insert an item
    bool insert(const Item& item) {
        size_t oldSize = size_;
        root_ = insertNode(root_, item);
        return size_ > oldSize;
    }
    
    // Get number of items
    size_t size() const {
        return size_;
    }
    
    // Check if an item with the given name exists
    bool contains(const std::string& name) const {
        return contains(name, root_);
    }
    
    // Query items in a range
    std::unordered_set<Item> query(const Item& start, const Item& end) const {
        std::unordered_set<Item> result;
        
        if (Comparator::lessThan(end, start)) {
            return result;  // Empty set
        }
        
        queryHelper(start, end, root_, result);
        return result;
    }
};
```

This implementation:
- Uses the specified `Comparator` for tree ordering
- Maintains AVL balance through rotations
- Provides O(log n) insertion
- Checks for duplicate names during insertion
- Implements range queries using the balanced tree structure

### Efficient Query Operations

The key advantage of tree-based structures for range queries is that we don't need to examine all nodes. The `queryHelper` method uses the tree ordering to prune the search:

1. If the current node's item is in the range, add it to the result
2. Only search the left subtree if the `start` item is less than the current node's item
3. Only search the right subtree if the `end` item is greater than the current node's item

This pruning makes range queries O(log n + k) where k is the number of items in the range, versus O(n) for hash-based containers.

## Performance Analysis

### Benchmarking Methodology

To accurately compare container implementations, we need a systematic benchmarking approach:

1. **Preparation**:
   - Use a consistent set of test data
   - Ensure comparable initial states
   - Warm up the system to minimize external factors

2. **Measurement**:
   - Time individual operations
   - Run multiple iterations to account for variability
   - Calculate average and variance

3. **Analysis**:
   - Compare against theoretical complexity bounds
   - Identify inflection points where different containers excel
   - Analyze scaling behavior as n increases

Let's implement a benchmarking framework:

```cpp
#include <chrono>
#include <vector>
#include <string>
#include <functional>
#include <iostream>
#include <iomanip>

// Utility class for timing operations
class Timer {
private:
    std::chrono::high_resolution_clock::time_point start_time;
    
public:
    void start() {
        start_time = std::chrono::high_resolution_clock::now();
    }
    
    double elapsedMilliseconds() {
        auto end_time = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time);
        return duration.count() / 1000.0;
    }
};

// Class for generating test items
class ItemGenerator {
private:
    unsigned int seed_;
    std::vector<std::string> used_names_;
    
public:
    ItemGenerator(unsigned int seed) : seed_(seed) {
        srand(seed);
    }
    
    Item randomItem() {
        std::string name = "Item" + std::to_string(rand() % 10000000);
        float weight = 0.1f + (rand() % 1000) / 10.0f;
        int type = rand() % 4;
        
        used_names_.push_back(name);
        return Item(name, weight, type);
    }
    
    std::string randomUsedName() {
        if (used_names_.empty()) return "";
        return used_names_[rand() % used_names_.size()];
    }
};

// Template function to benchmark contains() operation
template <typename InventoryType>
double benchmarkContains(InventoryType& inventory, const std::vector<std::string>& contained, 
                         const std::vector<std::string>& missing) {
    Timer timer;
    double total_time = 0.0;
    
    // Test for items that should be found
    for (const auto& name : contained) {
        timer.start();
        inventory.contains(name);
        total_time += timer.elapsedMilliseconds();
    }
    
    // Test for items that should not be found
    for (const auto& name : missing) {
        timer.start();
        inventory.contains(name);
        total_time += timer.elapsedMilliseconds();
    }
    
    // Return average time
    return total_time / (contained.size() + missing.size());
}

// Template function to benchmark query() operation
template <typename InventoryType, typename Comparator>
double benchmarkQuery(InventoryType& inventory, ItemGenerator& generator) {
    Timer timer;
    double total_time = 0.0;
    
    // Perform multiple query operations
    for (int i = 0; i < 10; i++) {
        // Create two items to define the query range
        std::string name1 = generator.randomUsedName();
        std::string name2 = generator.randomUsedName();
        
        Item start(name1, 0, 0);
        Item end(name2, 0, 0);
        
        // Ensure start <= end according to the comparator
        if (Comparator::lessThan(end, start)) {
            std::swap(start, end);
        }
        
        // Time the query operation
        timer.start();
        auto result = inventory.query(start, end);
        total_time += timer.elapsedMilliseconds();
    }
    
    // Return average time
    return total_time / 10.0;
}

// Run benchmarks for different inventory sizes
template <template<typename, typename...> class InventoryType, typename Comparator, typename... Args>
void runBenchmarks() {
    std::vector<int> sizes = {1000, 2000, 4000, 8000};
    
    std::cout << "| Container | Size | contains() (ms) | query() (ms) |\n";
    std::cout << "|-----------|------|----------------|-------------|\n";
    
    for (int n : sizes) {
        // Create and populate inventory
        InventoryType<Comparator, Args...> inventory;
        ItemGenerator generator(42);  // Consistent seed for reproducibility
        
        // Generate and store items
        for (int i = 0; i < n; i++) {
            inventory.pickup(generator.randomItem());
        }
        
        // Prepare test data
        std::vector<std::string> contained;
        std::vector<std::string> missing;
        
        // Generate 100 names that should be in the inventory
        for (int i = 0; i < 100; i++) {
            contained.push_back(generator.randomUsedName());
        }
        
        // Generate 100 names that should not be in the inventory
        for (int i = 0; i < 100; i++) {
            missing.push_back("Missing" + std::to_string(i));
        }
        
        // Run benchmarks
        double contains_time = benchmarkContains(inventory, contained, missing);
        double query_time = benchmarkQuery<InventoryType<Comparator, Args...>, Comparator>(inventory, generator);
        
        // Print results
        std::cout << "| " << typeid(InventoryType<Comparator, Args...>).name() 
                  << " | " << n 
                  << " | " << std::fixed << std::setprecision(6) << contains_time 
                  << " | " << std::fixed << std::setprecision(6) << query_time 
                  << " |\n";
    }
}
```

### Time Complexity Analysis

Based on our implementations, here's a theoretical analysis of time complexity:

| Container | contains() | query() | pickup() | discard() |
|-----------|------------|---------|----------|-----------|
| Inventory (vector) | O(n) | O(n) | O(n) | O(n) |
| Inventory (list) | O(n) | O(n) | O(n) | O(n) |
| HashInventory | O(1)* | O(n) | O(1)* | O(1)* |
| TreeInventory | O(log n)** | O(log n + k) | O(log n) | O(log n) |

\* Average case, can degrade to O(n) in worst case  
\** When using CompareItemName, otherwise O(n)  
k = number of items in the query range

The key observations:
1. Hash-based structures excel at individual item operations but not range queries
2. Tree-based structures provide good performance across all operations
3. Linear