What is Recursion?
------------------

**Recursion** is a programming concept where a method calls itself inside its own definition. Recursion refers to the method where the solution to a problem depends on solutions to smaller instances of the same problem. 

To understand recursion, it's helpful to think of a problem that can be broken down into smaller and smaller subproblems.

When to Use Recursion
---------------------

Recursion is especially potent in scenarios where:

1.  **Natural Hierarchy Exists**: For instance, in tasks like traversing a file directory.
2.  **Problem Can Be Broken Down**: Such as sorting, where a large list can be split into smaller ones.
3.  **Solution Requires Multiple Steps**: For example, calculating factorial values or Fibonacci numbers.

The smallest problem we know how to solve in recursion is the base case.
When true, the base case stops the recursive calls and returns a value.

Recursion works best when the solution is self-similar

**Example1:** recursive implementation of a merge sort 
`
class MergeSort {
    public: 
    void merge(int arr[], int left, int mid, int right){
        Calculate sizes of the two subarrays to be merged
        int n1 = mid - left + 1; 
        int n2 = right - mid; 

        //Create temporary arrays  
        for (int i = 0; i < n1; ++i)
            leftArray[i] ==  arr[left + i];
        for (int j = 0; j < n2; ++j)
            rightArray[j] = arr[mid + 1 + j];Z
        
        //Merge the two sorted subarrays into arr[left..right]
        int i = 0, j = 0; 
        int k = left; 
        while (i < n1 && j < n2) {
            if (leftArray[i] <= rightArray[j]) {
                arr[k] = leftArray[i]; 
                i++;
            } else {
                arr[k] = rightArray[j];
                j++;
            }
            k++;
        }

        //Copy the remaining elements of leftArray, if any 
        while (i < n1) {
            arr[k] = leftArray[i];
            i++; 
            k++;
        }

        //Copy the remaining elements of rightArray, if any 
        while(j < n2 ) { 
            arr[k] = rightArray[j]; 
            j++; 
            k++; 
        }

        // Free memory allocated for temporary arrays 
        delete[] leftArray; 
        delete[] rightArray; 
    }

    // method to recursively sort the array using merge sort 
    void sort(int arr[], int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2; 
            sort(arr, left, mid); // Sort the left half
            sort(arr, mid + 1, right) // Sort the right half 
            merge(arr, left, mid, right) // Merge the sorted halves
        }
    }
}

The algorithm continually splits the array in half; left to mid is one half, while mid + 1 to right is the other half. This splitting continues until each sub-array has a single element. In an array with a length of one, left and right will have the same value, which means left is no longer less than right. These sublists are then merged together, in a recursive manner, to produce a sorted list.

//Simple recursive call to add numbers from 0 to n 

`int findSum(int n) {
    if (n == 0)
        return 0; 
    else 
        return n + findSum(n-1); 
}

