# Chapter 10: Dynamic Programming

## 10.1 Algorithm Design Techniques Overview

Chapter 10 introduces several important algorithm design techniques, beginning with **greedy algorithms** before focusing on **dynamic programming**.

### Greedy Algorithms Summary
- Work in phases where decisions appear locally optimal without considering future consequences
- Choose local optimum at each step ("take what you can get now" approach)
- Previously introduced examples: Dijkstra's, Prim's, and Kruskal's algorithms (Chapter 9)
- When local optimum equals global optimum, algorithm is correct
- May produce suboptimal solutions when this isn't the case
- Sometimes used for approximate answers when exact solutions require more complex algorithms

## 10.3 Dynamic Programming

Dynamic programming is a powerful technique that addresses inefficiencies in recursive algorithms by systematically recording solutions to subproblems in a table.

### 10.3.1 Using a Table Instead of Recursion

The chapter illustrates the benefits of dynamic programming through examples:

#### Fibonacci Numbers Example
- Natural recursive implementation is highly inefficient
- Running time T(N) satisfies T(N) ≥ T(N−1) + T(N−2)
- Growth rate matches Fibonacci numbers themselves (exponential)
- Key insight: Computing F(N) only requires F(N−1) and F(N−2)
- By recording previously computed values, we achieve O(N) time complexity
- Further optimization: only need to store the two most recent values

#### Formula Evaluation Example
The chapter presents a more complex example with the recurrence relation:

C(N) = 2/N * ∑(i=0 to N-1) C(i) + N

**Recursive Implementation Issues:**
- Leads to redundant calculations of the same subproblems
- Exponential running time due to overlapping subproblems

**Table-Based Solution (Figure 10.45):**
```
double eval(int n)
{
    vector<double> c(n + 1);
    
    c[0] = 1.0;
    for(int i = 1; i <= n; ++i)
    {
        double sum = 0.0;
        
        for(int j = 0; j < i; ++j)
            sum += c[j];
        c[i] = 2.0 * sum / i + i;
    }
    
    return c[n];
}
```

**Dynamic Programming Benefits:**
- Avoids redundant recursive calls
- Reduces time complexity from exponential to O(N²)
- Can be further optimized to O(N) time complexity

### Key Dynamic Programming Principles

1. **Overlapping Subproblems**: Problems where the same subproblems are solved multiple times
2. **Optimal Substructure**: Optimal solution contains optimal solutions to subproblems
3. **Memoization**: Storing results of expensive function calls and returning cached result when same inputs occur again
4. **Bottom-up Approach**: Building solutions to smaller subproblems first, then using them to solve larger problems

### Implementation Approaches

1. **Top-down with Memoization**: 
   - Start with recursive solution
   - Add storage (usually array/table) to remember results of subproblems
   - Check table before computation; if result exists, return it
   
2. **Bottom-up with Tabulation**:
   - Start by solving smallest subproblems
   - Use their solutions to build up to the final problem
   - Usually implemented with iteration rather than recursion
   - Typically more efficient (no recursive overhead)

### When to Use Dynamic Programming

Dynamic programming is especially useful for problems with:
- Optimal substructure
- Overlapping subproblems
- Need for exhaustive search but with optimization opportunities

Common dynamic programming applications include:
- Shortest path problems
- Sequence alignment (e.g., DNA matching)
- Resource allocation problems
- Knapsack problems
- Matrix chain multiplication

## Practice Recommendations

1. Identify the recursive structure in the problem
2. Determine if there are overlapping subproblems
3. Choose between memoization and tabulation based on problem structure
4. Always look for opportunities to optimize space complexity (as shown in the Fibonacci example)
5. Practice converting recursive solutions to iterative, table-based solutions

## Exercise Note

The chapter suggests a simple change to the eval() function that would reduce its running time from O(N²) to O(N). (Hint: Consider maintaining a running sum rather than recalculating it for each iteration.)