/**
 * Hash Table Templates for Interview Success
 * Common patterns and templates for hash table problems
 */

#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <string>
using namespace std;

// ========================================
// PATTERN 1: TWO SUM / COMPLEMENT SEARCH
// ========================================
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> map; // value -> index
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (map.count(complement)) {
            return {map[complement], i};
        }
        map[nums[i]] = i;
    }
    return {};
}

// ========================================
// PATTERN 2: FREQUENCY COUNTING
// ========================================
bool isAnagram(string s, string t) {
    if (s.length() != t.length()) return false;
    
    unordered_map<char, int> count;
    for (char c : s) count[c]++;
    for (char c : t) count[c]--;
    
    for (auto& p : count) {
        if (p.second != 0) return false;
    }
    return true;
}

// ========================================
// PATTERN 3: DUPLICATE DETECTION
// ========================================
bool containsDuplicate(vector<int>& nums) {
    unordered_set<int> seen;
    for (int num : nums) {
        if (seen.count(num)) return true;
        seen.insert(num);
    }
    return false;
}

bool containsNearbyDuplicate(vector<int>& nums, int k) {
    unordered_map<int, int> map; // value -> most recent index
    for (int i = 0; i < nums.size(); i++) {
        if (map.count(nums[i]) && i - map[nums[i]] <= k) {
            return true;
        }
        map[nums[i]] = i;
    }
    return false;
}

// ========================================
// PATTERN 4: GROUPING/BUCKETING
// ========================================
vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> groups;
    
    for (string& s : strs) {
        string key = s;
        sort(key.begin(), key.end()); // sorted string as key
        groups[key].push_back(s);
    }
    
    vector<vector<string>> result;
    for (auto& group : groups) {
        result.push_back(group.second);
    }
    return result;
}

// ========================================
// PATTERN 5: SLIDING WINDOW WITH HASH
// ========================================
int lengthOfLongestSubstring(string s) {
    unordered_set<char> window;
    int left = 0, maxLen = 0;
    
    for (int right = 0; right < s.length(); right++) {
        // Shrink window while duplicate exists
        while (window.count(s[right])) {
            window.erase(s[left]);
            left++;
        }
        
        window.insert(s[right]);
        maxLen = max(maxLen, right - left + 1);
    }
    
    return maxLen;
}

// ========================================
// UTILITY FUNCTIONS
// ========================================

// Print hash map contents (debugging)
template<typename K, typename V>
void printMap(const unordered_map<K, V>& map) {
    for (const auto& pair : map) {
        cout << pair.first << " -> " << pair.second << "\n";
    }
}

// Check if two maps are equal
template<typename K, typename V>
bool mapsEqual(const unordered_map<K, V>& a, const unordered_map<K, V>& b) {
    if (a.size() != b.size()) return false;
    for (const auto& pair : a) {
        auto it = b.find(pair.first);
        if (it == b.end() || it->second != pair.second) {
            return false;
        }
    }
    return true;
}

// ========================================
// QUICK REFERENCE
// ========================================
/*
HASH TABLE OPERATIONS:
- Insert: map[key] = value     O(1) avg
- Access: map[key]             O(1) avg  
- Check:  map.count(key)       O(1) avg
- Delete: map.erase(key)       O(1) avg

COMMON PATTERNS:
1. Two Sum: Use complement search
2. Anagram: Count character frequencies  
3. Duplicates: Track seen elements
4. Grouping: Use property as key
5. Window: Track current window contents

INTERVIEW TIPS:
- Always check if key exists before accessing
- Use unordered_map/set for O(1) ops
- Consider space-time tradeoffs
- Handle edge cases (empty input, single element)
*/ 