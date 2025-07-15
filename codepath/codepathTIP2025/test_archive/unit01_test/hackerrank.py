#!/usr/bin/env python3
"""
TIP102 Unit 1 Version A (Standard) - Practice Implementation Skeleton
"""

# ============================================================================
# CODING PROBLEMS
# ============================================================================

# Problem 1: Unique Characters
def has_all_unique_characters(s):
    """Return True if every character in the string is unique."""
    pass


# Problem 2: Needle in Haystack
def find_needle(haystack, needle):
    """Return index of first occurrence of needle in haystack, or -1 if not found."""
    pass


# Problem 3: Can Place Flowers
def can_place_flowers(flowerbed, n):
    """Return True if n flowers can be planted without violating adjacency rules."""
    pass


# Problem 7: Find the Bug - Reverse List
def reverse_lst(lst):
    """Reverse the list in-place and return it."""
    pass


# ============================================================================
# MULTIPLE CHOICE ANALYSIS FUNCTIONS
# ============================================================================

# Problem 4: String Immutability Analysis
def analyze_string_immutability():
    """Analyze what happens when trying to modify a string character."""
    print("=== Problem 4: String Immutability Analysis ===")
    name = "codepath"
    print(f"Original string: {name}")
    
    try:
        name[0] = "C"  # This should raise an error
        print(f"Modified string: {name}")
    except TypeError as e:
        print(f"Error occurred: {e}")
        print("Explanation: Strings are immutable in Python")


# Problem 5: Adjacent Characters Count Analysis
def analyze_adjacent_count():
    """Analyze the mystery function that counts adjacent identical characters."""
    print("\n=== Problem 5: Adjacent Characters Count Analysis ===")
    
    def mystery_function(s):
        count = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
        return count
    
    test_string = "AABBAB"
    result = mystery_function(test_string)
    print(f"mystery_function('{test_string}') = {result}")
    
    # Step-by-step analysis
    print("\nStep-by-step analysis:")
    for i in range(1, len(test_string)):
        comparison = test_string[i] == test_string[i-1]
        print(f"Position {i}: '{test_string[i]}' == '{test_string[i-1]}' -> {comparison}")


# Problem 6: Threshold Sum Analysis
def analyze_threshold_sum():
    """Analyze the mystery function that sums elements within a threshold."""
    print("\n=== Problem 6: Threshold Sum Analysis ===")
    
    def mystery_function(lst, threshold):
        total = 0
        i = 0
        while i < len(lst) and total + lst[i] <= threshold:
            total += lst[i]
            i += 1
        return total
    
    test_list = [1, 2, 3, 4, 5]
    threshold = 7
    result = mystery_function(test_list, threshold)
    print(f"mystery_function({test_list}, {threshold}) = {result}")
    
    # Step-by-step analysis
    print("\nStep-by-step analysis:")
    total = 0
    for i, num in enumerate(test_list):
        if total + num <= threshold:
            total += num
            print(f"Step {i+1}: Add {num}, total = {total} (≤ {threshold}) ✓")
        else:
            print(f"Step {i+1}: Cannot add {num}, would make total = {total + num} (> {threshold}) ✗")
            break


# ============================================================================
# TEST CASES
# ============================================================================

def run_tests():
    """Run all test cases to verify implementations."""
    
    print("=" * 70)
    print("TIP102 UNIT 1 VERSION A PRACTICE TEST SUITE")
    print("=" * 70)
    
    # Test 1: Unique Characters
    print("\n1. Unique Characters")
    result1 = has_all_unique_characters("abcdef")
    result2 = has_all_unique_characters("aabbcc")
    result3 = has_all_unique_characters("")
    print(f"has_all_unique_characters('abcdef') = {result1} (expected: True)")
    print(f"has_all_unique_characters('aabbcc') = {result2} (expected: False)")
    print(f"has_all_unique_characters('') = {result3} (expected: True)")
    
    # Test 2: Needle in Haystack
    print("\n2. Needle in Haystack")
    result1 = find_needle("sadbutsad", "sad")
    result2 = find_needle("leetcode", "leeto")
    result3 = find_needle("mad", "madden")
    print(f"find_needle('sadbutsad', 'sad') = {result1} (expected: 0)")
    print(f"find_needle('leetcode', 'leeto') = {result2} (expected: -1)")
    print(f"find_needle('mad', 'madden') = {result3} (expected: -1)")
    
    # Test 3: Can Place Flowers
    print("\n3. Can Place Flowers")
    result1 = can_place_flowers([1,0,0,0,1], 1)
    result2 = can_place_flowers([1,0,0,0,1], 2)
    result3 = can_place_flowers([0,0,1,0,0], 1)
    result4 = can_place_flowers([1,0,0,0,0,1], 2)
    print(f"can_place_flowers([1,0,0,0,1], 1) = {result1} (expected: True)")
    print(f"can_place_flowers([1,0,0,0,1], 2) = {result2} (expected: False)")
    print(f"can_place_flowers([0,0,1,0,0], 1) = {result3} (expected: True)")
    print(f"can_place_flowers([1,0,0,0,0,1], 2) = {result4} (expected: True)")
    
    # Test 7: Reverse List
    print("\n7. Reverse List")
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40]
    list3 = [42]
    list4 = []
    
    # Create copies for testing since function modifies in-place
    test1 = list1.copy()
    test2 = list2.copy()
    test3 = list3.copy()
    test4 = list4.copy()
    
    result1 = reverse_lst(test1)
    result2 = reverse_lst(test2)
    result3 = reverse_lst(test3)
    result4 = reverse_lst(test4)
    
    print(f"reverse_lst([1, 2, 3, 4, 5]) = {result1} (expected: [5, 4, 3, 2, 1])")
    print(f"reverse_lst([10, 20, 30, 40]) = {result2} (expected: [40, 30, 20, 10])")
    print(f"reverse_lst([42]) = {result3} (expected: [42])")
    print(f"reverse_lst([]) = {result4} (expected: [])")
    
    print("\n" + "=" * 70)
    print("MULTIPLE CHOICE ANALYSIS")
    print("=" * 70)
    
    # Run multiple choice analyses
    analyze_string_immutability()
    analyze_adjacent_count()
    analyze_threshold_sum()
    
    print("\n" + "=" * 70)
    print("TEST SUITE COMPLETE")
    print("=" * 70)
    print("\nImplementation Tips:")
    print("- Problem 1: Use sets or dictionaries to track seen characters")
    print("- Problem 2: Consider using built-in string methods or manual iteration")
    print("- Problem 3: Check left and right neighbors, handle edge cases")
    print("- Problem 7: Use two pointers and temporary variable for swapping")
    print("\nKey Concepts:")
    print("- String immutability and character access")
    print("- Array traversal with boundary conditions")
    print("- Two-pointer technique for in-place operations")
    print("- Set-based duplicate detection")


if __name__ == "__main__":
    run_tests()