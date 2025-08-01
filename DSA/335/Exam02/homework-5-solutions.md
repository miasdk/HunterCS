# Homework 5: Hash Tables - Solutions and Explanations

## Part 1: Textbook Questions

### 5.1 Hash Table Construction

For the set {4371, 1323, 6173, 4199, 4344, 9679, 1989} and hash function h(x) = x mod 10:

#### a. Separate Chaining Hash Table

| Index | Chain |
|-------|-------|
| 0 | (empty) |
| 1 | 4371 → 1 → (end) |
| 2 | (empty) |
| 3 | 1323 → 6173 → (end) |
| 4 | 4344 → (end) |
| 5 | (empty) |
| 6 | (empty) |
| 7 | (empty) |
| 8 | (empty) |
| 9 | 4199 → 9679 → 1989 → (end) |

**Explanation:**
- 4371 % 10 = 1, so it's stored at index 1
- 1323 % 10 = 3, so it's stored at index 3
- 6173 % 10 = 3, collision with 1323, so add to chain at index 3
- 4199 % 10 = 9, so it's stored at index 9
- 4344 % 10 = 4, so it's stored at index 4
- 9679 % 10 = 9, collision with 4199, so add to chain at index 9
- 1989 % 10 = 9, collision with 4199 and 9679, so add to chain at index 9

#### b. Linear Probing Hash Table

| Index | Initial | After 4371 | After 1323 | After 6173 | After 4199 | After 4344 | After 9679 | After 1989 |
|-------|---------|------------|------------|------------|------------|------------|------------|------------|
| 0 | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | 9679 | 9679 |
| 1 | (empty) | 4371 | 4371 | 4371 | 4371 | 4371 | 4371 | 4371 |
| 2 | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | 1989 |
| 3 | (empty) | (empty) | 1323 | 1323 | 1323 | 1323 | 1323 | 1323 |
| 4 | (empty) | (empty) | (empty) | 6173 | 6173 | 6173 | 6173 | 6173 |
| 5 | (empty) | (empty) | (empty) | (empty) | (empty) | 4344 | 4344 | 4344 |
| 6 | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) |
| 7 | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) |
| 8 | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) |
| 9 | (empty) | (empty) | (empty) | (empty) | 4199 | 4199 | 4199 | 4199 |

**Explanation:**
- 4371 % 10 = 1, so it's stored at index 1
- 1323 % 10 = 3, so it's stored at index 3
- 6173 % 10 = 3, collision with 1323, linear probe to index 4
- 4199 % 10 = 9, so it's stored at index 9
- 4344 % 10 = 4, collision with 6173, linear probe to index 5
- 9679 % 10 = 9, collision with 4199, linear probe to index 0
- 1989 % 10 = 9, collision with 4199, linear probe to index 0, collision with 9679, linear probe to index 2

#### c. Quadratic Probing Hash Table

| Index | Initial | After 4371 | After 1323 | After 6173 | After 4199 | After 4344 | After 9679 | After 1989 |
|-------|---------|------------|------------|------------|------------|------------|------------|------------|
| 0 | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | 9679 | 9679 |
| 1 | (empty) | 4371 | 4371 | 4371 | 4371 | 4371 | 4371 | 4371 |
| 2 | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) |
| 3 | (empty) | (empty) | 1323 | 1323 | 1323 | 1323 | 1323 | 1323 |
| 4 | (empty) | (empty) | (empty) | 6173 | 6173 | 6173 | 6173 | 6173 |
| 5 | (empty) | (empty) | (empty) | (empty) | (empty) | 4344 | 4344 | 4344 |
| 6 | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) |
| 7 | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) |
| 8 | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | 1989 |
| 9 | (empty) | (empty) | (empty) | (empty) | 4199 | 4199 | 4199 | 4199 |

**Explanation:**
- 4371 % 10 = 1, so it's stored at index 1
- 1323 % 10 = 3, so it's stored at index 3
- 6173 % 10 = 3, collision with 1323, quadratic probe to index (3 + 1²) = 4
- 4199 % 10 = 9, so it's stored at index 9
- 4344 % 10 = 4, collision with 6173, quadratic probe to index (4 + 1²) = 5
- 9679 % 10 = 9, collision with 4199, quadratic probe to index (9 + 1²) % 10 = 0
- 1989 % 10 = 9, collision with 4199, quadratic probe to index (9 + 1²) % 10 = 0, collision with 9679, quadratic probe to index (9 + 2²) % 10 = 8

### 5.2 Rehashing

Rehashing the hash table in Exercise 5.1c using x % 23 as the new hash function:

| Index | Value |
|-------|-------|
| 0 | (empty) |
| 1 | 4371 |
| 2 | (empty) |
| 3 | (empty) |
| 4 | (empty) |
| 5 | (empty) |
| 6 | (empty) |
| 7 | (empty) |
| 8 | (empty) |
| 9 | 6173 |
| 10 | (empty) |
| 11 | 1989 |
| 12 | 1323 |
| 13 | 4199 |
| 14 | (empty) |
| 15 | (empty) |
| 16 | (empty) |
| 17 | (empty) |
| 18 | (empty) |
| 19 | 9679 |
| 20 | 4344 |
| 21 | (empty) |
| 22 | (empty) |

**Explanation:**
- 4371 % 23 = 1, so it's stored at index 1
- 1323 % 23 = 12, so it's stored at index 12
- 6173 % 23 = 9, so it's stored at index 9
- 4199 % 23 = 13, so it's stored at index 13
- 4344 % 23 = 20, so it's stored at index 20
- 9679 % 23 = 19, so it's stored at index 19
- 1989 % 23 = 11, so it's stored at index 11

Notice that with the larger table size and a prime number for modulo, we have no collisions, resulting in a more efficient table.

### 5.4 Rehashing to a Smaller Table

**Answer:** The table must be at least half empty (load factor ≤ 0.5)

**Explanation:**
If we rehash to a larger table when the load factor exceeds 1 (elements ≥ table size), for consistency we should rehash to a smaller table when the load factor falls below 0.5 (elements ≤ table size/2). This maintains a balance between space efficiency and performance. If the table is less than half full, we're wasting space, and rehashing to a table of half the size keeps the load factor in the desired range (0.5 to 1).

### 5.7b Revised Quadratic Probing Algorithm

**Answer:** The revised algorithm (inserting into the first inactive cell rather than the position suggested by findPos) is faster when there are many deleted elements in the table.

**Explanation:**
- **When it's faster:** If many elements have been deleted and marked as "inactive", the original algorithm would continue probing past these slots. The revised algorithm reuses these inactive slots immediately, resulting in shorter probe sequences and faster insertions.
- **When it's slower:** During lookups, we still need to continue probing past inactive slots, so we don't save any time there. In fact, the revised algorithm could be slightly slower for lookups because it increases the average probe length for elements inserted after deletions.

### 5.8 Cubic Probing

**Answer:** Cubic probing does not generally improve over quadratic probing.

**Explanation:**
Cubic probing uses the formula h(x) + i³ for handling collisions. The large jumps in the probe sequence result in:
1. Poor cache locality (accessing memory locations far apart)
2. Less efficient memory access patterns
3. No significant improvement in reducing clustering
4. More complex calculations for each probe
5. Potential for longer probe sequences

Quadratic probing already provides a good balance between reducing clustering and maintaining reasonable probe sequences, while cubic probing introduces unnecessary complexity without substantial benefits.

### 5.10 Collision Resolution Strategies

| Strategy | Pros | Cons |
|----------|------|------|
| Linear Probing | - Simple to implement<br>- Good cache locality<br>- Low memory overhead | - Primary clustering<br>- Performance degrades with high load factors |
| Quadratic Probing | - Reduces primary clustering<br>- Better performance than linear for high load factors | - Can fail to find empty slots in some cases<br>- Secondary clustering |
| Separate Chaining | - Simple deletion<br>- Works well with high load factors<br>- No "full table" problem | - Extra memory for linked list pointers<br>- Worse cache performance |
| Double Hashing | - Eliminates clustering<br>- More uniform distribution | - Requires a good secondary hash function<br>- More computation per probe |

### 5.12 Remembered Hash Values

**Answer:** Hash values remain valid as long as the hash function's key fields do not change.

**Explanation:**
For an Employee class with a stored hash value:
1. The hash value remains valid as long as any fields used in the hash calculation remain unchanged (e.g., employee ID, name, etc.)
2. If any field that contributes to the hash calculation is modified, the stored hash value must be invalidated or recalculated
3. The class should provide a mechanism to track when relevant fields change and update the stored hash value accordingly
4. This approach trades space (storing the hash) for time (avoiding recomputation)

## Part 2: Hash Functions

### Hash Function Analysis

#### Figure 5.2: Simple Sum of Characters
```cpp
int hash(const string & key, int tableSize) { 
    int hashVal = 0; 
    
    for(char ch : key)
        hashVal += ch; 
        
    return hashVal % tableSize; 
}
```

**Pros:**
- Very simple to implement
- Fast computation

**Cons:**
- Poor distribution for similar strings
- Anagrams produce the same hash value
- Inefficient for large keys
- High collision rate

#### Figure 5.3: Weighted First Three Characters
```cpp
int hash(const string & key, int tableSize) { 
    return (key[0] + 27 * key[1] + 729 * key[2]) % tableSize;
}
```

**Pros:**
- Fast for any length string
- Better distribution than simple sum

**Cons:**
- Only uses first three characters
- Poor for strings with common prefixes
- Ignores most of the string's content
- Doesn't work for strings shorter than 3 characters

#### Figure 5.4: Polynomial Hash
```cpp
unsigned int hash(const string & key, int tableSize) {
    unsigned int hashVal = 0; 
    
    for(char ch : key) 
        hashVal = 37 * hashVal + ch; 
        
    return hashVal % tableSize; 
}
```

**Pros:**
- Uses all characters in the string
- Good distribution properties
- Reduces collisions significantly
- Works for all string lengths

**Cons:**
- Slightly more computation required
- Potential for overflow with very long strings
- Choice of multiplier (37) affects distribution

### Function Explanations (p.200)

```cpp
void makeEmpty() { 
    for(auto & thisList : theLists) // Iterate through each list in the hash table
        thisList.clear();           // Clear each list to remove all elements
} 
```
This function empties the hash table by clearing each linked list at every position in the hash table.

```cpp
bool contains(const HashedObj & x) {
    // Get the list at the index computed by hashing x
    auto & whichList = theLists[myhash(x)];
    
    // Use the standard find algorithm to search for x in the list
    // Return true if x is found (iterator not equal to end of list)
    return find(begin(whichList), end(whichList), x) != end(whichList); 
}
```
This function checks if an element exists in the hash table by:
1. Computing the hash value for the element
2. Looking at the linked list at that hash position
3. Using the standard find algorithm to search for the element in the list

```cpp
bool remove(const HashedObj & x) {
    // Get the list at the index computed by hashing x
    auto & whichList = theLists[myhash(x)]; 
    
    // Find x in the list
    auto itr = find(begin(whichList), end(whichList), x); 
    
    // If x is not found, return false
    if(itr == end(whichList))
        return false; 
    
    // Remove x from the list and decrement the size counter
    whichList.erase(itr);
    --currentSize;
    return true;
}
```
This function removes an element from the hash table by:
1. Finding the list where the element should be
2. Searching for the element in that list
3. If found, erasing it and decrementing the size counter

```cpp
bool insert(const HashedObj & x) {
    // Get the list at the index computed by hashing x
    auto & whichList = theLists[myhash(x)];
    
    // Check if x is already in the list
    if(find(begin(whichList), end(whichList), x) != end(whichList))
        return false;
    
    // Add x to the list
    whichList.push_back(x);
    
    // Check if rehashing is needed and rehash if necessary
    if(++currentSize > theLists.size())
        rehash();
        
    return true;
}
```
This function inserts an element into the hash table by:
1. Finding the correct list based on the hash value
2. Checking if the element already exists (to avoid duplicates)
3. Adding the element to the end of the list if it doesn't exist
4. Incrementing the size counter and checking if rehashing is needed

## Part 3: Coding Questions

### 219. Contains Duplicate II

**Problem:** Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

```cpp
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        std::unordered_map<int, int> numToIndex; 

        // Iterate through the nums vector
        for(int i = 0; i < nums.size(); ++i) {
            // Check if the current number already exists in our map
            if(numToIndex.find(nums[i]) != numToIndex.end()) {
                // If it exists, check if the distance between indices is <= k
                if(i - numToIndex[nums[i]] <= k) {
                    return true;
                }
            }
            
            // Always update the map with the current index for this number
            numToIndex[nums[i]] = i; 
        }
        return false; 
    }
};
```

**Explanation:**
1. Create a hash map that maps each number to its most recent index
2. Iterate through the array:
   - If the current number is already in the map, check if the distance between the current index and the stored index is <= k
   - If yes, return true (found a pair)
   - If no or if the number isn't in the map yet, update the map with the current index
3. If we finish iterating without finding a pair, return false

**Time Complexity:** O(n) - we iterate through the array once
**Space Complexity:** O(min(n, k)) - at most we store k+1 elements in the hash map

### 187. Repeated DNA Sequences

**Problem:** Find all 10-letter-long sequences that occur more than once in a DNA string.

```cpp
class Solution {
public:
    std::vector<std::string> findRepeatedDnaSequences(std::string s) {
        std::vector<std::string> result;
        std::unordered_map<std::string, int> substringCount;

        // Edge case: If the string is shorter than 10 characters, return empty result
        if (s.length() < 10) {
            return result;
        }

        // Slide a window of size 10 over the string
        for (int i = 0; i <= s.length() - 10; ++i) {
            // Extract the current 10-letter substring
            std::string substring = s.substr(i, 10);

            // Increment the count for this substring
            substringCount[substring]++;

            // If the count reaches 2, add it to the result (to avoid duplicates)
            if (substringCount[substring] == 2) {
                result.push_back(substring);
            }
        }

        return result;
    }
};
```

**Explanation:**
1. Create a hash map to count occurrences of each 10-letter substring
2. Slide a window of size 10 over the input string
3. For each substring:
   - Increment its count in the hash map
   - If the count reaches exactly 2, add it to the result vector (we only add it once)
4. Return the result vector with all repeated sequences

**Time Complexity:** O(n·10) = O(n) where n is the length of the string, and 10 is the cost of hash computation and substring extraction
**Space Complexity:** O(n) in the worst case where there are many unique substrings
