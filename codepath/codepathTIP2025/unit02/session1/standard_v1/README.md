# Unit 2 Standard Problem Set

## Table of Contents

### [Problems 1-12](#problems-1-12)
- [Problem 1: Create Dictionary from Two Lists](#problem-1-create-dictionary-from-two-lists)
- [Problem 2: Dictionary Lookup with Default](#problem-2-dictionary-lookup-with-default)
- [Problem 3: Sum Dictionary Values](#problem-3-sum-dictionary-values)
- [Problem 4: Find Common Key-Value Pairs](#problem-4-find-common-key-value-pairs)
- [Problem 5: Find Most Frequent Value](#problem-5-find-most-frequent-value)
- [Problem 6: Sum All Maximum Values](#problem-6-sum-all-maximum-values)
- [Problem 7: Alternative Implementation](#problem-7-alternative-implementation)
- [Problem 8: Count Pairs with Same Value](#problem-8-count-pairs-with-same-value)
- [Problem 9: Sum of Index Differences](#problem-9-sum-of-index-differences)
- [Problem 10: Count Characters in Set](#problem-10-count-characters-in-set)
- [Problem 11: Word Pattern Matching](#problem-11-word-pattern-matching)
- [Problem 12: Sort by Custom Key](#problem-12-sort-by-custom-key)

### [Problems 13-24](#problems-13-24)
- [Problem 13: Create Dictionary from Two Lists](#problem-13-create-dictionary-from-two-lists)
- [Problem 14: Nested Dictionary Lookup](#problem-14-nested-dictionary-lookup)
- [Problem 15: Filter Dictionary by Range](#problem-15-filter-dictionary-by-range)
- [Problem 16: Dictionary Difference](#problem-16-dictionary-difference)
- [Problem 17: Find Most Frequent Item](#problem-17-find-most-frequent-item)
- [Problem 18: Check Complete Character Set](#problem-18-check-complete-character-set)
- [Problem 19: Count String Pairs](#problem-19-count-string-pairs)
- [Problem 20: Find Array Differences](#problem-20-find-array-differences)
- [Problem 21: Count Common Elements](#problem-21-count-common-elements)
- [Problem 22: Alternative Implementation](#problem-22-alternative-implementation)
- [Problem 23: Sort by Frequency](#problem-23-sort-by-frequency)
- [Problem 24: Find Final Destination](#problem-24-find-final-destination)

---

## Problems 1-12

### Problem 1: Create Dictionary from Two Lists

Given two lists of equal length, create a dictionary mapping elements from the first list to corresponding elements in the second list.

**Function Signature:**
```python
def lineup(artists, set_times):
    pass
```

**Example Usage:**
```python
artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))
```

**Example Output:**
```python
{"Kendrick Lamar": "9:30 PM", "Chappell Roan": "5:00 PM", "Mitski": "2:00 PM", "Rosalía": "7:30 PM"}
{}
```

**✨ AI Hint:** Dictionaries

---

### Problem 2: Dictionary Lookup with Default

Given a dictionary mapping keys to nested dictionaries, look up a key and return its nested dictionary. If the key doesn't exist, return a default error message.

**Function Signature:**
```python
def get_artist_info(artist, festival_schedule):
    pass
```

**Example Usage:**
```python
festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))
```

**Example Output:**
```python
{'day': 'Friday', 'time': '9:00 PM', 'stage': 'Main Stage'}
{'message': 'Artist not found'}
```

**✨ AI Hint:** Accessing Values in a Dictionary  
**💡 Hint:** Dictionary Access options

---

### Problem 3: Sum Dictionary Values

Given a dictionary mapping keys to integers, return the sum of all values.

**Function Signature:**
```python
def total_sales(ticket_sales):
    pass
```

**Example Usage:**
```python
ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
print(total_sales(ticket_sales))
```

**Example Output:**
```python
4500
```

**💡 Hint:** Accessing Keys, Values, and Key-Value Pairs

---

### Problem 4: Find Common Key-Value Pairs

Given two dictionaries, return a new dictionary containing only the key-value pairs that are identical in both dictionaries.

**Function Signature:**
```python
def identify_conflicts(venue1_schedule, venue2_schedule):
    pass
```

**Example Usage:**
```python
venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))
```

**Example Output:**
```python
{"Stromae": "9:00 PM", "HARDY": "7:00 PM"}
```

---

### Problem 5: Find Most Frequent Value

Given a dictionary mapping keys to values, return the value that appears most frequently. If there's a tie, return any of the tied values.

**Function Signature:**
```python
def best_set(votes):
    pass
```

**Example Usage:**
```python
votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))
```

**Example Output:**
```python
SZA
Ethel Cain
```

**Note:** SZA and Ethel Cain would both be acceptable answers for the second example

**✨ AI Hint:** Frequency Maps

---

### Problem 6: Sum All Maximum Values

Given an array of integers, find the maximum value and return the sum of all occurrences of that maximum value.

**Function Signature:**
```python
def max_audience_performances(audiences):
    pass
```

**Example Usage:**
```python
print(max_audience_performances([100, 200, 200, 150, 100, 250]))    # 250
print(max_audience_performances([120, 180, 220, 150, 220]))         # 440
```

---

### Problem 7: Alternative Implementation

Re-implement the previous problem using a different approach (if you used a dictionary, try without one; if you didn't use a dictionary, try with one). Compare the two solutions.

**Function Signature:**
```python
def max_audience_performances(audiences):
    pass
```

**Example Usage:**
```python
print(max_audience_performances([100, 200, 200, 150, 100, 250]))    # 250
print(max_audience_performances([120, 180, 220, 150, 220]))         # 440
```

---

### Problem 8: Count Pairs with Same Value

Given an array of integers, return the number of pairs (i, j) where i < j and the values at those indices are equal.

**Hint:** For n identical values, number of pairs = n × (n-1) / 2

**Function Signature:**
```python
def num_popular_pairs(popularity_scores):
    pass
```

**Example Usage:**
```python
print(num_popular_pairs([1, 2, 3, 1, 1, 3]))    # 4
print(num_popular_pairs([1, 1, 1, 1]))          # 6
print(num_popular_pairs([1, 2, 3]))             # 0
```

**💡 Hint:** Floor Division

---

### Problem 9: Sum of Index Differences

Given two arrays that are permutations of each other, return the sum of absolute differences between the indices of each element in both arrays.

**Function Signature:**
```python
def find_stage_arrangement_difference(s, t):
    """
    :type s: List[str]
    :type t: List[str]
    :rtype: int
    """
    pass
```

**Example Usage:**
```python
s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
print(find_stage_arrangement_difference(s1, t1))    # 2

s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]
print(find_stage_arrangement_difference(s2, t2))    # 12
```

**✨ AI Hint:** Frequency Maps

---

### Problem 10: Count Characters in Set

Given two strings, count how many characters from the second string are present in the first string (considering each occurrence).

**Implement the given pseudocode:**
1. Create an empty set called vip_set
2. For each character in vip_passes, add it to vip_set
3. Initialize a counter variable to 0
4. For each character in guests: if the character is in vip_set, increment the count by 1
5. Return the count

**Function Signature:**
```python
def num_VIP_guests(vip_passes, guests):
    pass
```

**Example Usage:**
```python
print(num_VIP_guests("aA", "aAAbbbb"))    # 3
print(num_VIP_guests("z", "ZZ"))          # 0
```

**✨ AI Hint:** Introduction to sets

---

### Problem 11: Word Pattern Matching

Given a pattern string and a sentence, return True if the sentence follows the same pattern (one-to-one correspondence between pattern characters and words).

**Fix the bugs in this code:**
```python
def schedule_pattern(pattern, schedule):
    genres = schedule.split()

    if len(genres) == len(pattern):
        return True

    char_to_genre = {}
    genre_to_char = {}

    for char, genre in zip(pattern, genres):
        if char in char_to_genre:
            if char_to_genre[char] == genre:
                return True
        else:
            char_to_genre[char] = genre

        if genre in genre_to_char:
            if genre_to_char[genre] == char:
                return True
        else:
            genre_to_char[genre] = char

    return False
```

**Example Usage:**
```python
print(schedule_pattern("abba", "rock jazz jazz rock"))     # True
print(schedule_pattern("abba", "rock jazz jazz blues"))    # False
print(schedule_pattern("aaaa", "rock jazz jazz rock"))     # False
```

**✨ AI Hint:** zip()

---

### Problem 12: Sort by Custom Key

Given two arrays of equal length (names and values), return the names sorted in descending order by their corresponding values.

**Function Signature:**
```python
def sort_performers(performer_names, performance_times):
    """
    :type performer_names: List[str]
    :type performance_times: List[int]
    :rtype: List[str]
    """
    pass
```

**Example Usage:**
```python
performer_names1 = ["Mary", "John", "Emma"]
performance_times1 = [180, 165, 170]
print(sort_performers(performer_names1, performance_times1))     # ["Mary", "Emma", "John"]

performer_names2 = ["Alice", "Bob", "Bob"]
performance_times2 = [155, 185, 150]
print(sort_performers(performer_names2, performance_times2))     # ["Bob", "Alice", "Bob"]
```

**✨ AI Hint:** sorted()

---

## Problems 13-24

### Problem 13: Create Dictionary from Two Lists

Given two lists of equal length, create a dictionary mapping elements from the first list to corresponding elements in the second list.

**Function Signature:**
```python
def space_crew(crew, position):
    pass
```

**Example Usage:**
```python
exp70_crew = ["Andreas Mogensen", "Jasmin Moghbeli", "Satoshi Furukawa", "Loral O'Hara", "Konstantin Borisov"]
exp70_positions = ["Commander", "Flight Engineer", "Flight Engineer", "Flight Engineer", "Flight Engineer"] 

ax3_crew = ["Michael Lopez-Alegria", "Walter Villadei", "Alper Gezeravci", "Marcus Wandt"]
ax3_positions = ["Commander", "Mission Pilot", "Mission Specialist", "Mission Specialist"]

print(space_crew(exp70_crew, exp70_positions))
print(space_crew(ax3_crew, ax3_positions))
```

**✨ AI Hint:** Dictionaries

---

### Problem 14: Nested Dictionary Lookup

Given a global dictionary and a key, return a formatted string with the nested dictionary values. If the key doesn't exist, return an error message.

**Function Signature:**
```python
def planet_lookup(planet_name):
    pass
```

**Example Usage:**
```python
planetary_info = {
    "Mercury": {"Moons": 0, "Orbital Period": 88},
    "Earth": {"Moons": 1, "Orbital Period": 365.25},
    "Mars": {"Moons": 2, "Orbital Period": 687},
    "Jupiter": {"Moons": 79, "Orbital Period": 10592}
}

print(planet_lookup("Jupiter"))    # "Planet Jupiter has an orbital period of 10592 Earth days and has 79 moons."
print(planet_lookup("Pluto"))      # "Sorry, I have no data on that planet."
```

**✨ AI Hint:** Accessing Values in a Dictionary  
**💡 Hint:** Dictionary Access options  
**💡 Hint:** Nested Data

---

### Problem 15: Filter Dictionary by Range

Given a dictionary mapping keys to integers and a range [min_val, max_val], return a list of keys whose values are outside this range.

**Function Signature:**
```python
def check_oxygen_levels(oxygen_levels, min_val, max_val):
    pass
```

**Example Usage:**
```python
oxygen_levels = {
    "Command Module": 21,
    "Habitation Module": 20,
    "Laboratory Module": 19,
    "Airlock": 22,
    "Storage Bay": 18
}

print(check_oxygen_levels(oxygen_levels, 19, 22))    # ['Storage Bay']
```

**💡 Hint:** Accessing Keys, Values, and Key-Value Pairs

---

### Problem 16: Dictionary Difference

Given two dictionaries, return a new dictionary containing only key-value pairs found in the first dictionary but not in the second.

**Function Signature:**
```python
def data_difference(experiment1, experiment2):
    pass
```

**Example Usage:**
```python
exp1_data = {'temperature': 22, 'pressure': 101.3, 'humidity': 45}
exp2_data = {'temperature': 18, 'pressure': 101.3, 'radiation': 0.5}

print(data_difference(exp1_data, exp2_data))    # {'temperature': 22, 'humidity': 45}
```

---

### Problem 17: Find Most Frequent Item

Given a list of strings, return the string that appears most frequently. If there's a tie, return any of the tied strings.

**Function Signature:**
```python
def get_winner(votes):
    pass
```

**Example Usage:**
```python
votes1 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert", "Colbert"]
votes2 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert"]

print(get_winner(votes1))    # "Colbert"
print(get_winner(votes2))    # "Serenity" (or "Colbert" - both acceptable)
```

**✨ AI Hint:** Frequency Maps

---

### Problem 18: Check Complete Character Set

Given a string containing only lowercase letters, return True if it contains every letter a-z at least once.

**Function Signature:**
```python
def check_if_complete_transmission(transmission):
    """
    :type transmission: str
    :rtype: bool
    """
    pass
```

**Example Usage:**
```python
print(check_if_complete_transmission("thequickbrownfoxjumpsoverthelazydog"))    # True
print(check_if_complete_transmission("spacetravel"))                            # False
```

---

### Problem 19: Count String Pairs

Given an array of distinct strings, return the maximum number of pairs that can be formed where one string is the reverse of another.

**Function Signature:**
```python
def max_number_of_string_pairs(signals):
    pass
```

**Example Usage:**
```python
print(max_number_of_string_pairs(["cd", "ac", "dc", "ca", "zz"]))    # 2
print(max_number_of_string_pairs(["ab", "ba", "cc"]))                # 1
print(max_number_of_string_pairs(["aa", "ab"]))                      # 0
```

---

### Problem 20: Find Array Differences

Given two integer arrays, return a list where the first element contains integers in the first array but not the second, and the second element contains integers in the second array but not the first.

**Implement the given pseudocode:**
1. Convert signals1 and signals2 to sets
2. Find the difference between set1 and set2 and store it in diff1
3. Find the difference between set2 and set1 and store it in diff2
4. Return the list [diff1, diff2]

**Function Signature:**
```python
def find_difference(signals1, signals2):
    pass
```

**Example Usage:**
```python
print(find_difference([1, 2, 3], [2, 4, 6]))       # [[1, 3], [4, 6]]
print(find_difference([1, 2, 3, 3], [1, 1, 2, 2])) # [[3], []]
```

**✨ AI Hint:** Introduction to sets

---

### Problem 21: Count Common Elements

Given two integer arrays, return [answer1, answer2] where answer1 is the count of elements in the first array that exist in the second array, and answer2 is the count of elements in the second array that exist in the first array.

**Function Signature:**
```python
def find_common_signals(signals1, signals2):
    pass
```

**Example Usage:**
```python
print(find_common_signals([2, 3, 2], [1, 2]))                    # [2, 1]
print(find_common_signals([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6])) # [3, 4]
print(find_common_signals([3, 4, 2, 3], [1, 5]))                # [0, 0]
```

---

### Problem 22: Alternative Implementation

Re-implement the previous problem using a different approach (if you used dictionaries, try sets; if you used sets, try dictionaries). Compare the two solutions.

**Function Signature:**
```python
def find_common_signals(signals1, signals2):
    pass
```

**Example Usage:**
```python
print(find_common_signals([2, 3, 2], [1, 2]))                    # [2, 1]
print(find_common_signals([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6])) # [3, 4]
print(find_common_signals([3, 4, 2, 3], [1, 5]))                # [0, 0]
```

---

### Problem 23: Sort by Frequency

Given an array of integers, sort them by frequency (ascending) and by value (descending) as a tiebreaker.

**Fix the bugs in this code:**
```python
def frequency_sort(signals):
    freq = {}
    for signal in signals:
        if signal in freq:
            freq[signal] += 1
        else:
            freq[signal] = 0

    sorted_signals = sorted(signals, key=lambda x: (freq[x], x))

    return sorted_signals
```

**Example Usage:**
```python
print(frequency_sort([1, 1, 2, 2, 2, 3]))            # [3, 1, 1, 2, 2, 2]
print(frequency_sort([2, 3, 1, 3, 2]))               # [1, 3, 3, 2, 2]
print(frequency_sort([-1, 1, -6, 4, 5, -6, 1, 4, 1])) # [5, -1, 4, 4, -6, -6, 1, 1, 1]
```

**✨ AI Hint:** sorted()  
**💡 Hint:** Lambda Functions

---

### Problem 24: Find Final Destination

Given an array of paths where paths[i] = [start, end], find the destination that has no outgoing path (the final destination in a linear chain).

**Function Signature:**
```python
def find_final_hub(paths):
    pass
```

**Example Usage:**
```python
paths1 = [["Earth", "Mars"], ["Mars", "Titan"], ["Titan", "Europa"]]
paths2 = [["Alpha", "Beta"], ["Gamma", "Alpha"], ["Beta", "Delta"]]
paths3 = [["StationA", "StationZ"]]

print(find_final_hub(paths1))     # "Europa"
print(find_final_hub(paths2))     # "Delta"
print(find_final_hub(paths3))     # "StationZ"
```