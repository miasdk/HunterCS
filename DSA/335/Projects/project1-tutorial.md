# Mastering C++ Move Semantics: An MMORPG Character System Implementation

## Table of Contents
- [1. Theoretical Foundations](#1-theoretical-foundations)
  - [1.1. Resource Ownership in C++](#11-resource-ownership-in-c)
  - [1.2. Move Semantics vs. Copy Semantics](#12-move-semantics-vs-copy-semantics)
  - [1.3. The Rule of Five](#13-the-rule-of-five)
  - [1.4. Performance Benefits of Move Operations](#14-performance-benefits-of-move-operations)
  - [1.5. Nested Object Hierarchies](#15-nested-object-hierarchies)
- [2. Core Concepts](#2-core-concepts)
  - [2.1. Understanding std::move](#21-understanding-stdmove)
  - [2.2. R-value References](#22-r-value-references)
  - [2.3. Deep vs. Shallow Copying](#23-deep-vs-shallow-copying)
  - [2.4. Resource Acquisition and Release Patterns](#24-resource-acquisition-and-release-patterns)
  - [2.5. Move Constructors and Move Assignment Operators](#25-move-constructors-and-move-assignment-operators)
  - [2.6. Dynamic Memory Management](#26-dynamic-memory-management)
- [3. Implementation Guide: MMORPG Character System](#3-implementation-guide-mmorpg-character-system)
  - [3.1. Creating an Item Class](#31-creating-an-item-class)
  - [3.2. Implementing the Inventory Class](#32-implementing-the-inventory-class)
  - [3.3. Developing the Player Class](#33-developing-the-player-class)
  - [3.4. Testing Move Operations](#34-testing-move-operations)
  - [3.5. Common Pitfalls and Solutions](#35-common-pitfalls-and-solutions)
- [4. Complete Code Examples](#4-complete-code-examples)
  - [4.1. Item Class Implementation](#41-item-class-implementation)
  - [4.2. Inventory Class Implementation](#42-inventory-class-implementation)
  - [4.3. Player Class Implementation](#43-player-class-implementation)
  - [4.4. Test Scenarios](#44-test-scenarios)
- [5. Visual Explanations](#5-visual-explanations)
  - [5.1. Memory Layout During Move Operations](#51-memory-layout-during-move-operations)
  - [5.2. Object Hierarchy Diagrams](#52-object-hierarchy-diagrams)
  - [5.3. State Transitions](#53-state-transitions)
  - [5.4. Performance Comparisons](#54-performance-comparisons)
- [6. Academic Context](#6-academic-context)
  - [6.1. Historical Evolution of Memory Management in C++](#61-historical-evolution-of-memory-management-in-c)
  - [6.2. Impact of Move Semantics on C++ Programming](#62-impact-of-move-semantics-on-c-programming)
  - [6.3. Resource Management Design Patterns](#63-resource-management-design-patterns)
  - [6.4. Best Practices for Class Hierarchies](#64-best-practices-for-class-hierarchies)
  - [6.5. Advanced Topics: Perfect Forwarding and Universal References](#65-advanced-topics-perfect-forwarding-and-universal-references)
- [7. Conclusion](#7-conclusion)
- [8. References](#8-references)

## 1. Theoretical Foundations

### 1.1. Resource Ownership in C++

In C++, resource ownership is a fundamental concept that dictates how objects manage and maintain access to finite system resources such as memory, file handles, network connections, and database connections. Unlike garbage-collected languages where memory management is largely automated, C++ gives programmers direct control over the lifecycle of resources, making explicit the question: *which object owns a particular resource at any given time?*

Resource ownership in C++ follows several key principles:

1. **Exclusive ownership**: In most cases, a resource should have exactly one owner at any given time.
2. **Lifetime management**: The owner is responsible for properly releasing the resource when it's no longer needed.
3. **Ownership transfer**: Ownership can be transferred from one object to another, either through copying (creating a duplicate resource) or moving (transferring the original resource).
4. **Resource safety**: The programming model should prevent resource leaks, dangling pointers, and double-free errors.

In our MMORPG example, consider a magical sword with unique properties. In the game world, this sword can only be in one inventory at a time. If a player gives this sword to another player, the first player no longer has it. This real-world ownership model aligns perfectly with C++ move semantics.

#### Why Resource Ownership Matters

Proper resource management is critical in C++ for several reasons:

- **Memory leaks**: Failing to release memory leads to resource exhaustion over time.
- **Performance**: Unnecessary copying of large resources impacts performance.
- **Correctness**: Dangling pointers and use-after-free bugs cause unpredictable behavior.
- **Scalability**: In an MMORPG, efficient resource management directly impacts how many players the system can support.

The evolution of resource management in C++ has progressed from manual memory management (malloc/free), to RAII (Resource Acquisition Is Initialization), to smart pointers, and finally to move semantics—each step improving safety and expressiveness.

### 1.2. Move Semantics vs. Copy Semantics

Before C++11, transferring objects primarily relied on copy semantics, which creates a duplicate of the source object. While straightforward, this approach has significant drawbacks, especially for resource-heavy objects like our game inventory that might contain hundreds of items.

#### Copy Semantics

Copy semantics involve:

1. **Deep copying**: Creating a duplicate of all resources owned by the source object.
2. **Resource duplication**: Allocating new memory for the target object.
3. **Value preservation**: After the operation, both source and target objects contain independent, equivalent resources.

```cpp
Inventory inventory1;
// Fill inventory1 with items...
Inventory inventory2 = inventory1;  // Copy constructor makes a complete duplicate
inventory1.addItem(sword);          // Only affects inventory1
```

#### Move Semantics

Move semantics, introduced in C++11, operate on a fundamentally different principle:

1. **Resource transfer**: Taking ownership of resources from the source object.
2. **No duplication**: Avoiding new memory allocation when possible.
3. **Source invalidation**: After the move, the source object is left in a valid but unspecified state (typically empty or "null").

```cpp
Inventory inventory1;
// Fill inventory1 with items...
Inventory inventory2 = std::move(inventory1);  // Move constructor transfers ownership
// inventory1 is now empty, inventory2 contains all the items
```

#### Key Differences

| Aspect | Copy Semantics | Move Semantics |
|--------|---------------|----------------|
| Performance | O(n) - proportional to object size | O(1) - typically constant time |
| Memory Usage | Duplicates resources | Reuses existing resources |
| Source Object After Operation | Unchanged | Empty or reset state |
| Use Case | When a duplicate is needed | When the source object is no longer needed |
| Implementation | Copy constructor, copy assignment | Move constructor, move assignment |

In our MMORPG context, when a player character hands an entire backpack to another character, it makes more sense to transfer ownership (move) rather than magically duplicate all contents (copy).

### 1.3. The Rule of Five

The "Rule of Five" (an evolution of the older "Rule of Three") states that if a class requires custom implementation of any of the following special member functions, it probably needs all five:

1. **Destructor**: Cleans up resources when an object is destroyed.
2. **Copy constructor**: Creates a new object as a copy of an existing one.
3. **Copy assignment operator**: Replaces the contents of an object with a copy of another.
4. **Move constructor**: Creates a new object by transferring resources from an existing one.
5. **Move assignment operator**: Replaces the contents of an object by transferring resources from another.

For a class managing resources like our `Inventory` class, implementing all five ensures consistent behavior regardless of how objects are created, destroyed, or transferred.

#### Destructor

The destructor releases resources owned by the object:

```cpp
~Inventory() {
    // Free all dynamically allocated items
    for (auto* item : items_) {
        delete item;
    }
}
```

#### Copy Constructor

The copy constructor creates a deep copy of another object:

```cpp
Inventory(const Inventory& other) {
    // Create new copies of all items in other
    items_.reserve(other.items_.size());
    for (const auto* item : other.items_) {
        items_.push_back(new Item(*item));  // Create a copy of each item
    }
}
```

#### Copy Assignment Operator

The copy assignment operator overwrites the current object with a deep copy:

```cpp
Inventory& operator=(const Inventory& other) {
    if (this != &other) {  // Protect against self-assignment
        // Clean up existing resources
        for (auto* item : items_) {
            delete item;
        }
        items_.clear();
        
        // Copy resources from other
        items_.reserve(other.items_.size());
        for (const auto* item : other.items_) {
            items_.push_back(new Item(*item));
        }
    }
    return *this;
}
```

#### Move Constructor

The move constructor transfers resources from another object:

```cpp
Inventory(Inventory&& other) noexcept {
    // Transfer ownership of resources
    items_ = std::move(other.items_);
    // Leave other in a valid but empty state
    // (std::vector already handles this for us)
}
```

#### Move Assignment Operator

The move assignment operator transfers resources from another object:

```cpp
Inventory& operator=(Inventory&& other) noexcept {
    if (this != &other) {  // Protect against self-assignment
        // Clean up existing resources
        for (auto* item : items_) {
            delete item;
        }
        
        // Transfer ownership of resources
        items_ = std::move(other.items_);
    }
    return *this;
}
```

When implementing the Rule of Five, consider:

- Mark move operations as `noexcept` to enable optimizations
- Handle self-assignment in assignment operators
- Ensure the moved-from object is left in a valid state
- Maintain class invariants in all operations

### 1.4. Performance Benefits of Move Operations

Move semantics provide significant performance advantages over copying, especially for resource-intensive objects. Let's examine these benefits in the context of our MMORPG character system.

#### Memory Allocation Costs

Memory allocation is expensive due to:
- System calls to the memory manager
- Potential fragmentation
- Thread synchronization in multithreaded environments
- Cache invalidation

When moving large objects like a player inventory with hundreds of items, we avoid these costs entirely by reusing already allocated memory.

#### Runtime Performance

Consider an inventory with 1000 items, each with various properties:

| Operation | Copy | Move |
|-----------|------|------|
| Memory Allocations | 1000+ | 0 |
| Memory Copies | ~1000 × size of Item | ~1 pointer copy |
| Approximate Time Cost | O(n) | O(1) |

In practical terms, this might be the difference between an operation taking milliseconds versus microseconds—critical in a real-time game environment where performance stutters break immersion.

#### Example Comparison

```cpp
// Measuring copy vs move for a large inventory
#include <chrono>

void performanceTest() {
    // Create an inventory with 10,000 items
    Inventory largeInventory;
    for (int i = 0; i < 10000; ++i) {
        largeInventory.addItem(new Item("Item" + std::to_string(i)));
    }
    
    // Measure copy time
    auto copyStart = std::chrono::high_resolution_clock::now();
    Inventory copiedInventory = largeInventory;  // Copy constructor
    auto copyEnd = std::chrono::high_resolution_clock::now();
    
    // Measure move time
    auto moveStart = std::chrono::high_resolution_clock::now();
    Inventory movedInventory = std::move(largeInventory);  // Move constructor
    auto moveEnd = std::chrono::high_resolution_clock::now();
    
    std::chrono::duration<double, std::milli> copyTime = copyEnd - copyStart;
    std::chrono::duration<double, std::milli> moveTime = moveEnd - moveStart;
    
    std::cout << "Copy time: " << copyTime.count() << " ms\n";
    std::cout << "Move time: " << moveTime.count() << " ms\n";
    std::cout << "Speedup factor: " << copyTime.count() / moveTime.count() << "x\n";
}
```

Typical results might show the move operation completing 100-1000x faster than the copy operation, depending on the size and complexity of the inventory items.

### 1.5. Nested Object Hierarchies

In complex systems like an MMORPG, objects naturally form hierarchies. A `Player` contains an `Inventory`, which contains multiple `Item` objects, which might contain `Enchantment` objects. This nesting creates unique challenges for resource management.

#### Resource Management Challenges in Hierarchies

1. **Ownership propagation**: When moving a `Player`, we must properly move its contained `Inventory`.
2. **Consistency maintenance**: All levels of the hierarchy must maintain their invariants during move operations.
3. **Resource tracking**: The system must track which resources belong to which objects.
4. **Circular references**: Care must be taken to avoid ownership cycles that could prevent proper cleanup.

#### Containment vs. Aggregation

In our MMORPG system, we have two primary relationships:

- **Containment** (composition): A strong ownership relationship where the container is responsible for the lifetime of the contained objects. Example: An `Inventory` owns its `Item` objects.
- **Aggregation**: A weaker relationship where objects are associated but have independent lifetimes. Example: A `Guild` has associated `Player` objects but doesn't own them.

Move semantics must respect these relationships. Moving a container should:
- Transfer ownership of contained objects (containment)
- Update, but not transfer ownership of, aggregated objects

#### Implementing Moves in Hierarchies

The key principle is recursive application of move semantics:

```cpp
// Player contains an Inventory through composition
class Player {
private:
    std::string name_;
    Inventory inventory_;
    // Other player attributes...

public:
    // Move constructor
    Player(Player&& other) noexcept
        : name_(std::move(other.name_)),
          inventory_(std::move(other.inventory_))  // Recursively moves the inventory
    {
        // other.name_ and other.inventory_ have been moved from
    }
    
    // Move assignment
    Player& operator=(Player&& other) noexcept {
        if (this != &other) {
            name_ = std::move(other.name_);
            inventory_ = std::move(other.inventory_);  // Recursively moves the inventory
        }
        return *this;
    }
};
```

The `Player`'s move operations automatically invoke the move operations of its members, creating a cascade of efficient resource transfers throughout the object hierarchy.

## 2. Core Concepts

### 2.1. Understanding std::move

`std::move` is perhaps the most misunderstood function in modern C++. Despite its name, it doesn't actually move anything—it's a cast that converts a value to an rvalue reference, enabling move semantics.

#### What std::move Really Does

```cpp
template <typename T>
typename std::remove_reference<T>::type&& move(T&& t) noexcept {
    return static_cast<typename std::remove_reference<T>::type&&>(t);
}
```

This seemingly complex function simply performs a cast that signals that an object may be "moved from"—allowing its resources to be transferred elsewhere.

#### When to Use std::move

Use `std::move` when:

1. **Transferring ownership**: When you want to explicitly transfer resources from one object to another.
   ```cpp
   Inventory newInventory = std::move(oldInventory);  // oldInventory is emptied
   ```

2. **Returning by value**: When returning a local variable from a function.
   ```cpp
   Inventory createInventory() {
       Inventory result;
       // Set up result...
       return std::move(result);  // Actually unnecessary due to NRVO
   }
   ```
   
   Note: The compiler's Return Value Optimization (RVO) and Named Return Value Optimization (NRVO) often make explicit `std::move` unnecessary in return statements, and may even prevent these optimizations.

3. **Moving into containers**: When inserting objects into containers.
   ```cpp
   std::vector<Inventory> inventories;
   Inventory temp;
   // Set up temp...
   inventories.push_back(std::move(temp));  // Move temp into the vector
   ```

4. **Implementing move operations**: In move constructors and move assignment operators.
   ```cpp
   Player(Player&& other) noexcept
       : name_(std::move(other.name_)),
         inventory_(std::move(other.inventory_))
   {
       // Implementation...
   }
   ```

#### Common Mistakes with std::move

1. **Moving twice from the same object**: Once moved from, an object should not be moved from again without being reset.
   ```cpp
   auto dest1 = std::move(source);  // Correct
   auto dest2 = std::move(source);  // Incorrect: source already moved from
   ```

2. **Moving const objects**: Moving from const objects typically results in a copy.
   ```cpp
   const Inventory constInv;
   auto dest = std::move(constInv);  // This actually copies, not moves
   ```

3. **Moving what shouldn't be moved**: Primitive types, small objects with no resources, or objects that maintain state invariants that would be violated by moving.
   ```cpp
   int a = 5;
   int b = std::move(a);  // No benefit, just complicates code
   ```

4. **Assuming the moved-from state**: The standard only guarantees that moved-from objects are in a valid but unspecified state. Don't assume they're empty or reset unless the class specifically guarantees this.

### 2.2. R-value References

R-value references, introduced in C++11 and denoted with `&&`, are the foundation of move semantics. They provide a way to bind to temporary objects, enabling the distinction between "objects that can be moved from" and "objects that should be copied."

#### L-values vs. R-values

To understand r-value references, we must first understand the difference between l-values and r-values:

- **L-value**: An expression that has identity (can be addressed) and persists beyond a single expression. Typically, anything you can take the address of.
  ```cpp
  Inventory inv;           // inv is an l-value
  std::string& name = str;  // name is an l-value reference to str
  ```

- **R-value**: An expression that is temporary or ephemeral, typically on the right side of an assignment. Cannot be addressed and only exists during expression evaluation.
  ```cpp
  Inventory();                  // A temporary Inventory is an r-value
  std::move(inv);               // Result of std::move is an r-value
  getInventory();               // Return value is an r-value
  Inventory{};                  // Temporary object is an r-value
  ```

#### R-value References Explained

An r-value reference (`T&&`) is a reference type that can bind to r-values (temporaries) but not l-values. This distinction allows functions to detect when they're operating on temporary objects that can safely be moved from.

```cpp
void processInventory(Inventory& lvalRef) {
    // Called with l-values (normal objects)
    std::cout << "Processing lvalue inventory\n";
}

void processInventory(Inventory&& rvalRef) {
    // Called with r-values (temporaries or moved objects)
    std::cout << "Processing rvalue inventory\n";
    // Safe to move from rvalRef because it's a temporary
    Inventory newInv = std::move(rvalRef);
}

// Usage:
Inventory permanent;
processInventory(permanent);            // Calls first overload
processInventory(Inventory{});          // Calls second overload
processInventory(std::move(permanent)); // Calls second overload
```

#### Reference Collapsing Rules

When dealing with templates and r-value references, C++ follows reference collapsing rules:

- `T& &` → `T&`
- `T& &&` → `T&`
- `T&& &` → `T&`
- `T&& &&` → `T&&`

These rules are critical for understanding how universal references work in template functions.

#### Move Semantics and R-value References

The combination of r-value references and move semantics allows the compiler to choose the most efficient operations:

```cpp
// In std::vector implementation
void push_back(const T& value) {
    // Copy construction - called for l-values
}

void push_back(T&& value) {
    // Move construction - called for r-values
}

// Usage:
std::vector<Inventory> inventories;
Inventory inv1;
inventories.push_back(inv1);              // Calls first overload (copy)
inventories.push_back(Inventory{});       // Calls second overload (move)
inventories.push_back(std::move(inv1));   // Calls second overload (move)
```

This selective behavior enables substantial performance improvements without changing client code.

### 2.3. Deep vs. Shallow Copying

Understanding the difference between deep and shallow copying is crucial for proper resource management in C++, especially when implementing custom classes for an MMORPG character system.

#### Shallow Copying

Shallow copying copies only the direct members of an object, not the objects pointed to by pointers or references:

```cpp
class ShallowInventory {
private:
    Item** items_;  // Array of pointers to Items
    size_t capacity_;
    size_t size_;

public:
    // Shallow copy constructor (problematic!)
    ShallowInventory(const ShallowInventory& other)
        : capacity_(other.capacity_),
          size_(other.size_) 
    {
        items_ = new Item*[capacity_];
        
        // This only copies pointers, not the Items themselves!
        std::memcpy(items_, other.items_, size_ * sizeof(Item*));
    }
};
```

Problems with shallow copying:
1. **Double deletion**: Both objects will try to delete the same memory
2. **Dangling pointers**: If one object deletes memory, the other has invalid pointers
3. **Unexpected side effects**: Modifying one object affects the other
4. **Resource leaks**: If responsibility is unclear, resources may never be freed

In our MMORPG, shallow copying an inventory would mean two players referencing the same item objects—causing chaos if one player sells or modifies "their" items!

#### Deep Copying

Deep copying creates independent duplicates of all resources owned by an object:

```cpp
class DeepInventory {
private:
    Item** items_;  // Array of pointers to Items
    size_t capacity_;
    size_t size_;

public:
    // Deep copy constructor (correct approach)
    DeepInventory(const DeepInventory& other)
        : capacity_(other.capacity_),
          size_(other.size_) 
    {
        items_ = new Item*[capacity_];
        
        // Create new independent copies of each Item
        for (size_t i = 0; i < size_; ++i) {
            items_[i] = new Item(*other.items_[i]);  // Copy constructor of Item
        }
    }
};
```

Benefits of deep copying:
1. **Independence**: Objects don't interfere with each other
2. **Safety**: No dangling pointers or double deletions
3. **Predictable behavior**: Changes to one object don't affect others
4. **Clear ownership**: Each object manages its own resources

#### When to Use Each Approach

| Approach | Use When |
|----------|----------|
| Deep Copy | • Resources must be independent<br>• Objects have full ownership of their resources<br>• Changes should not propagate between copies |
| Shallow Copy | • Creating a temporary view of an object<br>• Implementing reference semantics<br>• Using shared ownership (managed by shared_ptr) |
| Move | • Resource transfer is more appropriate than copying<br>• Performance is critical<br>• Source object no longer needed |

In our MMORPG:
- **Deep copy**: When cloning an entire character or duplicating magical items
- **Shallow copy**: When implementing a temporary item preview
- **Move**: When transferring items between inventories or characters

#### Modern C++ Approach: Copy-on-Write

A hybrid approach gaining popularity is Copy-on-Write (CoW), where resources are shared until modification is required:

```cpp
class CoWString {
private:
    struct StringData {
        char* data;
        size_t size;
        size_t refCount;
    };
    
    StringData* data_;
    
    void detach() {
        if (data_->refCount > 1) {
            // Only make a copy if shared with other strings
            --data_->refCount;
            StringData* newData = new StringData{
                new char[data_->size + 1],
                data_->size,
                1
            };
            std::strcpy(newData->data, data_->data);
            data_ = newData;
        }
    }

public:
    // Methods that modify the string call detach() first
    void append(const char* str) {
        detach();  // Ensure we have our own copy before modifying
        // Append implementation...
    }
};
```

This approach combines the efficiency of shallow copying with the safety of deep copying, at the cost of some implementation complexity.

### 2.4. Resource Acquisition and Release Patterns

Proper resource management is critical in C++ to prevent memory leaks, double deletions, and dangling pointers. Several established patterns help ensure correct behavior.

#### RAII (Resource Acquisition Is Initialization)

RAII is a fundamental C++ idiom where resource acquisition occurs during object initialization, and resource release occurs during object destruction:

```cpp
class RAIIFile {
private:
    FILE* file_;

public:
    // Constructor acquires resource
    RAIIFile(const char* filename, const char* mode) {
        file_ = fopen(filename, mode);
        if (!file_) {
            throw std::runtime_error("Failed to open file");
        }
    }
    
    // Destructor releases resource
    ~RAIIFile() {
        if (file_) {
            fclose(file_);
        }
    }
    
    // Prevent copying to avoid double closure
    RAIIFile(const RAIIFile&) = delete;
    RAIIFile& operator=(const RAIIFile&) = delete;
    
    // Allow moving to transfer ownership
    RAIIFile(RAIIFile&& other) noexcept : file_(other.file_) {
        other.file_ = nullptr;  // Prevent double close
    }
    
    RAIIFile& operator=(RAIIFile&& other) noexcept {
        if (this != &other) {
            // Release current resource
            if (file_) {
                fclose(file_);
            }
            
            // Acquire other's resource
            file_ = other.file_;
            other.file_ = nullptr;  // Prevent double close
        }
        return *this;
    }
    
    // Operations on the file...
};
```

Benefits of RAII:
1. **Exception safety**: Resources are released even if exceptions occur
2. **Leak prevention**: Automatic cleanup when objects go out of scope
3. **Locality**: Acquisition and release logic contained in class definition
4. **Clarity**: Resource lifetime tied to well-defined object lifetime

#### Smart Pointers

Modern C++ provides smart pointers that implement RAII for dynamic memory:

1. **unique_ptr**: Exclusive ownership model, perfect for our MMORPG items
   ```cpp
   class ModernInventory {
   private:
       std::vector<std::unique_ptr<Item>> items_;
   
   public:
       // Add item (transfers ownership to the inventory)
       void addItem(std::unique_ptr<Item> item) {
           items_.push_back(std::move(item));  // Must use std::move
       }
       
       // Get item (transfers ownership from the inventory)
       std::unique_ptr<Item> removeItem(size_t index) {
           if (index >= items_.size()) {
               throw std::out_of_range("Invalid item index");
           }
           
           auto item = std::move(items_[index]);
           items_.erase(items_.begin() + index);
           return item;  // Ownership transferred to caller
       }
   };
   ```

2. **shared_ptr**: Shared ownership with reference counting
   ```cpp
   // For items that can be viewed in multiple places
   // but are logically owned by a single inventory
   class PreviewInventory {
   private:
       std::vector<std::shared_ptr<Item>> items_;
       
   public:
       // Allow "viewing" an item without transferring ownership
       std::shared_ptr<Item> getItemPreview(size_t index) {
           if (index >= items_.size()) {
               throw std::out_of_range("Invalid item index");
           }
           
           return items_[index];  // Returns a shared_ptr (increases ref count)
       }
   };
   ```

3. **weak_ptr**: Non-owning reference to shared objects
   ```cpp
   // For tracking cached or equipped items without affecting ownership
   class EquipmentManager {
   private:
       std::weak_ptr<Item> equippedWeapon_;
       
   public:
       void equipWeapon(std::shared_ptr<Item> weapon) {
           equippedWeapon_ = weapon;  // Doesn't increase reference count
       }
       
       void useWeapon() {
           if (auto weapon = equippedWeapon_.lock()) {  // Check if still valid
               weapon->use();
           } else {
               // Weapon no longer exists
               std::cout << "Weapon is no longer available\n";
           }
       }
   };
   ```

#### Custom Deleter Pattern

For resources that aren't memory or require special cleanup:

```cpp
class TextureResource {
private:
    // Custom deleter for OpenGL textures
    struct TextureDeleter {
        void operator()(unsigned int* textureId) const {
            if (textureId) {
                glDeleteTextures(1, textureId);
                delete textureId;
            }
        }
    };
    
    // Managed texture resource with custom cleanup
    std::unique_ptr<unsigned int, TextureDeleter> textureId_;
    
public:
    TextureResource(const char* filename) {
        auto id = new unsigned int;
        glGenTextures(1, id);
        // Load texture from file...
        textureId_.reset(id);  // Take ownership
    }
    
    // Move constructor (handled by unique_ptr)
    TextureResource(TextureResource&&) = default;
    
    // Move assignment (handled by unique_ptr)
    TextureResource& operator=(TextureResource&&) = default;
    
    // No need for custom destructor, unique_ptr handles cleanup
};
```

#### Reset Pattern

When implementing move operations, a common pattern is to reset the source object after transferring its resources:

```cpp
class Connection {
private:
    int socket_;
    bool connected_;
    
    void reset() {
        socket_ = -1;
        connected_ = false;
    }
    
public:
    // Move constructor
    Connection(Connection&& other) noexcept
        : socket_(other.socket_),
          connected_(other.connected_)
    {
        other.reset();  // Reset the source
    }
    
    // Move assignment
    Connection& operator=(Connection&& other) noexcept {
        if (this != &other) {
            closeConnection();  // Clean up existing resources
            
            socket