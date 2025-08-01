"""
Unit [X] - Session [Y] - [Standard/Advanced]
[Topic]-Themed Problems

This file contains [standard/advanced] [topic] problems for you to implement.
Each problem includes the problem statement, function signature, and test cases.
"""

# ========================================
# PROBLEM 1: [PROBLEM NAME]
# ========================================

def problem_1(input_data):
    """
    [Problem description]
    
    Args:
        input_data: [Description of input]
        
    Returns:
        [Description of output]
        
    Example:
        problem_1([example_input]) → [expected_output]
    """
    # TODO: Implement your solution here
    pass

# ========================================
# PROBLEM 2: [PROBLEM NAME]
# ========================================

def problem_2(input_data):
    """
    [Problem description]
    
    Args:
        input_data: [Description of input]
        
    Returns:
        [Description of output]
        
    Example:
        problem_2([example_input]) → [expected_output]
    """
    # TODO: Implement your solution here
    pass

# ========================================
# PROBLEM 3: [PROBLEM NAME]
# ========================================

def problem_3(input_data):
    """
    [Problem description]
    
    Args:
        input_data: [Description of input]
        
    Returns:
        [Description of output]
        
    Example:
        problem_3([example_input]) → [expected_output]
    """
    # TODO: Implement your solution here
    pass

# ========================================
# TEST FUNCTIONS
# ========================================

def test_problem_1():
    """Test cases for problem 1"""
    print("Testing problem_1...")
    
    # Test case 1: Basic case
    result = problem_1([test_input])
    expected = [expected_output]
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Basic case passed")
    
    # Test case 2: Edge case
    result = problem_1([edge_case_input])
    expected = [expected_output]
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Edge case passed")
    
    print("All tests for problem_1 passed! 🎉")

def test_problem_2():
    """Test cases for problem 2"""
    print("Testing problem_2...")
    
    # Test case 1: Basic case
    result = problem_2([test_input])
    expected = [expected_output]
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Basic case passed")
    
    # Test case 2: Edge case
    result = problem_2([edge_case_input])
    expected = [expected_output]
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Edge case passed")
    
    print("All tests for problem_2 passed! 🎉")

def test_problem_3():
    """Test cases for problem 3"""
    print("Testing problem_3...")
    
    # Test case 1: Basic case
    result = problem_3([test_input])
    expected = [expected_output]
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Basic case passed")
    
    # Test case 2: Edge case
    result = problem_3([edge_case_input])
    expected = [expected_output]
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Edge case passed")
    
    print("All tests for problem_3 passed! 🎉")

def run_all_tests():
    """Run all test functions"""
    print("🧪 Running all problem tests...\n")
    
    try:
        test_problem_1()
        print()
        test_problem_2()
        print()
        test_problem_3()
        print()
        print("🎉 All problem tests passed! 🎉")
    except Exception as e:
        print(f"❌ Test failed: {e}")

if __name__ == "__main__":
    run_all_tests() 