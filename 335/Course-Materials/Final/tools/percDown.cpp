#include <iostream>
#include <vector>
#include <algorithm>
//Implementation of the percolation down algorithm
// Implement percDown. In this implementation, the heap starts at index 1, the value to be placed is in index 0, and the position of the hole is passed as a parameter. You are not permitted to use a temp variable for the value, it must remain in index 0 until the hole has been moved into its final position, and only then can it be placed in the hole.

void percDown(std::vector<int>& heap, std::vector<int>::size_type hole){
    std::vector<int>::size_type child; 

    ///Each iteration moves the hole down one if required 
    // Exits loop when hole is in place. 

    for(;hole * 2 <= heap.size() - 1; hole = child ){
        child = hole * 2;
        if (child != heap.size() - 1 && heap[child + 1] < heap[child])
            ++child; 
        if (heap[child] < heap[0])
            heap[hole] = heap[child]; 
        else 
            break;
    }

    heap[hole] = heap[0];
}