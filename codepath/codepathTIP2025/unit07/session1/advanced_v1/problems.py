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
    Problem 1: Counting the Layers of a Sandwich
    
    You're working at a deli, and need to count the layers of a sandwich to make sure 
    you made the order correctly. Each layer is represented by a nested list. Given a 
    list of lists sandwich where each list [] represents a sandwich layer, write a 
    recursive function count_layers() that returns the total number of sandwich layers.
    
    Evaluate the time and space complexity of your solution. Define your variables and 
    provide a rationale for why you believe your solution has the stated time and space complexity.
    
    Example Usage:
    sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
    sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]
    
    print(count_layers(sandwich1))  # Expected: 4
    print(count_layers(sandwich2))  # Expected: 5
    """
    # TODO: Implement your solution here
    pass


# ========================================
# PROBLEM 2: REVERSING DELI ORDERS
# ========================================

def reverse_orders(orders):
    """
    Problem 2: Reversing Deli Orders
    
    The deli counter is busy, and orders have piled up. To serve the last customer first, 
    you need to reverse the order of the deli orders. Given a string orders where each 
    individual order is separated by a single space, write a recursive function 
    reverse_orders() that returns a new string with the orders reversed.
    
    Evaluate the time and space complexity of your solution. Define your variables and 
    provide a rationale for why you believe your solution has the stated time and space complexity.
    
    Example Usage:
    print(reverse_orders("Bagel Sandwich Coffee"))
    # Expected Output: "Coffee Sandwich Bagel"
    """
    # TODO: Implement your solution here
    pass


# ========================================
# PROBLEM 3: SHARING THE COFFEE
# ========================================

def can_split_coffee(coffee, n):
    """
    Problem 3: Sharing the Coffee
    
    The deli staff is in desperate need of caffeine to keep them going through their shift 
    and has decided to divide the coffee supply equally among themselves. Each batch of 
    coffee is stored in containers of different sizes. Write a recursive function 
    can_split_coffee() that accepts a list of integers coffee representing the volume of 
    each batch of coffee and returns True if the coffee can be split evenly by volume 
    among n staff and False otherwise.
    
    Evaluate the time and space complexity of your solution. Define your variables and 
    provide a rationale for why you believe your solution has the stated time and space complexity.
    
    Example Usage:
    print(can_split_coffee([4, 4, 8], 2))    # Expected: True
    print(can_split_coffee([5, 10, 15], 4))  # Expected: False
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
    Problem 4: Super Sandwich
    
    A regular at the deli has requested a new order made by merging two different 
    sandwiches on the menu together. Given the heads of two linked lists sandwich_a 
    and sandwich_b where each node in the lists contains a spell segment, write a 
    recursive function merge_orders() that merges the two sandwiches together in the pattern:
    
    a1 -> b1 -> a2 -> b2 -> a3 -> b3 -> ...
    
    Return the head of the merged sandwich.
    
    Evaluate the time and space complexity of your solution. Define your variables and 
    provide a rationale for why you believe your solution has the stated time and space complexity.
    
    Example Usage:
    sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
    sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
    sandwich_c = Node('Bread')
    
    print_linked_list(merge_orders(sandwich_a, sandwich_b))
    # Expected: Bacon -> Turkey -> Lettuce -> Cheese -> Tomato -> Mayo
    
    print_linked_list(merge_orders(sandwich_a, sandwich_c))
    # Expected: Bacon -> Bread -> Lettuce -> Tomato
    """
    # TODO: Implement your solution here
    pass


# ========================================
# PROBLEM 5: SUPER SANDWICH II (ITERATIVE)
# ========================================

def merge_orders_iterative(sandwich_a, sandwich_b):
    """
    Problem 5: Super Sandwich II (Iterative)
    
    Below is an iterative solution to the merge_orders() function from the previous problem. 
    Compare your recursive solution to the iterative solution below.
    
    Discuss with your podmates. Which solution do you prefer? How do they compare on 
    time complexity? Space complexity?
    
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
# PROBLEM 6: TERNARY EXPRESSION
# ========================================

def evaluate_ternary_expression_recursive(expression):
    """
    Problem 6: Ternary Expression
    
    Given a string expression representing arbitrarily nested ternary expressions, 
    evaluate the expression, and return its result as a string.
    
    You can always assume that the given expression is valid and only contains digits, 
    '?', ':', 'T', and 'F' where 'T' is True and 'F' is False. All the numbers in 
    the expression are one-digit numbers (i.e., in the range [0, 9]).
    
    Ternary expressions use the following syntax:
    condition ? true_choice : false_choice
    
    - condition is evaluate first and determines which choice to make
    - true_choice is taken if condition evaluates to True
    - false_choice is taken if condition evaluates to False
    - The conditional expressions group right-to-left, and the result of the expression 
      will always evaluate to either a digit, 'T' or 'F'.
    
    We have provided an iterative solution that uses an explicit stack. Implement a 
    recursive solution evaluate_ternary_expression_recursive().
    
    Evaluate the time and space complexity of your solution. Define your variables and 
    provide a rationale for why you believe your solution has the stated time and space complexity.
    
    Example Usage:
    print(evaluate_ternary_expression_recursive("T?2:3"))        # Expected: "2"
    print(evaluate_ternary_expression_recursive("F?1:T?4:5"))   # Expected: "4"
    print(evaluate_ternary_expression_recursive("T?T?F:5:3"))   # Expected: "F"
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