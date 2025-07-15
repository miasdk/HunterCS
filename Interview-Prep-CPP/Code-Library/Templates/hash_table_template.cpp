#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <algorithm>

/**
 * C++ Hash Table Templates for Technical Interviews
 * 
 * This file contains ready-to-use templates for the most common
 * hash table patterns in coding interviews.
 * 
 * Patterns covered:
 * 1. Frequency Counting
 * 2. Complement Search (Two Sum family)
 * 3. Grouping and Classification
 * 4. Seen/Visited Tracking
 * 5. Prefix/Suffix Mapping
 */

// =================================================================
// PATTERN 1: FREQUENCY COUNTING
// =================================================================

/**
 * Template: Basic frequency counting
 * Time: O(n), Space: O(k) where k = unique elements
 */
template<typename T>
std::unordered_map<T, int> getFrequency(const std::vector<T>& arr) {
    std::unordered_map<T, int> freq;
    for (const T& item : arr) {
        freq[item]++;
    }
    return freq;
}

/**
 * Template: Find most frequent element
 * Time: O(n), Space: O(k)
 */
template<typename T>
T findMostFrequent(const std::vector<T>& arr) {
    auto freq = getFrequency(arr);
    
    T mostFrequent = arr[0];
    int maxCount = 0;
    
    for (const auto& [item, count] : freq) {
        if (count > maxCount) {
            maxCount = count;
            mostFrequent = item;
        }
    }
    
    return mostFrequent;
}

/**
 * LeetCode 242: Valid Anagram
 * Time: O(n), Space: O(1) - limited alphabet
 */
bool isAnagram(std::string s, std::string t) {
    if (s.length() != t.length()) return false;
    
    std::unordered_map<char, int> freq;
    
    // Count characters in s
    for (char c : s) freq[c]++;
    
    // Subtract characters in t
    for (char c : t) {
        freq[c]--;
        if (freq[c] == 0) freq.erase(c);
    }
    
    return freq.empty();
}

// =================================================================
// PATTERN 2: COMPLEMENT SEARCH (TWO SUM FAMILY)
// =================================================================

/**
 * LeetCode 1: Two Sum
 * Time: O(n), Space: O(n)
 */
std::vector<int> twoSum(std::vector<int>& nums, int target) {
    std::unordered_map<int, int> needed; // value -> index
    
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        
        auto it = needed.find(complement);
        if (it != needed.end()) {
            return {it->second, i};
        }
        
        needed[nums[i]] = i;
    }
    
    return {}; // No solution found
}

/**
 * Template: Check if pair exists that sums to target
 * Time: O(n), Space: O(n)
 */
bool hasPairSum(const std::vector<int>& nums, int target) {
    std::unordered_set<int> seen;
    
    for (int num : nums) {
        int complement = target - num;
        if (seen.count(complement)) {
            return true;
        }
        seen.insert(num);
    }
    
    return false;
}

/**
 * Template: Find all unique pairs that sum to target
 * Time: O(n), Space: O(n)
 */
std::vector<std::pair<int, int>> findAllPairs(std::vector<int>& nums, int target) {
    std::unordered_map<int, int> freq;
    std::vector<std::pair<int, int>> result;
    
    // Count frequencies
    for (int num : nums) freq[num]++;
    
    for (const auto& [num, count] : freq) {
        int complement = target - num;
        
        if (num == complement) {
            // Same number, need at least 2 occurrences
            if (count >= 2) {
                result.push_back({num, num});
            }
        } else if (freq.count(complement) && num < complement) {
            // Different numbers, avoid duplicates
            result.push_back({num, complement});
        }
    }
    
    return result;
}

// =================================================================
// PATTERN 3: GROUPING AND CLASSIFICATION
// =================================================================

/**
 * LeetCode 49: Group Anagrams
 * Time: O(n * k log k), Space: O(n * k) where k = average string length
 */
std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs) {
    std::unordered_map<std::string, std::vector<std::string>> groups;
    
    for (const std::string& str : strs) {
        std::string key = str;
        std::sort(key.begin(), key.end());
        groups[key].push_back(str);
    }
    
    std::vector<std::vector<std::string>> result;
    for (const auto& [key, group] : groups) {
        result.push_back(group);
    }
    
    return result;
}

/**
 * Template: Group by custom property
 * Time: O(n), Space: O(n)
 */
template<typename T, typename KeyFunc>
std::unordered_map<decltype(std::declval<KeyFunc>()(std::declval<T>())), std::vector<T>>
groupBy(const std::vector<T>& items, KeyFunc keyFunc) {
    std::unordered_map<decltype(keyFunc(items[0])), std::vector<T>> groups;
    
    for (const T& item : items) {
        auto key = keyFunc(item);
        groups[key].push_back(item);
    }
    
    return groups;
}

// =================================================================
// PATTERN 4: SEEN/VISITED TRACKING
// =================================================================

// Definition for singly-linked list (commonly used in interviews)
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

/**
 * LeetCode 141: Linked List Cycle
 * Time: O(n), Space: O(n)
 */
bool hasCycle(ListNode *head) {
    std::unordered_set<ListNode*> visited;
    
    ListNode* current = head;
    while (current) {
        if (visited.count(current)) {
            return true; // Cycle detected
        }
        visited.insert(current);
        current = current->next;
    }
    
    return false;
}

/**
 * LeetCode 217: Contains Duplicate
 * Time: O(n), Space: O(n)
 */
bool containsDuplicate(std::vector<int>& nums) {
    std::unordered_set<int> seen;
    
    for (int num : nums) {
        if (seen.count(num)) {
            return true;
        }
        seen.insert(num);
    }
    
    return false;
}

/**
 * Template: Track visited with additional data
 */
template<typename Node, typename Data>
class VisitedTracker {
private:
    std::unordered_map<Node, Data> visited;
    
public:
    bool isVisited(const Node& node) const {
        return visited.count(node) > 0;
    }
    
    void visit(const Node& node, const Data& data) {
        visited[node] = data;
    }
    
    const Data& getData(const Node& node) const {
        return visited.at(node);
    }
    
    void clear() {
        visited.clear();
    }
};

// =================================================================
// PATTERN 5: PREFIX/SUFFIX MAPPING
// =================================================================

/**
 * LeetCode 560: Subarray Sum Equals K
 * Time: O(n), Space: O(n)
 */
int subarraySum(std::vector<int>& nums, int k) {
    std::unordered_map<int, int> prefixSums; // sum -> count
    prefixSums[0] = 1; // Empty prefix
    
    int currentSum = 0;
    int result = 0;
    
    for (int num : nums) {
        currentSum += num;
        int needed = currentSum - k;
        
        if (prefixSums.count(needed)) {
            result += prefixSums[needed];
        }
        
        prefixSums[currentSum]++;
    }
    
    return result;
}

/**
 * Template: Prefix sum with custom operation
 * Time: O(n), Space: O(n)
 */
template<typename T, typename Op>
std::vector<T> computePrefixSums(const std::vector<T>& arr, Op operation, T identity) {
    std::vector<T> prefixSums(arr.size() + 1, identity);
    
    for (int i = 0; i < arr.size(); i++) {
        prefixSums[i + 1] = operation(prefixSums[i], arr[i]);
    }
    
    return prefixSums;
}

/**
 * LeetCode 525: Contiguous Array (Equal 0s and 1s)
 * Time: O(n), Space: O(n)
 */
int findMaxLength(std::vector<int>& nums) {
    std::unordered_map<int, int> firstOccurrence; // balance -> index
    firstOccurrence[0] = -1; // Before array starts
    
    int balance = 0;
    int maxLength = 0;
    
    for (int i = 0; i < nums.size(); i++) {
        balance += (nums[i] == 1) ? 1 : -1;
        
        if (firstOccurrence.count(balance)) {
            maxLength = std::max(maxLength, i - firstOccurrence[balance]);
        } else {
            firstOccurrence[balance] = i;
        }
    }
    
    return maxLength;
}

// =================================================================
// UTILITY FUNCTIONS
// =================================================================

/**
 * Custom hash function for pairs (useful for coordinate problems)
 */
struct PairHash {
    size_t operator()(const std::pair<int, int>& p) const {
        return std::hash<int>{}(p.first) ^ (std::hash<int>{}(p.second) << 1);
    }
};

/**
 * Custom hash function for vectors (useful for grouping problems)
 */
struct VectorHash {
    size_t operator()(const std::vector<int>& v) const {
        size_t hash = 0;
        for (int i : v) {
            hash ^= std::hash<int>{}(i) + 0x9e3779b9 + (hash << 6) + (hash >> 2);
        }
        return hash;
    }
};

/**
 * Rolling hash implementation for string problems
 */
class RollingHash {
private:
    static const long long BASE = 31;
    static const long long MOD = 1e9 + 7;
    
public:
    long long computeHash(const std::string& s) const {
        long long hash = 0;
        long long power = 1;
        
        for (char c : s) {
            hash = (hash + (c - 'a' + 1) * power) % MOD;
            power = (power * BASE) % MOD;
        }
        
        return hash;
    }
    
    long long updateHash(long long oldHash, char removeChar, char addChar, 
                        long long power, int windowSize) const {
        // Remove the leftmost character
        oldHash = (oldHash - (removeChar - 'a' + 1) + MOD) % MOD;
        oldHash = (oldHash * BASE) % MOD;
        
        // Add the new rightmost character
        oldHash = (oldHash + (addChar - 'a' + 1) * power) % MOD;
        
        return oldHash;
    }
};

// =================================================================
// INTERVIEW HELPERS
// =================================================================

/**
 * Pretty print hash map (useful for debugging)
 */
template<typename K, typename V>
void printHashMap(const std::unordered_map<K, V>& map, const std::string& name = "map") {
    std::cout << name << ": {";
    bool first = true;
    for (const auto& [key, value] : map) {
        if (!first) std::cout << ", ";
        std::cout << key << ": " << value;
        first = false;
    }
    std::cout << "}" << std::endl;
}

/**
 * Check if solution is correct for Two Sum
 */
bool validateTwoSum(const std::vector<int>& nums, const std::vector<int>& result, int target) {
    if (result.size() != 2) return false;
    int i = result[0], j = result[1];
    if (i < 0 || i >= nums.size() || j < 0 || j >= nums.size()) return false;
    return nums[i] + nums[j] == target && i != j;
}

// =================================================================
// EXAMPLE USAGE AND TESTING
// =================================================================

void demonstrateHashTablePatterns() {
    std::cout << "=== Hash Table Patterns Demo ===" << std::endl;
    
    // Pattern 1: Frequency Counting
    std::vector<int> nums = {1, 2, 2, 3, 3, 3};
    auto freq = getFrequency(nums);
    std::cout << "Most frequent: " << findMostFrequent(nums) << std::endl;
    
    // Pattern 2: Two Sum
    std::vector<int> twoSumNums = {2, 7, 11, 15};
    auto result = twoSum(twoSumNums, 9);
    std::cout << "Two Sum indices: [" << result[0] << ", " << result[1] << "]" << std::endl;
    
    // Pattern 3: Grouping
    std::vector<std::string> words = {"eat", "tea", "tan", "ate", "nat", "bat"};
    auto anagramGroups = groupAnagrams(words);
    std::cout << "Anagram groups count: " << anagramGroups.size() << std::endl;
    
    // Pattern 4: Duplicate detection
    std::vector<int> dupNums = {1, 2, 3, 1};
    std::cout << "Contains duplicate: " << containsDuplicate(dupNums) << std::endl;
    
    // Pattern 5: Subarray sum
    std::vector<int> subarrayNums = {1, 1, 1};
    std::cout << "Subarrays with sum 2: " << subarraySum(subarrayNums, 2) << std::endl;
}

// Uncomment to run demo
// int main() {
//     demonstrateHashTablePatterns();
//     return 0;
// } 