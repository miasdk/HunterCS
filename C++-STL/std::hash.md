# `std::hash` Reference Guide based on cplusplus.com 
made with Claude

## Overview

`std::hash` is a function object class that provides hash functions for various types in the C++ Standard Library. It's primarily used with unordered associative containers like `std::unordered_map` and `std::unordered_set` to compute hash values for keys.

## Header

```cpp
#include <functional>
```

## Template Definition

```cpp
template <class T>
struct hash;
```

## Standard Specializations

`std::hash` is specialized for the following types in the standard library:

| Type | Description |
|------|-------------|
| `bool` | Boolean type |
| `char` | Character type |
| `signed char` | Signed character type |
| `unsigned char` | Unsigned character type |
| `char16_t` | 16-bit character type |
| `char32_t` | 32-bit character type |
| `wchar_t` | Wide character type |
| `short` | Short integer type |
| `unsigned short` | Unsigned short integer type |
| `int` | Integer type |
| `unsigned int` | Unsigned integer type |
| `long` | Long integer type |
| `unsigned long` | Unsigned long integer type |
| `long long` | Long long integer type |
| `unsigned long long` | Unsigned long long integer type |
| `float` | Floating-point type |
| `double` | Double precision floating-point type |
| `long double` | Extended precision floating-point type |
| `std::nullptr_t` | Null pointer type |
| All pointer types | Including function pointers |
| `std::string` | String class |
| `std::u16string` | UTF-16 encoded string |
| `std::u32string` | UTF-32 encoded string |
| `std::wstring` | Wide string |
| `std::error_code` | Error code |
| `std::error_condition` | Error condition |
| `std::type_index` | Type index |
| `std::bitset` | (C++17) Bitset container |
| `std::unique_ptr` | (C++14) Smart pointer |
| `std::shared_ptr` | (C++14) Smart pointer |
| `std::optional` | (C++17) Optional value container |
| `std::variant` | (C++17) Variant container |
| `std::monostate` | (C++17) Variant helper type |

## Member Functions

### Function Call Operator

```cpp
size_t operator()(const T& val) const;
```

Returns a hash value for the argument `val`.

#### Parameters
- `val`: The value to hash

#### Return Value
A `size_t` value that represents the hash of the input.

## Using `std::hash`

### With Unordered Containers

```cpp
std::unordered_map<std::string, int, std::hash<std::string>> myMap;
std::unordered_set<int, std::hash<int>> mySet;
```

### Creating Custom Hash Functions

For user-defined types, you can specialize `std::hash`:

```cpp
struct Person {
    std::string name;
    int age;
    
    bool operator==(const Person& other) const {
        return name == other.name && age == other.age;
    }
};

namespace std {
    template<>
    struct hash<Person> {
        size_t operator()(const Person& p) const {
            // Combine hash values of members
            return hash<string>()(p.name) ^ (hash<int>()(p.age) << 1);
        }
    };
}
```

Alternatively, you can provide a custom hash function object:

```cpp
struct PersonHash {
    size_t operator()(const Person& p) const {
        return std::hash<std::string>()(p.name) ^ (std::hash<int>()(p.age) << 1);
    }
};

std::unordered_set<Person, PersonHash> personSet;
```

## Hash Combining Techniques

When creating hash functions for custom types with multiple members, it's common to combine individual hash values. Here are some approaches:

### Simple XOR Shifting

```cpp
size_t h1 = std::hash<std::string>()(obj.name);
size_t h2 = std::hash<int>()(obj.id);
return h1 ^ (h2 << 1);
```

### Boost's hash_combine (conceptual implementation)

```cpp
template <class T>
void hash_combine(std::size_t& seed, const T& v) {
    std::hash<T> hasher;
    seed ^= hasher(v) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
}
```

## Requirements for Custom Hash Functions

A good hash function should:

1. **Be deterministic**: Same input always produces the same output
2. **Have uniform distribution**: Minimize collisions
3. **Be efficient**: Compute quickly
4. **Be consistent with equality**: If two objects are equal (according to `operator==`), they must have the same hash value

## Performance Considerations

- Hash functions should be computationally inexpensive
- The distribution quality affects container performance
- Poor hash functions lead to more collisions, degrading container performance
- For complex types, balance between computation time and collision reduction

## Common Issues

- Hash collisions can degrade unordered container performance
- Default hash for floating-point types may not be ideal for all purposes
- Pointer hashing only considers the address, not the pointed-to value

## Example: Complete Usage

```cpp
#include <iostream>
#include <string>
#include <functional>
#include <unordered_map>

struct Point {
    int x, y;
    
    bool operator==(const Point& other) const {
        return x == other.x && y == other.y;
    }
};

namespace std {
    template<>
    struct hash<Point> {
        size_t operator()(const Point& p) const {
            return hash<int>()(p.x) ^ (hash<int>()(p.y) << 1);
        }
    };
}

int main() {
    std::unordered_map<Point, std::string> points;
    
    points[{1, 2}] = "Point(1,2)";
    points[{3, 4}] = "Point(3,4)";
    
    std::cout << "Hash of Point(1,2): " << std::hash<Point>()({1, 2}) << std::endl;
    std::cout << "Value: " << points[{1, 2}] << std::endl;
    
    return 0;
}
```

## C++20 Additions

### Heterogeneous Lookup Support

In C++20, `std::hash` supports heterogeneous lookup with the transparent hash:

```cpp
#include <functional>
#include <unordered_map>
#include <string>
#include <string_view>

struct StringHash {
    using is_transparent = void;
    
    size_t operator()(const char* str) const {
        return std::hash<std::string_view>()(str);
    }
    
    size_t operator()(std::string_view str) const {
        return std::hash<std::string_view>()(str);
    }
    
    size_t operator()(const std::string& str) const {
        return std::hash<std::string_view>()(str);
    }
};

// Usage with heterogeneous lookup
std::unordered_map<std::string, int, StringHash, std::equal_to<>> map;
```

## References

- [cplusplus.com - std::hash](http://www.cplusplus.com/reference/functional/hash/)
- [cppreference.com - std::hash](https://en.cppreference.com/w/cpp/utility/hash)
- [C++ Standard, Section 20.14.15 - Class template hash](https://isocpp.org/)
