7.7 Quicksort
As its name implies for C++, quicksort has historically been the fastest known generic
sorting algorithm in practice. Its average running time is O(N logN). It is very fast, mainly
due to a very tight and highly optimized inner loop. It has O(N2) worst-case performance,
but this can be made exponentially unlikely with a little effort

Arbitrarily choose
any item, and then form three groups: those smaller than the chosen item, those equal to
the chosen item, and those larger than the chosen item. Recursively sort the first and third
groups, and then concatenate the three groups

1. If the number of elements in S is 0 or 1, then return.
2. Pick any element v in S. This is called the pivot.
3. Partition S − {v} (the remaining elements in S) into two disjoint groups: S1 = {x ∈
S − {v}|x ≤ v}, and S2 = {x ∈ S − {v}|x ≥ v}.
4. Return {quicksort(S1) followed by v followed by quicksort(S2)}.

7.7.1 Picking the Pivot
Although the algorithm as described works no matter which element is chosen as pivot,
some choices are obviously better than others.

A safe course is merely to choose the pivot randomly.

Median-of-Three Partitioning
The median of a group of N numbers is the  N/2 th largest number. The best choice
of pivot would be the median of the array. Unfortunately, this is hard to calculate and
would slow down quicksort considerably. A good estimate can be obtained by picking
three elements randomly and using the median of these three as pivot. The randomness
turns out not to help much, so the common course is to use as pivot the median of the
left, right, and center elements. For instance, with input 8, 1, 4, 9, 6, 3, 5, 2, 7, 0 as before,
the left element is 8, the right element is 0, and the center (in position  (left + right)/2 )
element is 6. Thus, the pivot would be v = 6. Using median-of-three partitioning clearly
eliminates the bad case for sorted input (the partitions become equal in this case) and
actually reduces the number of comparisons by 14%.

7.7.2 Partitioning Strategy
There are several partitioning strategies used in practice, but the one described here is
known to give good results. It is very easy, as we shall see, to do this wrong or inefficiently,
but it is safe to use a known method. The first step is to get the pivot element out of
the way by swapping it with the last element. i starts at the first element and j starts at
the next-to-last element. If the original input was the same as before, the following figure
shows the current situation:
8 1 4 9 0 3 5 2 7 6
↑ ↑
i j
For now, we will assume that all the elements are distinct. Later on, we will worry about
what to do in the presence of duplicates. As a limiting case, our algorithm must do the
proper thing if all of the elements are identical. It is surprising how easy it is to do the
wrong thing.

The text discusses a critical implementation detail: what should happen when elements equal to the pivot are encountered during partitioning? There are four possible strategies:

Both i and j stop when they encounter elements equal to the pivot
i stops but j doesn't stop
j stops but i doesn't stop
Neither i nor j stops

The key insights:

Bias concern: If i and j behave differently (options 2 or 3), all elements equal to the pivot will end up in one partition, creating imbalance.
All-identical elements case: This is used as a test case to evaluate strategies:

If both pointers stop (option 1): Many seemingly "useless" swaps occur between identical elements, but this actually creates balanced partitions with sizes roughly N/2 each, giving O(N log N) performance.
If neither pointer stops (option 4): No swaps occur, which seems efficient, but the pivot ends up near the end, creating extremely unbalanced partitions (one tiny, one huge). This leads to O(N²) performance - just as bad as using the first element as pivot on sorted data.


Conclusion: It's better to do "unnecessary" swaps and get balanced partitions than to risk unbalanced partitions. Therefore, the best strategy is option 1: both i and j should stop when they encounter elements equal to the pivot.
Practical importance: This matters because even if your original input doesn't have many duplicates, recursive calls within quicksort may eventually work on subarrays with many identical elements.

This is a classic example of how subtle implementation decisions can dramatically affect algorithm performance in practice, even when the theoretical complexity remains O(N log N) for the best case.

7.7.6 A Linear-Expected-Time Algorithm for Selection
Quicksort can be modified to solve the selection problem, which we have seen in Chapters 1
and 6. Recall that by using a priority queue, we can find the kth largest (or smallest) element
in O(N + k logN). For the special case of finding the median, this gives an O(N logN)
algorithm.
Since we can sort the array in O(N logN) time, one might expect to obtain a better
time bound for selection. The algorithm we present to find the kth smallest element in a
set S is almost identical to quicksort. In fact, the first three steps are the same. We will
call this algorithm quickselect. Let |Si| denote the number of elements in Si. The steps of
quickselect are
1. If |S| = 1, then k = 1 and return the element in S as the answer. If a cutoff for small
arrays is being used and |S| ≤ CUTOFF, then sort S and return the kth smallest element.
2. Pick a pivot element, v ∈ S.
3. Partition S − {v} into S1 and S2, as was done with quicksort.
4. If k ≤ |S1|, then the kth smallest element must be in S1. In this case, return
quickselect(S1, k). If k = 1 + |S1|, then the pivot is the kth smallest element and
we can return it as the answer. Otherwise, the kth smallest element lies in S2, and it
is the (k − |S1| − 1)st smallest element in S2. We make a recursive call and return
quickselect(S2, k − |S1| − 1).
In contrast to quicksort, quickselect makes only one recursive call instead of two. The
worst case of quickselect is identical to that of quicksort and is O(N2). Intuitively,


7.6 Mergesort
We now turn our attention to mergesort. Mergesort runs in O(N logN) worst-case running
time, and the number of comparisons used is nearly optimal. It is a fine example of a
recursive algorithm.
The fundamental operation in this algorithm is merging two sorted lists.