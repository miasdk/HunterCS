# Question 9: Golf Scores Problem Breakdown

## Problem Statement
You're given a list of golf scores, each representing 1 round of golf played by 1 player, consisting of the golfer's name and how many strokes he took. **A golfer may appear multiple times on the list.** Print out each golfer's name and best (lowest) score. Use hash maps to do this in linear time. All golf scores are positive integers, and in golf, a lower score is better.

**Sample Input:** `{("Tiger Woods", 73), ("Jack Nicklaus", 71), ("Tiger Woods", 66), ("Arnold Palmer", 68)}`
**Sample Output:** `Tiger Woods 66, Jack Nicklaus 71, Arnold Palmer 68`

---

## Algorithm Approach

### Data Structure Choice
- **Primary Structure**: `std::unordered_map<std::string, int>`
  - **Key**: Player name (string)
  - **Value**: Best score so far (int)
- **Why unordered_map?**: O(1) average lookup and insertion time

### Algorithm Steps

#### Step 1: Declare the Data Structure
```cpp
std::unordered_map<std::string, int> bestScores;
```

#### Step 2: Process Input Vector
```cpp
for (const auto& score : scores) {
    std::string name = score.first;
    int currentScore = score.second;
    
    // Check if player exists and update best score
}
```

#### Step 3: Handle New vs Existing Players
```cpp
if (bestScores.find(name) == bestScores.end()) {
    // New player - add to map
    bestScores[name] = currentScore;
} else {
    // Existing player - update if current score is better (lower)
    if (currentScore < bestScores[name]) {
        bestScores[name] = currentScore;
    }
}
```

#### Step 4: Output Results
```cpp
for (const auto& player : bestScores) {
    std::cout << player.first << " " << player.second << ", ";
}
```

---

## Complete Solution

```cpp
void printBestScores(std::vector<std::pair<std::string, int>> scores) {
    // Step 1: Declare unordered map
    std::unordered_map<std::string, int> bestScores;
    
    // Step 2: Process each score entry
    for (const auto& score : scores) {
        std::string name = score.first;
        int currentScore = score.second;
        
        // Step 3: Check if player exists and update best score
        if (bestScores.find(name) == bestScores.end()) {
            // New player
            bestScores[name] = currentScore;
        } else {
            // Existing player - update if current score is better (lower)
            if (currentScore < bestScores[name]) {
                bestScores[name] = currentScore;
            }
        }
    }
    
    // Step 4: Print results
    for (const auto& player : bestScores) {
        std::cout << player.first << " " << player.second;
        // Add comma formatting as needed
    }
}
```

---

## Alternative Implementation (More Concise)

```cpp
void printBestScores(std::vector<std::pair<std::string, int>> scores) {
    std::unordered_map<std::string, int> bestScores;
    
    for (const auto& score : scores) {
        std::string name = score.first;
        int currentScore = score.second;
        
        // Use count() to check existence
        if (bestScores.count(name) == 0 || currentScore < bestScores[name]) {
            bestScores[name] = currentScore;
        }
    }
    
    // Output
    for (const auto& player : bestScores) {
        std::cout << player.first << " " << player.second << ", ";
    }
}
```

---

## Key Concepts & Pitfalls

### ✅ What You Need to Get Right

1. **Proper Map Declaration**: `std::unordered_map<std::string, int>`

2. **Accessing Pair Elements**: 
   - `score.first` for name
   - `score.second` for score value

3. **Existence Checking**: Use `.find()`, `.count()`, or handle the zero-initialization carefully

4. **Comparison Logic**: Lower scores are better in golf (`currentScore < bestScores[name]`)

5. **Iteration**: Use range-based for loops or iterators properly

### ❌ Common Mistakes to Avoid

1. **Wrong Data Types**: Using wrong template parameters for the map

2. **Zero-Value Confusion**: Treating a newly created map element with value 0 as an actual score

3. **Comparison Direction**: Using `>` instead of `<` (forgetting lower is better in golf)

4. **Syntax Errors**: Incorrect iterator usage or pair access

---

## Time Complexity Analysis

- **Overall**: O(n) where n is the number of score entries
- **Per Operation**: 
  - Map lookup: O(1) average
  - Map insertion: O(1) average
  - Iteration through final map: O(k) where k is number of unique players

---

## Why This Student Got Low Points

Looking at the graded response, the student received only 3/20 points because:

1. **Incorrect Map Declaration**: The fundamental data structure wasn't properly declared
2. **Missing Core Logic**: No proper handling of the key-value relationship
3. **Syntax Issues**: Multiple syntax errors that prevented compilation
4. **Incomplete Understanding**: The solution didn't demonstrate understanding of hash map operations

The grader noted: "You don't even declare the map right, and there's certainly nothing here that qualifies for any other parts of this rubric."