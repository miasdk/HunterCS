"""
Two Sum - The Most Important Interview Problem

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

LeetCode: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Pattern: Hash Table / Complement Search
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Hash table approach - O(n) time, O(n) space
    
    Algorithm:
    1. Iterate through array with index and value
    2. Calculate complement = target - current_number
    3. Check if complement exists in hash table
    4. If found, return [stored_index, current_index]
    5. If not found, store current_number -> current_index
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List of two indices that sum to target
        
    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
        >>> two_sum([3, 2, 4], 6)
        [1, 2]
    """
    seen = {}  # value -> index mapping
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return []  # No solution found


def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Brute force approach - O(n²) time, O(1) space
    
    Used for comparison and to show optimization thinking.
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_explicit_check(nums: List[int], target: int) -> List[int]:
    """
    Alternative implementation with explicit None check
    
    Some interviewers prefer explicit checks over 'in' operator
    """
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Explicit check using get()
        if seen.get(complement) is not None:
            return [seen[complement], i]
        
        seen[num] = i
    
    return []


def two_sum_with_validation(nums: List[int], target: int) -> List[int]:
    """
    Production-ready version with input validation
    
    Shows defensive programming skills
    """
    # Input validation
    if not nums or len(nums) < 2:
        return []
    
    seen = {}
    
    for i, num in enumerate(nums):
        # Handle potential overflow for very large numbers
        try:
            complement = target - num
        except OverflowError:
            continue
            
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return []


# ========================================
# VARIANTS AND EXTENSIONS
# ========================================

def two_sum_all_pairs(nums: List[int], target: int) -> List[List[int]]:
    """
    Find ALL pairs that sum to target (not just first one)
    
    Returns list of all index pairs
    """
    seen = {}
    result = []
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            # Add all previous occurrences of complement
            for prev_index in seen[complement]:
                result.append([prev_index, i])
        
        # Store current number's index
        if num not in seen:
            seen[num] = []
        seen[num].append(i)
    
    return result


def two_sum_values(nums: List[int], target: int) -> List[int]:
    """
    Return the actual values instead of indices
    """
    seen = set()
    
    for num in nums:
        complement = target - num
        if complement in seen:
            return [complement, num]
        seen.add(num)
    
    return []


def two_sum_closest(nums: List[int], target: int) -> List[int]:
    """
    Find pair with sum closest to target
    
    Returns indices of the closest pair
    """
    if len(nums) < 2:
        return []
    
    closest_sum = float('inf')
    result = []
    
    seen = {}
    
    for i, num in enumerate(nums):
        for prev_num, prev_idx in seen.items():
            current_sum = num + prev_num
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
                result = [prev_idx, i]
        
        seen[num] = i
    
    return result


# ========================================
# TEST CASES
# ========================================

def test_two_sum():
    """Comprehensive test cases"""
    
    # Basic test cases
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    
    # Edge cases
    assert two_sum([], 0) == []
    assert two_sum([1], 0) == []
    assert two_sum([1, 2], 4) == []
    
    # Negative numbers
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]
    
    # Zero cases
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]
    
    print("All tests passed!")


if __name__ == "__main__":
    # Run tests
    test_two_sum()
    
    # Interactive examples
    print("\n=== Two Sum Examples ===")
    
    # Example 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = two_sum(nums1, target1)
    print(f"Input: {nums1}, Target: {target1}")
    print(f"Output: {result1}")
    print(f"Values: [{nums1[result1[0]]}, {nums1[result1[1]]}]")
    print()
    
    # Example 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = two_sum(nums2, target2)
    print(f"Input: {nums2}, Target: {target2}")
    print(f"Output: {result2}")
    print(f"Values: [{nums2[result2[0]]}, {nums2[result2[1]]}]")


# ========================================
# INTERVIEW TALKING POINTS
# ========================================
"""
OPTIMIZATION PROGRESSION:
1. Brute force: O(n²) - check all pairs
2. Hash table: O(n) - single pass with complement lookup

KEY INSIGHTS:
- Hash table trades space for time
- Complement relationship: if a + b = target, then b = target - a
- Single pass is possible because we look for previously seen complements

EDGE CASES TO DISCUSS:
- Empty array or single element
- No solution exists
- Multiple solutions (return any or all?)
- Duplicate numbers
- Integer overflow for very large numbers

FOLLOW-UP QUESTIONS:
1. What if we need to return values instead of indices?
2. What if we need all pairs, not just one?
3. What if the array is sorted? (Two pointers approach)
4. What if we can't use extra space?
5. What about three sum or k sum?

PYTHON-SPECIFIC NOTES:
- Use 'in' operator for O(1) hash lookup
- dict.get() for safe access with default
- enumerate() for clean index/value iteration
- Type hints for professional code
""" 