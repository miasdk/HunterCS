#ifndef PRIORITY_QUEUE_H
#define PRIORITY_QUEUE_H

#include <vector>
#include <stdexcept>

template <typename Comparable>
class PriorityQueue {
public:
    // Constructors
    explicit PriorityQueue(int capacity = 100); // Default constructor with capacity
    explicit PriorityQueue(const std::vector<Comparable>& items); // Build from vector

    // Core Operations
    bool isEmpty() const;                      // Check if the queue is empty
    const Comparable& findMin() const;         // Get the minimum element
    void insert(const Comparable& x);          // Insert an element (by value)
    void insert(Comparable&& x);               // Insert an element (by move semantics)
    void deleteMin();                          // Remove the minimum element
    void deleteMin(Comparable& minItem);       // Remove the minimum and store it
    void makeEmpty();                          // Clear the priority queue

private:
    int currentSize;                           // Number of elements in the heap
    std::vector<Comparable> array;             // The heap array

    // Helper Methods
    void buildHeap();                          // Build the heap from an unordered array
    void percolateDown(int hole);              // Restore heap order by percolating down
};

#endif // PRIORITY_QUEUE_H

