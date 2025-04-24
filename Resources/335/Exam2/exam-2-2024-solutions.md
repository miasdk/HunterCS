# Exam 2 Solutions and Explanations

## Question 1: Quicksort Partitioning (8 pts)

**Problem:** Use the Hoare partitioning algorithm on the array: `[6, 2, 12, 9, 16, 4, 11, 3, 8, 10, 14, 15]` with 9 as the pivot.

**Solution:**

**Step 1:** Swap pivot (9) with last element (15)
- Array becomes: `[6, 2, 12, 15, 16, 4, 11, 3, 8, 10, 14, 9]`

**Step 2:** Initialize left pointer (i) at index 0 and right pointer (j) at index 10
- Find first element from left ≥ pivot (9): element 12 at index 2
- Find first element from right ≤ pivot (9): element 8 at index 8
- Swap elements: `[6, 2, 8, 15, 16, 4, 11, 3, 12, 10, 14, 9]`

**Step 3:** Continue with i=3, j=8
- Find next element from left ≥ pivot: element 15 at index 3
- Find next element from right ≤ pivot: element 3 at index 7
- Swap elements: `[6, 2, 8, 3, 16, 4, 11, 15, 12, 10, 14, 9]`

**Step 4:** Continue with i=4, j=7
- Find next element from left ≥ pivot: element 16 at index 4
- Find next element from right ≤ pivot: element 4 at index 5
- Swap elements: `[6, 2, 8, 3, 4, 16, 11, 15, 12, 10, 14, 9]`

**Step 5:** Continue with i=5, j=5
- Since i=j, pointers have met, partitioning is complete
- Swap pivot (9) with element at position j (16): `[6, 2, 8, 3, 4, 9, 11, 15, 12, 10, 14, 16]`

**Final partitioned array:** `[6, 2, 8, 3, 4, 9, 11, 15, 12, 10, 14, 16]`

**Key Points:**
- Hoare's algorithm uses two pointers moving toward each other
- Elements greater than or equal to the pivot go to the right side
- Elements less than or equal to the pivot go to the left side
- The pivot isn't necessarily in its final sorted position
- The algorithm terminates when the pointers meet or cross

## Question 2: Heap Insertion (8 pts)

**Problem:** Insert value 4 into the min heap: `[-, 2, 5, 6, 9, 8, 13, 7, 11, 10]`

**Solution:**

**Step 1:** Store 4 at index 0 as aq sentinel value
- Heap becomes: `[4, 2, 5, 6, 9, 8, 13, 7, 11, 10]`

**Step 2:** Insert at the end, creating a hole at position 10
- Increment heap size
- Heap becomes: `[4, 2, 5, 6, 9, 8, 13, 7, 11, 10, ?]`

**Step 3:** Percolate up - Compare with parent at index 5 (value 8)
- 4 < 8, so move 8 down to position 10
- Heap becomes: `[4, 2, 5, 6, 9, ?, 13, 7, 11, 10, 8]`
- Hole moves to position 5

**Step 4:** Continue percolating - Compare with parent at index 2 (value 5)
- 4 < 5, so move 5 down to position 5
- Heap becomes: `[4, 2, ?, 6, 9, 5, 13, 7, 11, 10, 8]`
- Hole moves to position 2

**Step 5:** Final step - Place 4 in the hole at position 2
- Heap becomes: `[4, 2, 4, 6, 9, 5, 13, 7, 11, 10, 8]`

**Final min heap:** `[4, 2, 4, 6, 9, 5, 13, 7, 11, 10, 8]`

**Key Points:**
- Using index 0 as a sentinel simplifies percolate-up logic
- Percolation compares with parent nodes and moves them down if needed
- We follow the path up the tree until finding the correct position
- The resulting heap must maintain the heap property (parent ≤ children)

## Question 3: Hash Insertion with Quadratic Probing (8 pts)

**Problem:** Insert elements 11, 1, 15, 2 into a hash table with function h(x) = x mod 10 using quadratic probing. Initial table has 21 at index 1, 3 at index 3, and 16 at index 6.

**Solution:**

**Inserting 11:**
- h(11) = 11 mod 10 = 1
- Index 1 is occupied (21), try h(11) + 1² = 2
- Index 2 is empty, insert 11 at index 2

**Inserting 1:**
- h(1) = 1 mod 10 = 1
- Index 1 is occupied (21), try h(1) + 1² = 2
- Index 2 is occupied (11), try h(1) + 2² = 5
- Index 5 is empty, insert 1 at index 5

**Inserting 15:**
- h(15) = 15 mod 10 = 5
- Index 5 is occupied (1), try h(15) + 1² = 6
- Index 6 is occupied (16), try h(15) + 2² = 9
- Index 9 is empty, insert 15 at index 9

**Inserting 2:**
- h(2) = 2 mod 10 = 2
- Index 2 is occupied (11), try h(2) + 1² = 3
- Index 3 is occupied (3), try h(2) + 2² = 6
- Index 6 is occupied (16), try h(2) + 3² = 11 (out of bounds)
- Apply modulo: 11 mod 10 = 1, index 1 is occupied (21)
- Try h(2) + 4² = 18, apply modulo: 18 mod 10 = 8
- Index 8 is empty, insert 2 at index 8

**Final hash table:**
- Index 0: empty
- Index 1: 21
- Index 2: 11
- Index 3: 3
- Index 4: empty
- Index 5: 1
- Index 6: 16
- Index 7: empty
- Index 8: 2
- Index 9: 15

**Key Points:**
- Quadratic probing uses probe sequence h(x), h(x) + 1², h(x) + 2², etc.
- This helps avoid primary clustering that occurs with linear probing
- We wrap around the table using modulo when necessary
- The probe sequence can potentially visit all table positions if the table size is a prime number

## Question 4: Introsort (15 pts)

**Problem:** Explain how introsort works and why its worst-case complexity is O(n log n).

**Solution:**

Introsort is a hybrid sorting algorithm that combines the best features of quicksort, heapsort, and insertion sort.

**How Introsort Works:**
1. Start with quicksort, which has excellent average-case performance
2. Track the recursion depth during the sorting process
3. If the recursion depth exceeds a threshold (typically 2×log₂n), switch to heapsort
4. For small partitions (below a fixed size threshold), switch to insertion sort

**Why Worst-Case is O(n log n):**

1. **Quicksort Portion:**
   - Normally, quicksort has O(n²) worst-case complexity
   - By limiting the recursion depth to O(log n), we cap the worst-case time for this portion at O(n log n)
   - This prevents the quadratic behavior on pathological inputs

2. **Heapsort Portion:**
   - If the recursion depth limit is reached, we switch to heapsort
   - Heapsort has a guaranteed O(n log n) worst-case time complexity
   - This ensures that even in worst-case scenarios, we maintain O(n log n) performance

3. **Insertion Sort Portion:**
   - For small partitions (typically size ≤ 16), we use insertion sort
   - Since these partitions are of constant size, insertion sort takes O(1) time for each
   - There are O(n) small partitions, so this contributes O(n) to the overall complexity

**Overall Complexity:**
- O(n log n) from the quicksort portion (with depth limiting)
- O(n log n) from the heapsort portion (if needed)
- O(n) from the insertion sort portion
- Total: O(n log n)

**Key Points:**
- Introsort adaptively selects the best algorithm based on the input characteristics
- It provides the average-case efficiency of quicksort
- It guarantees the worst-case efficiency of heapsort
- It leverages insertion sort's efficiency on small inputs
- This hybrid approach makes it practical and efficient for all input types

## Question 5: Algorithm Analysis with Heaps (20 pts)

**Problem:** Design an algorithm to select k golfers with the lowest scores from n applications, where 2 new applications arrive after each selection.

**Solution:**

**Approach:**
Use a min heap to efficiently access the golfer with the lowest score at each step.

**Algorithm:**
1. Create a min heap from the initial n applications
   - Use the buildHeap algorithm for O(n) efficiency
   - The score is the key by which the heap is organized

2. For each of the k selections:
   - Remove the root of the min heap (deleteMin)
   - This gives the golfer with the lowest score
   - Add 2 new applications to the heap (2 insert operations)

**Complexity Analysis:**
1. Initial buildHeap: O(n)
2. k deleteMin operations: O(k log(n+k))
   - Each operation is O(log m) where m is the current heap size
   - The heap size ranges from n to n+k over time

3. 2k insert operations: O(k log(n+k))
   - Each insertion is O(log m) where m is the current heap size

4. Total time complexity: O(n + k log(n+k))
   - The buildHeap dominates when k is small relative to n
   - The deleteMin and insert operations dominate when k is large

**Key Points:**
- A min heap is ideal for repeatedly finding the minimum element
- We must account for the changing size of the heap over time
- The complexity depends on both the initial number of applications n and the number of selections k
- The buildHeap operation is more efficient than inserting n elements one by one

## Question 6: Time Complexities (14 pts)

**Correct answers:**
1. Rehashing (average case): O(n)
2. Find a value in unordered_map: O(1) average, O(n) worst
3. deleteMin from min heap (average case): O(log n)
4. Partition around pivot (average case): O(n)
5. Find a key in ordered map: O(log n)
6. Find a key in unordered_map: O(1) average, O(n) worst
7. Quickselect (average case): O(n)

**Explanations:**

1. **Rehashing**: Requires visiting each element once and reh