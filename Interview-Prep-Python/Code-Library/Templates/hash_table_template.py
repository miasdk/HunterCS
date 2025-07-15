"""
Hash Table Templates for Python Interview Success
Common patterns and templates for hash table problems
"""

from collections import Counter, defaultdict
from typing import List, Dict, Set


# ========================================
# PATTERN 1: TWO SUM / COMPLEMENT SEARCH
# ========================================

def two_sum(nums: List[int], target: int) -> List[int]:
    """Hash table approach - O(n) time, O(n) space"""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def two_sum_all_pairs(nums: List[int], target: int) -> List[List[int]]:
    """Find all pairs that sum to target"""
    seen = {}
    result = []
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            # Add all previous occurrences
            for prev_idx in seen[complement]:
                result.append([prev_idx, i])
        
        if num not in seen:
            seen[num] = []
        seen[num].append(i)
    
    return result


# ========================================
# PATTERN 2: FREQUENCY COUNTING
# ========================================

def is_anagram(s: str, t: str) -> bool:
    """Multiple approaches for anagram checking"""
    
    # Method 1: Counter (most Pythonic)
    return Counter(s) == Counter(t)
    
    # Method 2: Manual counting (interview version)
    if len(s) != len(t):
        return False
    
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        count[char] = count.get(char, 0) - 1
        if count[char] == 0:
            del count[char]
    
    return len(count) == 0


def character_frequency(s: str) -> Dict[str, int]:
    """Various ways to count character frequency"""
    
    # Method 1: Counter
    return dict(Counter(s))
    
    # Method 2: get() method
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq
    
    # Method 3: defaultdict
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1
    return dict(freq)


# ========================================
# PATTERN 3: DUPLICATE DETECTION
# ========================================

def contains_duplicate(nums: List[int]) -> bool:
    """Check if array contains duplicates"""
    return len(nums) != len(set(nums))


def contains_duplicate_early_termination(nums: List[int]) -> bool:
    """Early termination version"""
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def find_duplicate(nums: List[int]) -> int:
    """Find the duplicate element"""
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1


# ========================================
# PATTERN 4: GROUPING/BUCKETING
# ========================================

def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Group strings that are anagrams"""
    groups = defaultdict(list)
    
    for s in strs:
        # Sorted string as key
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())


def group_by_character_count(strs: List[str]) -> List[List[str]]:
    """Group by character frequency signature"""
    groups = defaultdict(list)
    
    for s in strs:
        # Character count as key
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        groups[tuple(count)].append(s)
    
    return list(groups.values())


# ========================================
# PATTERN 5: SLIDING WINDOW WITH HASH
# ========================================

def longest_substring_without_repeating(s: str) -> int:
    """Sliding window with character tracking"""
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Shrink window while duplicate exists
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length


def longest_substring_k_distinct(s: str, k: int) -> int:
    """Longest substring with at most k distinct characters"""
    char_count = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Add current character
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Shrink window while more than k distinct
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length


# ========================================
# PATTERN 6: SET OPERATIONS
# ========================================

def intersection_of_arrays(nums1: List[int], nums2: List[int]) -> List[int]:
    """Intersection using sets"""
    return list(set(nums1) & set(nums2))


def union_of_arrays(nums1: List[int], nums2: List[int]) -> List[int]:
    """Union using sets"""
    return list(set(nums1) | set(nums2))


def difference_of_arrays(nums1: List[int], nums2: List[int]) -> List[int]:
    """Elements in nums1 but not in nums2"""
    return list(set(nums1) - set(nums2))


# ========================================
# UTILITY FUNCTIONS
# ========================================

def print_frequency_table(items: List) -> None:
    """Print frequency distribution"""
    freq = Counter(items)
    for item, count in freq.most_common():
        print(f"{item}: {count}")


def most_frequent_k(items: List, k: int) -> List:
    """Get k most frequent elements"""
    counter = Counter(items)
    return [item for item, count in counter.most_common(k)]


def least_frequent_k(items: List, k: int) -> List:
    """Get k least frequent elements"""
    counter = Counter(items)
    return [item for item, count in counter.most_common()[:-k-1:-1]]


# ========================================
# ADVANCED PATTERNS
# ========================================

def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    """Count subarrays with sum equal to k"""
    prefix_sum = 0
    sum_count = {0: 1}  # Handle case where prefix_sum == k
    result = 0
    
    for num in nums:
        prefix_sum += num
        
        # Check if (prefix_sum - k) exists
        if prefix_sum - k in sum_count:
            result += sum_count[prefix_sum - k]
        
        # Add current prefix_sum to count
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return result


def continuous_subarray_sum(nums: List[int], k: int) -> bool:
    """Check if subarray with sum multiple of k exists"""
    remainder_map = {0: -1}  # remainder -> index
    running_sum = 0
    
    for i, num in enumerate(nums):
        running_sum += num
        remainder = running_sum % k
        
        if remainder in remainder_map:
            # Check if subarray length >= 2
            if i - remainder_map[remainder] > 1:
                return True
        else:
            remainder_map[remainder] = i
    
    return False


# ========================================
# QUICK REFERENCE
# ========================================
"""
PYTHON HASH TABLE OPERATIONS:
- Insert: dict[key] = value     O(1) avg
- Access: dict[key]             O(1) avg, KeyError if missing
- Safe Access: dict.get(key)    O(1) avg, None if missing  
- Check: key in dict            O(1) avg
- Delete: del dict[key]         O(1) avg

COMMON PYTHON PATTERNS:
1. Two Sum: Use complement search with dict
2. Anagram: Counter(s1) == Counter(s2)
3. Duplicates: len(nums) != len(set(nums))
4. Grouping: defaultdict(list) with computed keys
5. Frequency: Counter(items) or dict with get()

PYTHON-SPECIFIC ADVANTAGES:
- dict.get(key, default) for safe access
- Counter for frequency analysis
- defaultdict for automatic initialization
- Set operations: &, |, - for intersection, union, difference
- List comprehensions for filtering

INTERVIEW TIPS:
- Use type hints for clarity
- Show multiple approaches (Counter vs manual)
- Explain time/space complexity
- Handle edge cases (empty input, single element)
""" 