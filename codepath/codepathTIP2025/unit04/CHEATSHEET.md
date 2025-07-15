# Unit 4 Cheatsheet

## Overview
Here is a helpful cheatsheet outlining common syntax and concepts that will help you in your problem solving journey! Use this as reference as you solve the breakout problems for Unit 4. This is not an exhaustive list of all data structures, algorithmic techniques, and syntax you may encounter; it only covers the most critical concepts needed to ace Unit 4. In addition to the material below, you will be expected to know any required concepts from previous units. You may also find advanced concepts and bonus concepts included at the bottom of this page helpful for solving problem set questions, but you are not required to know them for the unit assessment.

---

## Standard Concepts

### Asymptotic Analysis (Big O)
- **Time complexity:** Measurement of the amount of time an algorithm takes to run as the size of the input changes
- **Space complexity:** Measurement of the amount of memory an algorithm uses as the size of the input changes
- **Big O notation:** O(...) describes the relationship between input size and complexity

#### Common Big O Complexities
| Complexity | Name         | Description |
|------------|--------------|-------------|
| O(1)       | Constant     | Same time regardless of input size |
| O(log n)   | Logarithmic  | Grows proportional to log of input size |
| O(n)       | Linear       | Grows directly with input size |
| O(n log n) | Log Linear   | n * log n growth |
| O(n^2)     | Quadratic    | Grows with the square of input size |
| O(2^n)     | Exponential  | Doubles with each increase in input |

---

### Time Complexity
- Measures number of operations as input size changes
- Focus on worst-case unless otherwise stated
- Drop constants and lower-order terms in Big O

#### Examples
- Constant: `def add_from_1_to_n(n): return (n * (n + 1)) / 2` (O(1))
- Linear: `def add_from_1_to_n(n): total = 0; for i in range(1, n+1): total += i` (O(n))
- Quadratic: Nested loops, e.g. `for i in range(n): for j in range(n): ...` (O(n^2))

---

### Space Complexity
- Measures memory usage as input size changes
- Most single-value variables: O(1)
- Strings/lists: O(n)
- Dictionaries: O(n)
- Nested structures: O(n^2)

---

### Built-In Function Complexities
| Function         | Time Complexity |
|------------------|----------------|
| len()            | O(1)           |
| sequence[idx]    | O(1)           |
| sequence.sort()  | O(n log n)     |
| lst.append()     | O(1)           |
| lst.insert()     | O(n)           |
| dict.get()       | O(1)           |

---

## Advanced Concepts
- Complexities with multiple variables (e.g., O(m*n))
- Helper functions and their Big O

---

## Tips
- Use built-in functions efficiently
- Test with large inputs to check performance
- Always consider worst-case unless otherwise stated

--- 