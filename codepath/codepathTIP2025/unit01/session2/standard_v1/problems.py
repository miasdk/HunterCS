"""
Unit 01 Session 2 - Standard Version 1

Overview:
This problem set focuses on foundational Python concepts and problem-solving skills for Unit 01, Session 2 (Standard, Version 1).

Learning Objectives:
- Practice basic Python syntax and data structures
- Develop problem-solving strategies
- Gain familiarity with standard algorithms

Problems:
1. Problem 1: [Short description]
2. Problem 2: [Short description]
...
"""

# ==========================
# Version 1 Standard Set
# ==========================

# Problem 1: Reverse Sentence
def reverse_sentence(sentence):
    """
    Reverse the words in a sentence.
    :param sentence: A string containing the sentence to reverse.
    :return: A string with the words in reverse order.
    """
    words = sentence.split() # Split the sentence into words
    reversed_words = words[::-1] # Reverse the list of words
    return ' '.join(reversed_words) # Join the reversed words into a single string

# Demo / Test cases
if __name__ == "__main__":
    sentence1 = "tubby little cubby all stuffed with fluff"
    print(reverse_sentence(sentence1))  # Output: "fluff with stuffed all cubby little tubby"

    sentence2 = "Pooh"
    print(reverse_sentence(sentence2))  # Output: "Pooh"

# Problem 2: Goldilocks Number
def goldilocks_approved(nums):
    for num in nums:
        if num != min(nums) and num != max(nums):
            return num
    return -1  # If no such number exists, return -1
    pass

# Demo / Test cases
if __name__ == "__main__":
    nums1 = [3, 2, 1, 4]
    print(goldilocks_approved(nums1))  # Output: 3 or 2

    nums2 = [1, 2]
    print(goldilocks_approved(nums2))  # Output: -1

    nums3 = [2, 1, 3]
    print(goldilocks_approved(nums3))  # Output: 2


#Problem 3: Delete Minimum

def delete_minimum_elements(hunny_jar_sizes):
    removed_elements = []
    while hunny_jar_sizes:
        min_element = min(hunny_jar_sizes)  # Find the minimum element
        removed_elements.append(min_element)  # Add it to the result list
        hunny_jar_sizes.remove(min_element)  # Remove it from the original list
    return removed_elements  # Return the list of removed elements

# Demo / Test cases
if __name__ == "__main__":
    hunny_jar_sizes1 = [5, 3, 2, 4, 1]
    print(delete_minimum_elements(hunny_jar_sizes1))  # Output: [1, 2, 3, 4, 5]
    hunny_jar_sizes2 = [5, 2, 1, 8, 2]
    print(delete_minimum_elements(hunny_jar_sizes2))  # Output: [1, 2, 2, 5, 8]

# Problem 4: Sum of Digits

def sum_of_digits(num):
    """
    Calculate the sum of the digits of a number.
    :param num: An integer whose digits are to be summed.
    :return: The sum of the digits of num.
    """
    return sum(int(digit) for digit in str(num))  # Convert num to string, iterate over each character, convert back to int and sum

# Demo / Test cases
if __name__ == "__main__":
    num1 = 423
    print(sum_of_digits(num1))  # Output: 9
    num2 = 4
    print(sum_of_digits(num2))  # Output: 4
    
# Problem 5: Bouncy, Flouncy, Trouncy, Pouncy

def final_value_after_operations(operations):
    sum = 1 # Initial value of tigger is 1
    for operation in operations:
        if operation == "bouncy" or operation == "flouncy":
            sum += 1
        elif operation == "trouncy" or operation == "pouncy":
            sum -= 1
    return sum  # Return the final value of tigger after all operations are performed
    pass

# Demo / Test cases

if __name__ == "__main__":
    operations1 = ["trouncy", "flouncy", "flouncy"]
    print(final_value_after_operations(operations1))  # Output: 2

    operations2 = ["bouncy", "bouncy", "flouncy"]
    print(final_value_after_operations(operations2))  # Output: 4


# Problem 6: Acronym

def is_acronym(words, s):
    concatenated = ''.join(word[0] for word in words)  # Concatenate the first characters of each word
    return concatenated == s  # Check if the concatenated string matches s

    pass


# Problem 7: Good Things Come in Threes

def make_divisible_by_3(nums):
   def make_divisible_by_3(nums):
    min_operations = 0
    for num in nums:
        remainder = num % 3
        if remainder == 0:
            continue
        else:
            min_operations += 1  # For remainder 1 or 2, only 1 operation is needed
    return min_operations  # Return the total minimum operations needed to make all elements divisible by 3
    pass


# Problem 8: Exclusive Elements

def exclusive_elemts(lst1, lst2):
    exclusive = []
    for item in lst1: 
        if item not in lst2: 
            exclusive.append(item)
    for item in lst2:
        if item not in lst1:
            exclusive.append(item)
    return exclusive  # Return the list of exclusive elements from both lists   
    pass

# Demo / Test cases
if __name__ == "__main__":
    lst1 = ["pooh", "roo", "piglet"]
    lst2 = ["piglet", "eeyore", "owl"]
    print(exclusive_elemts(lst1, lst2))  # Output: ["pooh", "roo", "eeyore", "owl"]

    lst1 = ["pooh", "roo"]
    lst2 = ["piglet", "eeyore", "owl", "kanga"]
    print(exclusive_elemts(lst1, lst2))  # Output: ["pooh", "roo", "piglet", "eeyore", "owl", "kanga"]

    lst1 = ["pooh", "roo", "piglet"]
    lst2 = ["pooh", "roo", "piglet"]
    print(exclusive_elemts(lst1, lst2))  # Output: []

# Problem 9: Merge Strings Alternately

def merge_alternately(word1, word2):
    """
    Merge two strings by alternating their characters. If one string is longer,
    append the remaining characters at the end.

    This approach uses slicing and list appending for readability and efficiency.
    Instead of using a nested for loop (like you might in C++), we:
      - Loop through both strings up to the length of the shorter one, appending one character from each at a time.
      - Then, append any remaining characters from the longer string using slicing:
        merged.append(word1[min_length:])  # Adds leftover characters from word1, if any
        merged.append(word2[min_length:])  # Adds leftover characters from word2, if any
    This is much cleaner and more Pythonic than a nested loop.

    Example:
        word1 = "hfa"
        word2 = "eflump"
        # After the loop: merged = ['h', 'e', 'f', 'f', 'a', 'l']
        # word1[3:] is '', word2[3:] is 'ump'
        # Final merged: ['h', 'e', 'f', 'f', 'a', 'l', '', 'ump'] -> "heffalump"
    """
    merged = []
    min_length = min(len(word1), len(word2))

    for i in range(min_length):
        merged.append(word1[i])
        merged.append(word2[i])
    merged.append(word1[min_length:])  # Append remaining characters from word1 if any
    merged.append(word2[min_length:])  # Append remaining characters from word2 if any
    return ''.join(merged)  # Join the list into a string and return it
    pass


# Problem 10: Eeyore's House

def good_pairs(pile1, pile2, k):
    count = 0
    for i in range(len(pile1)):
        for j in range(len(pile2)):
            if pile1[i] % (pile2[j] * k) == 0:  # Check if pile1[i] is divisible by pile2[j] * k
                count += 1  # Increment count for each good pair found
    return count  # Return the total count of good pairs found
    pass



# ==========================
# Version 2 Standard Set
# ==========================

# Problem 1: Are They Equivalent?
def are_equivalent(word1, word2):
    return ''.join(word1) == ''.join(word2)  # Join the strings in word1 and word2 and compare them

# Demo / Test cases
if __name__ == "__main__":
    word1 = ["bat", "man"]
    word2 = ["b", "atman"]
    print(are_equivalent(word1, word2))  # Output: True
    
    word1 = ["alfred", "pennyworth"]

# Problem 2: Count Evens
def count_evens(lst):
   sum = 0
   for string in lst:
        if len(string) % 2 == 0:
            sum += 1
   return sum  # Return the number of strings with an even length in the list

# Demo / Test cases
if __name__ == "__main__":
    lst = ["na", "nana", "nanana", "batman", "!"]
    print(count_evens(lst))  # Output: 4


# Problem 3: Remove Name
def remove_name(people, secret_identity):
    while secret_identity in people:
        people.remove(secret_identity)
    return people  # Return the list after removing all occurrences of secret_identity
# Demo / Test cases
if __name__ == "__main__":
    people = ["batman", "robin", "batman", "pooh"]
    secret_identity = "batman"
    print(remove_name(people, secret_identity))  # Output: ['robin', 'pooh']

    people = ["batman", "robin", "pooh"]
    secret_identity = "batman"
    print(remove_name(people, secret_identity))  # Output: ['robin', 'pooh']

#Problem 4: Count digits

def count_digits(n):
    #Base case: n = 0 
    if n == 0: 
        return 1 
    count = 0 
    #Handle negative input 
    n = abs(n)
    while n > 0: 
        #isolate last integer 
        n = n // 10 
        #add to count
        count += 1 
    return count 
# // 10 floor division isolates the last integer 

#Problem 5: Move Zeros 
def move_zeroes(lst):
    #isolate non zeroes 
    non_zeroes = [x for x in lst if x != 0]
    #get zeroes by subtracting non zeroes from length 
    zeroes = [0] * (len(lst)-len(non_zeroes)) 
    return non_zeroes + zeroes 
    
            
    pass

#Problem 6: Reverse Vowels of a String 
def reverse_vowels(s):
    vowels = "aeiouAEIOU" 
    #string are immutable so we need to convert to a list whose elements we can change around 
    s_list = list(s) 
    i, j = 0, len(s) - 1 
    while i < j: 
        if s_list[i] not in vowels: 
            j -= 1 
        else: 
            s_list[i], s_list[j] = s_list[j]
            i += 1 
            j -= 1 
    return ''.join(s_list)

    pass


#Problem 7: Vantage Point

def highest_altitude(gain):
    
    pass

"""
Problem 8: Left and Right Sum Differences

Given a 0-indexed integer array nums, write a function left_right_difference that returns a 0-indexed integer array answer where:

len(answer) == len(nums)
answer[i] = left_sum[i] - right_sum[i]

Where:
left_sum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, left_sum[i] = 0
right_sum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, right_sum[i] = 0

Example Usage:

nums = [10, 4, 8, 3]
left_right_difference(nums)  # Output: [-15, -1, 11, 22]

nums = [1]
left_right_difference(nums)  # Output: [0]
"""

def left_right_difference(nums):
    pass

"""
Problem 9: Common Cause

Write a function common_elements() that takes in two lists lst1 and lst2 and returns a list of the elements that are common to both lists.

Example Usage:

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["super speed", "time travel", "dimensional travel"]
common_elements(lst1, lst2)  # Output: ["super speed"]

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["martial arts", "stealth", "master detective"]
common_elements(lst1, lst2)  # Output: []

✨ AI Hint: Nested Loops
"""

def common_elements(lst1, lst2):
    pass

"""
Problem 10: Exposing Superman

Metropolis has a population n, with each citizen assigned an integer id from 1 to n. There's a rumor that Superman is an ordinary citizen among this group.

If Superman is an ordinary citizen, then:
Superman trusts nobody.
Everybody (except for Superman) trusts Superman.
There is exactly one citizen that satisfies properties 1 and 2.

Write a function expose_superman() that accepts a 2D array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of Superman if he is hiding amongst the population and can be identified, or return -1 otherwise.

Example Usage:

n = 2
trust = [[1, 2]]
expose_superman(trust, n)  # Output: 2

n = 3
trust = [[1, 3], [2, 3]]
expose_superman(trust, n)  # Output: 3

n = 3
trust = [[1, 3], [2, 3], [3, 1]]
expose_superman(trust, n)  # Output: -1
"""

def expose_superman(trust, n):
    pass