# Unit 2 Advanced Problem Set

## Table of Contents

### [Problems 1-8](#problems-1-8)
- [Problem 1: Sum Dictionary Values](#problem-1-sum-dictionary-values)
- [Problem 2: Check Pangram](#problem-2-check-pangram)
- [Problem 3: Find All Duplicates](#problem-3-find-all-duplicates)
- [Problem 4: Remove One Character for Equal Frequencies](#problem-4-remove-one-character-for-equal-frequencies)
- [Problem 5: Two Sum](#problem-5-two-sum)
- [Problem 6: Group by Size Requirements](#problem-6-group-by-size-requirements)
- [Problem 7: Minimum Steps to Anagram](#problem-7-minimum-steps-to-anagram)
- [Problem 8: Count Unique Action Minutes](#problem-8-count-unique-action-minutes)

### [Problems 9-16](#problems-9-16)
- [Problem 9: Dictionary Difference Calculation](#problem-9-dictionary-difference-calculation)
- [Problem 10: Find Common Elements](#problem-10-find-common-elements)
- [Problem 11: Filter by Frequency Threshold](#problem-11-filter-by-frequency-threshold)
- [Problem 12: Count Concatenation Pairs](#problem-12-count-concatenation-pairs)
- [Problem 13: Detect Duplicates Within Distance](#problem-13-detect-duplicates-within-distance)
- [Problem 14: Categorize by Loss Count](#problem-14-categorize-by-loss-count)
- [Problem 15: Most Frequent Word Excluding Banned](#problem-15-most-frequent-word-excluding-banned)
- [Problem 16: Create Usage Table](#problem-16-create-usage-table)

---

## Problems 1-8

### Problem 1: Sum Dictionary Values

Given a dictionary where values are integers, return the total sum of all values.

**Function Signature:**
```python
def total_treasure(treasure_map):
    pass
```

**Example Usage:**
```python
treasure_map1 = {"Cove": 3, "Beach": 7, "Forest": 5}
treasure_map2 = {"Shipwreck": 10, "Cave": 20, "Lagoon": 15, "Island Peak": 5}

print(total_treasures(treasure_map1))     # 15
print(total_treasures(treasure_map2))     # 50
```

**✨ AI Hint:** Dictionaries  
**✨ AI Hint:** Accessing Values in a Dictionary  
**💡 Hint:** Dictionary Access options  
**💡 Hint:** Accessing Keys, Values, and Key-Value Pairs

---

### Problem 2: Check Pangram

Given a string containing only lowercase English letters and whitespace, return True if it contains every letter of the alphabet at least once.

**Function Signature:**
```python
def can_trust_message(message):
    pass
```

**Example Usage:**
```python
print(can_trust_message("sphinx of black quartz judge my vow"))    # True
print(can_trust_message("trust me"))                               # False
```

**✨ AI Hint:** Introduction to sets

---

### Problem 3: Find All Duplicates

Given an integer array of length n where all integers are in range [1, n] and each integer appears once or twice, return an array of all integers that appear twice.

**Function Signature:**
```python
def find_duplicate_chests(chests):
    pass
```

**Example Usage:**
```python
print(find_duplicate_chests([4, 3, 2, 7, 8, 2, 3, 1]))    # [2, 3]
print(find_duplicate_chests([1, 1, 2]))                    # [1]
print(find_duplicate_chests([1]))                          # []
```

**✨ AI Hint:** Frequency Maps

---

### Problem 4: Remove One Character for Equal Frequencies

Given a string of lowercase letters, return True if removing exactly one character makes all remaining characters have equal frequency.

**Function Signature:**
```python
def is_balanced(code):
    pass
```

**Example Usage:**
```python
print(is_balanced("arghh"))    # True (remove 'h' → "argh", each char appears once)
print(is_balanced("haha"))     # False (impossible to balance by removing one char)
```

---

### Problem 5: Two Sum

Given an array of integers and a target sum, return the indices of two numbers that add up to the target. Assume exactly one solution exists and you cannot use the same element twice.

**Function Signature:**
```python
def find_treasure_indices(gold_amounts, target):
    pass
```

**Example Usage:**
```python
print(find_treasure_indices([2, 7, 11, 15], 9))    # [0, 1]
print(find_treasure_indices([3, 2, 4], 6))         # [1, 2]
print(find_treasure_indices([3, 3], 6))            # [0, 1]
```

---

### Problem 6: Group by Size Requirements

Given an array where `group_sizes[i]` is the required group size for person i, return a list of groups where each person i is in a group of size `group_sizes[i]`.

**Function Signature:**
```python
def organize_pirate_crew(group_sizes):
    pass
```

**Example Usage:**
```python
print(organize_pirate_crew([3, 3, 3, 3, 3, 1, 3]))    # [[5], [0, 1, 2], [3, 4, 6]]
print(organize_pirate_crew([2, 1, 3, 3, 3, 2]))       # [[1], [0, 5], [2, 3, 4]]
```

---

### Problem 7: Minimum Steps to Anagram

Given two strings of the same length, return the minimum number of character replacements needed to make the second string an anagram of the first.

**Function Signature:**
```python
def min_steps_to_match_maps(map1, map2):
    pass
```

**Example Usage:**
```python
print(min_steps_to_match_maps("bab", "aba"))           # 1
print(min_steps_to_match_maps("treasure", "huntgold")) # 6
print(min_steps_to_match_maps("anagram", "mangaar"))   # 0
```

---

### Problem 8: Count Unique Action Minutes

Given a 2D array `logs` where `logs[i] = [pirateID, time]` and integer k, return an array where `answer[j]` is the number of pirates who performed actions in exactly j unique minutes.

**Function Signature:**
```python
def counting_pirates_action_minutes(logs, k):
    pass
```

**Example Usage:**
```python
logs1 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
print(counting_pirates_action_minutes(logs1, 5))    # [0, 2, 0, 0, 0]

logs2 = [[1, 1], [2, 2], [2, 3]]
print(counting_pirates_action_minutes(logs2, 4))    # [1, 1, 0, 0]
```

---

## Problems 9-16

### Problem 9: Dictionary Difference Calculation

Given two dictionaries with the same keys, return a new dictionary where each value is the difference (second dict value - first dict value) for each key.

**Function Signature:**
```python
def analyze_library(library_catalog, actual_distribution):
    pass
```

**Example Usage:**
```python
library_catalog = {"Room A": 150, "Room B": 200, "Room C": 250, "Room D": 300}
actual_distribution = {"Room A": 150, "Room B": 190, "Room C": 260, "Room D": 300}

print(analyze_library(library_catalog, actual_distribution))
# {'Room A': 0, 'Room B': -10, 'Room C': 10, 'Room D': 0}
```

**✨ AI Hint:** Dictionaries  
**✨ AI Hint:** Accessing Values in a Dictionary  
**💡 Hint:** Dictionary Access options  
**💡 Hint:** Accessing Keys, Values, and Key-Value Pairs

---

### Problem 10: Find Common Elements

Given two lists of strings, return a list of elements that appear in both lists.

**Function Signature:**
```python
def find_common_artifacts(artifacts1, artifacts2):
    pass
```

**Example Usage:**
```python
artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

print(find_common_artifacts(artifacts1, artifacts2))    # ["Golden Vase", "Bronze Shield"]
```

**✨ AI Hint:** Introduction to sets

---

### Problem 11: Filter by Frequency Threshold

Given a list of strings and an integer threshold, return a list of all strings that appear fewer than threshold times.

**Function Signature:**
```python
def declutter(souvenirs, threshold):
    pass
```

**Example Usage:**
```python
souvenirs1 = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"]
print(declutter(souvenirs1, 3))    # ["alien egg", "map", "map", "statue"]

souvenirs2 = ["postcard", "postcard", "postcard", "sword"]
print(declutter(souvenirs2, 2))    # ["sword"]
```

**✨ AI Hint:** Frequency Maps

---

### Problem 12: Count Concatenation Pairs

Given an array of digit strings and a target string, return the number of pairs (i, j) where i ≠ j and concatenating `portals[i] + portals[j]` equals the target.

**Function Signature:**
```python
def num_of_time_portals(portals, destination):
    pass
```

**Example Usage:**
```python
print(num_of_time_portals(["777", "7", "77", "77"], "7777"))    # 4
print(num_of_time_portals(["123", "4", "12", "34"], "1234"))    # 2
print(num_of_time_portals(["1", "1", "1"], "11"))              # 6
```

---

### Problem 13: Detect Duplicates Within Distance

Given an array and integer k, return True if there exist two distinct indices i and j such that `nums[i] == nums[j]` and the absolute difference between i and j is at most k.

**Function Signature:**
```python
def detect_temporal_anomaly(time_points, k):
    pass
```

**Example Usage:**
```python
print(detect_temporal_anomaly([1, 2, 3, 1], 3))        # True
print(detect_temporal_anomaly([1, 0, 1, 1], 1))        # True
print(detect_temporal_anomaly([1, 2, 3, 1, 2, 3], 2))  # False
```

---

### Problem 14: Categorize by Loss Count

Given a 2D array `races` where `races[i] = [winner, loser]`, return two lists: all participants who never lost, and all participants who lost exactly once.

**Function Signature:**
```python
def find_travelers(races):
    pass
```

**Example Usage:**
```python
races1 = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
print(find_travelers(races1))    # [[1, 2, 10], [4, 5, 7, 8]]

races2 = [[2, 3], [1, 3], [5, 4], [6, 4]]
print(find_travelers(races2))    # [[1, 2, 5, 6], []]
```

---

### Problem 15: Most Frequent Word Excluding Banned

Given a text string and a list of banned words, return the most frequent word that is not banned. Ignore punctuation and case.

**Function Signature:**
```python
def find_most_frequent_word(text, illegibles):
    pass
```

**Example Usage:**
```python
print(find_most_frequent_word("a.", []))                                           # "a"
print(find_most_frequent_word("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))  # "ball"
```

**Example 2 Explanation:** "hit" occurs 3 times but is banned. "ball" occurs twice and is the most frequent non-banned word.

**💡 Hint:** Cleaning up the String

---

### Problem 16: Create Usage Table

Given usage records `[traveler_name, portal_number, time_used]`, create a table showing portal usage count by time. Return as 2D array with headers.

**Function Signature:**
```python
def display_time_portal_usage(usage_records):
    pass
```

**Example Usage:**
```python
usage_records1 = [["David","3","10:00"], ["Corina","10","10:15"], ["David","3","10:30"], 
                  ["Carla","5","11:00"], ["Carla","5","10:00"], ["Rous","3","10:00"]]

print(display_time_portal_usage(usage_records1))
# [['Portal','10:00','10:15','10:30','11:00'],['3','2','0','1','0'],['5','1','0','0','1'],['10','0','1','0','0']]

usage_records2 = [["James","12","11:00"], ["Ratesh","12","11:00"], ["Amadeus","12","11:00"], 
                  ["Adam","1","09:00"], ["Brianna","1","09:00"]]

print(display_time_portal_usage(usage_records2))
# [['Portal','09:00','11:00'],['1','2','0'],['12','0','3']]

usage_records3 = [["Laura","2","08:00"], ["Jhon","2","08:15"], ["Melissa","2","08:30"]]

print(display_time_portal_usage(usage_records3))
# [['Portal','08:00','08:15','08:30'],['2','1','1','1']]
```