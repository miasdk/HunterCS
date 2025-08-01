# Exam 1 Solutions and Explanations

## Question 1: AVL Tree Deletion (12 pts)

**Problem:** Delete 64 from an AVL tree and rebalance as needed.

**Solution:**

1. **Delete 64:**
   - Find node 64 in the tree
   - Replace it with its inorder successor (or predecessor)
   - In this case, node 61 becomes the left child of 74

2. **Check for imbalance:**
   - Travel up the tree and verify balance factors
   - Node 74 becomes imbalanced with a balance factor of -2 (left side too tall)

3. **Rebalance:**
   - Perform a right-left rotation (double rotation) on node 74
   - First, right rotation on the left subtree
   - Then, left rotation on the unbalanced node
   - The tree is now balanced

**Key Points:**
- AVL tree deletion requires maintaining balance factors
- After deletion, check all ancestors of the deleted node for imbalance
- Balance factors ensure tree height is O(log n)
- Double rotations are necessary when the imbalance follows a "zig-zag" pattern

## Question 2: Merge With Move (20 pts)

**Problem:** Implement a function to merge two sorted vectors using move semantics.

**Solution:**

```cpp
std::vector<Foo> merge(std::vector<Foo>& vec1, std::vector<Foo>& vec2) {
    // Construct new vector to return
    std::vector<Foo> merged;
    
    // Reserve space to avoid reallocations
    merged.reserve(vec1.size() + vec2.size());
    
    // Set up iterators for both vectors
    auto it1 = vec1.begin();
    auto it2 = vec2.begin();
    
    // Traverse both vectors together
    while (it1 != vec1.end() && it2 != vec2.end()) {
        // Compare elements and copy the smaller one
        if (*it1 < *it2) {
            // Use std::move to avoid deep copying
            merged.push_back(std::move(*it1));
            // Increment only iterator for vec1
            ++it1;
        } else {
            merged.push_back(std::move(*it2));
            ++it2;
        }
    }
    
    // Copy remaining elements from vec1 (if any)
    while (it1 != vec1.end()) {
        merged.push_back(std::move(*it1));
        ++it1;
    }
    
    // Copy remaining elements from vec2 (if any)
    while (it2 != vec2.end()) {
        merged.push_back(std::move(*it2));
        ++it2;
    }
    
    // Return the merged vector
    return merged;
}
```

**Key Points:**
- We use iterators to traverse both vectors simultaneously
- `std::move` converts lvalues to rvalues, enabling move semantics
- Moving elements is more efficient than copying for objects with resources
- We only increment the iterator of the vector whose element we just moved
- After one vector is exhausted, we move the remaining elements from the other vector

## Question 3: Complexity Analysis (Medium) (5 pts)

**Problem:** Analyze the time complexity of the following code:

```cpp
int i, j, k = 0;
for (i = n / 2; i <= n; i++) {
    for (j = 2; j <= n; j = j * 2) {
        k = k + n / 2;
    }
}
```

**Solution:** O(n log n)

**Analysis:**
1. **Outer loop**: Runs from i = n/2 to n, so it executes n/2 times, which is O(n)
2. **Inner loop**: Variable j starts at 2 and doubles each time (j = j*2) until j > n
   - This creates a logarithmic sequence: 2, 4, 8, 16, ...
   - j will reach n after log₂n iterations
   - So the inner loop runs log₂n times, which is O(log n)
3. **Combined complexity**: O(n) * O(log n) = O(n log n)

## Question 4: B-tree Analysis (20 pts)

**Problem:** Analyze the time complexity of searching in a B-tree with order M and height H.

**Solution:**

1. **Search for key in each node:**
   - Each node can contain up to M-1 keys
   - Using binary search within a node takes O(log M) time
   - Linear search would take O(M) time, but is less efficient

2. **Visit H nodes:**
   - We need to traverse from root to leaf, visiting H nodes
   - Each traversal step requires finding the correct child pointer
   - This requires H node accesses

3. **Total local accesses:**
   - We perform a binary search in each of the H nodes
   - Total time: O(H log M)

4. **Remote accesses:**
   - We need to follow H-1 child pointers
   - Each pointer access is O(1)
   - Total remote accesses: O(H)

5. **Overall complexity:**
   - Dominated by local access time: O(H log M)
   - Since H = log_M(n) for a B-tree with n elements, this can be rewritten as O(log M × log_M n)

**Key Points:**
- B-trees optimize for disk access by minimizing the height of the tree
- The order M influences both the search time within a node and the height of the tree
- Binary search within nodes provides significant performance improvement over linear search

## Question 5: Complexities of Basic Operations (12 pts)

**Correct answers:**
1. Access vector (worst): O(1)
2. Insert in splay tree (amortized): O(log n)
3. Delete from AVL tree (worst): O(log n)
4. Find in sorted linked list (average): O(n)
5. Find in an AVL tree (average): O(log n)
6. Find in binary search tree (worst): O(n)

**Explanations:**

1. **Vector access**: Direct indexing in constant time regardless of vector size
2. **Splay tree insert**: Requires finding the insertion position and splaying, which is O(log n) amortized
3. **AVL tree delete**: Requires finding the node, deleting it, and rebalancing, all O(log n) operations
4. **Sorted linked list search**: Requires sequential traversal from the beginning, taking O(n) time
5. **AVL tree search**: Uses binary search tree property with balanced height of O(log n)
6. **BST worst-case search**: In a degenerate tree (e.g., all right children), search becomes O(n)

## Question 6: Move Semantics (9 pts)

**Problem:** Explain what happens in the following code:
```cpp
std::vector<string> blurbs1, blurbs2;
// assume blurbs1 and blurbs2 are filled with strings
blurbs1.push_back(std::move(blurbs2.at(5)));
```

**Solution:**

1. `std::move(blurbs2.at(5))` converts the string at index 5 in blurbs2 to an rvalue reference
   - This doesn't actually move anything yet, just changes how the compiler treats the object

2. `push_back` is overloaded to accept rvalue references
   - When given an rvalue reference, it uses move semantics instead of copy semantics
   - This invokes the move constructor of std::string rather than the copy constructor

3. The move constructor efficiently transfers ownership of the string's internal buffer
   - No deep copying of the character data occurs
   - The source string (blurbs2[5]) is left in a valid but unspecified state (typically empty)

**Key Points:**
- Move semantics avoid unnecessary copying of resources (memory, file handles, etc.)
- `std::move` is just a cast that enables move semantics; it doesn't itself move anything
- After the move, the source object remains valid but may not contain the original value

## Question 7: Complexity Analysis (Easy) (5 pts)

**Problem:** Analyze the time complexity of the following code:

```cpp
int a = 0, b = 0;
for (i = 0; i < n; i++) {
    a = a + i;
}
for (j = 0; j < n; j++) {
    b = b + j;
}
```

**Solution:** O(n)

**Analysis:**
1. First loop: Iterates n times, each iteration is O(1) work, so O(n) total
2. Second loop: Also iterates n times, each iteration is O(1) work, so O(n) total
3. Combined complexity: O(n) + O(n) = O(n)

This is a case of sequential loops, so we add the complexities rather than multiply them.

## Question 8: Upper Bound (12 pts)

**Problem:** Implement a function to find the highest bid less than or equal to a given price.

**Solution:**

```cpp
std::set<float>::iterator winning_bid(std::set<float> bids, float price) {
    // Get iterator to first element greater than price
    auto it = bids.upper_bound(price);
    
    // If all bids are <= price, upper_bound returns end()
    // If all bids are > price, upper_bound returns begin()
    if (it == bids.begin()) {
        // No bids are <= price
        return bids.end();
    }
    
    // Move to the highest element <= price
    --it;
    
    return it;
}
```

**Key Points:**
- `upper_bound` returns an iterator to the first element greater than the given value
- We need to decrement this iterator to get the highest element less than or equal to price
- If `upper_bound` returns `begin()`, there are no elements less than or equal to price
- This approach avoids traversing the entire set, making it O(log n) instead of O(n)

## Question 9: Splay Trees (5 pts)

**Problem:** Explain a benefit of splay trees over AVL trees.

**Solution:**
Splay trees move recently accessed elements to the root, effectively creating a caching effect. Elements that are accessed frequently will stay near the top of the tree, making subsequent accesses more efficient. This is particularly beneficial when access patterns show locality of reference, where recently accessed items are likely to be accessed again soon.

**Additional benefits:**
- Splay trees don't require storing height or balance information at each node
- They're simpler to implement than AVL trees
- They have good amortized performance without the overhead of strict balancing
- They automatically adapt to access patterns

## Question 10: Iterator Invalidation (10 pts)

**Problem:** Compare iterator invalidation between list::delete, list::insert, vector::insert.

**Solution:**

**list::delete:**
- When you delete a node from a list, the iterator pointing to that node is immediately invalidated
- Other iterators to different nodes remain valid
- This is because the memory for the deleted node is freed, making the iterator point to invalid memory

**list::insert:**
- Inserting into a list doesn't invalidate any existing iterators
- The iterator to the node you're inserting before or after remains valid
- This is because list nodes are allocated independently, and insertion just redirects pointers

**vector::insert:**
- If the insertion causes the vector to resize, all iterators are invalidated
- Even without resizing, any iterator pointing to elements at or after the insertion point are invalidated
- This is because vectors store elements in contiguous memory, and insertion may require shifting elements

**Key Difference:**
Lists provide stronger iterator stability since they don't need contiguous memory. In vectors, insertions and deletions can invalidate many or all iterators due to the contiguous memory requirement.
