"""
Unit 7 - Session 1 - Standard v1
Marvel-Themed Recursion Problems

This file contains 9 recursion problems for you to implement.
Each problem includes the problem statement, function signature, and test cases.
"""

# ========================================
# PROBLEM 1: COUNTING IRON MAN'S SUITS
# ========================================

def count_suits_iterative(suits):
    """
    Count the total number of suits in Stark's collection iteratively.
    Do not use the len() function.
    
    Example:
    count_suits_iterative(["Mark I", "Mark II", "Mark III"]) → 3
    """
    # TODO: Implement your solution here
    pass


def count_suits_recursive(suits):
    """
    Count the total number of suits in Stark's collection recursively.
    
    Example:
    count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]) → 4
    """
    # TODO: Implement your solution here
    pass


# ========================================
# PROBLEM 2: COLLECTING INFINITY STONES
# ========================================

def sum_stones(stones):
    """
    Calculate the total power of all Infinity Stones using recursion.
    
    Example:
    sum_stones([5, 10, 15, 20, 25, 30]) → 105
    sum_stones([12, 8, 22, 16, 10]) → 68
    """
    # TODO: Implement your solution here
    pass


# ========================================
# PROBLEM 3: COUNTING UNIQUE SUITS
# ========================================

def count_unique_suits_iterative(suits):
    """
    Count the number of unique suits in Stark's collection iteratively.
    
    Example:
    count_unique_suits_iterative(["Mark I", "Mark II", "Mark III"]) → 3
    """
    # TODO: Implement your solution here
    pass


def count_unique_suits_recursive(suits):
    """
    Count the number of unique suits in Stark's collection recursively.
    
    Example:
    count_unique_suits_recursive(["Mark I", "Mark I", "Mark III"]) → 2
    """
    # TODO: Implement your solution here
    pass


# ========================================
# PROBLEM 4: CALCULATING GROOT'S GROWTH
# ========================================

def fibonacci_growth(n):
    """
    Calculate Groot's height using Fibonacci sequence recursively.
    
    F(0) = 0, F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1
    
    Example:
    fibonacci_growth(5) → 5
    fibonacci_growth(8) → 21
    """
    # TODO: Implement your solution here
    pass


# ========================================
# PROBLEM 5: POWER OF THE FANTASTIC FOUR
# ========================================

def power_of_four(n):
    """
    Calculate 4 raised to the nth power recursively.
    Handle negative exponents (4^(-n) = 1/4^n).
    
    Example:
    power_of_four(2) → 16    (4^2 = 16)
    power_of_four(-2) → 0.0625  (4^(-2) = 1/16 = 0.0625)
    """
    # TODO: Implement your solution here
    pass


# ========================================
# PROBLEM 6: STRONGEST AVENGER
# ========================================

def strongest_avenger(strengths):
    """
    Find the maximum strength among the Avengers recursively.
    Do not use the max() function.
    
    Example:
    strongest_avenger([88, 92, 95, 99, 97, 100, 94]) → 100
    strongest_avenger([50, 75, 85, 60, 90]) → 90
    """
    # TODO: Implement your solution here
    pass


# ========================================
# PROBLEM 7: COUNTING VIBRANIUM DEPOSITS
# ========================================

def count_deposits(resources):
    """
    Count the number of 'V' characters (vibranium deposits) in a string recursively.
    
    Example:
    count_deposits("VVVVV") → 5
    count_deposits("VXVYGA") → 2
    """
    # TODO: Implement your solution here
    pass


# ========================================
# PROBLEM 8: MERGING MISSIONS
# ========================================

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_linked_list(head):
    """Helper function to print linked list for testing."""
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


def merge_missions(mission1, mission2):
    """
    Merge two sorted linked lists of missions recursively.
    
    Example:
    mission1 = Node(1, Node(2, Node(4)))
    mission2 = Node(1, Node(3, Node(4)))
    merge_missions(mission1, mission2) → 1 -> 1 -> 2 -> 3 -> 4 -> 4
    """
    # TODO: Implement your solution here
    pass


# ========================================
# PROBLEM 9: MERGING MISSIONS II (ITERATIVE)
# ========================================

def merge_missions_iterative(mission1, mission2):
    """
    Iterative version of merge_missions for comparison.
    
    Compare this with your recursive solution:
    - Which is easier to understand?
    - Which uses less space?
    - Which would you prefer in an interview?
    """
    temp = Node(0)  # Temporary node to simplify the merging process
    tail = temp

    while mission1 and mission2:
        if mission1.value < mission2.value:
            tail.next = mission1
            mission1 = mission1.next
        else:
            tail.next = mission2
            mission2 = mission2.next
        tail = tail.next

    # Attach the remaining nodes, if any
    if mission1:
        tail.next = mission1
    elif mission2:
        tail.next = mission2

    return temp.next  # Return the head of the merged linked list


# ========================================
# TESTING FUNCTIONS
# ========================================

def test_count_suits():
    """Test Problem 1: Counting Iron Man's Suits"""
    print("=== Testing Count Suits ===")
    
    suits1 = ["Mark I", "Mark II", "Mark III"]
    suits2 = ["Mark I", "Mark I", "Mark III", "Mark IV"]
    
    print(f"Suits: {suits1}")
    print(f"Iterative count: {count_suits_iterative(suits1)}")  # Expected: 3
    print(f"Recursive count: {count_suits_recursive(suits1)}")  # Expected: 3
    
    print(f"Suits: {suits2}")
    print(f"Iterative count: {count_suits_iterative(suits2)}")  # Expected: 4
    print(f"Recursive count: {count_suits_recursive(suits2)}")  # Expected: 4


def test_sum_stones():
    """Test Problem 2: Collecting Infinity Stones"""
    print("\n=== Testing Sum Stones ===")
    
    stones1 = [5, 10, 15, 20, 25, 30]
    stones2 = [12, 8, 22, 16, 10]
    
    print(f"Stones: {stones1}")
    print(f"Total power: {sum_stones(stones1)}")  # Expected: 105
    
    print(f"Stones: {stones2}")
    print(f"Total power: {sum_stones(stones2)}")  # Expected: 68


def test_count_unique_suits():
    """Test Problem 3: Counting Unique Suits"""
    print("\n=== Testing Count Unique Suits ===")
    
    suits1 = ["Mark I", "Mark II", "Mark III"]
    suits2 = ["Mark I", "Mark I", "Mark III"]
    
    print(f"Suits: {suits1}")
    print(f"Iterative unique count: {count_unique_suits_iterative(suits1)}")  # Expected: 3
    print(f"Recursive unique count: {count_unique_suits_recursive(suits1)}")  # Expected: 3
    
    print(f"Suits: {suits2}")
    print(f"Iterative unique count: {count_unique_suits_iterative(suits2)}")  # Expected: 2
    print(f"Recursive unique count: {count_unique_suits_recursive(suits2)}")  # Expected: 2


def test_fibonacci_growth():
    """Test Problem 4: Calculating Groot's Growth"""
    print("\n=== Testing Fibonacci Growth ===")
    
    print(f"Groot's height after 5 months: {fibonacci_growth(5)}")  # Expected: 5
    print(f"Groot's height after 8 months: {fibonacci_growth(8)}")  # Expected: 21
    print(f"Groot's height after 10 months: {fibonacci_growth(10)}")  # Expected: 55


def test_power_of_four():
    """Test Problem 5: Power of the Fantastic Four"""
    print("\n=== Testing Power of Four ===")
    
    print(f"4^2 = {power_of_four(2)}")  # Expected: 16
    print(f"4^(-2) = {power_of_four(-2)}")  # Expected: 0.0625
    print(f"4^0 = {power_of_four(0)}")  # Expected: 1
    print(f"4^3 = {power_of_four(3)}")  # Expected: 64


def test_strongest_avenger():
    """Test Problem 6: Strongest Avenger"""
    print("\n=== Testing Strongest Avenger ===")
    
    strengths1 = [88, 92, 95, 99, 97, 100, 94]
    strengths2 = [50, 75, 85, 60, 90]
    
    print(f"Strengths: {strengths1}")
    print(f"Strongest: {strongest_avenger(strengths1)}")  # Expected: 100
    
    print(f"Strengths: {strengths2}")
    print(f"Strongest: {strongest_avenger(strengths2)}")  # Expected: 90


def test_count_deposits():
    """Test Problem 7: Counting Vibranium Deposits"""
    print("\n=== Testing Count Deposits ===")
    
    resources1 = "VVVVV"
    resources2 = "VXVYGA"
    resources3 = "GOLD"
    
    print(f"Resources: '{resources1}'")
    print(f"Vibranium deposits: {count_deposits(resources1)}")  # Expected: 5
    
    print(f"Resources: '{resources2}'")
    print(f"Vibranium deposits: {count_deposits(resources2)}")  # Expected: 2
    
    print(f"Resources: '{resources3}'")
    print(f"Vibranium deposits: {count_deposits(resources3)}")  # Expected: 0


def test_merge_missions():
    """Test Problem 8: Merging Missions (Recursive)"""
    print("\n=== Testing Merge Missions (Recursive) ===")
    
    # Create test linked lists
    mission1 = Node(1, Node(2, Node(4)))
    mission2 = Node(1, Node(3, Node(4)))
    
    print("Merging missions:")
    print("Mission1: 1 -> 2 -> 4")
    print("Mission2: 1 -> 3 -> 4")
    merged = merge_missions(mission1, mission2)
    print("Result: ", end="")
    print_linked_list(merged)  # Expected: 1 -> 1 -> 2 -> 3 -> 4 -> 4
    
    # Test with different lengths
    mission3 = Node(1, Node(3))
    mission4 = Node(2, Node(4, Node(5)))
    
    print("\nMerging missions:")
    print("Mission3: 1 -> 3")
    print("Mission4: 2 -> 4 -> 5")
    merged2 = merge_missions(mission3, mission4)
    print("Result: ", end="")
    print_linked_list(merged2)  # Expected: 1 -> 2 -> 3 -> 4 -> 5


def test_merge_missions_iterative():
    """Test Problem 9: Merging Missions (Iterative)"""
    print("\n=== Testing Merge Missions (Iterative) ===")
    
    # Create test linked lists
    mission1 = Node(1, Node(2, Node(4)))
    mission2 = Node(1, Node(3, Node(4)))
    
    print("Merging missions (iterative):")
    print("Mission1: 1 -> 2 -> 4")
    print("Mission2: 1 -> 3 -> 4")
    merged = merge_missions_iterative(mission1, mission2)
    print("Result: ", end="")
    print_linked_list(merged)  # Expected: 1 -> 1 -> 2 -> 3 -> 4 -> 4


def run_all_tests():
    """Run all test functions."""
    test_count_suits()
    test_sum_stones()
    test_count_unique_suits()
    test_fibonacci_growth()
    test_power_of_four()
    test_strongest_avenger()
    test_count_deposits()
    test_merge_missions()
    test_merge_missions_iterative()


if __name__ == "__main__":
    run_all_tests() 