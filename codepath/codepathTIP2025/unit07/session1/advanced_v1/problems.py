"""
Unit 7 - Session 1 - Advanced v1
Recursion Problems for Interview Prep

This file contains 6 recursion problems for you to implement.
Each problem includes the problem statement, function signature, and test cases.
"""

# ========================================
# PROBLEM 1: COUNTING THE LAYERS OF A SANDWICH
# ========================================

def count_layers(sandwich):
    """
    Count the total number of layers in a sandwich represented by nested lists.
    
    Each string represents one layer. Count all strings in the nested structure.
    
    Example:
    sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
    count_layers(sandwich1) → 4
    
    sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]
    count_layers(sandwich2) → 5
    """
    # TODO: Implement your solution here
    pass


# ========================================
# PROBLEM 2: REVERSING DELI ORDERS
# ========================================

def reverse_orders(orders):
    """
    Reverse the order of words in a string separated by spaces.
    
    Example:
    reverse_orders("Bagel Sandwich Coffee") → "Coffee Sandwich Bagel"
    """
    # TODO: Implement your solution here
    pass


# ========================================
# PROBLEM 3: SHARING THE COFFEE
# ========================================

def can_split_coffee(coffee, n):
    """
    Check if coffee volumes can be split evenly among n people.
    
    Example:
    can_split_coffee([4, 4, 8], 2) → True   (4+4+8=16, 16/2=8 each)
    can_split_coffee([5, 10, 15], 4) → False (5+10+15=30, 30/4=7.5 not even)
    """
    # TODO: Implement your solution here
    pass


# ========================================
# PROBLEM 4: SUPER SANDWICH
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


def merge_orders(sandwich_a, sandwich_b):
    """
    Merge two linked lists in alternating pattern: a1->b1->a2->b2->...
    
    Example:
    a = Bacon->Lettuce->Tomato
    b = Turkey->Cheese->Mayo
    merge_orders(a, b) → Bacon->Turkey->Lettuce->Cheese->Tomato->Mayo
    """
    # TODO: Implement your solution here
    pass


# ========================================
# PROBLEM 5: SUPER SANDWICH II (ITERATIVE)
# ========================================

def merge_orders_iterative(sandwich_a, sandwich_b):
    """
    Iterative version of merge_orders for comparison.
    
    Compare this with your recursive solution:
    - Which is easier to understand?
    - Which uses less space?
    - Which would you prefer in an interview?
    """
    # If either list is empty, return the other
    if not sandwich_a:
        return sandwich_b
    if not sandwich_b:
        return sandwich_a

    # Start with the first node of sandwich_a
    head = sandwich_a
    
    # Loop through both lists until one is exhausted
    while sandwich_a and sandwich_b:
        # Store the next pointers
        next_a = sandwich_a.next
        next_b = sandwich_b.next
        
        # Merge sandwich_b after sandwich_a
        sandwich_a.next = sandwich_b
        
        # If there's more in sandwich_a, add it after sandwich_b
        if next_a:
            sandwich_b.next = next_a
        
        # Move to the next nodes
        sandwich_a = next_a
        sandwich_b = next_b

    # Return the head of the new merged list
    return head


# ========================================
# PROBLEM 6: TERNARY EXPRESSION
# ========================================

def evaluate_ternary_expression_recursive(expression):
    """
    Evaluate a ternary expression: condition ? true_value : false_value
    
    Rules:
    - 'T' = True, 'F' = False
    - Numbers are single digits 0-9
    - Expressions group right-to-left
    
    Examples:
    "T?2:3" → "2"        (True, so take 2)
    "F?1:T?4:5" → "4"    (False, so take T?4:5, which is True, so take 4)
    "T?T?F:5:3" → "F"    (True, so take T?F:5, which is True, so take F)
    """
    # TODO: Implement your solution here
    pass


def evaluate_ternary_expression_iterative(expression):
    """
    Iterative solution using stack (provided for comparison).
    """
    stack = []
    
    # Traverse the expression from right to left
    for i in range(len(expression) - 1, -1, -1):
        char = expression[i]
        
        if stack and stack[-1] == '?':
            stack.pop()  # Remove the '?'
            true_expr = stack.pop()  # True expression
            stack.pop()  # Remove the ':'
            false_expr = stack.pop()  # False expression
            
            if char == 'T':
                stack.append(true_expr)
            else:
                stack.append(false_expr)
        else:
            stack.append(char)
    
    return stack[0]


# ========================================
# TESTING FUNCTIONS
# ========================================

def test_count_layers():
    """Test Problem 1: Counting Layers"""
    print("=== Testing Count Layers ===")
    
    sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
    sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]
    
    print(f"Sandwich 1: {sandwich1}")
    print(f"Layers: {count_layers(sandwich1)}")  # Expected: 4
    
    print(f"Sandwich 2: {sandwich2}")
    print(f"Layers: {count_layers(sandwich2)}")  # Expected: 5
    
    # Additional test cases
    empty_sandwich = []
    print(f"Empty sandwich: {count_layers(empty_sandwich)}")  # Expected: 0
    
    simple_sandwich = ["bread", "cheese", "bread"]
    print(f"Simple sandwich: {count_layers(simple_sandwich)}")  # Expected: 3


def test_reverse_orders():
    """Test Problem 2: Reversing Orders"""
    print("\n=== Testing Reverse Orders ===")
    
    orders1 = "Bagel Sandwich Coffee"
    print(f"Original: '{orders1}'")
    print(f"Reversed: '{reverse_orders(orders1)}'")  # Expected: "Coffee Sandwich Bagel"
    
    # Additional test cases
    single_order = "Coffee"
    print(f"Single order: '{reverse_orders(single_order)}'")  # Expected: "Coffee"
    
    empty_orders = ""
    print(f"Empty orders: '{reverse_orders(empty_orders)}'")  # Expected: ""


def test_can_split_coffee():
    """Test Problem 3: Coffee Splitting"""
    print("\n=== Testing Coffee Splitting ===")
    
    coffee1 = [4, 4, 8]
    n1 = 2
    print(f"Coffee: {coffee1}, Staff: {n1}")
    print(f"Can split: {can_split_coffee(coffee1, n1)}")  # Expected: True
    
    coffee2 = [5, 10, 15]
    n2 = 4
    print(f"Coffee: {coffee2}, Staff: {n2}")
    print(f"Can split: {can_split_coffee(coffee2, n2)}")  # Expected: False
    
    # Additional test cases
    coffee3 = [2, 2, 2, 2]
    n3 = 2
    print(f"Coffee: {coffee3}, Staff: {n3}")
    print(f"Can split: {can_split_coffee(coffee3, n3)}")  # Expected: True


def test_merge_orders():
    """Test Problem 4: Merge Orders (Recursive)"""
    print("\n=== Testing Merge Orders (Recursive) ===")
    
    # Create test linked lists
    sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
    sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
    sandwich_c = Node('Bread')
    
    print("Merging sandwich_a and sandwich_b:")
    merged1 = merge_orders(sandwich_a, sandwich_b)
    print_linked_list(merged1)  # Expected: Bacon -> Turkey -> Lettuce -> Cheese -> Tomato -> Mayo
    
    # Create fresh lists for second test
    sandwich_a2 = Node('Bacon', Node('Lettuce', Node('Tomato')))
    sandwich_c2 = Node('Bread')
    
    print("Merging sandwich_a and sandwich_c:")
    merged2 = merge_orders(sandwich_a2, sandwich_c2)
    print_linked_list(merged2)  # Expected: Bacon -> Bread -> Lettuce -> Tomato


def test_merge_orders_iterative():
    """Test Problem 5: Merge Orders (Iterative)"""
    print("\n=== Testing Merge Orders (Iterative) ===")
    
    # Create test linked lists
    sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
    sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
    sandwich_c = Node('Bread')
    
    print("Merging sandwich_a and sandwich_b (iterative):")
    merged1 = merge_orders_iterative(sandwich_a, sandwich_b)
    print_linked_list(merged1)
    
    # Create fresh lists for second test
    sandwich_a2 = Node('Bacon', Node('Lettuce', Node('Tomato')))
    sandwich_c2 = Node('Bread')
    
    print("Merging sandwich_a and sandwich_c (iterative):")
    merged2 = merge_orders_iterative(sandwich_a2, sandwich_c2)
    print_linked_list(merged2)


def test_ternary_expressions():
    """Test Problem 6: Ternary Expressions"""
    print("\n=== Testing Ternary Expressions ===")
    
    expr1 = "T?2:3"
    print(f"Expression: {expr1}")
    result1 = evaluate_ternary_expression_recursive(expr1)
    print(f"Result: {result1}")  # Expected: "2"
    
    expr2 = "F?1:T?4:5"
    print(f"Expression: {expr2}")
    result2 = evaluate_ternary_expression_recursive(expr2)
    print(f"Result: {result2}")  # Expected: "4"
    
    expr3 = "T?T?F:5:3"
    print(f"Expression: {expr3}")
    result3 = evaluate_ternary_expression_recursive(expr3)
    print(f"Result: {result3}")  # Expected: "F"
    
    # Compare with iterative solution
    print("\nComparing recursive vs iterative:")
    print(f"Recursive: {evaluate_ternary_expression_recursive(expr1)}")
    print(f"Iterative: {evaluate_ternary_expression_iterative(expr1)}")


def run_all_tests():
    """Run all test functions."""
    test_count_layers()
    test_reverse_orders()
    test_can_split_coffee()
    test_merge_orders()
    test_merge_orders_iterative()
    test_ternary_expressions()


if __name__ == "__main__":
    run_all_tests() 