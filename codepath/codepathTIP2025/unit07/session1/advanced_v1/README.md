# Unit 7 - Session 1 - Advanced v1: Recursion Problems

## 📚 Learning Objectives

By the end of this session, you should be able to:

1. **Implement recursive solutions** for complex problems involving nested data structures
2. **Analyze time and space complexity** of recursive algorithms
3. **Compare recursive vs iterative approaches** and understand trade-offs
4. **Handle edge cases** and base cases in recursive functions
5. **Debug recursive algorithms** effectively

## 🎯 Problem Overview

This session contains 6 advanced recursion problems that test different aspects of recursive thinking:

### Problem 1: Counting the Layers of a Sandwich
- **Focus**: Nested data structure traversal
- **Key Concept**: Recursive counting with type checking
- **Complexity**: O(n) time, O(d) space

### Problem 2: Reversing Deli Orders
- **Focus**: String manipulation with recursion
- **Key Concept**: Recursive string reversal
- **Complexity**: O(n) time, O(n) space

### Problem 3: Sharing the Coffee
- **Focus**: Backtracking and constraint satisfaction
- **Key Concept**: Recursive search with pruning
- **Complexity**: O(2^n) time, O(n) space

### Problem 4: Super Sandwich (Recursive)
- **Focus**: Linked list manipulation
- **Key Concept**: Recursive merging with pointer manipulation
- **Complexity**: O(min(m,n)) time, O(min(m,n)) space

### Problem 5: Super Sandwich II (Iterative)
- **Focus**: Iterative vs recursive comparison
- **Key Concept**: Space optimization
- **Complexity**: O(min(m,n)) time, O(1) space

### Problem 6: Ternary Expression
- **Focus**: Expression parsing and evaluation
- **Key Concept**: Recursive parsing with nested structures
- **Complexity**: O(n) time, O(n) space

## 🔍 Complexity Analysis Guide

### Time Complexity Variables
- **n**: Length of input (string, array, etc.)
- **m, n**: Lengths of two different inputs
- **d**: Maximum depth of recursion
- **k**: Number of recursive branches

### Space Complexity Factors
- **Recursion Stack**: O(d) where d is recursion depth
- **Auxiliary Space**: Additional data structures used
- **Input Space**: Space required to store input

### Common Patterns
1. **Linear Recursion**: O(n) time, O(n) space
2. **Tree Recursion**: O(2^n) time, O(n) space
3. **Tail Recursion**: O(n) time, O(1) space (with optimization)

## 🛠️ Implementation Strategies

### 1. Base Case Identification
```python
# Always identify base cases first
if not input_data:
    return base_value
```

### 2. Recursive Case Structure
```python
# Break problem into smaller subproblems
result = recursive_function(smaller_input)
return combine(result, current_element)
```

### 3. Helper Functions
```python
# Use helper functions for complex logic
def main_function(input):
    return helper_function(input, initial_state)

def helper_function(input, state):
    # Recursive logic here
    pass
```

## 🧪 Testing Approach

### Test Case Categories
1. **Empty Input**: `[]`, `""`, `None`
2. **Single Element**: `[1]`, `"a"`
3. **Multiple Elements**: Normal cases
4. **Edge Cases**: Maximum values, special characters
5. **Complex Cases**: Nested structures, large inputs

### Debugging Tips
1. **Add print statements** to trace recursion
2. **Use a debugger** to step through recursive calls
3. **Draw recursion trees** for complex problems
4. **Check base cases** first when debugging

## 📊 Problem-Specific Analysis

### Problem 1: Counting Layers
```python
def count_layers(sandwich):
    if not sandwich:
        return 0
    if isinstance(sandwich, str):
        return 1
    return sum(count_layers(layer) for layer in sandwich)
```

**Key Insights:**
- Type checking (`isinstance`) for base case
- Sum of recursive calls for nested lists
- Handles mixed data types gracefully

### Problem 2: Reversing Orders
```python
def reverse_orders(orders):
    if not orders:
        return ""
    space_index = orders.find(' ')
    if space_index == -1:
        return orders
    return reverse_orders(orders[space_index + 1:]) + " " + orders[:space_index]
```

**Key Insights:**
- String splitting with recursion
- Concatenation order matters
- Handles single words and empty strings

### Problem 3: Coffee Splitting
```python
def can_split_coffee(coffee, n):
    total = sum(coffee)
    if total % n != 0:
        return False
    return helper(coffee, n, total // n, 0, [0] * n)
```

**Key Insights:**
- Backtracking with pruning
- Early termination for impossible cases
- State tracking through recursion

### Problem 4: Linked List Merging
```python
def merge_orders(a, b):
    if not a: return b
    if not b: return a
    a.next = merge_orders(b, a.next)
    return a
```

**Key Insights:**
- Pointer manipulation in recursion
- Alternating pattern through recursion
- Base cases handle empty lists

### Problem 5: Iterative Comparison
```python
def merge_orders_iterative(a, b):
    if not a: return b
    if not b: return a
    head = a
    while a and b:
        next_a, next_b = a.next, b.next
        a.next = b
        if next_a:
            b.next = next_a
        a, b = next_a, next_b
    return head
```

**Key Insights:**
- Same time complexity, better space complexity
- Explicit pointer manipulation
- Loop-based state management

### Problem 6: Ternary Expression
```python
def evaluate_ternary_recursive(expr):
    if not expr or '?' not in expr:
        return expr
    condition = expr[:expr.find('?')]
    colon_index = find_matching_colon(expr, expr.find('?'))
    true_expr = expr[expr.find('?') + 1:colon_index]
    false_expr = expr[colon_index + 1:]
    return evaluate_ternary_recursive(true_expr if condition == 'T' else false_expr)
```

**Key Insights:**
- Expression parsing with recursion
- Nested structure handling
- Conditional evaluation

## 🎯 Interview Tips

### Recursion Best Practices
1. **Always start with base cases**
2. **Draw recursion trees** for complex problems
3. **Consider space complexity** of recursion stack
4. **Look for tail recursion optimization** opportunities
5. **Use helper functions** for complex state management

### Common Pitfalls
1. **Missing base cases** causing infinite recursion
2. **Incorrect recursive case** logic
3. **Not considering space complexity**
4. **Forgetting to handle edge cases**
5. **Over-complicating simple problems**

### Optimization Strategies
1. **Memoization** for repeated subproblems
2. **Tail recursion** for space optimization
3. **Iterative conversion** when possible
4. **Early termination** for impossible cases
5. **Pruning** for search problems

## 📈 Practice Recommendations

### Beginner Level
- Start with Problems 1 and 2
- Focus on understanding base cases
- Practice drawing recursion trees

### Intermediate Level
- Tackle Problems 3 and 4
- Compare recursive vs iterative solutions
- Analyze complexity trade-offs

### Advanced Level
- Master Problem 6 (ternary expressions)
- Implement optimizations
- Handle complex edge cases

## 🔗 Related Topics

- **Dynamic Programming**: Recursion with memoization
- **Tree Traversal**: Recursive tree algorithms
- **Backtracking**: Recursive search with pruning
- **Divide and Conquer**: Recursive problem decomposition
- **Graph Algorithms**: Recursive graph traversal

## 📝 Study Checklist

- [ ] Implement all 6 problems
- [ ] Analyze time and space complexity for each
- [ ] Compare recursive vs iterative solutions
- [ ] Test with edge cases
- [ ] Practice drawing recursion trees
- [ ] Understand base case importance
- [ ] Master helper function patterns
- [ ] Practice debugging recursive code

## 🚀 Next Steps

After completing this session:
1. **Practice similar problems** on LeetCode/HackerRank
2. **Implement iterative versions** of recursive solutions
3. **Study dynamic programming** (recursion with memoization)
4. **Explore tree and graph algorithms**
5. **Practice system design** with recursive components

---

*Remember: Recursion is a powerful tool, but it's not always the best solution. Always consider the trade-offs between recursive and iterative approaches!* 