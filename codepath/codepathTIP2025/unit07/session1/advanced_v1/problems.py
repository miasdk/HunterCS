"""
Unit 7 - Session 1 - Advanced v1
Recursion Problems for Interview Prep

This file contains 6 recursion problems with complete implementations,
complexity analysis, and comprehensive test cases.
"""

# ========================================
# PROBLEM 1: COUNTING THE LAYERS OF A SANDWICH
# ========================================

def count_layers(sandwich):
    """
    Recursively count the layers of a sandwich represented by nested lists.
    
    Time Complexity: O(n) where n is the total number of elements in the sandwich
    Space Complexity: O(d) where d is the maximum depth of nesting (recursion stack)
    
    Variables:
    - n: total number of elements in the sandwich structure
    - d: maximum depth of nesting in the sandwich structure
    
    Rationale:
    - We visit each element exactly once during recursion
    - Space complexity is determined by the recursion stack depth
    """
    if not sandwich:
        return 0
    
    # Base case: if it's a string (actual layer), count it
    if isinstance(sandwich, str):
        return 1
    
    # Recursive case: sum up layers from all nested lists
    total_layers = 0
    for layer in sandwich:
        total_layers += count_layers(layer)
    
    return total_layers


# ========================================
# PROBLEM 2: REVERSING DELI ORDERS
# ========================================

def reverse_orders(orders):
    """
    Recursively reverse the order of deli orders separated by spaces.
    
    Time Complexity: O(n) where n is the length of the orders string
    Space Complexity: O(n) for the recursion stack and string operations
    
    Variables:
    - n: length of the orders string
    
    Rationale:
    - We process each character once during recursion
    - Space is used for recursion stack and string concatenation
    """
    if not orders:
        return ""
    
    # Find the first space
    space_index = orders.find(' ')
    
    # Base case: no space found (single word)
    if space_index == -1:
        return orders
    
    # Recursive case: reverse the rest and append the first word
    first_word = orders[:space_index]
    remaining_orders = orders[space_index + 1:]
    
    reversed_remaining = reverse_orders(remaining_orders)
    
    if reversed_remaining:
        return reversed_remaining + " " + first_word
    else:
        return first_word


# ========================================
# PROBLEM 3: SHARING THE COFFEE
# ========================================

def can_split_coffee(coffee, n):
    """
    Recursively determine if coffee can be split evenly among n staff.
    
    Time Complexity: O(2^n) in worst case due to exponential recursive calls
    Space Complexity: O(n) for the recursion stack
    
    Variables:
    - n: number of staff members
    - m: number of coffee containers
    
    Rationale:
    - Each recursive call can branch into multiple possibilities
    - Space is bounded by the recursion stack depth
    """
    if not coffee:
        return n == 0
    
    if n == 0:
        return not coffee
    
    total_volume = sum(coffee)
    target_per_person = total_volume / n
    
    # If total volume can't be divided evenly, return False
    if total_volume % n != 0:
        return False
    
    return _can_split_helper(coffee, n, target_per_person, 0, [0] * n)


def _can_split_helper(coffee, n, target, coffee_index, current_splits):
    """
    Helper function for recursive coffee splitting.
    
    Args:
        coffee: list of coffee volumes
        n: number of staff
        target: target volume per person
        coffee_index: current coffee container index
        current_splits: current volume assigned to each person
    """
    # Base case: all coffee containers processed
    if coffee_index >= len(coffee):
        return all(split == target for split in current_splits)
    
    current_volume = coffee[coffee_index]
    
    # Try assigning current volume to each person
    for person in range(n):
        if current_splits[person] + current_volume <= target:
            current_splits[person] += current_volume
            
            if _can_split_helper(coffee, n, target, coffee_index + 1, current_splits):
                return True
            
            # Backtrack
            current_splits[person] -= current_volume
    
    return False


# ========================================
# PROBLEM 4: SUPER SANDWICH (RECURSIVE)
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
    Recursively merge two linked list sandwiches in alternating pattern.
    
    Time Complexity: O(min(m, n)) where m and n are lengths of the lists
    Space Complexity: O(min(m, n)) for the recursion stack
    
    Variables:
    - m: length of sandwich_a
    - n: length of sandwich_b
    
    Rationale:
    - We process each node once during recursion
    - Space is bounded by the recursion stack depth
    """
    # Base cases: if either list is empty, return the other
    if not sandwich_a:
        return sandwich_b
    if not sandwich_b:
        return sandwich_a
    
    # Store next pointers
    next_a = sandwich_a.next
    next_b = sandwich_b.next
    
    # Link current nodes
    sandwich_a.next = sandwich_b
    
    # Recursively merge the remaining parts
    sandwich_b.next = merge_orders(next_a, next_b)
    
    return sandwich_a


# ========================================
# PROBLEM 5: SUPER SANDWICH II (ITERATIVE)
# ========================================

def merge_orders_iterative(sandwich_a, sandwich_b):
    """
    Iterative solution to merge two linked list sandwiches.
    
    Time Complexity: O(min(m, n)) where m and n are lengths of the lists
    Space Complexity: O(1) - only uses a constant amount of extra space
    
    Variables:
    - m: length of sandwich_a
    - n: length of sandwich_b
    
    Rationale:
    - We visit each node once during iteration
    - Space is constant as we only use a few variables
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
# PROBLEM 6: TERNARY EXPRESSION (RECURSIVE)
# ========================================

def evaluate_ternary_expression_recursive(expression):
    """
    Recursively evaluate a ternary expression.
    
    Time Complexity: O(n) where n is the length of the expression
    Space Complexity: O(n) for the recursion stack
    
    Variables:
    - n: length of the expression string
    
    Rationale:
    - We process each character once during recursion
    - Space is bounded by the recursion stack depth
    """
    if not expression:
        return ""
    
    # Find the first '?' to identify the condition
    question_mark = expression.find('?')
    if question_mark == -1:
        return expression
    
    # Extract condition (everything before '?')
    condition = expression[:question_mark]
    
    # Find the corresponding ':' for this '?'
    colon_index = _find_matching_colon(expression, question_mark)
    if colon_index == -1:
        return expression
    
    # Extract true and false expressions
    true_expr = expression[question_mark + 1:colon_index]
    false_expr = expression[colon_index + 1:]
    
    # Evaluate based on condition
    if condition == 'T':
        return evaluate_ternary_expression_recursive(true_expr)
    else:  # condition == 'F'
        return evaluate_ternary_expression_recursive(false_expr)


def _find_matching_colon(expression, question_mark):
    """
    Find the colon that matches the question mark at question_mark.
    Handles nested ternary expressions correctly.
    """
    count = 0
    for i in range(question_mark, len(expression)):
        if expression[i] == '?':
            count += 1
        elif expression[i] == ':':
            count -= 1
            if count == 0:
                return i
    return -1


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