# Unit 5 Cheatsheet

## Overview
Here is a helpful cheatsheet outlining common syntax and concepts that will help you in your problem solving journey! Use this as reference as you solve the breakout problems for Unit 5. This is not an exhaustive list of all data structures, algorithmic techniques, and syntax you may encounter; it only covers the most critical concepts needed to ace Unit 5. In addition to the material below, you will be expected to know any required concepts from previous units. You may also find advanced concepts and bonus concepts included at the bottom of this page helpful for solving problem set questions, but you are not required to know them for the unit assessment.

---

## Standard Concepts

### Object Oriented Programming (OOP)
- Programming paradigm using objects and their interactions
- Objects have properties (variables) and methods (functions)

#### Classes
- Blueprints for custom data types
- Define properties and methods

```python
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
```

#### Instantiating a Class
- Use the class name to create an object
```python
my_dog = Dog('Fido', 'Cocker Spaniel', 'Ada Lovelace')
```

#### Accessing Properties and Methods
```python
print(my_dog.name)  # Access property
my_dog.call_dog()   # Call method
```

---

### Linked Lists
- Ordered collection of nodes, each with a value and a reference to the next node
- Not a built-in Python type; must define a class

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
```

#### Traversal
```python
def traverse(head):
    current = head
    while current:
        # Do something with current.value
        current = current.next
```

---

## Advanced Concepts

### Multiple Pass Technique
- Traverse a linked list multiple times for different purposes
- Example: Get length, then process nodes

### Temporary Head Technique
- Use a dummy node to simplify edge cases (e.g., deleting the head)

### Slow-Fast Pointer Technique
- Use two pointers moving at different speeds (e.g., cycle detection)

---

## Bonus Syntax & Concepts
- `lst.extend(x)`: Append all elements from x
- `lst.reverse()`: Reverse the list in place

--- 