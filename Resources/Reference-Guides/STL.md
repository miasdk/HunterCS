# C++ STL Cheat Sheet

## Containers
| Container        | Description                          | Common Operations          | Time Complexity |
|------------------|--------------------------------------|---------------------------|-----------------|
| `std::vector`    | Dynamic array                        | `push_back`, `pop_back`   | O(1) amortized  |
| `std::list`      | Doubly-linked list                  | `push_front`, `pop_front` | O(1)            |
| `std::set`       | Ordered unique elements             | `insert`, `find`          | O(log n)        |
| `std::map`       | Ordered key-value pairs             | `insert`, `find`          | O(log n)        |
| `std::unordered_set` | Hash-based unique elements       | `insert`, `find`          | O(1) average    |
| `std::unordered_map` | Hash-based key-value pairs       | `insert`, `find`          | O(1) average    |

## Iterators
| Iterator Type       | Description                          | Example Containers        |
|---------------------|--------------------------------------|---------------------------|
| Random Access       | Supports arithmetic (e.g., `it + 2`) | `std::vector`, `std::deque` |
| Bidirectional       | Supports `++` and `--`               | `std::list`, `std::set`   |
| Forward             | Supports only `++`                   | `std::forward_list`       |

## Algorithms
| Algorithm          | Description                          | Example Usage             |
|--------------------|--------------------------------------|---------------------------|
| `std::sort`        | Sorts a range of elements            | `std::sort(v.begin(), v.end())` |
| `std::find`        | Finds an element in a range          | `std::find(v.begin(), v.end(), value)` |
| `std::binary_search` | Checks if an element exists in a sorted range | `std::binary_search(v.begin(), v.end(), value)` |