# Comprehensive Guide to C++ Vectors

## Table of Contents
- [Introduction to Vectors](#introduction-to-vectors)
- [Vector Declaration and Initialization](#vector-declaration-and-initialization)
- [Member Types](#member-types)
- [Vector Constructors](#vector-constructors)
- [Element Access](#element-access)
- [Iterators](#iterators)
- [Capacity and Size Management](#capacity-and-size-management)
- [Modifiers](#modifiers)
- [Operations](#operations)
- [Allocator](#allocator)
- [Time Complexity Analysis](#time-complexity-analysis)
- [Vector vs Other Containers](#vector-vs-other-containers)
- [Vector<bool> Specialization](#vectorbool-specialization)
- [Best Practices](#best-practices)
- [Common Pitfalls](#common-pitfalls)

## Introduction to Vectors

Vectors in C++ are dynamic array-like containers that belong to the Standard Template Library (STL). Unlike traditional arrays, vectors can resize dynamically during runtime, making them more flexible and easier to use.

Key features of vectors:
- Dynamic size management (grows and shrinks as needed)
- Elements stored contiguously in memory (like arrays)
- Random access to elements via indices (constant time)
- Automatic memory management
- Support for various operations like inserting, removing elements

To use vectors, you need to include the vector header:

```cpp
#include <vector>
```

## Vector Declaration and Initialization

### Declaration

The basic syntax for declaring a vector:

```cpp
std::vector<T> vector_name;
```

Where `T` is the data type of elements the vector will store.

### Initialization Methods

1. **Default Initialization (Empty Vector)**:
```cpp
std::vector<int> vec1;  // Creates an empty vector
```

2. **Initialization with Size**:
```cpp
std::vector<int> vec2(5);  // Creates a vector with 5 elements, all initialized to 0
```

3. **Initialization with Size and Value**:
```cpp
std::vector<int> vec3(5, 10);  // Creates a vector with 5 elements, all initialized to 10
```

4. **Initialization with List (C++11 and later)**:
```cpp
std::vector<int> vec4 = {1, 2, 3, 4, 5};  // Initializer list
std::vector<int> vec5{1, 2, 3, 4, 5};     // Uniform initialization
```

5. **Initialization from Another Vector**:
```cpp
std::vector<int> vec6(vec5);  // Copy of vec5
std::vector<int> vec7 = vec5; // Another way to copy
```

6. **Initialization with Iterators**:
```cpp
std::vector<int> vec8(vec5.begin(), vec5.end());  // Using iterators from another vector
```

7. **Initialization from Array**:
```cpp
int arr[] = {1, 2, 3, 4, 5};
std::vector<int> vec9(arr, arr + sizeof(arr) / sizeof(arr[0]));
```

## Member Types

Vectors define several member types:

| Member Type | Definition |
|-------------|------------|
| `value_type` | The type of the elements (T) |
| `allocator_type` | The allocator type (defaults to `allocator<T>`) |
| `reference` | Reference to element (usually `T&`) |
| `const_reference` | Const reference to element (usually `const T&`) |
| `pointer` | Pointer to element (usually `T*`) |
| `const_pointer` | Const pointer to element (usually `const T*`) |
| `iterator` | Random access iterator to elements |
| `const_iterator` | Const random access iterator to elements |
| `reverse_iterator` | Reverse iterator (`reverse_iterator<iterator>`) |
| `const_reverse_iterator` | Const reverse iterator (`reverse_iterator<const_iterator>`) |
| `difference_type` | Signed integer type for differences between iterators |
| `size_type` | Unsigned integer type for sizes |

## Vector Constructors

Vectors provide several constructors:

1. **Default Constructor**:
```cpp
std::vector<int> vec;  // Creates an empty vector
```

2. **Fill Constructor**:
```cpp
std::vector<int> vec(5, 10);  // Creates a vector with 5 elements, all set to 10
```

3. **Range Constructor**:
```cpp
std::vector<int> vec2(vec.begin(), vec.begin() + 3);  // Creates a vector with the first 3 elements of vec
```

4. **Copy Constructor**:
```cpp
std::vector<int> vec3(vec);  // Creates a copy of vec
```

5. **Move Constructor (C++11)**:
```cpp
std::vector<int> vec4(std::move(vec));  // Moves resources from vec to vec4
```

6. **Initializer List Constructor (C++11)**:
```cpp
std::vector<int> vec5 = {1, 2, 3, 4, 5};  // Creates a vector with elements 1, 2, 3, 4, 5
```

## Element Access

Vectors provide several methods to access elements:

1. **operator[]**:
```cpp
vec[0] = 10;  // Sets the first element to 10
int x = vec[1];  // Gets the second element
```
Note: No bounds checking, undefined behavior if index is out of range.
Time complexity: O(1)

2. **at()**:
```cpp
vec.at(0) = 10;  // Sets the first element to 10
int x = vec.at(1);  // Gets the second element
```
Note: Performs bounds checking, throws `std::out_of_range` exception if index is out of range.
Time complexity: O(1)

3. **front()**:
```cpp
int x = vec.front();  // Gets the first element
```
Time complexity: O(1)

4. **back()**:
```cpp
int x = vec.back();  // Gets the last element
```
Time complexity: O(1)

5. **data()** (C++11):
```cpp
int* p = vec.data();  // Gets a direct pointer to the memory array
```
Time complexity: O(1)

## Iterators

Vectors provide various iterators for traversing elements:

1. **begin() / end()**:
```cpp
for (auto it = vec.begin(); it != vec.end(); ++it) {
    // Access element using *it
}
```
Time complexity: O(1) to obtain the iterator

2. **cbegin() / cend()** (C++11):
```cpp
for (auto it = vec.cbegin(); it != vec.cend(); ++it) {
    // Access element using *it (read-only)
}
```
Time complexity: O(1) to obtain the iterator

3. **rbegin() / rend()**:
```cpp
for (auto it = vec.rbegin(); it != vec.rend(); ++it) {
    // Access element using *it (in reverse order)
}
```
Time complexity: O(1) to obtain the iterator

4. **crbegin() / crend()** (C++11):
```cpp
for (auto it = vec.crbegin(); it != vec.crend(); ++it) {
    // Access element using *it (in reverse order, read-only)
}
```
Time complexity: O(1) to obtain the iterator

5. **Range-based for loop** (C++11):
```cpp
for (const auto& elem : vec) {
    // Access element directly
}
```

## Capacity and Size Management

Vectors provide methods to manage capacity and size:

1. **size()**:
```cpp
size_t s = vec.size();  // Gets the number of elements
```
Time complexity: O(1)

2. **empty()**:
```cpp
bool is_empty = vec.empty();  // Checks if the vector is empty
```
Time complexity: O(1)

3. **capacity()**:
```cpp
size_t c = vec.capacity();  // Gets the current capacity (size of allocated storage)
```
Time complexity: O(1)

4. **max_size()**:
```cpp
size_t m = vec.max_size();  // Gets the maximum possible number of elements
```
Time complexity: O(1)

5. **reserve()**:
```cpp
vec.reserve(100);  // Increases capacity to at least 100 elements
```
Time complexity: O(n) if reallocation occurs, where n is size()

6. **shrink_to_fit()** (C++11):
```cpp
vec.shrink_to_fit();  // Reduces capacity to match the size
```
Time complexity: Implementation-dependent, typically O(n)

7. **resize()**:
```cpp
vec.resize(10);      // Resizes to 10 elements, new elements initialized to 0
vec.resize(15, 42);  // Resizes to 15 elements, new elements initialized to 42
```
Time complexity: Linear in the number of elements inserted/deleted

## Modifiers

Vectors provide methods to modify their contents:

1. **push_back()**:
```cpp
vec.push_back(42);  // Adds an element to the end
```
Time complexity: Amortized O(1)

2. **pop_back()**:
```cpp
vec.pop_back();  // Removes the last element
```
Time complexity: O(1)

3. **insert()**:
```cpp
vec.insert(vec.begin() + 2, 42);               // Inserts 42 at position 2
vec.insert(vec.begin() + 2, 3, 42);            // Inserts 3 copies of 42 at position 2
vec.insert(vec.begin() + 2, {1, 2, 3});        // Inserts initializer list at position 2
vec.insert(vec.begin() + 2, v2.begin(), v2.end()); // Inserts elements from another vector
```
Time complexity: O(n + m) where n is the number of elements inserted and m is the number of elements after insertion point

4. **emplace()**:
```cpp
vec.emplace(vec.begin() + 2, 42);  // Constructs element in-place at position 2
```
Time complexity: O(n) where n is the number of elements after insertion point

5. **emplace_back()**:
```cpp
vec.emplace_back(42);  // Constructs element in-place at the end
```
Time complexity: Amortized O(1)

6. **erase()**:
```cpp
vec.erase(vec.begin() + 2);                  // Removes element at position 2
vec.erase(vec.begin() + 2, vec.begin() + 5); // Removes elements from position 2 to 4
```
Time complexity: O(n) where n is the number of elements after erased elements

7. **clear()**:
```cpp
vec.clear();  // Removes all elements
```
Time complexity: Linear in size()

8. **swap()**:
```cpp
vec1.swap(vec2);  // Swaps contents with another vector
std::swap(vec1, vec2);  // Alternative way to swap
```
Time complexity: O(1)

9. **assign()**:
```cpp
vec.assign(5, 10);                   // Assigns 5 copies of value 10
vec.assign({1, 2, 3, 4, 5});         // Assigns values from initializer list
vec.assign(v2.begin(), v2.end());    // Assigns values from another container
```
Time complexity: Linear in the new size + the number of elements deleted

## Operations

Vectors support various operations:

1. **Comparison Operators**:
```cpp
bool are_equal = (vec1 == vec2);  // Checks if vec1 and vec2 have the same elements
bool is_less = (vec1 < vec2);     // Lexicographical comparison
```
Time complexity: Linear in size() for the comparison

2. **Range Operations**:
```cpp
// Find an element
auto it = std::find(vec.begin(), vec.end(), 42);
if (it != vec.end()) {
    // Element found
}

// Sort the vector
std::sort(vec.begin(), vec.end());

// Reverse the vector
std::reverse(vec.begin(), vec.end());

// Count occurrences
int count = std::count(vec.begin(), vec.end(), 42);
```

## Allocator

Vectors use an allocator to manage memory:

```cpp
// Create a vector with a custom allocator
std::vector<int, MyAllocator<int>> vec;

// Get the allocator
MyAllocator<int> alloc = vec.get_allocator();
```

## Time Complexity Analysis

Here's a summary of time complexities for common vector operations:

| Operation | Time Complexity |
|-----------|-----------------|
| Random access (operator[], at()) | O(1) |
| Insert or remove at the end (push_back, pop_back) | Amortized O(1) |
| Insert or remove at the beginning or middle | O(n) |
| Find element (unsorted vector) | O(n) |
| Find element (sorted vector, using binary_search) | O(log n) |
| Size operations (size(), empty(), capacity()) | O(1) |
| Iteration through all elements | O(n) |
| clear() | O(n) |
| erase() single element | O(n) |
| erase() range of elements | O(n) |
| reserve() | O(n) if reallocation needed |
| resize() | O(n) if growing or shrinking |
| shrink_to_fit() | O(n) |

### Memory Reallocation Strategy

When a vector needs to grow beyond its current capacity, it typically:
1. Allocates a new, larger memory block (often 1.5 or 2 times the current capacity)
2. Moves or copies all existing elements to the new block
3. Deallocates the old memory block

This strategy ensures that push_back() operations have an amortized O(1) time complexity, even though occasional reallocations take O(n) time.

## Vector vs Other Containers

### Vector vs Array
- **Vector**: Dynamic size, slightly higher memory overhead, more functionalities
- **Array**: Fixed size, lower memory overhead, fewer functionalities

### Vector vs List
- **Vector**: Contiguous memory, fast random access, slow insertion/deletion in the middle
- **List**: Non-contiguous memory, slow random access, fast insertion/deletion anywhere

### Vector vs Deque
- **Vector**: Single contiguous memory block, fast random access, slow insertion at the beginning
- **Deque**: Multiple memory blocks, slightly slower random access, fast insertion at both ends

## Vector<bool> Specialization

`std::vector<bool>` is a specialized implementation that optimizes space by storing boolean values as individual bits:

```cpp
std::vector<bool> bvec = {true, false, true};
bvec[1] = true;  // Sets the second element to true
bool b = bvec[0];  // Gets the first element
```

Special considerations:
- Reference to a bit is not a real reference (it's a proxy object)
- May have different performance characteristics than regular vectors
- Not guaranteed to store elements contiguously in the standard bitwise sense

## Best Practices

1. **Reserve space in advance when size is known**:
```cpp
vec.reserve(1000);  // Avoids multiple reallocations if adding ~1000 elements
```

2. **Use emplace_back() instead of push_back() for complex objects**:
```cpp
// Avoid:
vec.push_back(MyClass(arg1, arg2));

// Prefer:
vec.emplace_back(arg1, arg2);  // Constructs object in-place
```

3. **Use range-based for loop for iteration (C++11)**:
```cpp
// Avoid:
for (size_t i = 0; i < vec.size(); ++i) {
    // Use vec[i]
}

// Prefer:
for (const auto& elem : vec) {
    // Use elem directly
}
```

4. **Use at() for safe access with bounds checking**:
```cpp
// Avoid in performance-critical code, but safer:
try {
    val = vec.at(i);  // Throws std::out_of_range if i is out of bounds
} catch (const std::out_of_range& e) {
    // Handle out-of-range access
}
```

5. **Use clear() + shrink_to_fit() to truly free memory**:
```cpp
vec.clear();         // Removes all elements
vec.shrink_to_fit(); // Reduces capacity to fit size (may free memory)
```

6. **Use move semantics (C++11) to avoid copies**:
```cpp
std::vector<MyClass> vec1;
// ...
std::vector<MyClass> vec2 = std::move(vec1);  // Moves resources from vec1 to vec2
```

## Common Pitfalls

1. **Iterator invalidation**: Iterators, pointers, and references to vector elements can be invalidated when:
   - Adding elements if a reallocation occurs
   - Removing elements (only iterators at or after the point of removal)

```cpp
// Dangerous: iterator may be invalidated
auto it = vec.begin();
vec.push_back(42);  // Might cause reallocation
*it = 10;  // Undefined behavior if reallocation occurred
```

2. **Range checking**: operator[] doesn't check bounds, which can lead to undefined behavior:

```cpp
// Dangerous: no bounds checking
int val = vec[1000];  // Undefined behavior if vec.size() <= 1000

// Safe: bounds checking
try {
    val = vec.at(1000);  // Throws if out of bounds
} catch (const std::out_of_range& e) {
    // Handle out-of-range access
}
```

3. **Performance issues with frequent insertions/deletions in the middle**:

```cpp
// Inefficient for many insertions
for (int i = 0; i < 1000; ++i) {
    vec.insert(vec.begin(), i);  // Each insertion shifts all elements
}

// Better alternatives:
// 1. Insert at the end and reverse
for (int i = 0; i < 1000; ++i) {
    vec.push_back(i);
}
std::reverse(vec.begin(), vec.end());

// 2. Use another container like std::deque or std::list
// 3. Reserve space in advance if possible
vec.reserve(1000);
```

4. **Memory leaks with pointer elements**: Vectors don't automatically delete dynamically allocated objects:

```cpp
std::vector<MyClass*> vec;
vec.push_back(new MyClass());
// ...
vec.clear();  // Doesn't delete the MyClass object!

// Proper cleanup:
for (auto ptr : vec) {
    delete ptr;
}
vec.clear();

// Better solution: use smart pointers
std::vector<std::unique_ptr<MyClass>> vec2;
vec2.push_back(std::make_unique<MyClass>());
// No manual cleanup needed
```

5. **Size vs capacity confusion**:

```cpp
vec.reserve(100);  // Sets capacity to at least 100, but size remains unchanged
// vec.size() might still be 0

vec.resize(100);   // Changes size to 100, may also change capacity
// vec.size() is now 100
```
