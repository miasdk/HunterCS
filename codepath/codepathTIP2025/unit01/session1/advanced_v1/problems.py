#!/usr/bin/env python3
"""
Unit 01 Session 1 - Advanced Version 1

Overview:
This problem set focuses on advanced Python concepts and problem-solving skills for Unit 01, Session 1 (Advanced, Version 1).

Learning Objectives:
- Apply advanced Python syntax and data structures
- Tackle more challenging algorithmic problems
- Develop deeper problem-solving strategies

Problems:
1. Problem 1: [Short description]
2. Problem 2: [Short description]
...
"""

# ============================================================================
# BASIC PROBLEMS
# ============================================================================

def linear_search(lst, target):
    """Find the first occurrence of target in lst. Return -1 if not found."""
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1


def final_value_after_operations(operations):
    """Process operations starting from 1. bouncy/flouncy=+1, trouncy/pouncy=-1."""
    dict = {"bouncy": 1, "flouncy": 1, "trouncy": -1, "pouncy": -1}
    value = 1
    for operation in operations:
        value += dict[operation]   
    return value 


def tiggerfy(word):
    """Remove substrings 't', 'i', 'gg', 'er' from word (case insensitive)."""
    word = word.lower()
    #Removing all occurences of each substring
    word = word.replace("t", "")
    word = word.replace("i", "")
    word = word.replace("gg", "")
    word = word.replace("er", "")
    return word

def non_decreasing(nums):
    """Check if array capppp become non-decreasing with at most one modification."""
    pass


def find_missing_clues(clues, lower, upper):
    """Find missing numbers in range and return as sorted list of ranges."""
    pass


def harvest(vegetable_patch):
    """Count occurrences of 'c' in 2D matrix."""
    pass


def good_pairs(pile1, pile2, k):
    """Count pairs where pile1[i] is divisible by pile2[j] * k."""
    pass


def local_maximums(grid):
    """Find maximum value in every contiguous 3x3 submatrix."""
    pass


# ============================================================================
# ADVANCED PROBLEMS
# ============================================================================

def words_with_char(words, x):
    """Return indices of words that contain character x."""
    pass


def hulk_smash(n):
    """Generate 1-indexed array based on divisibility rules."""
    pass


def shuffle(message, indices):
    """Rearrange string characters based on index mapping."""
    pass


def minimum_boxes(meals, capacity):
    """Find minimum boxes needed to pack all meals."""
    pass


def wealthiest_customer(accounts):
    """Find customer with maximum wealth. Return [index, total_wealth]."""
    pass


def smaller_than_current(nums):
    """For each element, count how many other elements are smaller."""
    pass


def diagonal_sum(grid):
    """Sum primary and secondary diagonals (avoid double-counting center)."""
    pass


def defuse(code, k):
    """Decrypt circular array based on key value k."""
    pass


# ============================================================================
# TEST CASES
# ============================================================================

def run_tests():
    """Run all test cases to verify implementations."""
    
    print("=" * 60)
    print("BASIC PROBLEMS TEST SUITE")
    print("=" * 60)
    
    # Test 1: Linear Search
    print("\n1. Linear Search")
    items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
    result1 = linear_search(items, 'hunny')
    result2 = linear_search(items, 'red balloon')
    print(f"linear_search({items}, 'hunny') = {result1} (expected: 3)")
    print(f"linear_search({items}, 'red balloon') = {result2} (expected: -1)")
    
    # Test 2: Variable Operations
    print("\n2. Variable Operations")
    operations1 = ["trouncy", "flouncy", "flouncy"]
    operations2 = ["bouncy", "bouncy", "flouncy"]
    result1 = final_value_after_operations(operations1)
    result2 = final_value_after_operations(operations2)
    print(f"final_value_after_operations({operations1}) = {result1} (expected: 2)")
    print(f"final_value_after_operations({operations2}) = {result2} (expected: 4)")
    
    # Test 3: String Filtering
    print("\n3. String Filtering")
    result1 = tiggerfy("Trigger")
    result2 = tiggerfy("eggplant")
    result3 = tiggerfy("Choir")
    print(f"tiggerfy('Trigger') = '{result1}' (expected: 'r')")
    print(f"tiggerfy('eggplant') = '{result2}' (expected: 'eplan')")
    print(f"tiggerfy('Choir') = '{result3}' (expected: 'Chor')")
    
    # Test 4: Non-decreasing Array
    print("\n4. Non-decreasing Array")
    result1 = non_decreasing([4, 2, 3])
    result2 = non_decreasing([4, 2, 1])
    print(f"non_decreasing([4, 2, 3]) = {result1} (expected: True)")
    print(f"non_decreasing([4, 2, 1]) = {result2} (expected: False)")
    
    # Test 5: Missing Range Detection
    print("\n5. Missing Range Detection")
    clues = [0, 1, 3, 50, 75]
    result = find_missing_clues(clues, 0, 99)
    print(f"find_missing_clues({clues}, 0, 99) = {result}")
    print("Expected: [[2, 2], [4, 49], [51, 74], [76, 99]]")
    
    # Test 6: 2D Matrix Counting
    print("\n6. 2D Matrix Counting")
    vegetable_patch = [
        ['x', 'c', 'x'],
        ['x', 'x', 'x'],
        ['x', 'c', 'c'],
        ['c', 'c', 'c']
    ]
    result = harvest(vegetable_patch)
    print(f"harvest(vegetable_patch) = {result} (expected: 6)")
    
    # Test 7: Divisible Pairs
    print("\n7. Divisible Pairs")
    pile1 = [1, 3, 4]
    pile2 = [1, 3, 4]
    k = 1
    result1 = good_pairs(pile1, pile2, k)
    
    pile1_2 = [1, 2, 4, 12]
    pile2_2 = [2, 4]
    k_2 = 3
    result2 = good_pairs(pile1_2, pile2_2, k_2)
    
    print(f"good_pairs([1, 3, 4], [1, 3, 4], 1) = {result1} (expected: 5)")
    print(f"good_pairs([1, 2, 4, 12], [2, 4], 3) = {result2} (expected: 2)")
    
    # Test 8: Local Matrix Maximums
    print("\n8. Local Matrix Maximums")
    grid = [
        [9, 9, 8, 1],
        [5, 6, 2, 6],
        [8, 2, 6, 4],
        [6, 2, 2, 2]
    ]
    result = local_maximums(grid)
    print(f"local_maximums(4x4 grid) = {result} (expected: [[9, 9], [8, 6]])")
    
    print("\n" + "=" * 60)
    print("ADVANCED PROBLEMS TEST SUITE")
    print("=" * 60)
    
    # Test 9: Character Search in Words
    print("\n9. Character Search in Words")
    words = ["batman", "superman"]
    result1 = words_with_char(words, "a")
    words2 = ["black panther", "hulk", "black widow", "thor"]
    result2 = words_with_char(words2, "a")
    words3 = ["star-lord", "gamora", "groot", "rocket"]
    result3 = words_with_char(words3, "z")
    print(f"words_with_char(['batman', 'superman'], 'a') = {result1} (expected: [0, 1])")
    print(f"words_with_char(heroes, 'a') = {result2} (expected: [0, 2])")
    print(f"words_with_char(guardians, 'z') = {result3} (expected: [])")
    
    # Test 10: FizzBuzz Variant
    print("\n10. FizzBuzz Variant")
    result1 = hulk_smash(3)
    result2 = hulk_smash(5)
    result3 = hulk_smash(15)
    print(f"hulk_smash(3) = {result1}")
    print("Expected: ['1', '2', 'Hulk']")
    print(f"hulk_smash(5) = {result2}")
    print("Expected: ['1', '2', 'Hulk', '4', 'Smash']")
    print(f"hulk_smash(15) length = {len(result3) if result3 else 0} (expected: 15)")
    
    # Test 11: String Shuffling
    print("\n11. String Shuffling")
    message = "evil"
    indices = [3, 1, 2, 0]
    result1 = shuffle(message, indices)
    message2 = "findme"
    indices2 = [0, 1, 2, 3, 4, 5]
    result2 = shuffle(message2, indices2)
    print(f"shuffle('evil', [3, 1, 2, 0]) = '{result1}' (expected: 'lvie')")
    print(f"shuffle('findme', [0, 1, 2, 3, 4, 5]) = '{result2}' (expected: 'findme')")
    
    # Test 12: Greedy Box Packing
    print("\n12. Greedy Box Packing")
    meals = [1, 3, 2]
    capacity = [4, 3, 1, 5, 2]
    result1 = minimum_boxes(meals, capacity)
    meals2 = [5, 5, 5]
    capacity2 = [2, 4, 2, 7]
    result2 = minimum_boxes(meals2, capacity2)
    print(f"minimum_boxes([1, 3, 2], [4, 3, 1, 5, 2]) = {result1} (expected: 2)")
    print(f"minimum_boxes([5, 5, 5], [2, 4, 2, 7]) = {result2} (expected: 4)")
    
    # Test 13: Maximum Row Sum
    print("\n13. Maximum Row Sum")
    accounts = [
        [1, 2, 3],
        [3, 2, 1]
    ]
    result1 = wealthiest_customer(accounts)
    accounts2 = [
        [1, 5],
        [7, 3],
        [3, 5]
    ]
    result2 = wealthiest_customer(accounts2)
    accounts3 = [
        [2, 8, 7],
        [7, 1, 3],
        [1, 9, 5]
    ]
    result3 = wealthiest_customer(accounts3)
    print(f"wealthiest_customer(accounts1) = {result1} (expected: [0, 6])")
    print(f"wealthiest_customer(accounts2) = {result2} (expected: [1, 10])")
    print(f"wealthiest_customer(accounts3) = {result3} (expected: [0, 17])")
    
    # Test 14: Element Comparison Count
    print("\n14. Element Comparison Count")
    nums = [8, 1, 2, 2, 3]
    result1 = smaller_than_current(nums)
    nums2 = [6, 5, 4, 8]
    result2 = smaller_than_current(nums2)
    nums3 = [7, 7, 7, 7]
    result3 = smaller_than_current(nums3)
    print(f"smaller_than_current([8, 1, 2, 2, 3]) = {result1} (expected: [4, 0, 1, 1, 3])")
    print(f"smaller_than_current([6, 5, 4, 8]) = {result2} (expected: [2, 1, 0, 3])")
    print(f"smaller_than_current([7, 7, 7, 7]) = {result3} (expected: [0, 0, 0, 0])")
    
    # Test 15: Matrix Diagonal Sum
    print("\n15. Matrix Diagonal Sum")
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result1 = diagonal_sum(grid)
    grid2 = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    result2 = diagonal_sum(grid2)
    grid3 = [[5]]
    result3 = diagonal_sum(grid3)
    print(f"diagonal_sum(3x3 grid) = {result1} (expected: 25)")
    print(f"diagonal_sum(4x4 ones) = {result2} (expected: 8)")
    print(f"diagonal_sum([[5]]) = {result3} (expected: 5)")
    
    # Test 16: Circular Array Decryption
    print("\n16. Circular Array Decryption")
    code = [5, 7, 1, 4]
    k = 3
    result1 = defuse(code, k)
    code2 = [1, 2, 3, 4]
    k2 = 0
    result2 = defuse(code2, k2)
    code3 = [2, 4, 9, 3]
    k3 = -2
    result3 = defuse(code3, k3)
    print(f"defuse([5, 7, 1, 4], 3) = {result1} (expected: [12, 10, 16, 13])")
    print(f"defuse([1, 2, 3, 4], 0) = {result2} (expected: [0, 0, 0, 0])")
    print(f"defuse([2, 4, 9, 3], -2) = {result3} (expected: [12, 5, 6, 13])")
    
    print("\n" + "=" * 60)
    print("TEST SUITE COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()