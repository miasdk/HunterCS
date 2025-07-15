# Advanced Problem Sets

## Table of Contents

### [Problems 1-6](#problems-1-6)
- [Problem 1: Longest Balanced Subsequence](#problem-1-longest-balanced-subsequence)
- [Problem 2: Valid Permutation Check](#problem-2-valid-permutation-check)
- [Problem 3: Group Strings by Frequency](#problem-3-group-strings-by-frequency)
- [Problem 4: Subdomain Visit Count](#problem-4-subdomain-visit-count)
- [Problem 5: Sum of Beauty of All Substrings](#problem-5-sum-of-beauty-of-all-substrings)
- [Problem 6: Subarrays Divisible by K](#problem-6-subarrays-divisible-by-k)

### [Problems 7-12](#problems-7-12)
- [Problem 7: Maximum String Copies](#problem-7-maximum-string-copies)
- [Problem 8: Sentence Similarity](#problem-8-sentence-similarity)
- [Problem 9: Bulls and Cows](#problem-9-bulls-and-cows)
- [Problem 10: Count Pairs with Power of Two Sum](#problem-10-count-pairs-with-power-of-two-sum)
- [Problem 11: Make File Names Unique](#problem-11-make-file-names-unique)
- [Problem 12: Check Pairing Divisibility](#problem-12-check-pairing-divisibility)

---

## Problems 1-6

### Problem 1: Longest Balanced Subsequence

Given an integer array, find the length of the longest subsequence where the difference between the maximum and minimum values is exactly 1.

**Function Signature:**
```python
def find_balanced_subsequence(art_pieces):
    pass
```

**Example Usage:**
```python
print(find_balanced_subsequence([1,3,2,2,5,2,3,7]))    # 5 (subsequence: [3,2,2,2,3])
print(find_balanced_subsequence([1,2,3,4]))            # 2
print(find_balanced_subsequence([1,1,1,1]))            # 0
```

---

### Problem 2: Valid Permutation Check

Check if an array is a permutation of `base[n] = [1, 2, ..., n-1, n, n]` for some n. The base array contains integers 1 to n-1 exactly once, and integer n twice.

**Function Signature:**
```python
def is_authentic_collection(art_pieces):
    pass
```

**Example Usage:**
```python
print(is_authentic_collection([2, 1, 3]))       # False
print(is_authentic_collection([1, 3, 3, 2]))    # True (permutation of [1,2,3,3])
print(is_authentic_collection([1, 1]))          # True (permutation of [1,1])
```

---

### Problem 3: Group Strings by Frequency

Given an array of strings, organize them into a 2D array where each row contains distinct strings and the number of rows is minimized.

**Function Signature:**
```python
def organize_exhibition(collection):
    pass
```

**Example Usage:**
```python
print(organize_exhibition(["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", "Kahlo", "O'Keefe"]))
# [["O'Keefe", "Kahlo", "Picasso", "Warhol"], ["O'Keefe", "Kahlo"], ["O'Keefe"]]

print(organize_exhibition(["Kusama", "Monet", "Ofili", "Banksy"]))
# [["Kusama", "Monet", "Ofili", "Banksy"]]
```

---

### Problem 4: Subdomain Visit Count

Given an array of count-paired domains like `["9001 modern.artmuseum.com"]`, return the count for each domain and subdomain. Visiting `"modern.artmuseum.com"` also visits `"artmuseum.com"` and `"com"`.

**Function Signature:**
```python
def subdomain_visits(cpdomains):
    pass
```

**Example Usage:**
```python
print(subdomain_visits(["9001 modern.artmuseum.com"]))
# ["9001 artmuseum.com", "9001 modern.artmuseum.com", "9001 com"]

print(subdomain_visits(["900 abstract.gallery.com", "50 impressionism.com", "1 contemporary.gallery.com", "5 medieval.org"]))
# ["901 gallery.com", "50 impressionism.com", "900 abstract.gallery.com", "5 medieval.org", "5 org", "1 contemporary.gallery.com", "951 com"]
```

---

### Problem 5: Sum of Beauty of All Substrings

Given a string, calculate the sum of beauty of all substrings. Beauty is defined as the difference between the highest and lowest character frequencies in a substring.

**Function Signature:**
```python
def beauty_sum(collection):
    pass
```

**Example Usage:**
```python
print(beauty_sum("aabcb"))      # 5
print(beauty_sum("aabcbaa"))    # 17
```

**Example 1 Explanation:** Substrings with non-zero beauty: `["aab","aabc","aabcb","abcb","bcb"]`, each with beauty = 1.

---

### Problem 6: Subarrays Divisible by K

Given an integer array and integer k, return the number of non-empty subarrays where the sum is divisible by k.

**Function Signature:**
```python
def count_divisible_collections(collection_sizes, k):
    pass
```

**Example Usage:**
```python
print(count_divisible_collections([4, 5, 0, -2, -3, 1], 5))    # 7
print(count_divisible_collections([5], 9))                     # 0
```

**Example 1 Explanation:** 7 subarrays with sum divisible by 5: `[4, 5, 0, -2, -3, 1]`, `[5]`, `[5, 0]`, `[5, 0, -2, -3]`, `[0]`, `[0, -2, -3]`, `[-2, -3]`

---

## Problems 7-12

### Problem 7: Maximum String Copies

Given two strings `ingredients` and `target_meal`, return the maximum number of copies of `target_meal` you can form by rearranging characters from `ingredients`.

**Function Signature:**
```python
def max_attempts(ingredients, target_meal):
    pass
```

**Example Usage:**
```python
print(max_attempts("aabbbcccc", "abc"))           # 2
print(max_attempts("ppppqqqrrr", "pqr"))          # 3  
print(max_attempts("ingredientsforcooking", "cooking"))  # 1
```

**✨ AI Hint:** Representing Infinite Values

---

### Problem 8: Sentence Similarity

Given two sentences as string arrays and an array of similar word pairs, determine if the sentences are similar. Two sentences are similar if they have the same length and each corresponding pair of words is similar.

**Function Signature:**
```python
def is_similar(sentence1, sentence2, similar_pairs):
    pass
```

**Example Usage:**
```python
sentence1 = ["my", "type", "on", "paper"]
sentence2 = ["my", "type", "in", "theory"]
similar_pairs = [["on", "in"], ["paper", "theory"]]
print(is_similar(sentence1, sentence2, similar_pairs))    # True

sentence3 = ["no", "tea", "no", "shade"]
sentence4 = ["no", "offense"]
similar_pairs2 = [["shade", "offense"]]
print(is_similar(sentence3, sentence4, similar_pairs2))   # False (different lengths)
```

---

### Problem 9: Bulls and Cows

Given a secret number and a guess, return a hint in format "xAyB" where x is the number of bulls (correct digits in correct position) and y is the number of cows (correct digits in wrong position).

**Function Signature:**
```python
def get_hint(secret, guess):
    pass
```

**Example Usage:**
```python
print(get_hint("1807", "7810"))    # "1A3B"
print(get_hint("1123", "0111"))    # "1A1B"
```

---

### Problem 10: Count Pairs with Power of Two Sum

Given an array of integers, return the number of pairs where the sum is a power of two. Return result modulo 10^9 + 7.

**Function Signature:**
```python
def count_winning_pairings(star_power):
    pass
```

**Example Usage:**
```python
print(count_winning_pairings([1, 3, 5, 7, 9]))        # 4
print(count_winning_pairings([1, 1, 1, 3, 3, 3, 7]))  # 15
```

---

### Problem 11: Make File Names Unique

Given an array of desired file names, return an array where each name is unique. If a name is already taken, append "(k)" where k is the smallest positive integer that makes it unique.

**Function Signature:**
```python
def assign_unique_nicknames(nicknames):
    pass
```

**Example Usage:**
```python
print(assign_unique_nicknames(["Champ","Diva","Champ","Ace"]))
# ["Champ","Diva","Champ(1)","Ace"]

print(assign_unique_nicknames(["Ace","Ace","Ace","Maverick"]))
# ["Ace","Ace(1)","Ace(2)","Maverick"]

print(assign_unique_nicknames(["Star","Star","Star","Star","Star"]))
# ["Star","Star(1)","Star(2)","Star(3)","Star(4)"]
```

---

### Problem 12: Check Pairing Divisibility

Given an array of integers and integer k, determine if you can pair all elements such that each pair's sum is divisible by k.

**Function Signature:**
```python
def pair_contestants(scores, k):
    pass
```

**Example Usage:**
```python
print(pair_contestants([1,2,3,4,5,10,6,7,8,9], 5))    # True
print(pair_contestants([1,2,3,4,5,6], 7))             # True
print(pair_contestants([1,2,3,4,5,6], 10))            # False
```