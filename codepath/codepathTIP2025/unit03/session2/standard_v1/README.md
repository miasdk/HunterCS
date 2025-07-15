# Breakout Problems Session 2

## Table of Contents

### [Standard Problem Set Version 1](#standard-problem-set-version-1)
- [Manage Performance Stage Changes](#manage-performance-stage-changes)
- [Queue of Performance Requests](#queue-of-performance-requests)
- [Collecting Points at Festival Booths](#collecting-points-at-festival-booths)
- [Festival Booth Navigation](#festival-booth-navigation)
- [Merge Performance Schedules](#merge-performance-schedules)
- [Next Greater Event](#next-greater-event)
- [Sort Performances by Type](#sort-performances-by-type)

### [Standard Problem Set Version 2](#standard-problem-set-version-2)
- [Final Costs After Supply Discount](#final-costs-after-supply-discount)
- [Find First Symmetrical Landmark](#find-first-symmetrical-landmark)
- [Terrain Elevation Match](#terrain-elevation-match)
- [Find Expedition Log Concatenation Value](#find-expedition-log-concatenation-value)
- [Number of Explorers Unable to Gather Supplies](#number-of-explorers-unable-to-gather-supplies)
- [Count Balanced Terrain Subsections](#count-balanced-terrain-subsections)
- [Check Signal Prefix in Transmission](#check-signal-prefix-in-transmission)

## Standard Problem Set Version 1

### Manage Performance Stage Changes
Manage stage scheduling using stack operations for schedule, cancel, and reschedule actions.

**Function Signature:**
```python
def manage_stage_changes(changes):
    pass
```

**Example Usage:**
```python
print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))
# Returns: ["A", "C", "B", "D"]

print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
# Returns: []

print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 
# Returns: ["Z"]
```

**Key Concept:** Stack operations for undo/redo functionality

**Hint:** Stacks

---

### Queue of Performance Requests
Process performance requests in priority order using queue management.

**Function Signature:**
```python
def process_performance_requests(requests):
    pass
```

**Example Usage:**
```python
print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
# Returns: ['Music', 'Dance', 'Drama']

print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
# Returns: ['Concert', 'Stand-up Comedy', 'Poetry', 'Magic Show']
```

**Key Concept:** Priority queue processing

**Hint:** Queues

---

### Collecting Points at Festival Booths
Calculate total points collected using stack-based booth visiting simulation.

**Function Signature:**
```python
def collect_festival_points(points):
    pass
```

**Example Usage:**
```python
print(collect_festival_points([5, 8, 3, 10]))  # Returns: 26
print(collect_festival_points([2, 7, 4, 6]))   # Returns: 19
print(collect_festival_points([1, 5, 9, 2, 8])) # Returns: 25
```

**Key Concept:** Stack-based accumulation

---

### Festival Booth Navigation
Simulate treasure hunt navigation with backtracking using stack operations.

**Function Signature:**
```python
def booth_navigation(clues):
    pass
```

**Example Usage:**
```python
print(booth_navigation([1, 2, "back", 3, 4]))  # Returns: [1, 3, 4]
print(booth_navigation([5, 3, 2, "back", "back", 7]))  # Returns: [5, 7]
print(booth_navigation([1, "back", 2, "back", "back", 3]))  # Returns: [3]
```

**Key Concept:** Stack-based backtracking

---

### Merge Performance Schedules
Merge two schedules alternately, handling different lengths.

**Function Signature:**
```python
def merge_schedules(schedule1, schedule2):
    pass
```

**Example Usage:**
```python
print(merge_schedules("abc", "pqr"))   # Returns: "apbqcr"
print(merge_schedules("ab", "pqrs"))   # Returns: "apbqrs"
print(merge_schedules("abcd", "pq"))   # Returns: "apbqcd"
```

**Key Concept:** Two-pointer alternating merge

**Hint:** Two Pointer Technique

---

### Next Greater Event
Find next greater element for each item in subset array.

**Function Signature:**
```python
def next_greater_event(schedule1, schedule2):
    pass
```

**Example Usage:**
```python
print(next_greater_event([4, 1, 2], [1, 3, 4, 2]))  # Returns: [-1, 3, -1]
print(next_greater_event([2, 4], [1, 2, 3, 4]))     # Returns: [3, -1]
```

**Key Concept:** Stack-based next greater element

---

### Sort Performances by Type
Partition array into even and odd elements.

**Function Signature:**
```python
def sort_performances_by_type(performances):
    pass
```

**Example Usage:**
```python
print(sort_performances_by_type([3, 1, 2, 4]))  # Returns: [4, 2, 1, 3]
print(sort_performances_by_type([0]))           # Returns: [0]
```

**Key Concept:** Array partitioning by parity

---

## Standard Problem Set Version 2

### Final Costs After Supply Discount
Calculate final costs after applying discount based on next smaller element.

**Function Signature:**
```python
def final_supply_costs(costs):
    pass
```

**Example Usage:**
```python
print(final_supply_costs([8, 4, 6, 2, 3]))  # Returns: [4, 2, 4, 2, 3]
print(final_supply_costs([1, 2, 3, 4, 5]))  # Returns: [1, 2, 3, 4, 5]
print(final_supply_costs([10, 1, 1, 6]))    # Returns: [9, 0, 1, 6]
```

**Key Concept:** Stack-based next smaller element with discount calculation

**Hint:** Stacks

---

### Find First Symmetrical Landmark
Find the first palindromic string in an array.

**Function Signature:**
```python
def first_symmetrical_landmark(landmarks):
    pass
```

**Example Usage:**
```python
print(first_symmetrical_landmark(["canyon","forest","rotor","mountain"]))  # Returns: "rotor"
print(first_symmetrical_landmark(["plateau","valley","cliff"]))            # Returns: ""
```

**Key Concept:** Palindrome detection with two pointers

**Hint:** Two Pointer Technique, Helper Functions

---

### Terrain Elevation Match
Reconstruct elevation sequence from increase/decrease pattern.

**Function Signature:**
```python
def terrain_elevation_match(terrain):
    pass
```

**Example Usage:**
```python
print(terrain_elevation_match("IDID"))  # Returns: [0, 4, 1, 3, 2]
print(terrain_elevation_match("III"))   # Returns: [0, 1, 2, 3]
print(terrain_elevation_match("DDI"))   # Returns: [3, 2, 0, 1]
```

**Key Concept:** Pattern-based sequence reconstruction

---

### Find Expedition Log Concatenation Value
Calculate total concatenation value by combining first and last elements.

**Function Signature:**
```python
def find_the_log_conc_val(logs):
    pass
```

**Example Usage:**
```python
print(find_the_log_conc_val([7, 52, 2, 4]))      # Returns: 596
print(find_the_log_conc_val([5, 14, 13, 8, 12])) # Returns: 673
```

**Key Concept:** Two-pointer concatenation with string conversion

---

### Number of Explorers Unable to Gather Supplies
Simulate queue and stack interaction to count unmatched explorers.

**Function Signature:**
```python
def count_explorers(explorers, supplies):
    pass
```

**Example Usage:**
```python
print(count_explorers([1, 1, 0, 0], [0, 1, 0, 1]))        # Returns: 0
print(count_explorers([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1])) # Returns: 3
```

**Key Concept:** Queue simulation with stack-based supply distribution

---

### Count Balanced Terrain Subsections
Count substrings with equal numbers of 0s and 1s grouped consecutively.

**Function Signature:**
```python
def count_balanced_terrain_subsections(terrain):
    pass
```

**Example Usage:**
```python
print(count_balanced_terrain_subsections("00110011"))  # Returns: 6
print(count_balanced_terrain_subsections("10101"))     # Returns: 4
```

**Key Concept:** Substring analysis with balance checking

---

### Check Signal Prefix in Transmission
Find index of first word that starts with given prefix.

**Function Signature:**
```python
def is_prefix_of_signal(transmission, searchSignal):
    pass
```

**Example Usage:**
```python
print(is_prefix_of_signal("i love eating burger", "burg"))       # Returns: 4
print(is_prefix_of_signal("this problem is an easy problem", "pro")) # Returns: 2
print(is_prefix_of_signal("i am tired", "you"))                  # Returns: -1
```

**Key Concept:** String prefix matching with indexing