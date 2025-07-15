# Unit 01 Session 1 - Standard Version 1

## Overview
This problem set focuses on foundational Python concepts and problem-solving skills for Unit 01, Session 1 (Standard, Version 1).

## Learning Objectives
- Practice basic Python syntax and data structures
- Develop problem-solving strategies
- Gain familiarity with standard algorithms

## Problems
1. **Problem 1:** [Short description]
2. **Problem 2:** [Short description]
3. **Problem 3:** [Short description]
...

## Key Concepts
- Data Structures: List, Dict
- Algorithms: Linear search, basic loops
- Python Features: List comprehensions, string methods

## Tips & Pitfalls
- Read each problem carefully
- Test your code with edge cases
- Avoid off-by-one errors

## Testing
- [ ] All problems have test cases
- [ ] Edge cases considered

---

## Table of Contents

### [Problems 1-12](#problems-1-12)
- [Problem 1: Print Statement](#problem-1-print-statement)
- [Problem 2: Function with Parameter](#problem-2-function-with-parameter)
- [Problem 3: Conditional Statements](#problem-3-conditional-statements)
- [Problem 4: Safe List Access](#problem-4-safe-list-access)
- [Problem 5: Sum List Elements](#problem-5-sum-list-elements)
- [Problem 6: Transform List Elements](#problem-6-transform-list-elements)
- [Problem 7: Count Elements Below Threshold](#problem-7-count-elements-below-threshold)
- [Problem 8: Numbered List Output](#problem-8-numbered-list-output)
- [Problem 9: Check All Even Numbers](#problem-9-check-all-even-numbers)
- [Problem 10: Find All Divisors](#problem-10-find-all-divisors)
- [Problem 11: Remove Specific Characters](#problem-11-remove-specific-characters)
- [Problem 12: Find All Indices of Value](#problem-12-find-all-indices-of-value)

### [Problems 13-24](#problems-13-24)
- [Problem 13: Print Statement](#problem-13-print-statement)
- [Problem 14: Mad Libs Function](#problem-14-mad-libs-function)
- [Problem 15: Year-Based Lookup](#problem-15-year-based-lookup)
- [Problem 16: Get Last Element](#problem-16-get-last-element)
- [Problem 17: Concatenate Strings](#problem-17-concatenate-strings)
- [Problem 18: Square List Elements](#problem-18-square-list-elements)
- [Problem 19: Repeat String Pattern](#problem-19-repeat-string-pattern)
- [Problem 20: Find All Occurrences](#problem-20-find-all-occurrences)
- [Problem 21: Filter Odd Numbers](#problem-21-filter-odd-numbers)
- [Problem 22: Count Difference](#problem-22-count-difference)
- [Problem 23: Running Sum In-Place](#problem-23-running-sum-in-place)
- [Problem 24: Shuffle Two Halves](#problem-24-shuffle-two-halves)

---

## Problems 1-12

### Problem 1: Print Statement

Write a function that prints a specific string.

**Function Signature:**
```python
def welcome():
    pass
```

**Example Usage:**
```python
welcome()
```

**Example Output:**
```python
Welcome to The Hundred Acre Wood!
```

**💡 Hint:** Python Functions  
**💡 Hint:** Python Strings  
**💡 Hint:** print() function

---

### Problem 2: Function with Parameter

Write a function that accepts a string parameter and prints a formatted message using that parameter.

**Function Signature:**
```python
def greeting(name):
    pass
```

**Example Usage:**
```python
greeting("Michael")
greeting("Winnie the Pooh")
```

**Example Output:**
```python
Welcome to The Hundred Acre Wood Michael! My name is Christopher Robin.
Welcome to The Hundred Acre Wood Winnie the Pooh! My name is Christopher Robin.
```

**💡 Hint:** Variables  
**💡 Hint:** Parameters  
**💡 Hint:** Formatted Strings

---

### Problem 3: Conditional Statements

Write a function that prints different responses based on the input character using the mapping below:

| Character | Response |
|-----------|----------|
| "Pooh" | "Oh bother!" |
| "Tigger" | "TTFN: Ta-ta for now!" |
| "Eeyore" | "Thanks for noticing me." |
| "Christopher Robin" | "Silly old bear." |

If the character doesn't match, print "Sorry! I don't know {character}'s catchphrase!"

**Function Signature:**
```python
def print_catchphrase(character):
    pass
```

**Example Usage:**
```python
print_catchphrase("Pooh")
print_catchphrase("Piglet")
```

**Example Output:**
```python
"Oh bother!"
"Sorry! I don't know Piglet's catchphrase!"
```

**✨ AI Hint:** Conditionals

---

### Problem 4: Safe List Access

Write a function that returns the element at index x in a list. If x is not a valid index, return None.

**Function Signature:**
```python
def get_item(items, x):
    pass
```

**Example Usage:**
```python
items = ["piglet", "pooh", "roo", "rabbit"]
print(get_item(items, 2))    # "roo"
print(get_item(items, 5))    # None
```

**✨ AI Hint:** List indexing  
**✨ AI Hint:** To Print or to Return?

---

### Problem 5: Sum List Elements

Write a function that returns the sum of all elements in a list of integers. Do not use the built-in sum() function.

**Function Signature:**
```python
def sum_honey(hunny_jars):
    pass
```

**Example Usage:**
```python
print(sum_honey([2, 3, 4, 5]))    # 14
print(sum_honey([]))              # 0
```

**✨ AI Hint:** For Loops  
**✨ AI Hint:** Accumulator Variable

---

### Problem 6: Transform List Elements

Write a function that multiplies each element in a list by 2 and returns the new list.

**Function Signature:**
```python
def doubled(hunny_jars):
    pass
```

**Example Usage:**
```python
print(doubled([1, 2, 3]))    # [2, 4, 6]
```

---

### Problem 7: Count Elements Below Threshold

Write a function that counts how many elements in a list are less than a given threshold.

**Function Signature:**
```python
def count_less_than(race_times, threshold):
    pass
```

**Example Usage:**
```python
print(count_less_than([1, 2, 3, 4, 5, 6], 4))    # 3
print(count_less_than([], 4))                     # 0
```

---

### Problem 8: Numbered List Output

Write a function that prints a numbered to-do list in the format:
```
Pooh's To Dos:
1. Task 1
2. Task 2
...
```

**Function Signature:**
```python
def print_todo_list(tasks):
    pass
```

**Example Usage:**
```python
tasks = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(tasks)
```

**Example Output:**
```python
Pooh's To Dos:
1. Count all the bees in the hive
2. Chase all the clouds from the sky
3. Think
4. Stoutness Exercises
```

**✨ AI Hint:** range()

---

### Problem 9: Check All Even Numbers

Write a function that returns True if all numbers in a list are even, False otherwise.

**Function Signature:**
```python
def can_pair(item_quantities):
    pass
```

**Example Usage:**
```python
print(can_pair([2, 4, 6, 8]))    # True
print(can_pair([1, 2, 3, 4]))    # False
print(can_pair([]))              # True
```

**💡 Hint:** Remainders with Modulus Division

---

### Problem 10: Find All Divisors

Write a function that returns a list of all divisors of a given positive integer.

**Function Signature:**
```python
def split_haycorns(quantity):
    pass
```

**Example Usage:**
```python
print(split_haycorns(6))    # [1, 2, 3, 6]
print(split_haycorns(1))    # [1]
```

---

### Problem 11: Remove Specific Characters

Write a function that removes all occurrences of the letters 't', 'i', 'g', 'e', and 'r' from a string.

**Function Signature:**
```python
def tiggerfy(s):
    pass
```

**Example Usage:**
```python
print(tiggerfy("suspicerous"))    # "suspcous"
print(tiggerfy("Trigger"))        # ""
print(tiggerfy("Hunny"))          # "Hunny"
```

**💡 Hint:** String Methods

---

### Problem 12: Find All Indices of Value

Write a function that returns a list of all indices where a specific value appears in a list.

**Function Signature:**
```python
def locate_thistles(items):
    pass
```

**Example Usage:**
```python
items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))    # [0, 3]

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))    # []
```

---

## Problems 13-24

### Problem 13: Print Statement

Write a function that prints a specific string.

**Function Signature:**
```python
def batman():
    pass
```

**Example Usage:**
```python
batman()
```

**Example Output:**
```python
I am vengeance. I am the night. I am Batman!
```

**💡 Hint:** Python Functions  
**💡 Hint:** Python Strings  
**💡 Hint:** print() function

---

### Problem 14: Mad Libs Function

Write a function that accepts a verb parameter and prints a formatted sentence using that verb.

**Function Signature:**
```python
def madlib(verb):
    pass
```

**Example Usage:**
```python
madlib("give up")
madlib("nap")
```

**Example Output:**
```python
"I have one power. I never give up. - Batman"
"I have one power. I never nap. - Batman"
```

**💡 Hint:** Variables  
**💡 Hint:** Parameters  
**💡 Hint:** Formatted Strings

---

### Problem 15: Year-Based Lookup

Write a function that prints the Batman movie title for a given year using this mapping:

| Year | Movie Title |
|------|-------------|
| 2005 | "Batman Begins" |
| 2008 | "The Dark Knight" |
| 2012 | "The Dark Knight Rises" |

If the year doesn't match, print "Christopher Nolan did not release a Batman movie in {year}."

**Function Signature:**
```python
def trilogy(year):
    pass
```

**Example Usage:**
```python
trilogy(2008)    # "The Dark Knight"
trilogy(1998)    # "Christopher Nolan did not release a Batman movie in 1998."
```

**✨ AI Hint:** Conditionals

---

### Problem 16: Get Last Element

Write a function that returns the last element in a list. If the list is empty, return None.

**Function Signature:**
```python
def get_last(items):
    pass
```

**Example Usage:**
```python
items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
print(get_last(items))    # "black adam"
print(get_last([]))       # None
```

**✨ AI Hint:** List indexing  
**✨ AI Hint:** To Print or to Return?

---

### Problem 17: Concatenate Strings

Write a function that concatenates all strings in a list into one string.

**Function Signature:**
```python
def concatenate(words):
    pass
```

**Example Usage:**
```python
print(concatenate(["vengeance", "darkness", "batman"]))    # "vengeancedarknessbatman"
print(concatenate([]))                                     # ""
```

**✨ AI Hint:** For Loops  
**✨ AI Hint:** Accumulator Variable

---

### Problem 18: Square List Elements

Write a function that squares each element in a list of integers and returns the new list.

**Function Signature:**
```python
def squared(numbers):
    pass
```

**Example Usage:**
```python
print(squared([1, 2, 3]))    # [1, 4, 9]
```

---

### Problem 19: Repeat String Pattern

Write a function that prints "nanana batman!" where "na" is repeated x times. Do not use the * operator.

**Function Signature:**
```python
def nanana_batman(x):
    pass
```

**Example Usage:**
```python
nanana_batman(6)    # "nananananana batman!"
nanana_batman(0)    # "batman!"
```

**✨ AI Hint:** range()

---

### Problem 20: Find All Occurrences

Write a function that returns a list of all indices where a specific value appears in a list.

**Function Signature:**
```python
def find_villain(crowd, villain):
    pass
```

**Example Usage:**
```python
crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
print(find_villain(crowd, villain))    # [1, 4, 6]
```

---

### Problem 21: Filter Odd Numbers

Write a function that returns a new list containing only the odd numbers from the input list.

**Function Signature:**
```python
def get_odds(nums):
    pass
```

**Example Usage:**
```python
print(get_odds([1, 2, 3, 4]))    # [1, 3]
print(get_odds([2, 4, 6, 8]))    # []
```

**💡 Hint:** Remainders with Modulus Division

---

### Problem 22: Count Difference

Write a function that returns the number of odd numbers minus the number of even numbers in a list.

**Function Signature:**
```python
def up_and_down(lst):
    pass
```

**Example Usage:**
```python
print(up_and_down([1, 2, 3]))      # 1 (2 odd - 1 even)
print(up_and_down([1, 3, 5]))      # 3 (3 odd - 0 even)
print(up_and_down([2, 4, 10, 2]))  # -4 (0 odd - 4 even)
```

---

### Problem 23: Running Sum In-Place

Write a function that modifies a list in-place to contain the running sum. You cannot create new lists.

**Function Signature:**
```python
def running_sum(superhero_stats):
    pass
```

**Example Usage:**
```python
stats = [1, 2, 3, 4]
running_sum(stats)
print(stats)    # [1, 3, 6, 10]

stats = [1, 1, 1, 1, 1]
running_sum(stats)
print(stats)    # [1, 2, 3, 4, 5]

stats = [3, 1, 2, 10, 1]
running_sum(stats)
print(stats)    # [3, 4, 6, 16, 17]
```

---

### Problem 24: Shuffle Two Halves

Write a function that takes a list of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn] and returns it in the form [x1,y1,x2,y2,...,xn,yn].

**Function Signature:**
```python
def shuffle(cards):
    pass
```

**Example Usage:**
```python
print(shuffle(['Joker', 'Queen', 2, 3, 'Ace', 7]))
# ['Joker', 3, 'Queen', 'Ace', 2, 7]

print(shuffle([9, 2, 3, 'Joker', 'Joker', 3, 2, 9]))
# [9, 'Joker', 2, 3, 3, 2, 'Joker', 9]

print(shuffle([10, 10, 2, 2]))
# [10, 2, 10, 2]
```