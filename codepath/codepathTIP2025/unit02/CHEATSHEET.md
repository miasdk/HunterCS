# Unit 2 Cheatsheet

## Table of Contents

### [Overview](#overview)

### [Standard Concepts](#standard-concepts)
#### [Built-In Functions](#built-in-functions)
- [Type Casting](#type-casting)
- [Infinity](#infinity)
- [Round Function](#round-function)
- [Absolute Value Function](#absolute-value-function)
- [Enumerate](#enumerate)
- [Zip](#zip)

#### [Dictionary Methods & Syntax](#dictionary-methods--syntax)
- [Setting and Updating Values](#setting-and-updating-values)
- [Accessing Elements](#accessing-elements)
- [Pop Method](#pop-method)
- [Keys Method](#keys-method)
- [Values Method](#values-method)
- [Items Method](#items-method)

#### [Python Syntax](#python-syntax)
- [Nested Data Structures](#nested-data-structures)
- [Nested Loops](#nested-loops)
- [Sets](#sets)

### [Advanced Concepts](#advanced-concepts)
#### [Built-In Functions](#built-in-functions-1)
- [Sorted](#sorted)

#### [Python Syntax](#python-syntax-1)
- [Lambda Functions](#lambda-functions)
- [Ternary Operators](#ternary-operators)
- [Dictionary Comprehensions](#dictionary-comprehensions)
- [Tuples](#tuples)

### [Bonus Syntax & Concepts](#bonus-syntax--concepts)

## Overview

This cheatsheet outlines common syntax and concepts for problem-solving in Python Unit 2. Use this as a reference while you solve the breakout problems for Unit 2. This covers the most critical concepts but is not exhaustive. You are expected to know any required concepts from previous units.

---

## Standard Concepts

> ‼️ This material is in scope for the Standard Unit 2 assessment.

### Built-In Functions

### Type Casting

Type casting is the process of transforming or 'casting' data from one type into another type.

#### int(x)
```python
int(x)  # Casts a float or string to an integer
```

**Parameters:**
- `x`: the float or string to turn into an integer
- Floats will be rounded down

**Returns:** x as an integer

**Example Usage:**
```python
x = int(2.5)    # x will be 2
y = int("5")    # y will be 5
```

#### float(x)
```python
float(x)  # Cast an integer or string to a floating point number
```

**Parameters:**
- `x`: the integer or string to turn into a float

**Returns:** x as a float

**Example Usage:**
```python
x = float(2)      # x will be 2.0
y = float("5")    # y will be 5.0
z = float("5.3")  # z will be 5.3
```

#### str(x)
```python
str(x)  # Transform a data type into a string
```

**Parameters:**
- `x`: a data type, commonly an integer, to turn into a string
- `x` can also be more complex data types like lists or dictionaries!

**Returns:** x as a string

**Example Usage:**
```python
x = str(2)              # x will be "2"
y = str(2.0)            # y will be "2.0"
z = str([1, 2, 3, 4])   # z will be "[1, 2, 3, 4]"
```

### Infinity

We can represent positive and negative infinity with the following syntax:

```python
positive_infinity = float('inf')
negative_infinity = float('-inf')
```

Infinity is often used as an initial value when finding some unknown value, especially a minimum or maximum value.

**Example Usage:**
```python
lst = [5, 4, 3, 2, 1]

def get_min(lst):   
    minimum = float('inf')
    for num in lst:
        if num < minimum:
            minimum = num
    return minimum
```

In the above example, infinity is used to find the minimum value in a list of numbers. We assume the minimum is the largest number possible (infinity), then update our assumption as we iterate through the list and find values lower than infinity.

Infinity is also commonly used as a return value to handle edge cases.

**Example Usage:**
```python
def safe_divide(a, b):
    if b == 0:
        if a > 0:
            return float('inf')
        else:
            return float('-inf')
    return a / b
```

In the above example infinity is used to gracefully handle cases where a user tries to divide a number by zero. Normally, dividing a number by zero would result in Python raising a ZeroDivisionError.

### Round Function

```python
round(number, decimal)  # Returns a given number rounded to the specified decimal
```

**Parameters:**
- `number`: the number to be rounded (required)
- `decimal`: number of decimals to include in the rounded number (optional, defaults to 0)

**Returns:** the rounded number

**Example Usage:**
```python
# Example 1: Round to hundredth
x = 3.14159
rounded = round(x, 2)
print(rounded)  # Prints 3.14

# Example 2: Round to nearest whole number
x = 3.14159
rounded = round(x)
print(rounded)  # Prints 3
```

### Absolute Value Function

```python
abs(number)  # Returns the absolute value of a number
```

The absolute value is its distance from 0 on a numberline and is mathematically denoted as |x|.

**Parameters:**
- `number`: the number to find the absolute value of (required)

**Returns:** number's absolute value

**Example Usage:**
```python
# Example 1: Absolute value of a positive integer
absolute_value = abs(5)
print(absolute_value)  # Prints 5

# Example 2: Absolute value of a negative integer
absolute_value = abs(-5)
print(absolute_value)  # Prints 5

# Example 3: Absolute value of a float
absolute_value = abs(-3.14)
print(absolute_value)  # 3.14
```

### Enumerate

```python
enumerate(x)  # Takes an iterable and adds a counter to the function
```

It is often used to loop over the indices and values of an iterable simultaneously.

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

Zip is useful for iterating over multiple iterables in parallel or for combining data from separate iterables.

**Parameters:**
- `x`: an iterable object such as a list, dictionary, or string
- `y`: an iterable object such as a list, dictionary, or string
- Optionally accepts additional iterables to zip with x and y

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

### Dictionary Methods & Syntax

### Setting and Updating Values

You can add new key-value pairs or update the value of an existing key using the assignment operator `=`. If the key does not exist, a new key-value pair is added to the dictionary.

**Example Usage:**
```python
d = {'a': 1, 'b': 2, 'c': 3}

d['d'] = 4          # Adds a new key 'd' with value 4
print(d)            # Outputs: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

d['a'] = 100        # Updates the value of key 'a'
print(d)            # Outputs: {'a': 100, 'b': 2, 'c': 3, 'd': 4}
```

### Accessing Elements

Dictionaries in Python allow you to access values using the keys. This can be done primarily in two ways:

#### Method 1: Direct access by Key

You can access the value associated with a specific key directly using square brackets `[]`. If the key is not found, this will raise a KeyError.

**Example Usage:**
```python
d = {'a': 1, 'b': 2, 'c': 3}
print(d['a'])  # Outputs: 1
print(d['b'])  # Outputs: 2
```

#### Method 2: Using the get() Method

```python
d.get(key, default_val)  # Returns the value of the item with the specified key
```

Alternatively, you can use the `get()` method, which provides a safer way to access values. The `get()` method returns `None` if the key is not found, or a default value that you can specify.

**Parameters:**
- `key`: the key of the value you want to access (required)
- `default_val`: default value to return if the specified key does not exist (optional, defaults to None)

**Returns:** the value of item paired with key

**Example Usage:**
```python
d = {'a': 1, 'b': 2, 'c': 3}
print(d.get('a'))              # Outputs: 1
print(d.get('z'))              # Outputs: None
print(d.get('z', 'Not Found')) # Outputs: 'Not Found'
```

### Pop Method

```python
d.pop(key, default_val)  # Removes and returns the value of the specified key
```

**Parameters:**
- `key`: the key of the item you want to remove (required)
- `default_val`: default value to return if the specified key does not exist (optional, raises KeyError if not specified)

**Returns:** the value of the removed item

**Example Usage:**
```python
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Example 1: Pop without default_val
d.pop('a')  # Returns 1
print(d)    # Prints {'b': 2, 'c': 3, 'd': 4}
# d.pop('e')  # Raises KeyError

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Example 2: Pop with default_val
d.pop('a', None)  # Returns 1
print(d)          # Prints {'b': 2, 'c': 3, 'd': 4}
d.pop('e', None)  # Returns None
print(d)          # Prints {'b': 2, 'c': 3, 'd': 4}
```

### Keys Method

```python
d.keys()  # Returns a list of the keys in the dictionary
```

- Does not have any required parameters
- Returns a list of keys in the specified dictionary

**Example Usage:**
```python
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

keys = d.keys()
print(keys)  # Prints dict_keys(['a', 'b', 'c', 'd'])
```

### Values Method

```python
d.values()  # Returns a list of the values in the dictionary
```

- Does not have any required parameters
- Returns a list of values in the specified dictionary

**Example Usage:**
```python
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

values = d.values()
print(values)  # Prints dict_values([1, 2, 3, 4])
```

### Items Method

```python
d.items()  # Returns a list of the key-value pairs in a dictionary
```

- Does not have any required parameters
- Returns a list of key-value pairs in the specified dictionary. Each key-value pair is represented as a tuple

**Example Usage:**
```python
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

items = d.items()
print(items)  # Prints dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
```

### Python Syntax

### Nested Data Structures

Lists and other data structures used to store multiple items in a single variable can be nested. This means that lists can store other lists.

The container list is referred to as the **outer list**, while each list nested inside is referred to as an **inner list**.

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

**Accessing and Modifying Lists:**
```python
# Example 1: Retrieving Album Data 
albums = [
    ["Sabrina Carpenter", "Short n' Sweet"], 
    ["FKA Twigs", "Magdalene"],
    ["Elliot Smith", "Either/Or"]
]

first_album = albums[0]
print(first_album)  # Output: ["Sabrina Carpenter", "Short n' Sweet"]

# Example 2: Updating a Row in a Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[2] = [100, 200, 300]
print(matrix)  # Output: [[1, 2, 3], [4, 5, 6], [100, 200, 300]]
```

**Multiple Indices:**
```python
# Example 1: Retrieving a Singer
albums = [
    ["Sabrina Carpenter", "Short n' Sweet"], 
    ["FKA Twigs", "Magdalene"],
    ["Elliot Smith", "Either/Or"]
]

fka_twigs = albums[1][0]
print(fka_twigs)  # Output: FKA Twigs

# Example 2: Updating a cell in a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[1][1] = "Surprise!"
print(matrix)  # Output: [[1, 2, 3], [4, 'Surprise!', 6], [7, 8, 9]]
```

**Nested Dictionaries and Mixed Structures:**
```python
# Example 1: Nested Dictionaries
address_book = {
    "John Doe": {
        "phone": "555-1234",
        "email": "johndoe@example.com",
        "address": {
            "street": "123 Maple Street",
            "city": "Springfield",
            "state": "IL",
            "zip": "62701"
        }
    },
    "Jane Smith": {
        "phone": "555-5678",
        "email": "janesmith@example.com",
        "address": {
            "street": "456 Oak Avenue",
            "city": "Shelbyville",
            "state": "IL",
            "zip": "62565"
        }
    }
}

john_email = address_book["John Doe"]["email"]
print(john_email)  # Output: 'johndoe@example.com'

# Example 2: List of Dictionaries
students = [
    {
        "name": "John Doe",
        "age": 16,
        "grade": "11th",
        "favorite_subject": "Math"
    },
    {
        "name": "Jane Smith",
        "age": 17,
        "grade": "12th",
        "favorite_subject": "English"
    },
    {
        "name": "Emily Johnson",
        "age": 16,
        "grade": "11th",
        "favorite_subject": "Biology"
    }
]

jane_age = students[1]["age"]
print(jane_age)  # Output: 17
```

### Nested Loops

Just as a nested list means a list within a list, a nested loop means a loop within a loop! They allow us to perform repeated actions within repeated actions.

When we nest loops, the inner loop will run completely every time the outer loop runs once.

Think of the outer loop as the short hour hand of an analog clock, and the inner loop as the longer minute hand. The minute hand has to complete a full rotation around the clock before the hour hand increments once.

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
        num -= 1  # Decrement the number by 1 each time
    
    print("---")  # Separator to indicate moving to the next number

# Output:
# Counting down from 3:
# 3
# 2
# 1
# 0
# ---
# Counting down from 5:
# 5
# 4
# 3
# 2
# 1
# 0
# ---
# Counting down from 2:
# 2
# 1
# 0
# ---
```

> ⚠️ **Performance Warning**: Nested loops can significantly increase execution time, especially with large inputs or deep nesting. Always consider whether there is an alternative solution before nesting loops deeply.

### Sets

Sets are a built-in data structure in Python that represent an unordered collection of unique elements. They are often used to track seen values, eliminate duplicates, and find overlap between multiple pieces of data.

**Set Characteristics:**
- **Unordered**: Sets do not maintain any particular order of elements (not indexed like lists or strings)
- **Unique elements**: Every element in a set must be unique. Duplicates are automatically removed
- **Mutable**: Sets can be modified. Values can be added or removed without creating a new set
- **Iterable**: Sets can be iterated over using a loop

**Creating Sets:**
```python
# Create a new Set
my_set = {1, 2, 3, 4}

# Using the set() function
another_set = set([1, 2, 3, 4])

# Creating an empty set
empty_set = set()  # Note: {} creates an empty dictionary, not a set
```

**Basic Set Operations:**
```python
my_set = {1, 2, 3}

my_set.add(4)       # {1, 2, 3, 4}
my_set.remove(2)    # {1, 3, 4}
# my_set.remove(5)  # Raises KeyError
my_set.discard(5)   # {1, 3, 4} - No error if element not found
my_set.clear()      # {}
```

**Set Mathematical Operations:**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union: Elements in either set
union_set = set1 | set2           # {1, 2, 3, 4, 5}

# Intersection: Elements common to both sets
intersection_set = set1 & set2    # {3}

# Difference: Elements in set1 but not in set2
difference_set = set1 - set2      # {1, 2}

# Symmetric Difference: Elements in either set, but not both
symmetric_difference_set = set1 ^ set2  # {1, 2, 4, 5}
```

---

## Advanced Concepts

> ‼️ This material is in scope for the Advanced Unit 2 assessment. The standard material above is also in scope for advanced assessments.

### Built-In Functions

### Sorted

```python
sorted(x)  # Returns a sorted list of the iterable x
```

**Parameters:**
- `x`: an iterable such as a list, dictionary, tuple, etc. to sort (required)
- `key`: a function that specifies a custom sorting order (optional, defaults to ascending order)
- `reverse`: True or False. If True, items will be sorted in descending order (optional, defaults to False)

**Returns:** x as a sorted list

**Example Usage:**
```python
# Example 1: Sorting a List in Ascending Order
lst = [1, 5, 3]
result = sorted(lst)
print(result)  # Output: [1, 3, 5]

# Example 2: Sorting a List in Descending Order
lst = [1, 5, 3]
result = sorted(lst, reverse=True)
print(result)  # Output: [5, 3, 1]

# Example 3: Sorting Keys in a Dictionary
my_dict = {'apple': 2, 'banana': 3, 'cherry': 1}
result = sorted(my_dict)
print(result)  # Output: ['apple', 'banana', 'cherry']

# Example 4: Sorting Strings by Length
words = ["apple", "orange", "banana", "grape"]
result = sorted(words, key=len)
print(result)  # Output: ['apple', 'grape', 'orange', 'banana']

# Example 5: Sorting By Last Character With a Custom Function
def last_character(s):
    return s[-1]

words = ["apple", "banana", "cherry", "date"]
result = sorted(words, key=last_character)
print(result)  # Output: ['banana', 'apple', 'date', 'cherry']
```

### Python Syntax

### Lambda Functions

```python
lambda arg1, arg2, etc.: expression  # Anonymous function that returns the result of evaluating expression
```

A lambda function is an anonymous function, meaning it is a function without a name.

**Example Usage:**
```python
# Example 1: Lambda Function with 1 Argument
return_value = lambda x: x + 10
print(return_value(100))  # Prints 110

# Example 2: Lambda Function with Multiple Arguments
return_value = lambda a, b: a + b
print(return_value(10, 20))  # Prints 30
```

Lambda functions are often used with the `sorted()` function to specify a custom sort key. Previously, we've seen that we can create a function to sort an iterable in a custom way.

**Example Usage:**
```python
# Example 1: Sorting By Last Character With a Custom Function (No Lambda)
def last_character(s):
    return s[-1]

words = ["apple", "banana", "cherry", "date"]
result = sorted(words, key=last_character)
print(result)  # Output: ['banana', 'apple', 'date', 'cherry']
```

With a lambda function, we can shorten this to:

```python
words = ["apple", "banana", "cherry", "date"]
result = sorted(words, key=lambda x: x[-1])
print(result)  # Output: ['banana', 'apple', 'date', 'cherry']
```

### Ternary Operators

A ternary operator is special shorthand syntax that allows us to write simple if-else conditions on a single line.

The general syntax for a single line if-else statement is:

```python
value_if_true if condition else value_if_false
```

**Example Usage:**
```python
a = 10
b = 20

# Ternary operator
max_value = a if a > b else b

# Normal conditional syntax equivalent
if a > b:
    max_value = a
else: 
    max_value = b
```

### Dictionary Comprehensions

```python
result_dict = {key_expression: value_expression for item in iterable}
```

Makes a dictionary pairing `key_expression` with `value_expression` on each element in an iterable and stores the result of each evaluation in `result_dict`.

Just as we can create lists based on values in other lists using a list comprehension, we can create new dictionaries based off of values in other dictionaries, lists or strings.

**Example Usage:**
```python
# Example 1: Map Integers to Their Square
lst = [1, 2, 3, 4, 5, 6]
squares = {x: x**2 for x in lst}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

# Example 2: Converting List of Tuples to a Dictionary
pairs = [('a', 1), ('b', 2), ('c', 3)]
dictionary = {key: value for key, value in pairs}
print(dictionary)  # {'a': 1, 'b': 2, 'c': 3}

# Example 3: Even Squares
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

### Tuples

A tuple is a data type used to store multiple items in a single variable. In most cases tuples are used to group together 2-3 items. Tuples that store 3 items are sometimes referred to as a 'triple'. Tuples are commonly used to store pairs of data together or return multiple values inside a function.

Tuples are defined using round brackets.

**Example Usage:**
```python
my_tuple = ("Mario", "Luigi")
print(my_tuple)  # Prints ("Mario", "Luigi")
```

Like lists and strings, we can use indices to access elements of a tuple:

**Example Usage:**
```python
my_tuple = ("Mario", "Luigi")
mario = my_tuple[0] 
luigi = my_tuple[1]
print(mario)  # Prints "Mario"
print(luigi)  # Prints "Luigi" 
```

Like strings, tuples are **immutable**, meaning we cannot update the contents of a tuple. If we update the contents of a tuple, we create a new tuple.

**Example Usage:**
```python
my_tuple = (10, 20)
# my_tuple[0] = 30  # Results in TypeError: 'tuple' object does not support item assignment
```

---

## Bonus Syntax & Concepts

> 💡 These concepts are nice to know but not required for Unit 2 problems. They are **not in scope** for either Standard or Advanced assessments.

### Additional Methods and Functions
```python
remove(x)       # Removes first element with value x from list
defaultdict()   # Creates a dictionary with default values for new or missing keys. Helps to avoid KeyErrors!
Counter(x)      # Creates a dictionary that stores elements of iterable x as keys and their counts as values
d.copy()        # Returns a copy of the dictionary d
```

### What's the difference between sorted() and sort()?

- **`sorted()`**: Returns a new sorted list, leaving the original unchanged
- **`sort()`**: Sorts the list in place, modifying the original list and returning `None`

```python
# Using sorted() - original list unchanged
original = [3, 1, 2]
new_list = sorted(original)
print(original)   # [3, 1, 2]
print(new_list)   # [1, 2, 3]

# Using sort() - original list modified
original = [3, 1, 2]
original.sort()
print(original)   # [1, 2, 3]
```