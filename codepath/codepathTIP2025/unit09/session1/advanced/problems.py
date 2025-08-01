"""
Unit 9 - Session 1 - Advanced
Tree Traversal and Manipulation Problems

This file contains advanced tree traversal and manipulation problems for you to implement.
Each problem includes the problem statement, function signature, and test cases.
"""

# ========================================
# PROBLEM 1: Croquembouche II
# ========================================

class Puff():
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def listify_design(design):
    """
    Traverse the croquembouche in tier order (level by level, left to right).
    
    Args:
        design: Root of binary tree representing cream puffs
        
    Returns:
        List of lists where each inner list represents a tier (level) of the croquembouche
        and contains the flavors of each cream puff on that tier from left to right
        
    Example:
        listify_design(croquembouche) → [['Vanilla'], ['Chocolate', 'Strawberry'], ['Vanilla', 'Matcha']]
    """
    # TODO: Implement your solution here
    pass

# ========================================
# PROBLEM 2: Icing Cupcakes in Zigzag Order
# ========================================

class TreeNode():
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def zigzag_icing_order(cupcakes):
    """
    Ice cupcakes in zigzag order (left to right, then right to left alternating).
    
    Args:
        cupcakes: Root of binary tree representing cupcakes
        
    Returns:
        List of cupcake values in the order they were iced
        
    Example:
        zigzag_icing_order(cupcakes) → ['Chocolate', 'Lemon', 'Vanilla', 'Strawberry', 'Hazelnut', 'Red Velvet']
    """
    # TODO: Implement your solution here
    pass

# ========================================
# PROBLEM 3: Larger Order Tree
# ========================================

def larger_order_tree(orders):
    """
    Convert BST to 'larger order tree' where each node's value equals its original value
    plus the sum of all node values greater than it.
    
    Args:
        orders: Root of binary search tree representing orders
        
    Returns:
        Root of the modified tree
        
    Example:
        larger_order_tree(orders) → Modified tree with updated values
    """
    # TODO: Implement your solution here
    pass

# ========================================
# PROBLEM 4: Find Next Order to Fulfill Today
# ========================================

def next_order_to_fulfill(order_tree, order):
    """
    Find the next order to fulfill on the same level as the given order.
    
    Args:
        order_tree: Root of binary tree representing orders
        order: TreeNode object representing current order being fulfilled
        
    Returns:
        Next order to fulfill on the same level, or None if order is the last of the day
        
    Example:
        next_order_to_fulfill(cupcakes, cake) → eclair
        next_order_to_fulfill(cupcakes, cookies) → None
    """
    # TODO: Implement your solution here
    pass

# ========================================
# PROBLEM 5: Add Row of Cupcakes to Display
# ========================================

def add_row(display, flavor, depth):
    """
    Add a row of cupcakes with given flavor at the specified depth.
    
    Args:
        display: Root of binary tree representing cupcake display
        flavor: String representing the flavor of new cupcakes
        depth: Integer representing the depth where to add the row
        
    Returns:
        Root of the modified tree
        
    Example:
        add_row(display, "Mocha", 3) → Modified tree with new row at depth 3
    """
    # TODO: Implement your solution here
    pass

# ========================================
# PROBLEM 6: Maximum Icing Difference
# ========================================

def max_icing_difference(root):
    """
    Find the maximum icing difference between any ancestor-descendant pair.
    
    Args:
        root: Root of binary tree representing cupcake display
        
    Returns:
        Maximum difference between any ancestor-descendant pair
        
    Example:
        max_icing_difference(display) → 7
    """
    # TODO: Implement your solution here
    pass

# ========================================
# HELPER FUNCTIONS FOR TESTING
# ========================================

def build_tree(values, index=0):
    """Helper function to build a binary tree from a list of values"""
    if index >= len(values) or values[index] is None:
        return None
    
    root = TreeNode(values[index])
    root.left = build_tree(values, 2 * index + 1)
    root.right = build_tree(values, 2 * index + 2)
    return root

def print_tree(root):
    """Helper function to print tree in level order"""
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result

# ========================================
# TEST FUNCTIONS
# ========================================

def test_problem_1():
    """Test cases for problem 1: Croquembouche II"""
    print("Testing problem_1: Croquembouche II...")
    
    # Test case 1: Basic case
    croquembouche = Puff("Vanilla", 
                        Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                        Puff("Strawberry"))
    result = listify_design(croquembouche)
    expected = [['Vanilla'], ['Chocolate', 'Strawberry'], ['Vanilla', 'Matcha']]
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Basic case passed")
    
    # Test case 2: Single node
    single_puff = Puff("Chocolate")
    result = listify_design(single_puff)
    expected = [['Chocolate']]
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Single node case passed")
    
    print("All tests for problem_1 passed! 🎉")

def test_problem_2():
    """Test cases for problem 2: Icing Cupcakes in Zigzag Order"""
    print("Testing problem_2: Icing Cupcakes in Zigzag Order...")
    
    # Test case 1: Basic case
    flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
    cupcakes = build_tree(flavors)
    result = zigzag_icing_order(cupcakes)
    expected = ['Chocolate', 'Lemon', 'Vanilla', 'Strawberry', 'Hazelnut', 'Red Velvet']
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Basic case passed")
    
    # Test case 2: Single node
    single_cupcake = TreeNode("Vanilla")
    result = zigzag_icing_order(single_cupcake)
    expected = ['Vanilla']
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Single node case passed")
    
    print("All tests for problem_2 passed! 🎉")

def test_problem_3():
    """Test cases for problem 3: Larger Order Tree"""
    print("Testing problem_3: Larger Order Tree...")
    
    # Test case 1: Basic case
    order_sizes = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    orders = build_tree(order_sizes)
    result = larger_order_tree(orders)
    # Note: This is a complex test that would need the actual implementation
    print("✓ Test case prepared (implementation needed)")
    
    print("All tests for problem_3 prepared! 🎉")

def test_problem_4():
    """Test cases for problem 4: Find Next Order to Fulfill Today"""
    print("Testing problem_4: Find Next Order to Fulfill Today...")
    
    # Test case 1: Basic case
    cupcakes = TreeNode("Cupcakes")
    macaron = TreeNode("Macaron")
    cookies = TreeNode("Cookies")
    cake = TreeNode("Cake")
    eclair = TreeNode("Eclair")
    croissant = TreeNode("Croissant")
    
    cupcakes.left, cupcakes.right = macaron, cookies
    macaron.right = cake
    cookies.left, cookies.right = eclair, croissant
    
    result1 = next_order_to_fulfill(cupcakes, cake)
    result2 = next_order_to_fulfill(cupcakes, cookies)
    
    # Note: This test requires the actual implementation
    print("✓ Test case prepared (implementation needed)")
    
    print("All tests for problem_4 prepared! 🎉")

def test_problem_5():
    """Test cases for problem 5: Add Row of Cupcakes to Display"""
    print("Testing problem_5: Add Row of Cupcakes to Display...")
    
    # Test case 1: Basic case
    cupcake_flavors = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Red Velvet"]
    display = build_tree(cupcake_flavors)
    result = add_row(display, "Mocha", 3)
    # Note: This test requires the actual implementation
    print("✓ Test case prepared (implementation needed)")
    
    print("All tests for problem_5 prepared! 🎉")

def test_problem_6():
    """Test cases for problem 6: Maximum Icing Difference"""
    print("Testing problem_6: Maximum Icing Difference...")
    
    # Test case 1: Basic case
    sweetness_levels = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
    display = build_tree(sweetness_levels)
    result = max_icing_difference(display)
    expected = 7  # |8 - 1| = 7
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Basic case passed")
    
    # Test case 2: Single node
    single_cupcake = TreeNode(5)
    result = max_icing_difference(single_cupcake)
    expected = 0  # No ancestor-descendant pairs
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Single node case passed")
    
    print("All tests for problem_6 passed! 🎉")

def run_all_tests():
    """Run all test functions"""
    print("🧪 Running all advanced problem tests...\n")
    
    try:
        test_problem_1()
        print()
        test_problem_2()
        print()
        test_problem_3()
        print()
        test_problem_4()
        print()
        test_problem_5()
        print()
        test_problem_6()
        print()
        print("🎉 All problem tests completed! 🎉")
    except Exception as e:
        print(f"❌ Test failed: {e}")

if __name__ == "__main__":
    run_all_tests() 