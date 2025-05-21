# Comprehensive Guide to Sorting Algorithms

This guide provides a detailed overview of the sorting algorithms commonly covered in CSCI 33500, including their implementations, time and space complexity analysis, and key characteristics.

## Quick Reference Table

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable | In-Place | Notes |
|-----------|-----------|--------------|------------|-------|--------|----------|-------|
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes | Efficient for small or nearly sorted data |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Yes | Simple but inefficient |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes | Rarely used in practice |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No | Consistent performance, external sorting |
| Quicksort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Yes | Often fastest in practice |
| Heapsort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes | Guaranteed O(n log n), in-place |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(n+k) | Yes | No | Linear time for integer keys in small range |
| Radix Sort | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | O(n+k) | Yes | No | Linear time for fixed-length keys |
| Bucket Sort | O(n+k) | O(n+k) | O(n²) | O(n+k) | Yes | No | Efficient with uniform distribution |
| Shell Sort | O(n log n) | Depends on gap | O(n²) | O(1) | No | Yes | Improvement of insertion sort |

## 1. Insertion Sort

### Algorithm Description
Insertion sort builds the final sorted array one item at a time. It iterates through an array, consuming one input element at each repetition, and growing a sorted output list. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.

### Implementation
```cpp
void insertionSort(vector<int>& arr) {
    for (int i = 1; i < arr.size(); i++) {
        int key = arr[i];
        int j = i - 1;
        
        // Move elements greater than key to one position ahead
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
```

### Complexity Analysis
- **Time Complexity**:
  - Best case: O(n) (already sorted)
  - Average case: O(n²)
  - Worst case: O(n²) (reverse sorted)
- **Space Complexity**: O(1) (in-place)

### Key Properties
- **Stable**: Yes (equal elements maintain relative order)
- **Adaptive**: Yes (efficient for nearly sorted data)
- **In-place**: Yes (requires constant extra space)
- **Online**: Yes (can sort as it receives input)

## 2. Selection Sort

### Algorithm Description
Selection sort divides the input list into two parts: a sorted sublist of items built up from left to right and a sublist of the remaining unsorted items. It repeatedly finds the minimum element from the unsorted sublist and moves it to the end of the sorted sublist.

### Implementation
```cpp
void selectionSort(vector<int>& arr) {
    for (int i = 0; i < arr.size() - 1; i++) {
        // Find the minimum element in unsorted array
        int min_idx = i;
        for (int j = i + 1; j < arr.size(); j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        
        // Swap the found minimum element with the first element
        swap(arr[min_idx], arr[i]);
    }
}
```

### Complexity Analysis
- **Time Complexity**:
  - Best case: O(n²)
  - Average case: O(n²)
  - Worst case: O(n²)
- **Space Complexity**: O(1) (in-place)

### Key Properties
- **Stable**: No (swaps can change order of equal elements)
- **Adaptive**: No (performance doesn't improve for nearly sorted data)
- **In-place**: Yes (requires constant extra space)
- **Online**: No (requires entire input list)

## 3. Bubble Sort

### Algorithm Description
Bubble sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated until the list is sorted.

### Implementation
```cpp
void bubbleSort(vector<int>& arr) {
    for (int i = 0; i < arr.size() - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < arr.size() - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        // If no swapping occurred in this pass, array is sorted
        if (!swapped) {
            break;
        }
    }
}
```

### Complexity Analysis
- **Time Complexity**:
  - Best case: O(n) (already sorted, with early termination)
  - Average case: O(n²)
  - Worst case: O(n²) (reverse sorted)
- **Space Complexity**: O(1) (in-place)

### Key Properties
- **Stable**: Yes (doesn't swap equal elements)
- **Adaptive**: Yes (with early termination check)
- **In-place**: Yes (requires constant extra space)
- **Online**: No (requires entire input list)

### Use Cases
- **Educational purposes**: Simple to understand and implement
- **Small datasets**: Can be efficient for very small arrays
- **Nearly sorted data**: With the early termination optimization
- **When stability is important** and the dataset is small

## 4. Merge Sort

### Algorithm Description
Merge sort is a divide-and-conquer algorithm that divides the input array into two halves, recursively sorts them, and then merges the sorted halves.

### Implementation
```cpp
void merge(vector<int>& arr, int left, int mid, int right) {
    // Create temporary arrays
    int n1 = mid - left + 1;
    int n2 = right - mid;
    vector<int> L(n1), R(n2);
    
    // Copy data to temp arrays
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];
    
    // Merge the temp arrays back into arr[left..right]
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    
    // Copy the remaining elements
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        
        // Sort first and second halves
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        
        // Merge the sorted halves
        merge(arr, left, mid, right);
    }
}
```

### Complexity Analysis
- **Time Complexity**:
  - Best case: O(n log n)
  - Average case: O(n log n)
  - Worst case: O(n log n)
- **Space Complexity**: O(n)

### Key Properties
- **Stable**: Yes (maintains relative order of equal elements)
- **Adaptive**: No (performance doesn't improve for partially sorted data)
- **In-place**: No (requires additional space for merging)
- **Online**: No (requires entire input list)

### Use Cases
- **Large datasets**: Consistent O(n log n) performance regardless of input
- **External sorting**: When data doesn't fit in memory
- **When stability is required**: Preserves order of equal elements
- **Parallel computing**: Easily parallelizable for multi-threaded sorting
- **Linked list sorting**: Particularly efficient for linked lists

## 5. Quicksort

### Algorithm Description
Quicksort is a divide-and-conquer algorithm that selects a 'pivot' element and partitions the array such that elements less than the pivot come before it, and elements greater than the pivot come after it. It then recursively sorts the sub-arrays.

### Implementation
```cpp
int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high]; // Choose the rightmost element as pivot
    int i = low - 1; // Index of smaller element
    
    for (int j = low; j < high; j++) {
        // If current element is smaller than or equal to pivot
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        // Partition the array
        int pi = partition(arr, low, high);
        
        // Sort elements before and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
```

### Complexity Analysis
- **Time Complexity**:
  - Best case: O(n log n) (balanced partitioning)
  - Average case: O(n log n)
  - Worst case: O(n²) (unbalanced partitioning, e.g., already sorted)
- **Space Complexity**: O(log n) for recursion stack

### Key Properties
- **Stable**: No (elements may be reordered during partitioning)
- **Adaptive**: Partially (performance varies with input)
- **In-place**: Yes (doesn't require extra storage)
- **Online**: No (requires entire input list)

### Use Cases
- **General-purpose sorting**: Often the fastest in practice for random data
- **When average case performance matters more than worst case**
- **Internal sorting** (when all data fits in memory)
- **When in-place sorting is needed** to minimize memory usage
- **Systems with good cache performance**: Due to localized memory reference pattern

## 6. Heapsort

### Algorithm Description
Heapsort builds a max-heap from the input data, then repeatedly extracts the maximum element from the heap and rebuilds the heap until all elements are extracted in order.

### Implementation
```cpp
void heapify(vector<int>& arr, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    
    // If left child is larger than root
    if (left < n && arr[left] > arr[largest])
        largest = left;
    
    // If right child is larger than largest so far
    if (right < n && arr[right] > arr[largest])
        largest = right;
    
    // If largest is not root
    if (largest != i) {
        swap(arr[i], arr[largest]);
        
        // Recursively heapify the affected sub-tree
        heapify(arr, n, largest);
    }
}

void heapSort(vector<int>& arr) {
    int n = arr.size();
    
    // Build heap (rearrange array)
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
    
    // Extract elements from heap one by one
    for (int i = n - 1; i > 0; i--) {
        // Move current root to end
        swap(arr[0], arr[i]);
        
        // Call heapify on the reduced heap
        heapify(arr, i, 0);
    }
}
```

### Complexity Analysis
- **Time Complexity**:
  - Best case: O(n log n)
  - Average case: O(n log n)
  - Worst case: O(n log n)
- **Space Complexity**: O(1) (in-place)

### Key Properties
- **Stable**: No (elements may be reordered during heapification)
- **Adaptive**: No (performance doesn't improve for partially sorted data)
- **In-place**: Yes (doesn't require extra storage)
- **Online**: No (requires entire input list)

### Use Cases
- **When worst-case guarantees are important**: Unlike quicksort
- **When memory usage is a concern**: In-place with O(1) extra space
- **Real-time systems** requiring guaranteed time bounds
- **Priority queue implementation**: Related data structure
- **When both time and space efficiency are priorities** and stability is not needed

## 7. Counting Sort

### Algorithm Description
Counting sort is an integer sorting algorithm that works by counting the number of objects with distinct key values, then using arithmetic to determine the positions of each key in the output sequence.

### Implementation
```cpp
void countingSort(vector<int>& arr) {
    // Find the maximum element
    int max = *max_element(arr.begin(), arr.end());
    
    // Create a count array to store count of each element
    vector<int> count(max + 1, 0);
    
    // Store count of each element
    for (int i = 0; i < arr.size(); i++)
        count[arr[i]]++;
    
    // Change count[i] so that count[i] contains the position of this element in output array
    for (int i = 1; i <= max; i++)
        count[i] += count[i - 1];
    
    // Build the output array
    vector<int> output(arr.size());
    for (int i = arr.size() - 1; i >= 0; i--) {
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }
    
    // Copy the output array to arr
    for (int i = 0; i < arr.size(); i++)
        arr[i] = output[i];
}
```

### Complexity Analysis
- **Time Complexity**: O(n + k) where n is the number of elements and k is the range of input
- **Space Complexity**: O(n + k)

### Key Properties
- **Stable**: Yes (maintains relative order of equal elements)
- **Adaptive**: No (performance doesn't improve for partially sorted data)
- **In-place**: No (requires additional space)
- **Online**: No (requires entire input list)

### Use Cases
- **Integer sorting** with a limited range
- **When the range of elements (k) is not significantly larger than the number of elements (n)**
- **Radix sort**: As a subroutine
- **Arrays with many duplicate values**
- **Applications where counting frequency is already needed**

## 8. Radix Sort

### Algorithm Description
Radix sort is a non-comparative integer sorting algorithm that sorts data with integer keys by grouping keys by individual digits which share the same significant position and value.

### Implementation
```cpp
// A function to do counting sort on arr[] according to the digit at exp
void countSort(vector<int>& arr, int exp) {
    int n = arr.size();
    vector<int> output(n);
    vector<int> count(10, 0);
    
    // Store count of occurrences in count[]
    for (int i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;
    
    // Change count[i] so that count[i] contains actual
    // position of this digit in output[]
    for (int i = 1; i < 10; i++)
        count[i] += count[i - 1];
    
    // Build the output array
    for (int i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
    
    // Copy the output array to arr[]
    for (int i = 0; i < n; i++)
        arr[i] = output[i];
}

void radixSort(vector<int>& arr) {
    // Find the maximum number to know number of digits
    int max = *max_element(arr.begin(), arr.end());
    
    // Do counting sort for every digit
    for (int exp = 1; max / exp > 0; exp *= 10)
        countSort(arr, exp);
}
```

### Complexity Analysis
- **Time Complexity**: O(d * (n + k)) where d is the number of digits, n is the number of elements, and k is the range of each digit (usually 10)
- **Space Complexity**: O(n + k)

### Key Properties
- **Stable**: Yes (maintains relative order of equal elements)
- **Adaptive**: No (performance doesn't improve for partially sorted data)
- **In-place**: No (requires additional space)
- **Online**: No (requires entire input list)

### Use Cases
- **Integer or string sorting** with fixed-length keys
- **Large numbers with relatively few digits**
- **When a stable sort is required for numeric data**
- **Database sorting**: Especially for numeric fields
- **Machine-level applications** where integer keys are common

## 9. Bucket Sort

### Algorithm Description
Bucket sort divides the input into a finite number of buckets, each of which is then sorted individually, typically using another sorting algorithm or by recursively applying bucket sort.

### Implementation
```cpp
void bucketSort(vector<float>& arr) {
    int n = arr.size();
    
    // Create n empty buckets
    vector<vector<float>> buckets(n);
    
    // Put array elements into different buckets
    for (int i = 0; i < n; i++) {
        int bucketIndex = n * arr[i];
        buckets[bucketIndex].push_back(arr[i]);
    }
    
    // Sort individual buckets
    for (int i = 0; i < n; i++)
        sort(buckets[i].begin(), buckets[i].end());
    
    // Concatenate all buckets into arr[]
    int index = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < buckets[i].size(); j++)
            arr[index++] = buckets[i][j];
}
```

### Complexity Analysis
- **Time Complexity**:
  - Best case: O(n + k) where k is the number of buckets
  - Average case: O(n + n²/k + k) when elements are uniformly distributed
  - Worst case: O(n²) when all elements go into the same bucket
- **Space Complexity**: O(n + k)

### Key Properties
- **Stable**: Yes (if the underlying sort is stable)
- **Adaptive**: Partially (depends on the distribution)
- **In-place**: No (requires additional space)
- **Online**: No (requires entire input list)

### Use Cases
- **Uniformly distributed data** (e.g., values in range [0,1])
- **When input is likely to be spread across buckets evenly**
- **External sorting**: Can be modified for external memory
- **When data access patterns matter** for cache efficiency
- **Database applications**: For certain types of indexed data

## 10. Shell Sort

### Algorithm Description
Shell sort is an extension of insertion sort that allows the exchange of items that are far apart. It sorts elements at specific intervals, gradually reducing the interval to 1, at which point it becomes insertion sort.

### Implementation
```cpp
void shellSort(vector<int>& arr) {
    int n = arr.size();
    
    // Start with a big gap, then reduce the gap
    for (int gap = n/2; gap > 0; gap /= 2) {
        // Do a gapped insertion sort for this gap size
        for (int i = gap; i < n; i++) {
            // Add arr[i] to the elements that have been gap sorted
            int temp = arr[i];
            int j;
            
            // Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap)
                arr[j] = arr[j - gap];
            
            // Put temp in its correct location
            arr[j] = temp;
        }
    }
}
```

### Complexity Analysis
- **Time Complexity**:
  - Best case: O(n log n) (depends on gap sequence)
  - Average case: Depends on gap sequence
  - Worst case: O(n²) with simple gap sequences
- **Space Complexity**: O(1) (in-place)

### Key Properties
- **Stable**: No (elements may be reordered during gap inserts)
- **Adaptive**: Yes (performs better on partially sorted arrays)
- **In-place**: Yes (requires constant extra space)
- **Online**: No (requires entire input list)

### Use Cases
- **Medium-sized arrays** (faster than insertion sort, simpler than quicksort)
- **Embedded systems** where simplicity and memory usage matter
- **When a modest improvement over insertion sort is needed**
- **Systems with expensive writes** (fewer writes than quicksort)
- **As part of hybrid sorting algorithms**

## Choosing the Right Sorting Algorithm

When selecting a sorting algorithm, consider these factors:

1. **Data size**: For small datasets, simpler algorithms like insertion sort may outperform asymptotically optimal algorithms due to lower overhead.

2. **Data characteristics**:
   - Nearly sorted data: Consider insertion sort or bubble sort with early termination
   - Uniformly distributed data: Consider bucket sort
   - Limited range integers: Consider counting sort or radix sort
   - Random data: Consider quicksort or mergesort

3. **Stability requirement**: If maintaining the relative order of equal elements is important, choose a stable sort (insertion, merge, counting, radix).

4. **Memory constraints**: In-place sorts like heapsort or quicksort use less additional memory than merge sort.

5. **Worst-case guarantees**: If worst-case performance is critical, avoid quicksort in favor of heapsort or mergesort.

6. **Parallelizability**: If multi-threading is available, consider parallelizable algorithms like mergesort.

7. **External sorting**: If data doesn't fit in memory, consider merge sort or modified bucket sort.

## Exam Preparation Tips

When answering exam questions about sorting:

1. **Know the complexity bounds** for all sorting algorithms in best, average, and worst cases.

2. **Understand when each algorithm is optimal** based on input characteristics.

3. **Be prepared to trace through the steps** of common sorting algorithms (especially quicksort, heapsort, and mergesort).

4. **Identify which algorithms are stable** and which are in-place.

5. **Be able to analyze modifications** to standard algorithms (e.g., quicksort with different pivot selection strategies).

6. **Consider hybrid approaches** when asked for optimal solutions (e.g., insertion sort for small partitions in quicksort).

7. **Practice implementing key sorting algorithms** from scratch, especially partition for quicksort and heapify for heapsort.
