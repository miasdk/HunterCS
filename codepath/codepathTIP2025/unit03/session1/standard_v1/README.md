# Standard Problem Set

## Table of Contents

### [Problems 1-7](#problems-1-7)
- [Problem 1: Valid Parentheses](#problem-1-valid-parentheses)
- [Problem 2: Reverse Array with Stack](#problem-2-reverse-array-with-stack)
- [Problem 3: Valid Palindrome](#problem-3-valid-palindrome)
- [Problem 4: Squares of Sorted Array](#problem-4-squares-of-sorted-array)
- [Problem 5: Remove Adjacent Duplicates](#problem-5-remove-adjacent-duplicates)
- [Problem 6: Reverse Words in String](#problem-6-reverse-words-in-string)
- [Problem 7: Backspace String Compare](#problem-7-backspace-string-compare)

### [Problems 8-14](#problems-8-14)
- [Problem 8: Time in Queue](#problem-8-time-in-queue)
- [Problem 9: Reverse Array In-Place](#problem-9-reverse-array-in-place)
- [Problem 10: Remove All Adjacent Duplicates](#problem-10-remove-all-adjacent-duplicates)
- [Problem 11: Minimum Average of Min-Max Pairs](#problem-11-minimum-average-of-min-max-pairs)
- [Problem 12: Remove String Pairs](#problem-12-remove-string-pairs)
- [Problem 13: Array Operations with Zeros](#problem-13-array-operations-with-zeros)
- [Problem 14: Make Palindrome Lexicographically Smallest](#problem-14-make-palindrome-lexicographically-smallest)

---

## Problems 1-7

### Problem 1: Valid Parentheses

Given a string containing only `()`, `[]`, and `{}`, determine if the string is valid. A string is valid if brackets are properly opened and closed in the correct order.

**Function Signature:**
```python
def is_valid_post_format(posts):
    pass
```

**Example Usage:**
```python
print(is_valid_post_format("()"))        # True
print(is_valid_post_format("()[]{}"))    # True
print(is_valid_post_format("(]"))        # False
```

**✨ AI Hint:** Stacks  
**💡 Hint:** Pseudocode

---

### Problem 2: Reverse Array with Stack

Given an array of strings, return the array in reverse order using a stack.

**Function Signature:**
```python
def reverse_comments_queue(comments):
    pass
```

**Example Usage:**
```python
print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
# ['Thanks for sharing.', 'Love it!', 'Great post!']

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
# ['Well written.', 'Interesting read.', 'First!']
```

---

### Problem 3: Valid Palindrome

Given a string, determine if it's a palindrome when ignoring spaces, punctuation, and case. Use the two-pointer method.

**Function Signature:**
```python
def is_symmetrical_title(title):
    pass
```

**Example Usage:**
```python
print(is_symmetrical_title("A Santa at NASA"))    # True
print(is_symmetrical_title("Social Media"))       # False
```

**💡 Hint:** Two Pointer Technique

---

### Problem 4: Squares of Sorted Array

Given an integer array sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

**Your Task:**
1. Read through the existing solution and add comments
2. Modify the solution to use the two-pointer technique

**Existing Solution to Analyze:**
```python
def engagement_boost(engagements):
    squared_engagements = []
    
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    squared_engagements.sort(reverse=True)
    
    result = [0] * len(engagements)
    position = len(engagements) - 1
    
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return result
```

**Example Usage:**
```python
print(engagement_boost([-4, -1, 0, 3, 10]))    # [0, 1, 9, 16, 100]
print(engagement_boost([-7, -3, 2, 3, 11]))    # [4, 9, 9, 49, 121]
```

---

### Problem 5: Remove Adjacent Duplicates

Given a string of lowercase and uppercase letters, remove adjacent pairs where one is lowercase and the other is uppercase of the same letter. Keep removing until no more pairs exist.

**Function Signature:**
```python
def clean_post(post):
    pass
```

**Example Usage:**
```python
print(clean_post("poOost"))     # "post"
print(clean_post("abBAcC"))     # ""
print(clean_post("s"))          # "s"
```

**💡 Hint:** Choosing the Right Approach  
**💡 Hint:** Useful Built-In Methods

---

### Problem 6: Reverse Words in String

Given a string, reverse the order of characters in each word while preserving whitespace and word order. Use a queue.

**Function Signature:**
```python
def edit_post(post):
    pass
```

**Example Usage:**
```python
print(edit_post("Boost your engagement with these tips"))
# "tsooB ruoy tnemegagn htiw eseht spit"

print(edit_post("Check out my latest vlog"))
# "kcehC tuo ym tsetal golv"
```

**✨ AI Hint:** Queues

---

### Problem 7: Backspace String Compare

Given two strings where `#` represents a backspace character, determine if they are equal after processing all backspaces.

**Function Signature:**
```python
def post_compare(draft1, draft2):
    pass
```

**Example Usage:**
```python
print(post_compare("ab#c", "ad#c"))     # True
print(post_compare("ab##", "c#d#"))     # True
print(post_compare("a#c", "b"))         # False
```

**💡 Hint:** Helper Functions

---

## Problems 8-14

### Problem 8: Time in Queue

There are n users in a queue. Each user has a number of items to process. Users process one item at a time and go to the back of the queue if they have more items. Return the time for user at position k to finish all their items.

**Function Signature:**
```python
def time_required_to_stream(movies, k):
    pass
```

**Example Usage:**
```python
print(time_required_to_stream([2, 3, 2], 2))    # 6
print(time_required_to_stream([5, 1, 1, 1], 0)) # 8
```

**✨ AI Hint:** Queues  
**💡 Hint:** Pseudocode

---

### Problem 9: Reverse Array In-Place

Given an array, reverse it in-place using the two-pointer approach. Do not use list slicing.

**Function Signature:**
```python
def reverse_watchlist(watchlist):
    pass
```

**Example Usage:**
```python
watchlist = ["Breaking Bad", "Stranger Things", "The Crown", "The Witcher"]
print(reverse_watchlist(watchlist))
# ['The Witcher', 'The Crown', 'Stranger Things', 'Breaking Bad']
```

**💡 Hint:** Two Pointer Technique

---

### Problem 10: Remove All Adjacent Duplicates

Given a string, repeatedly remove adjacent duplicate characters until no more can be removed.

**Function Signature:**
```python
def remove_duplicate_shows(schedule):
    pass
```

**Example Usage:**
```python
print(remove_duplicate_shows("abbaca"))    # "ca"
print(remove_duplicate_shows("azxxzy"))    # "ay"
```

**✨ AI Hint:** Stacks  
**💡 Hint:** Pseudocode

---

### Problem 11: Minimum Average of Min-Max Pairs

Given an array of n integers (n is even), repeatedly remove the minimum and maximum elements and calculate their average. Return the minimum of all averages.

**Function Signature:**
```python
def minimum_average_view_count(view_counts):
    pass
```

**Example Usage:**
```python
print(minimum_average_view_count([7, 8, 3, 4, 15, 13, 4, 1]))   # 5.5
print(minimum_average_view_count([1, 9, 8, 3, 10, 5]))          # 5.5
print(minimum_average_view_count([1, 2, 3, 7, 8, 9]))           # 5.0
```

---

### Problem 12: Remove String Pairs

Given a string of uppercase letters, remove all occurrences of "AB" or "CD" pairs. Return the minimum possible length after all removals.

**Function Signature:**
```python
def min_remaining_watchlist(watchlist):
    pass
```

**Example Usage:**
```python
print(min_remaining_watchlist("ABFCACDB"))    # 2
print(min_remaining_watchlist("ACBBD"))       # 5
```

---

### Problem 13: Array Operations with Zeros

Given an array of non-negative integers, apply n-1 operations: if `arr[i] == arr[i+1]`, multiply `arr[i]` by 2 and set `arr[i+1]` to 0. After all operations, shift all zeros to the end.

**Function Signature:**
```python
def apply_rating_operations(ratings):
    pass
```

**Example Usage:**
```python
print(apply_rating_operations([1, 2, 2, 1, 1, 0]))    # [1, 4, 2, 0, 0, 0]
print(apply_rating_operations([0, 1]))                 # [1, 0]
```

---

### Problem 14: Make Palindrome Lexicographically Smallest

Given a string of lowercase letters, make it a palindrome with minimum operations. If multiple palindromes are possible, return the lexicographically smallest one.

**Implement the following pseudocode:**

1. Convert string to list
2. Initialize left pointer at start, right pointer at end
3. While left < right:
   - If characters differ, replace the lexicographically larger one with the smaller one
   - Move pointers inward
4. Convert back to string and return

**Function Signature:**
```python
def make_smallest_watchlist(watchlist):
    pass
```

**Example Usage:**
```python
print(make_smallest_watchlist("egcfe"))     # "efcfe"
print(make_smallest_watchlist("abcd"))      # "abba"
print(make_smallest_watchlist("seven"))     # "neven"
```