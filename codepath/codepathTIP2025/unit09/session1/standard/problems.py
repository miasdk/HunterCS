"""
Unit 9 - Session 1 - Standard
Tree Traversal and Manipulation Problems

This file contains standard tree traversal and manipulation problems for you to implement.
Each problem includes the problem statement, function signature, and test cases.
"""

# ========================================
# PROBLEM 1: Merging Cookie Orders
# ========================================

class TreeNode():
    def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right

def merge_orders(order1, order2):
    """
    Merge two binary trees representing cookie orders.
    
    Args:
        order1: Root of first binary tree representing cookie order
        order2: Root of second binary tree representing cookie order
        
    Returns:
        Root of the merged tree where overlapping nodes are summed
        
    Example:
        merge_orders(order1, order2) → Root of merged tree
    """
    # TODO: Implement your solution here
    if order1 is None:
        return order2
    if order2 is None:
        return order1
    
    # Merge the current nodes
    order1.val += order2.val
    
    # Recursively merge left and right subtrees
    order1.left = merge_orders(order1.left, order2.left)
    order1.right = merge_orders(order1.right, order2.right)
    
    return order1

# ========================================
# PROBLEM 2: Croquembouche
# ========================================

class Puff():
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    """
    Print cream puff flavors in level order (left to right, level by level).
    
    Args:
        design: Root of binary tree representing cream puffs
        
    Returns:
        List of flavors in level order traversal
        
    Example:
        print_design(croquembouche) → ['Vanilla', 'Chocolate', 'Strawberry', 'Vanilla', 'Matcha']
    """
    # TODO: Implement your solution here
    pass

# ========================================
# PROBLEM 3: Maximum Tiers in Cake
# ========================================

def max_tiers(cake):
    """
    Find the maximum number of tiers (height) in the cake.
    
    Args:
        cake: Root of binary tree representing cake sections
        
    Returns:
        Maximum number of tiers (height of the tree)
        
    Example:
        max_tiers(cake) → 3
    """
    # TODO: Implement your solution here
    pass

# ========================================
# PROBLEM 4: Maximum Tiers in Cake II
# ========================================

def max_tiers_alt(cake):
    """
    Find the maximum number of tiers using alternative approach (BFS if DFS was used before, vice versa).
    
    Args:
        cake: Root of binary tree representing cake sections
        
    Returns:
        Maximum number of tiers (height of the tree)
        
    Example:
        max_tiers_alt(cake) → 3
    """
    # TODO: Implement your solution here
    pass

# ========================================
# PROBLEM 5: Can Fulfill Order
# ========================================

def can_fulfill_order(inventory, order_size):
    """
    Check if there's a root-to-leaf path that sums to the order size.
    
    Args:
        inventory: Root of binary tree representing baked goods inventory
        order_size: Integer representing the required order size
        
    Returns:
        True if order can be fulfilled, False otherwise
        
    Example:
        can_fulfill_order(baked_goods, 22) → True
        can_fulfill_order(baked_goods, 2) → False
    """
    # TODO: Implement your solution here
    pass

# ========================================
# PROBLEM 6: Icing Cupcakes in Zigzag Order
# ========================================

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
    """Test cases for problem 1: Merging Cookie Orders"""
    print("Testing problem_1: Merging Cookie Orders...")
    
    # Test case 1: Basic case
    cookies1 = [1, 3, 2, 5]
    cookies2 = [2, 1, 3, None, 4, None, 7]
    order1 = build_tree(cookies1)
    order2 = build_tree(cookies2)
    result = merge_orders(order1, order2)
    expected = [3, 4, 5, 5, 4, None, 7]
    assert print_tree(result) == expected, f"Expected {expected}, got {print_tree(result)}"
    print("✓ Basic case passed")
    
    # Test case 2: One empty tree
    empty_tree = None
    single_tree = TreeNode(5)
    result = merge_orders(empty_tree, single_tree)
    expected = [5]
    assert print_tree(result) == expected, f"Expected {expected}, got {print_tree(result)}"
    print("✓ Empty tree case passed")
    
    print("All tests for problem_1 passed! 🎉")

def test_problem_2():
    """Test cases for problem 2: Croquembouche"""
    print("Testing problem_2: Croquembouche...")
    
    # Test case 1: Basic case
    croquembouche = Puff("Vanilla", 
                        Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                        Puff("Strawberry"))
    result = print_design(croquembouche)
    expected = ['Vanilla', 'Chocolate', 'Strawberry', 'Vanilla', 'Matcha']
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Basic case passed")
    
    # Test case 2: Single puff
    single_puff = Puff("Chocolate")
    result = print_design(single_puff)
    expected = ['Chocolate']
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Single puff case passed")
    
    print("All tests for problem_2 passed! 🎉")

def test_problem_3():
    """Test cases for problem 3: Maximum Tiers in Cake"""
    print("Testing problem_3: Maximum Tiers in Cake...")
    
    # Test case 1: Basic case
    cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
    cake = build_tree(cake_sections)
    result = max_tiers(cake)
    expected = 3
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Basic case passed")
    
    # Test case 2: Single node
    single_cake = TreeNode("Vanilla")
    result = max_tiers(single_cake)
    expected = 1
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Single node case passed")
    
    print("All tests for problem_3 passed! 🎉")

def test_problem_4():
    """Test cases for problem 4: Maximum Tiers in Cake II"""
    print("Testing problem_4: Maximum Tiers in Cake II...")
    
    # Test case 1: Basic case
    cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
    cake = build_tree(cake_sections)
    result = max_tiers_alt(cake)
    expected = 3
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Basic case passed")
    
    # Test case 2: Single node
    single_cake = TreeNode("Vanilla")
    result = max_tiers_alt(single_cake)
    expected = 1
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Single node case passed")
    
    print("All tests for problem_4 passed! 🎉")

def test_problem_5():
    """Test cases for problem 5: Can Fulfill Order"""
    print("Testing problem_5: Can Fulfill Order...")
    
    # Test case 1: Basic case
    quantities = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    baked_goods = build_tree(quantities)
    result1 = can_fulfill_order(baked_goods, 22)
    result2 = can_fulfill_order(baked_goods, 2)
    assert result1 == True, f"Expected True, got {result1}"
    assert result2 == False, f"Expected False, got {result2}"
    print("✓ Basic case passed")
    
    # Test case 2: Single node
    single_good = TreeNode(5)
    result = can_fulfill_order(single_good, 5)
    assert result == True, f"Expected True, got {result}"
    print("✓ Single node case passed")
    
    print("All tests for problem_5 passed! 🎉")

def test_problem_6():
    """Test cases for problem 6: Icing Cupcakes in Zigzag Order"""
    print("Testing problem_6: Icing Cupcakes in Zigzag Order...")
    
    # Test case 1: Basic case
    flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
    cupcakes = build_tree(flavors)
    result = zigzag_icing_order(cupcakes)
    expected = ['Chocolate', 'Lemon', 'Vanilla', 'Strawberry', 'Hazelnut', 'Red Velvet']
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Basic case passed")
    
    # Test case 2: Single cupcake
    single_cupcake = TreeNode("Vanilla")
    result = zigzag_icing_order(single_cupcake)
    expected = ['Vanilla']
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Single cupcake case passed")
    
    print("All tests for problem_6 passed! 🎉")

def run_all_tests():
    """Run all test functions"""
    print("🧪 Running all standard problem tests...\n")
    
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