# Unit 7 - Session 1 - Standard v1: Marvel-Themed Recursion Practice

## 📚 Learning Objectives

By the end of this session, you should be able to:

1. **Implement basic recursive solutions** for common problems
2. **Compare iterative vs recursive approaches** and understand trade-offs
3. **Handle base cases** and recursive cases properly
4. **Analyze time and space complexity** of recursive algorithms
5. **Debug recursive functions** effectively

## 🎯 Problem Overview

This session contains 9 Marvel-themed recursion problems for you to implement. Each problem includes:
- Clear problem statement with Marvel context
- Function signature and expected behavior
- Test cases to verify your implementation
- Complexity analysis requirements

**Note: These are practice problems - you need to implement the solutions yourself!**

### Problem 1: Counting Iron Man's Suits
- **Focus**: Basic counting with iteration vs recursion
- **Key Concept**: Comparing iterative and recursive approaches
- **Complexity**: O(n) time, O(1) iterative space, O(n) recursive space

### Problem 2: Collecting Infinity Stones
- **Focus**: Array summation with recursion
- **Key Concept**: Recursive array traversal
- **Complexity**: O(n) time, O(n) space

### Problem 3: Counting Unique Suits
- **Focus**: Unique element counting
- **Key Concept**: Multiple recursive cases
- **Complexity**: O(n²) time, O(n) space

### Problem 4: Calculating Groot's Growth
- **Focus**: Fibonacci sequence implementation
- **Key Concept**: Classic recursive pattern
- **Complexity**: O(2^n) time, O(n) space

### Problem 5: Power of the Fantastic Four
- **Focus**: Exponentiation with negative powers
- **Key Concept**: Handling edge cases in recursion
- **Complexity**: O(n) time, O(n) space

### Problem 6: Strongest Avenger
- **Focus**: Finding maximum value recursively
- **Key Concept**: Recursive comparison
- **Complexity**: O(n) time, O(n) space

### Problem 7: Counting Vibranium Deposits
- **Focus**: String traversal with recursion
- **Key Concept**: Character counting in strings
- **Complexity**: O(n) time, O(n) space

### Problem 8: Merging Missions
- **Focus**: Linked list merging with recursion
- **Key Concept**: Recursive pointer manipulation
- **Complexity**: O(m+n) time, O(m+n) space

### Problem 9: Merging Missions II (Iterative)
- **Focus**: Iterative vs recursive comparison
- **Key Concept**: Space optimization
- **Complexity**: O(m+n) time, O(1) space

## 🔍 Recursion Fundamentals

### Base Cases
```python
# Always identify base cases first
if not input_data:
    return base_value
```

### Recursive Cases
```python
# Break problem into smaller subproblems
result = recursive_function(smaller_input)
return combine(result, current_element)
```

### Common Patterns
1. **Linear Recursion**: One recursive call per step
2. **Tree Recursion**: Multiple recursive calls per step
3. **Tail Recursion**: Recursive call is the last operation

## 🧪 Testing Strategy

### Test Case Categories
1. **Empty Input**: `[]`, `""`, `None`
2. **Single Element**: `[1]`, `"a"`
3. **Multiple Elements**: Normal cases
4. **Edge Cases**: Maximum values, special characters
5. **Complex Cases**: Large inputs, nested structures

### Debugging Tips
1. **Add print statements** to trace recursion
2. **Use a debugger** to step through recursive calls
3. **Draw recursion trees** for complex problems
4. **Check base cases** first when debugging

## 📊 Problem-Specific Analysis

### Problem 1: Counting Suits
```python
def count_suits_iterative(suits):
    count = 0
    for suit in suits:
        count += 1
    return count

def count_suits_recursive(suits):
    if not suits:
        return 0
    return 1 + count_suits_recursive(suits[1:])
```

**Key Insights:**
- Iterative: O(1) space, straightforward
- Recursive: O(n) space due to call stack
- Both: O(n) time complexity

### Problem 2: Sum Stones
```python
def sum_stones(stones):
    if not stones:
        return 0
    return stones[0] + sum_stones(stones[1:])
```

**Key Insights:**
- Classic recursive array summation
- Base case: empty array returns 0
- Recursive case: first element + sum of rest

### Problem 3: Unique Suits
```python
def count_unique_recursive(suits):
    if not suits:
        return 0
    if suits[0] in suits[1:]:
        return count_unique_recursive(suits[1:])
    return 1 + count_unique_recursive(suits[1:])
```

**Key Insights:**
- Multiple recursive cases
- Check for duplicates before counting
- O(n²) time due to `in` operation

### Problem 4: Fibonacci Growth
```python
def fibonacci_growth(n):
    if n <= 1:
        return n
    return fibonacci_growth(n-1) + fibonacci_growth(n-2)
```

**Key Insights:**
- Classic Fibonacci implementation
- Two recursive calls per step
- Exponential time complexity O(2^n)

### Problem 5: Power of Four
```python
def power_of_four(n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power_of_four(-n)
    return 4 * power_of_four(n-1)
```

**Key Insights:**
- Handle negative exponents
- Base case: n = 0 returns 1
- Recursive case: multiply by 4

### Problem 6: Strongest Avenger
```python
def strongest_avenger(strengths):
    if len(strengths) == 1:
        return strengths[0]
    return max(strengths[0], strongest_avenger(strengths[1:]))
```

**Key Insights:**
- Recursive maximum finding
- Base case: single element
- Recursive case: compare first with max of rest

### Problem 7: Count Deposits
```python
def count_deposits(resources):
    if not resources:
        return 0
    count = 1 if resources[0] == 'V' else 0
    return count + count_deposits(resources[1:])
```

**Key Insights:**
- String traversal with recursion
- Count 'V' characters only
- Simple recursive pattern

### Problem 8: Merge Missions
```python
def merge_missions(mission1, mission2):
    if not mission1:
        return mission2
    if not mission2:
        return mission1
    if mission1.value <= mission2.value:
        mission1.next = merge_missions(mission1.next, mission2)
        return mission1
    else:
        mission2.next = merge_missions(mission1, mission2.next)
        return mission2
```

**Key Insights:**
- Recursive linked list merging
- Compare values and merge accordingly
- Handle empty lists as base cases

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
- Start with Problems 1, 2, and 7
- Focus on understanding base cases
- Practice drawing recursion trees

### Intermediate Level
- Tackle Problems 3, 4, and 6
- Compare recursive vs iterative solutions
- Analyze complexity trade-offs

### Advanced Level
- Master Problems 5 and 8
- Implement optimizations
- Handle complex edge cases

## 🔗 Related Topics

- **Dynamic Programming**: Recursion with memoization
- **Tree Traversal**: Recursive tree algorithms
- **Backtracking**: Recursive search with pruning
- **Divide and Conquer**: Recursive problem decomposition
- **Graph Algorithms**: Recursive graph traversal

## 📝 Study Checklist

- [ ] Implement all 9 problems
- [ ] Compare iterative vs recursive solutions
- [ ] Analyze time and space complexity for each
- [ ] Test with edge cases
- [ ] Practice drawing recursion trees
- [ ] Understand base case importance
- [ ] Master recursive patterns
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