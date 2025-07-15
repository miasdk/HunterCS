# Unit 1 Cheatsheet

## Table of Contents

### [Overview](#overview)

### [Standard Concepts](#standard-concepts)
#### [Built-In Functions](#built-in-functions)
- [Print](#print)
- [Length](#length)
- [Range](#range)
- [Sum](#sum)
- [Min](#min)
- [Max](#max)

#### [List Methods & Syntax](#list-methods--syntax)
- [Append Method](#append-method)
- [Sort Method](#sort-method)

#### [String Methods & Syntax](#string-methods--syntax)
- [Lower Method](#lower-method)
- [Split Method](#split-method)
- [Join Method](#join-method)
- [Strip Method](#strip-method)

#### [Python Syntax](#python-syntax)
- [Variables](#variables)
- [Conditionals](#conditionals)
- [Functions](#functions)
- [Formatted Strings](#formatted-strings)
- [Remainder Division](#remainder-division)
- [For Loops](#for-loops)
- [While Loops](#while-loops)

#### [Comparing Strings and Lists](#comparing-strings-and-lists)

### [Advanced Concepts](#advanced-concepts)
#### [Built-in Functions](#built-in-functions-1)
- [Enumerate](#enumerate)
- [Zip](#zip)

#### [Python Syntax](#python-syntax-1)
- [Nested Lists](#nested-lists)
- [Nested Loops](#nested-loops)
- [List Comprehensions](#list-comprehensions)

#### [Two Pointer Technique](#two-pointer-technique)
- [Opposite Direction Pointers](#opposite-direction-pointers)
- [Same Direction Pointers](#same-direction-pointers)
- [When to Use Two-Pointer Technique](#when-to-use-two-pointer-technique)

### [Bonus Syntax & Concepts](#bonus-syntax--concepts)
#### [Additional List Methods](#additional-list-methods)
#### [Additional Built-in Functions](#additional-built-in-functions)
#### [Additional String Methods](#additional-string-methods)
#### [Sets](#sets)

## Overview

This cheatsheet outlines common syntax and concepts for problem-solving in Python. Use this as a reference for Unit 1 problems. This covers the most critical concepts but is not exhaustive. You'll be expected to know any required concepts from previous units.

---

## Standard Concepts

> ‼️ This material is in scope for the Standard Unit 1 assessment.

### Built-In Functions

### Print
```python
print(s)  # Prints the message s to the console
```

**Parameters:**
- `s`: the message you would like to print

**Example Usage:**
```python
# Example 1: Printing a string
print("Welcome to TIP102!")  # Prints "Welcome to TIP102!" to the console

# Example 2: Printing an integer
print(100)  # Prints 100 to the console

# Example 3: Printing a variable
s = "Welcome to CodePath!"
num = 7
print(s)    # Prints "Welcome to CodePath" to the console
print(num)  # Prints 7 to the console

# Example 4: Printing a list
lst = ["TIP101", "TIP102", "TIP103"]
print(lst)  # Prints ["TIP101", "TIP102", "TIP103"] to the console

# Example 5: Printing an expression
x = 5
y = 3
print(x + y)  # Prints 8 to the console
```

### Length
```python
len(s)  # Returns the length of a list or string
```

**Parameters:**
- `s`: the list or string we would like to get the length of

**Returns:** the number of items in a list or the number of characters in a string

**Example Usage:**
```python
# Example 1: Getting the length of a list
lst = ['a', 'b', 'c']
lst_length = len(lst) 
print(lst_length)  # Output: 3

# Example 2: Getting the length of string
s = 'abcd'
s_length = len(s)
print(s_length)  # Output: 4
```

### Range
```python
range(start, stop, step)  # Returns a sequence of numbers
```

**Parameters:**
- `start`: the first number in the sequence (optional, defaults to 0)
- `stop`: the last value in the sequence (exclusive, required)
- `step`: how much to increment each number (optional, defaults to 1)

**Example Usage:**
```python
# Example 1: Just the stop value 
range(10)  # Evaluates to: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# Example 2: Start and stop value
range(1, 11)  # Evaluates to: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# Example 3: Start, stop, and step value
range(0, 30, 5)  # Evaluates to: 0, 5, 10, 15, 20, 25
```

### Sum
```python
sum(x)  # Returns the sum of all values in a list
```

**Example:**
```python
sum([1, 2, 3, 4])  # Evaluates to 10
```

### Min
```python
min(x)  # Returns the argument with the lowest value or the item with the lowest value in a list
```

**Example Usage:**
```python
# Example 1: Minimum item in a list
min([2, 3, 4, 1, 5])  # Evaluates to 1

# Example 2: Argument with minimum value
min(5, 2, 3)  # Evaluates to 2

# Example 3: Smallest string
min(['a', 'b', 'c', 'aa'])  # Evaluates to 'a'
```

### Max
```python
max(x)  # Returns the argument with the highest value or the item with the highest value in a list
```

**Example Usage:**
```python
# Example 1: Maximum item in a list
max([2, 3, 5, 1, 4])  # Evaluates to 5

# Example 2: Argument with maximum value
max(5, 2, 3)  # Evaluates to 5

# Example 3: Maximum string
max(['a', 'b', 'c', 'aa'])  # Evaluates to 'c'
```

### List Methods & Syntax

### Append Method
```python
lst.append(item)  # Adds an item to the end of the list
```

**Parameters:**
- `item`: the item you would like to add to the list

**Example Usage:**
```python
# Example: Add an integer to the list
lst = [1, 2, 3, 4]
lst.append(5)
print(lst)  # Prints [1, 2, 3, 4, 5]
```

### Sort Method
```python
lst.sort()  # Sorts the list in ascending order
```

- Does not have any required parameters
- Does not return any value

**Example Usage:**
```python
# Example 1: List of integers
lst = [4, 2, 1, 3]
lst.sort()
print(lst)  # Prints [1, 2, 3, 4]

# Example 2: List of strings
lst = ['b', 'a', 'd', 'c']
lst.sort()
print(lst)  # Prints ['a', 'b', 'c', 'd']
```

### String Methods & Syntax

### Lower Method
```python
s.lower()  # Returns s as a lowercase string
```

- Accepts no parameters
- Returns a lowercase string

**Example Usage:**
```python
# Example 1: Mixed case
s = 'Hello World!'
lowered = s.lower()
print(lowered)  # Prints 'hello world!'

# Example 2: All uppercase
s = 'HELLO WORLD'
lowered = s.lower()
print(lowered)  # Prints 'hello world'
```

### Split Method
```python
s.split(separator)  # Splits the string into a list along whitespace or specified separator
```

**Parameters:**
- `separator`: The characters along which the string will be split (optional, defaults to whitespace)

**Returns:** a list of the substrings of s split by the specified separator

**Example Usage:**
```python
# Example 1: Split along whitespace
s = 'Never gonna give you up'
split = s.split()
print(split)  # Prints ['Never', 'gonna', 'give', 'you', 'up']

# Example 2: Split along specified separator
s = 'Never-gonna-let-you-down'
split = s.split("-")
print(split)  # Prints ['Never', 'gonna', 'let', 'you', 'down']
```

### Join Method
```python
s.join(x)  # Turns an iterable x into a string using s as a separator between elements
```

**Parameters:**
- `x`: the iterable whose items will be joined together into a string (required)

**Returns:** a string of the items in x separated by s

**Example Usage:**
```python
# Example 1: Join items in a list separated by space
lst = ['Never', 'gonna', 'run', 'around', 'and', 'desert', 'you']
joined = ' '.join(lst)
print(joined)  # Prints 'Never gonna run around and desert you'

# Example 2: Join items in a list separated by dash
lst = ['Never', 'gonna', 'make', 'you', 'cry']
joined = '-'.join(lst)
print(joined)  # Prints 'Never-gonna-make-you-cry'
```

### Strip Method
```python
s.strip(characters)  # Removes whitespace or specified characters from either end of the string
```

**Parameters:**
- `characters`: the characters/substring to remove from either end of s (optional, defaults to whitespace)

**Returns:** the string s with whitespace or characters removed

**Example Usage:**
```python
# Example 1: Strip whitespace
s = '       Never gonna say goodbye       '
stripped = s.strip()
print(stripped)  # Prints 'Never gonna say goodbye'

# Example 2: Strip question marks
s = '????Never gonna tell a lie and hurt you?????'
stripped = s.strip('?')
print(stripped)  # Prints 'Never gonna tell a lie and hurt you'
```

### Python Syntax

### Variables

In Python, variables do not need to be declared using a keyword. We simply create variables by giving them a name and assigning a value.

Variable names use snake_case and should have underscores between words.

**Example Usage:**
```python
# Example 1: Integer variable
var1 = 10

# Example 2: String Variable
var2 = "Codepath"

# Example 3: Boolean Variable
my_boolean = True

print(var1)        # Prints 10
print(var2)        # Prints 'Codepath'
print(my_boolean)  # Prints True
```

Python variables are dynamically typed, meaning we do not need to specify the type when declaring it, and the variable type can change over time.

**Example Usage:**
```python
# Example: Changing x from an int to a string
x = 10
print(x)  # Prints 10

x = "Hello"
print(x)  # Prints 'Hello'
```

### Conditionals

In Python, conditionals are defined using the `if`, `elif` and `else` keywords. The body of the conditional will execute if the expression evaluates to `True`.

**Example Usage:**
```python
# Example 1: Simple if statement
x = 3
if x > 1:
    print("This line will execute!")

if x > 5:
    print("This line will not execute!")

# Output: 'This line will execute!'

# Example 2: If-Elif statement
x = 10
y = 20

if x > y:
    print("x is greater than y")
elif y > x:
    print("y is greater than x")

# Output: 'y is greater than x'

# Example 3: If-Elif-Else statement
x = 20
y = 20

if x > y:
    print("x is greater than y")
elif y > x:
    print("y is greater than x")
else:
    print("x and y are equal")

# Output: 'x and y are equal'
```

### Functions

In Python, functions are defined using the `def` keyword.

**Example Usage:**
```python
# Example: Function that prints Hello world!
def function_example():
    print("Hello world!")
```

Functions can be called by writing the function name followed by parentheses.

**Example Usage:**
```python
# Example: Calling a function
function_example()  # Prints 'Hello world!'
```

We can add parameters to our function by placing them inside the parentheses separated by commas.

**Example Usage:**
```python
# Example: Function with 2 parameters
def function_w_parameters(parameter1, parameter2):
    print("Parameter 1: ", parameter1)
    print("Parameter 2: ", parameter2)

function_w_parameters("Interview", "Prep")
# Output:
# Parameter 1: Interview
# Parameter 2: Prep
```

We can return a value using the `return` keyword. By default, a function returns `None`.

**Example Usage:**
```python
# Example: Function that returns sum of two numbers
def sum(a, b):
    return a + b

# Example: Function without a return value
def sum_without_returning(a, b):
    a + b

return_val1 = sum(4, 2)
return_val2 = sum_without_returning(4, 2)
print(return_val1)  # Output: 6
print(return_val2)  # Output: None
```

### Formatted Strings

Formatted strings or f-strings allow us to insert variable expressions into Python strings.

To create an f-string, place `f` before the quotation marks and add curly brackets around any variables.

**Example Usage:**
```python
# Example 1: Adding a variable to a string
name = "Michael"
print(f"Welcome to Codepath, {name}!")  # Prints 'Welcome to CodePath, Michael!'

# Example 2: Adding an expression to a string
a = 3
b = 5
print(f"The sum of {a} and {b} is {a + b}")  # Prints 'The sum of 3 and 5 is 8'
```

### Remainder Division

The `%` operator is also known as the modulo operator and performs remainder division. `x % y` returns the remainder after dividing x by y.

**Example Usage:**
```python
print(5 % 2)   # Prints 1 because 5 / 2 = 2 remainder 1
print(10 % 2)  # Prints 0 because 10 / 2 = 5 remainder 0
```

### For Loops

```python
for num in nums:  # Iterates through every number in nums
```

For loops allow you to iterate over a sequence (such as a list, string, or range) and execute a block of code multiple times.

**Example Usage:**
```python
# Example 1: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Outputs each fruit on a new line

# Example 2: Using a for loop with a range
for i in range(5):
    print(i)  # Prints numbers 0 to 4
```

### While Loops

```python
while condition:  # Iterates while the condition evaluates to True
```

While loops allow you to repeat a block of code so long as a condition evaluates to `True`. This is useful when the number of iterations is not predetermined.

**Example Usage:**
```python
# Example 1: Indeterminate number of iterations
user_input = ""
while user_input != "quit":
    user_input = input("Enter a command (type 'quit' to exit): ")
print("You exited the loop.")

# Example 2: Processing data until a condition is met
i = 1
while i < 6:
    print(i)  
    i += 1 
```

**Important Notes:**
- You must create any variables that are part of the conditions yourself
- You must ensure your loop body makes progress towards termination to avoid infinite loops

```python
# Example: Infinite Loop (DON'T DO THIS)
i = 1
while i < 6:
    print(i)
# Because i never increments, this will run forever
```

### Comparing Strings and Lists

#### Similarities
- **Ordered sequences**: Both are ordered sequences of data
- **Indexed by Integers**: Both can be indexed using integers (e.g. `lst[0]` or `s[0]`)
- **Sliceable**: Both can be sliced to access subsections (e.g. `lst[1:3]` or `s[1:3]`)
- **Iterable**: Both can be looped over using a for loop
- **Length**: We can use `len()` function to get the length of either

#### Differences

**Content Type:**
- **Strings**: ordered sequence of character elements only
- **Lists**: ordered sequence of elements that can be of any type (integers, strings, other lists, etc.)

**Mutability:**
- **Strings**: immutable (not changeable)
```python
s = 'Try'
s[0] = 'C'  # Results in TypeError: 'str' object does not support item assignment
```

- **Lists**: mutable (changeable)
```python
lst = ['T', 'r', 'y']
lst[0] = 'C'
print(lst)  # Prints ['C', 'r', 'y'] 
```

---

## Advanced Concepts

> ‼️ This material is in scope for the Advanced Unit 1 assessment. The Standard material above is also in scope for Advanced assessments.

### Built-in Functions

### Enumerate
```python
enumerate(x)  # Takes an iterable and adds a counter to it
```

**Parameters:**
- `x`: an iterable object such as a list, dictionary, or string (required)
- `start`: the value to start the counter at (optional, defaults to 0)

**Returns:** a sequence of numbers coupled with values in given iterable

**Example Usage:**
```python
# Example 1: Iterating over indices and characters in a string
my_string = 'code'
for index, char in enumerate(my_string):
    print(index, char)

# Prints:
# 0 c
# 1 o
# 2 d
# 3 e

# Example 2: Enumerate with start value specified
cereals = ['cheerios', 'fruity pebbles', 'cocoa puffs']
for count, cereal in enumerate(cereals, start=1):
    print(count, cereal)

# Prints:
# 1 cheerios
# 2 fruity pebbles
# 3 cocoa puffs
```

### Zip
```python
zip(x, y)  # Takes two or more iterables and returns a sequence of tuples
```

**Parameters:**
- `x`, `y`: iterable objects such as lists, dictionaries, or strings
- Optionally accepts additional iterables

**Returns:** a sequence of tuples pairing x[i] with y[i] where 0 <= i <= min(len(x), len(y))

**Example Usage:**
```python
# Example 1: Zipping Two Lists
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
zipped = zip(names, ages)
print(list(zipped))  # Prints [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Example 2: Zipping Lists of Different Lengths
names = ['Alice', 'Bob', 'Charlie', 'David']
ages = [25, 30, 35]
zipped = zip(names, ages)
print(list(zipped))  # Prints [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

### Python Syntax

### Nested Lists

Lists can store other lists. The container list is the **outer list**, while each nested list is an **inner list**.

**Example Usage:**
```python
# Simple List
singers = ["Sabrina Carpenter", "FKA Twigs", "Elliot Smith"]

# Nested List
albums = [
    ["Sabrina Carpenter", "Short n' Sweet"], 
    ["FKA Twigs", "Magdalene"],
    ["Elliot Smith", "Either/Or"]
]

# Nested Lists Where Inner Lists Have Unequal Length
numbers = [
    [1],
    [1, 2],
    [1, 2, 3]
]

# Triply Nested List
water_levels = ["Shallow", ["Deep", ["Deeper"]]]
```

**Dimensions:**
- **1D list**: Simple list like `singers`
- **2D list**: List of lists like `albums` or `numbers`
- **Matrix**: 2D list where each inner list has the same length

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

**Accessing Elements:**
```python
# Accessing inner lists
albums = [
    ["Sabrina Carpenter", "Short n' Sweet"], 
    ["FKA Twigs", "Magdalene"],
    ["Elliot Smith", "Either/Or"]
]

first_album = albums[0]
print(first_album)  # Output: ["Sabrina Carpenter", "Short n' Sweet"]

# Accessing elements within inner lists
fka_twigs = albums[1][0]
print(fka_twigs)  # Output: FKA Twigs

# Updating elements
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[1][1] = "Surprise!"
print(matrix)  # Output: [[1, 2, 3], [4, 'Surprise!', 6], [7, 8, 9]]
```

### Nested Loops

A nested loop means a loop within a loop. They allow us to perform repeated actions within repeated actions.

When we nest loops, the inner loop runs completely every time the outer loop runs once.

**Example Usage:**
```python
for i in range(1, 4):
    print("Outer loop incremented")
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")

# Output:
# Outer loop incremented
# i = 1, j = 1
# i = 1, j = 2
# i = 1, j = 3
# Outer loop incremented
# i = 2, j = 1
# i = 2, j = 2
# i = 2, j = 3
# Outer loop incremented
# i = 3, j = 1
# i = 3, j = 2
# i = 3, j = 3
```

**Iterating over Matrices:**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Using nested loops to iterate over the matrix
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()  # Print a new line after each row

# Output:
# 1 2 3 
# 4 5 6 
# 7 8 9 
```

**Mixed Loop Types:**
```python
numbers = [3, 5, 2]

# Outer for loop iterates over each number in the list
for num in numbers:
    print(f"Counting down from {num}:")
    
    # Inner while loop counts down from the current number to 0
    while num >= 0:
        print(num)
        num -= 1
    
    print("---")
```

> ⚠️ **Performance Warning**: Nested loops can significantly increase execution time, especially with large inputs or deep nesting. Consider alternatives when possible.

### List Comprehensions

```python
result_list = [expression for element in lst]  # Evaluates expression on each element
```

List comprehensions provide shorthand syntax for creating a new list using values of an existing list.

**Traditional approach:**
```python
nums = [1, 2, 3, 4, 5]
doubled = []

for num in nums:
    doubled.append(num * 2)

print(doubled)  # Output: [2, 4, 6, 8, 10]
```

**List comprehension:**
```python
nums = [1, 2, 3, 4, 5]
doubled = [value * 2 for value in nums]
print(doubled)  # Output: [2, 4, 6, 8, 10]
```

**With Conditions:**
```python
result_list = [expression for element in lst if condition]
```

**Traditional approach:**
```python
words = ["I", "Love", "Codepath!"]
result = []

for word in words:
    if len(word) > 5:
        result.append(word)

print(result)  # Output: ['Codepath!']
```

**List comprehension with condition:**
```python
words = ["I", "Love", "Codepath!"]
result = [word for word in words if len(word) > 5]
print(result)  # Output: ['Codepath!']
```

### Two Pointer Technique

The two-pointer approach uses two pointer variables to track different indices in a list or string, moving them based on certain conditions.

### Opposite Direction Pointers

Initialize one pointer at the beginning and another at the end, then move them inwards toward each other.

**Example: Reversing a list**
```python
def reverse_list(arr):
    left_pointer = 0
    right_pointer = len(arr) - 1
    
    while left_pointer < right_pointer:
        # Swap elements
        arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
        left_pointer += 1
        right_pointer -= 1
    
    return arr
```

**Template:**
```python
left_pointer = 0
right_pointer = len(word) - 1
while left_pointer < right_pointer:
    # Process elements at both pointers
    left_pointer += 1
    right_pointer -= 1
```

### Same Direction Pointers

Point one pointer at the beginning of one list and another pointer at the beginning of a second list, incrementing each conditionally.

**Example: Merging two sorted lists**
```python
def merge_sorted_lists(nums1, nums2):
    nums1_pointer = 0
    nums2_pointer = 0
    merged = []
    
    while nums1_pointer < len(nums1) and nums2_pointer < len(nums2):
        if nums1[nums1_pointer] <= nums2[nums2_pointer]:
            merged.append(nums1[nums1_pointer])
            nums1_pointer += 1
        else:
            merged.append(nums2[nums2_pointer])
            nums2_pointer += 1
    
    # Add remaining elements
    while nums1_pointer < len(nums1):
        merged.append(nums1[nums1_pointer])
        nums1_pointer += 1
    
    while nums2_pointer < len(nums2):
        merged.append(nums2[nums2_pointer])
        nums2_pointer += 1
    
    return merged
```

**Template:**
```python
nums1_pointer = 0
nums2_pointer = 0

while nums1_pointer < len(nums1) and nums2_pointer < len(nums2):
    if condition:
        # operation
        nums1_pointer += 1
    else:
        # operation
        nums2_pointer += 1
```

### When to Use Two-Pointer Technique

**Data Structure Indicators:**
- Strings, arrays, and linked lists

**Problem Type Indicators:**
- **Reducing Nested Loops**: Can improve solutions that use multiple for loops
- **Searching for Pairs/Triplets**: Finding pairs or triplets in sorted arrays (e.g., Two Sum Problem)
- **In Place Operations**: Performing operations without extra data structures (e.g., Removing Duplicates)
- **Comparing Opposite Ends**: Processing elements from both ends (e.g., Valid Palindrome)
- **Partitioning Problems**: Dividing data into multiple parts

---

## Bonus Syntax & Concepts

> 💡 These concepts are nice to know but not required for Unit 1 problems. They are **not in scope** for either Standard or Advanced assessments.

### Additional List Methods
```python
lst.insert(x, item)   # Inserts item into list at index x
lst.remove(item)      # Removes item from list
lst.pop(x)           # Removes element at index x from list
lst.copy()           # Creates a copy of a list
```

### Additional Built-in Functions
```python
abs(x)               # Returns the absolute value of number x
```

### Additional String Methods
```python
s.isalpha()          # Returns True if all characters are alphabetic letters (a-z)
s.isalnum()          # Returns True if all characters are alphanumeric (a-z or 0-9)
s.find(x)            # Returns start index of first occurrence of substring x (-1 if not found)
s.count(x)           # Returns frequency of substring x in the string
```

### Sets
A useful data type for grouping multiple pieces of data. Data in sets is unordered, unchangeable, and cannot contain duplicates.

```python
# Creating a set
my_set = {1, 2, 3, 4, 5}
unique_letters = set("hello")  # {'h', 'e', 'l', 'o'}

# Set operations
my_set.add(6)         # Add element
my_set.remove(1)      # Remove element
len(my_set)           # Get size
3 in my_set           # Check membership
```