# Recursion: Complete Guide to Recursive Programming

## 📋 Table of Contents
- [Overview](#overview)
- [Basic Concepts](#basic-concepts)
- [Recursion vs Iteration](#recursion-vs-iteration)
- [Types of Recursion](#types-of-recursion)
- [Common Recursive Patterns](#common-recursive-patterns)
- [Recursive Data Structures](#recursive-data-structures)
- [Optimization Techniques](#optimization-techniques)
- [Common Mistakes](#common-mistakes)
- [Practice Problems](#practice-problems)
- [Quick Reference](#quick-reference)

---

## Overview

**Recursion** is a programming technique where a function calls itself to solve a problem by breaking it down into smaller, similar subproblems.

### **Key Characteristics**
- **Self-Reference**: Function calls itself
- **Base Case**: Stopping condition to prevent infinite recursion
- **Recursive Case**: Problem broken down into smaller instances
- **Stack Usage**: Each recursive call uses stack memory

---

## Basic Concepts

### **Recursive Function Structure**
Every recursive function has two essential parts:

```cpp
ReturnType recursiveFunction(Parameters) {
    // 1. Base Case(s) - stopping condition
    if (baseCondition) {
        return baseValue;
    }
    
    // 2. Recursive Case - break down problem
    return recursiveFunction(smallerProblem);
}
```

### **Example: Factorial**
```cpp
int factorial(int n) {
    // Base case
    if (n <= 1) {
        return 1;
    }
    
    // Recursive case
    return n * factorial(n - 1);
}
```

**Execution Trace for factorial(4)**:
```
factorial(4) = 4 × factorial(3)
factorial(3) = 3 × factorial(2)
factorial(2) = 2 × factorial(1)
factorial(1) = 1 (base case)
factorial(2) = 2 × 1 = 2
factorial(3) = 3 × 2 = 6
factorial(4) = 4 × 6 = 24
```

### **Example: Fibonacci**
```cpp
int fibonacci(int n) {
    // Base cases
    if (n <= 1) {
        return n;
    }
    
    // Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```

---

## Recursion vs Iteration

### **When to Use Recursion**
- **Natural recursive structure** (trees, graphs, file systems)
- **Divide and conquer** problems
- **Backtracking** algorithms
- **Mathematical definitions** (factorial, Fibonacci)

### **When to Use Iteration**
- **Performance critical** applications
- **Memory constrained** environments
- **Simple loops** and counting
- **Avoiding stack overflow**

### **Comparison Example: Sum of Array**

**Recursive Approach**:
```cpp
int sumRecursive(int arr[], int size) {
    // Base case
    if (size == 0) {
        return 0;
    }
    
    // Recursive case
    return arr[0] + sumRecursive(arr + 1, size - 1);
}
```

**Iterative Approach**:
```cpp
int sumIterative(int arr[], int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum;
}
```

### **Performance Comparison**

| Aspect | Recursion | Iteration |
|--------|-----------|-----------|
| **Memory** | O(n) stack space | O(1) extra space |
| **Speed** | Slower (function call overhead) | Faster |
| **Readability** | Often clearer | Can be complex |
| **Debugging** | Harder to trace | Easier to trace |

---

## Types of Recursion

### **1. Direct Recursion**
Function calls itself directly.

```cpp
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);  // Direct call
}
```

### **2. Indirect Recursion**
Function calls another function that eventually calls the original.

```cpp
int functionA(int n) {
    if (n <= 0) return 1;
    return n * functionB(n - 1);  // Calls functionB
}

int functionB(int n) {
    if (n <= 0) return 1;
    return n * functionA(n - 1);  // Calls functionA
}
```

### **3. Tail Recursion**
Recursive call is the last operation in the function.

```cpp
int factorialTail(int n, int accumulator = 1) {
    if (n <= 1) return accumulator;
    return factorialTail(n - 1, n * accumulator);  // Tail call
}
```

**Benefits of Tail Recursion**:
- Can be optimized by compiler to iteration
- No stack overflow risk
- Better performance

### **4. Multiple Recursion**
Function makes multiple recursive calls.

```cpp
int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);  // Two recursive calls
}
```

---

## Common Recursive Patterns

### **1. Linear Recursion**
Single recursive call per function.

```cpp
int linearSum(int arr[], int size) {
    if (size == 0) return 0;
    return arr[0] + linearSum(arr + 1, size - 1);
}
```

### **2. Binary Recursion**
Two recursive calls per function.

```cpp
int binarySearch(int arr[], int left, int right, int target) {
    if (left > right) return -1;
    
    int mid = left + (right - left) / 2;
    
    if (arr[mid] == target) return mid;
    if (arr[mid] > target) {
        return binarySearch(arr, left, mid - 1, target);  // Left half
    } else {
        return binarySearch(arr, mid + 1, right, target); // Right half
    }
}
```

### **3. Tree Recursion**
Multiple recursive calls (like tree traversal).

```cpp
void preorderTraversal(TreeNode* root) {
    if (root == nullptr) return;
    
    cout << root->val << " ";                    // Visit current
    preorderTraversal(root->left);               // Traverse left
    preorderTraversal(root->right);              // Traverse right
}
```

### **4. Backtracking**
Try different choices and backtrack if needed.

```cpp
bool solveSudoku(int grid[9][9]) {
    int row, col;
    
    // Find empty cell
    if (!findEmpty(grid, row, col)) {
        return true;  // Puzzle solved
    }
    
    // Try digits 1-9
    for (int num = 1; num <= 9; num++) {
        if (isSafe(grid, row, col, num)) {
            grid[row][col] = num;
            
            if (solveSudoku(grid)) {
                return true;  // Success
            }
            
            grid[row][col] = 0;  // Backtrack
        }
    }
    
    return false;  // No solution
}
```

---

## Recursive Data Structures

### **1. Linked Lists**
```cpp
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// Recursive traversal
void printList(ListNode* head) {
    if (head == nullptr) return;
    cout << head->val << " ";
    printList(head->next);
}

// Recursive reverse
ListNode* reverseList(ListNode* head) {
    if (head == nullptr || head->next == nullptr) {
        return head;
    }
    
    ListNode* newHead = reverseList(head->next);
    head->next->next = head;
    head->next = nullptr;
    return newHead;
}
```

### **2. Binary Trees**
```cpp
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// Inorder traversal
void inorderTraversal(TreeNode* root) {
    if (root == nullptr) return;
    
    inorderTraversal(root->left);   // Left subtree
    cout << root->val << " ";       // Current node
    inorderTraversal(root->right);  // Right subtree
}

// Tree height
int treeHeight(TreeNode* root) {
    if (root == nullptr) return -1;
    
    int leftHeight = treeHeight(root->left);
    int rightHeight = treeHeight(root->right);
    
    return 1 + max(leftHeight, rightHeight);
}
```

### **3. Graphs (DFS)**
```cpp
void dfs(vector<vector<int>>& graph, vector<bool>& visited, int node) {
    visited[node] = true;
    cout << node << " ";
    
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            dfs(graph, visited, neighbor);
        }
    }
}
```

---

## Optimization Techniques

### **1. Memoization**
Store results of expensive recursive calls.

```cpp
int fibonacciMemo(int n, vector<int>& memo) {
    if (n <= 1) return n;
    
    if (memo[n] != -1) {
        return memo[n];  // Return cached result
    }
    
    memo[n] = fibonacciMemo(n - 1, memo) + fibonacciMemo(n - 2, memo);
    return memo[n];
}

int fibonacci(int n) {
    vector<int> memo(n + 1, -1);
    return fibonacciMemo(n, memo);
}
```

### **2. Tail Call Optimization**
Convert to tail recursion for better performance.

```cpp
// Non-tail recursive
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);  // Multiplication after recursive call
}

// Tail recursive
int factorialTail(int n, int accumulator = 1) {
    if (n <= 1) return accumulator;
    return factorialTail(n - 1, n * accumulator);  // Tail call
}
```

### **3. Iterative Conversion**
Convert recursive algorithms to iterative.

```cpp
// Recursive
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

// Iterative
int factorialIterative(int n) {
    int result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}
```

---

## Common Mistakes

### **1. Missing Base Case**
```cpp
// WRONG - No base case
int infiniteRecursion(int n) {
    return n + infiniteRecursion(n - 1);  // Never stops!
}

// CORRECT
int sumToN(int n) {
    if (n <= 0) return 0;  // Base case
    return n + sumToN(n - 1);
}
```

### **2. Incorrect Base Case**
```cpp
// WRONG - Wrong base case
int factorial(int n) {
    if (n == 0) return 0;  // Should return 1
    return n * factorial(n - 1);
}

// CORRECT
int factorial(int n) {
    if (n <= 1) return 1;  // Correct base case
    return n * factorial(n - 1);
}
```

### **3. Not Making Progress**
```cpp
// WRONG - Doesn't make progress toward base case
int badRecursion(int n) {
    if (n <= 0) return 0;
    return badRecursion(n);  // Same n, never changes
}

// CORRECT
int goodRecursion(int n) {
    if (n <= 0) return 0;
    return goodRecursion(n - 1);  // Makes progress
}
```

### **4. Stack Overflow**
```cpp
// WRONG - Too deep recursion
int deepRecursion(int n) {
    if (n <= 0) return 0;
    return 1 + deepRecursion(n - 1);  // Can cause stack overflow for large n
}

// CORRECT - Use iteration for large inputs
int safeRecursion(int n) {
    if (n > 10000) {
        // Use iteration for large values
        int result = 0;
        for (int i = 0; i <= n; i++) {
            result += i;
        }
        return result;
    }
    
    if (n <= 0) return 0;
    return n + safeRecursion(n - 1);
}
```

---

## Practice Problems

### **Problem 1: Power Function**
Implement `pow(x, n)` using recursion.

```cpp
double myPow(double x, int n) {
    if (n == 0) return 1;
    if (n == 1) return x;
    if (n == -1) return 1 / x;
    
    double half = myPow(x, n / 2);
    if (n % 2 == 0) {
        return half * half;
    } else {
        return half * half * (n > 0 ? x : 1 / x);
    }
}
```

### **Problem 2: Merge Sort**
Implement merge sort recursively.

```cpp
void merge(vector<int>& arr, int left, int mid, int right) {
    vector<int> temp(right - left + 1);
    int i = left, j = mid + 1, k = 0;
    
    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) {
            temp[k++] = arr[i++];
        } else {
            temp[k++] = arr[j++];
        }
    }
    
    while (i <= mid) temp[k++] = arr[i++];
    while (j <= right) temp[k++] = arr[j++];
    
    for (int p = 0; p < k; p++) {
        arr[left + p] = temp[p];
    }
}

void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}
```

### **Problem 3: Tower of Hanoi**
Solve the Tower of Hanoi puzzle.

```cpp
void towerOfHanoi(int n, char from, char aux, char to) {
    if (n == 1) {
        cout << "Move disk 1 from " << from << " to " << to << endl;
        return;
    }
    
    towerOfHanoi(n - 1, from, to, aux);
    cout << "Move disk " << n << " from " << from << " to " << to << endl;
    towerOfHanoi(n - 1, aux, from, to);
}
```

---

## Quick Reference

### **Recursive Function Template**
```cpp
ReturnType recursiveFunction(Parameters) {
    // Base case(s)
    if (baseCondition) {
        return baseValue;
    }
    
    // Recursive case(s)
    return recursiveFunction(smallerProblem);
}
```

### **Common Base Cases**
- **Arrays/Lists**: Empty or single element
- **Numbers**: 0, 1, or negative values
- **Trees**: nullptr (empty tree)
- **Strings**: Empty string or single character

### **Recursion Patterns**
- **Linear**: Single recursive call
- **Binary**: Two recursive calls
- **Tree**: Multiple recursive calls
- **Tail**: Recursive call is last operation

### **Optimization Strategies**
- **Memoization**: Cache results
- **Tail Recursion**: Convert to iteration
- **Iterative Conversion**: Replace with loops
- **Early Termination**: Stop when possible

### **Debugging Tips**
1. **Trace the execution** step by step
2. **Check base cases** carefully
3. **Verify progress** toward base case
4. **Monitor stack depth** for overflow
5. **Use print statements** to track calls

### **Exam Tips**
1. **Always identify base case first**
2. **Ensure problem gets smaller** in recursive calls
3. **Consider stack space** for deep recursion
4. **Use memoization** for repeated subproblems
5. **Convert to iteration** if performance is critical

---

*Master recursion and you'll have a powerful tool for solving complex problems elegantly!* 