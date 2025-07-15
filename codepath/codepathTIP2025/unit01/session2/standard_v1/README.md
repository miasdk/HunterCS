# Unit 01 Session 2 - Standard Version 1

## Overview
This problem set focuses on foundational Python concepts and problem-solving skills for Unit 01, Session 2 (Standard, Version 1).

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

# Coding Problems Reference

## Table of Contents

### [Version 1 Standard Set](#version-1-standard-set)
- [Problem 1: Reverse Sentence](#problem-1-reverse-sentence)
- [Problem 2: Goldilocks Number](#problem-2-goldilocks-number)
- [Problem 3: Delete Minimum](#problem-3-delete-minimum)
- [Problem 4: Sum of Digits](#problem-4-sum-of-digits)
- [Problem 5: Bouncy, Flouncy, Trouncy, Pouncy](#problem-5-bouncy-flouncy-trouncy-pouncy)
- [Problem 6: Acronym](#problem-6-acronym)
- [Problem 7: Good Things Come in Threes](#problem-7-good-things-come-in-threes)
- [Problem 8: Exclusive Elements](#problem-8-exclusive-elements)
- [Problem 9: Merge Strings Alternately](#problem-9-merge-strings-alternately)
- [Problem 10: Eeyore's House](#problem-10-eeyores-house)

### [Version 2 Standard Set](#version-2-standard-set)
- [Problem 1: String Array Equivalency](#problem-1-string-array-equivalency)
- [Problem 2: Count Even Strings](#problem-2-count-even-strings)
- [Problem 3: Secret Identity](#problem-3-secret-identity)
- [Problem 4: Count Digits](#problem-4-count-digits)
- [Problem 5: Move Zeroes](#problem-5-move-zeroes)
- [Problem 6: Reverse Vowels of a String](#problem-6-reverse-vowels-of-a-string)
- [Problem 7: Vantage Point](#problem-7-vantage-point)
- [Problem 8: Left and Right Sum Differences](#problem-8-left-and-right-sum-differences)
- [Problem 9: Common Cause](#problem-9-common-cause)
- [Problem 10: Exposing Superman](#problem-10-exposing-superman)

---

## Version 1 Standard Set

### Problem 1: Reverse Sentence

Write a function `reverse_sentence()` that takes in a string sentence and returns the sentence with the order of the words reversed. The sentence will contain only alphabetic characters and spaces to separate the words. If there is only one word in the sentence, the function should return the original string.

**Example Usage:**
```python
sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)  # Output: "fluff with stuffed all cubby little tubby"

sentence = "Pooh"
reverse_sentence(sentence)  # Output: "Pooh"
```

### Problem 2: Goldilocks Number

Write a function `goldilocks_approved(nums)` that takes a list of distinct positive integers and returns any number that is neither the minimum nor the maximum in the list. If no such number exists, return -1.

**Example Usage:**
```python
nums = [3, 2, 1, 4]
goldilocks_approved(nums)  # Output: 3 or 2

nums = [1, 2]
goldilocks_approved(nums)  # Output: -1

nums = [2, 1, 3]
goldilocks_approved(nums)  # Output: 2
```

### Problem 3: Delete Minimum

Pooh is eating all of his hunny jars in order of smallest to largest. Given a list of integers `hunny_jar_sizes`, write a function `delete_minimum_elements()` that continuously removes the minimum element until the list is empty. Return a new list of the elements of `hunny_jar_sizes` in the order in which they were removed.

**Example Usage:**
```python
hunny_jar_sizes = [5, 3, 2, 4, 1]
delete_minimum_elements(hunny_jar_sizes)  # Output: [1, 2, 3, 4, 5]

hunny_jar_sizes = [5, 2, 1, 8, 2]
delete_minimum_elements(hunny_jar_sizes)  # Output: [1, 2, 2, 5, 8]
```

### Problem 4: Sum of Digits

Write a function `sum_of_digits()` that accepts an integer num and returns the sum of num's digits.

**Example Usage:**
```python
num = 423
sum_of_digits(num)  # Output: 9

num = 4
sum_of_digits(num)  # Output: 4
```

### Problem 5: Bouncy, Flouncy, Trouncy, Pouncy

Tigger has developed a new programming language Tiger with only four operations and one variable `tigger`.

- `bouncy` and `flouncy` both increment the value of the variable `tigger` by 1
- `trouncy` and `pouncy` both decrement the value of the variable `tigger` by 1
- Initially, the value of `tigger` is 1 because he's the only tigger around! 

Given a list of strings `operations` containing a list of operations, return the final value of `tigger` after performing all the operations.

**Example Usage:**
```python
operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)  # Output: 2

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)  # Output: 4
```

### Problem 6: Acronym

Given an array of strings `words` and a string `s`, implement a function `is_acronym()` that returns `True` if `s` is an acronym of `words` and returns `False` otherwise.

The string `s` is considered an acronym of `words` if it can be formed by concatenating the first character of each string in `words` in order. For example, "pb" can be formed from ["pooh", "bear"], but it can't be formed from ["bear", "pooh"].

**Example Usage:**
```python
words = ["christopher", "robin", "milne"]
s = "crm"
is_acronym(words, s)  # Output: True
```

### Problem 7: Good Things Come in Threes

Write a function `make_divisible_by_3()` that accepts an integer array `nums`. In one operation, you can add or subtract 1 from any element of `nums`. Return the minimum number of operations to make all elements of `nums` divisible by 3.

**Example Usage:**
```python
nums = [1, 2, 3, 4]
make_divisible_by_3(nums)  # Output: 3

nums = [3, 6, 9]
make_divisible_by_3(nums)  # Output: 0
```

### Problem 8: Exclusive Elements

Given two lists `lst1` and `lst2`, write a function `exclusive_elemts()` that returns a new list that contains the elements which are in `lst1` but not in `lst2` and the elements that are in `lst2` but not in `lst1`.

**Example Usage:**
```python
lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
exclusive_elemts(lst1, lst2)  # Output: ["pooh", "roo", "eeyore", "owl"]

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
exclusive_elemts(lst1, lst2)  # Output: ["pooh", "roo", "piglet", "eeyore", "owl", "kanga"]

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
exclusive_elemts(lst1, lst2)  # Output: []
```

### Problem 9: Merge Strings Alternately

Write a function `merge_alternately()` that accepts two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

**Example Usage:**
```python
word1 = "wol"
word2 = "oze"
merge_alternately(word1, word2)  # Output: "woozle"

word1 = "hfa"
word2 = "eflump"
merge_alternately(word1, word2)  # Output: "heffalump"

word1 = "eyre"
word2 = "eo"
merge_alternately(word1, word2)  # Output: "eeyore"
```

### Problem 10: Eeyore's House

Eeyore has collected two piles of sticks to rebuild his house and needs to choose pairs of sticks whose lengths are the right proportion. Write a function `good_pairs()` that accepts two integer arrays `pile1` and `pile2` where each integer represents the length of a stick. The function also accepts a positive integer `k`. The function should return the number of good pairs.

A pair `(i, j)` is called good if `pile1[i]` is divisible by `pile2[j] * k`. Assume `0 <= i <= len(pile1) - 1` and `0 <= j <= len(pile2) - 1`.

**Example Usage:**
```python
pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
good_pairs(pile1, pile2, k)  # Output: 5

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
good_pairs(pile1, pile2, k)  # Output: 2
```

---

## Version 2 Standard Set

### Problem 1: String Array Equivalency

Given two string arrays `word1` and `word2`, return `True` if the two arrays represent the same string, and `False` otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

**Example Usage:**
```python
word1 = ["bat", "man"]
word2 = ["b", "atman"]
are_equivalent(word1, word2)  # Output: True

word1 = ["alfred", "pennyworth"]
word2 = ["alfredpenny", "word"]
are_equivalent(word1, word2)  # Output: False

word1 = ["cat", "wom", "an"]
word2 = ["catwoman"]
are_equivalent(word1, word2)  # Output: True
```

**💡 Hint:** String Methods

### Problem 2: Count Even Strings

Implement a function `count_evens()` that accepts a list of strings `lst` as a parameter. The function should return the number of strings with an even length in the list.

**Example Usage:**
```python
lst = ["na", "nana", "nanana", "batman", "!"]
count_evens(lst)  # Output: 4

lst = ["the", "joker", "robin"]
count_evens(lst)  # Output: 0

lst = ["you", "either", "die", "a", "hero", "or", "you", "live", "long", "enough", "to", "see", "yourself", "become", "the", "villain"]
count_evens(lst)  # Output: 9
```

**💡 Hint:** Remainders with Modulus Division

### Problem 3: Secret Identity

Write a function `remove_name()` to keep Batman's secret identity hidden. The function accepts a list of names `people` and a string `secret_identity` and should return the list with any instances of `secret_identity` removed. The list must be modified in place; you may not create any new lists as part of your solution. Relative order of the remaining elements must be maintained.

**Example Usage:**
```python
people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
secret_identity = 'Bruce Wayne'
remove_name(people, secret_identity)  # Output: ['Batman', 'Superman', 'The Riddler']
```

**💡 Hint:** While Loops

### Problem 4: Count Digits

Given a non-negative integer `n`, write a function `count_digits()` that returns the number of digits in `n`. You may not cast `n` to a string.

**Example Usage:**
```python
n = 964
count_digits(n)  # Output: 3

n = 0
count_digits(n)  # Output: 1
```

**💡 Hint:** Floor Division

### Problem 5: Move Zeroes

Write a function `move_zeroes` that accepts an integer array `nums` and returns a new list with all 0s moved to the end of list. The relative order of the non-zero elements in the original list should be maintained.

**Example Usage:**
```python
lst = [1, 0, 2, 0, 3, 0]
move_zeroes(lst)  # Output: [1, 2, 3, 0, 0, 0]
```

### Problem 6: Reverse Vowels of a String

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases and more than once.

**Example Usage:**
```python
s = "robin"
reverse_vowels(s)  # Output: "ribon"

s = "BATgirl"
reverse_vowels(s)  # Output: "BiTgArl"

s = "batman"
reverse_vowels(s)  # Output: "batman"
```

### Problem 7: Vantage Point

Batman is going on a scouting trip, surveying an area where he thinks Harley Quinn might commit her next crime spree. The area has many hills with different heights and Batman wants to find the tallest one to get the best vantage point. His scout trip consists of `n + 1` points at different altitudes. Batman starts his trip at point 0 with altitude 0.

Write a function `highest_altitude()` that accepts an integer array `gain` of length `n` where `gain[i]` is the net gain in altitude between points `i` and `i + 1` for all `(0 <= i < n)`. Return the highest altitude of a point.

**Example Usage:**
```python
gain = [-5, 1, 5, 0, -7]
highest_altitude(gain)  # Output: 1

gain = [-4, -3, -2, -1, 4, 3, 2]
highest_altitude(gain)  # Output: 0
```

### Problem 8: Left and Right Sum Differences

Given a 0-indexed integer array `nums`, write a function `left_right_difference` that returns a 0-indexed integer array `answer` where:

- `len(answer) == len(nums)`
- `answer[i] = left_sum[i] - right_sum[i]`

Where:
- `left_sum[i]` is the sum of elements to the left of the index `i` in the array `nums`. If there is no such element, `left_sum[i] = 0`
- `right_sum[i]` is the sum of elements to the right of the index `i` in the array `nums`. If there is no such element, `right_sum[i] = 0`

**Example Usage:**
```python
nums = [10, 4, 8, 3]
left_right_difference(nums)  # Output: [-15, -1, 11, 22]

nums = [1]
left_right_difference(nums)  # Output: [0]
```

### Problem 9: Common Cause

Write a function `common_elements()` that takes in two lists `lst1` and `lst2` and returns a list of the elements that are common to both lists.

**Example Usage:**
```python
lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["super speed", "time travel", "dimensional travel"]
common_elements(lst1, lst2)  # Output: ["super speed"]

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["martial arts", "stealth", "master detective"]
common_elements(lst1, lst2)  # Output: []
```

**✨ AI Hint:** Nested Loops

### Problem 10: Exposing Superman

Metropolis has a population `n`, with each citizen assigned an integer id from 1 to `n`. There's a rumor that Superman is an ordinary citizen among this group.

If Superman is an ordinary citizen, then:
1. Superman trusts nobody.
2. Everybody (except for Superman) trusts Superman.
3. There is exactly one citizen that satisfies properties 1 and 2.

Write a function `expose_superman()` that accepts a 2D array `trust` where `trust[i] = [ai, bi]` representing that the person labeled `ai` trusts the person labeled `bi`. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of Superman if he is hiding amongst the population and can be identified, or return -1 otherwise.

**Example Usage:**
```python
n = 2
trust = [[1, 2]]
expose_superman(trust, n)  # Output: 2

n = 3
trust = [[1, 3], [2, 3]]
expose_superman(trust, n)  # Output: 3

n = 3
trust = [[1, 3], [2, 3], [3, 1]]
expose_superman(trust, n)  # Output: -1
```