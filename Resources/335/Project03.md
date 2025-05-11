# Project 3: Ranking Algorithms
## Implementation Guide & Learning Resource

This guide follows the exact sequence of tasks from the project description, providing both implementation steps and educational context for each component.

## Table of Contents
- [Overview](#overview)
- [Task 1: Offline Algorithms](#task-1-offline-algorithms)
  - [Part A: Stop Heaping Around (heapRank)](#part-a-stop-heaping-around-heaprank)
  - [Part B: Quicktime Events (quickSelectRank)](#part-b-quicktime-events-quickselectrank)
- [Task 2: Going Online](#task-2-going-online)
  - [Part A: "Live" Streaming (VectorPlayerStream)](#part-a-live-streaming-vectorplayerstream)
  - [Part B: replaceMin Implementation](#part-b-replacemin-implementation)
  - [Part C: rankIncoming Implementation](#part-c-rankincoming-implementation)
- [Extra Credit: API Integration](#extra-credit-api-integration)
- [Building and Testing](#building-and-testing)
- [Key Concepts & References](#key-concepts--references)

## Overview

This project focuses on implementing algorithms to select and sort the top 10% of players by level using different approaches:

1. **Offline algorithms** that process all data at once:
   - Heap-based selection and sorting
   - Quickselect/Quicksort hybrid

2. **Online algorithm** that processes data sequentially:
   - Stream-based processing with continuous updating
   - Maintaining a "leaderboard" of top players

Each approach highlights different algorithm design principles, data structures, and efficiency considerations.

## Task 1: Offline Algorithms

### Part A: Stop Heaping Around (heapRank)

**Concept: Heap-based Selection**

A heap is a specialized tree-based data structure that satisfies the heap property: in a max-heap, for any node C, if P is a parent node of C, then the value of P is greater than or equal to the value of C. This property makes heaps excellent for priority queues and selection tasks.

**Implementation Steps:**

1. Add necessary includes to Leaderboard.cpp:
```cpp
#include <algorithm>  // For heap operations
#include <chrono>     // For timing
#include <cmath>      // For floor function
```

2. Implement heapRank function:
```cpp
namespace Offline {

RankingResult heapRank(std::vector<Player>& players) {
    // Start timing
    auto start = std::chrono::high_resolution_clock::now();
    
    // Calculate how many players represent the top 10%
    size_t topCount = std::floor(0.1 * players.size());
    
    // Create a max-heap using the entire vector
    // Note: We use a lambda to specify max-heap behavior
    std::make_heap(players.begin(), players.end(), 
                  [](const Player& a, const Player& b) { return a.level_ < b.level_; });
    
    // Extract top elements one by one
    std::vector<Player> topPlayers;
    for (size_t i = 0; i < topCount; ++i) {
        // Move max element to the end and restore heap property for the rest
        std::pop_heap(players.begin(), players.end() - i, 
                     [](const Player& a, const Player& b) { return a.level_ < b.level_; });
        
        // Add extracted player to our result
        topPlayers.push_back(players[players.size() - 1 - i]);
    }
    
    // Sort the result in ascending order
    std::sort(topPlayers.begin(), topPlayers.end(), 
             [](const Player& a, const Player& b) { return a.level_ < b.level_; });
    
    // End timing and calculate elapsed time
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> elapsed = end - start;
    
    // Return the result object with empty cutoffs (only used for online algorithm)
    return {topPlayers, {}, elapsed.count()};
}

} // namespace Offline
```

**Learning Notes:**
- **STL Heap Operations**: The C++ STL provides four main heap operations:
  - `std::make_heap`: Converts a range to a heap in linear time O(n)
  - `std::push_heap`: Adds an element to a heap in logarithmic time O(log n)
  - `std::pop_heap`: Removes the largest element in logarithmic time O(log n)
  - `std::sort_heap`: Sorts elements of a heap in linearithmic time O(n log n)

- **In-place Algorithm**: This implementation modifies the input vector directly (in-place) with only O(1) extra memory, besides the required result vector.

- **Memory Efficiency**: Using raw heap operations on vectors is more memory-efficient than using a priority_queue, since we avoid creating a separate container.

**References:**
- [C++ make_heap](https://en.cppreference.com/w/cpp/algorithm/make_heap)
- [C++ pop_heap](https://en.cppreference.com/w/cpp/algorithm/pop_heap)
- [Heap Data Structure](https://www.geeksforgeeks.org/heap-data-structure/)

### Part B: Quicktime Events (quickSelectRank)

**Concept: Quickselect & Quicksort Hybrid**

Quickselect is a selection algorithm to find the kth smallest element in an unordered list. It's related to quicksort, with the key difference being that quickselect only recursively processes one side of the partition (the side containing the kth element), while quicksort processes both sides.

**Implementation Steps:**

1. Add helper function prototypes in Leaderboard.hpp (within the Offline namespace):
```cpp
// Helper function prototypes for quickSelectRank
int partition(std::vector<Player>& players, int left, int right);
void quickSelect(std::vector<Player>& players, int left, int right, int k);
void quickSort(std::vector<Player>& players, int left, int right);
```

2. Implement helper functions and quickSelectRank in Leaderboard.cpp:
```cpp
namespace Offline {

// Helper function: Partition array around pivot
int partition(std::vector<Player>& players, int left, int right) {
    // Choose rightmost element as pivot
    Player pivot = players[right];
    int i = left - 1;
    
    // Move all elements <= pivot to the left side
    for (int j = left; j < right; j++) {
        if (players[j].level_ <= pivot.level_) {
            i++;
            std::swap(players[i], players[j]);
        }
    }
    
    // Place pivot in its final sorted position
    std::swap(players[i + 1], players[right]);
    return i + 1;  // Return pivot's index
}

// Helper function: Find kth element using quickselect
void quickSelect(std::vector<Player>& players, int left, int right, int k) {
    if (left >= right) return;
    
    // Partition and get pivot index
    int pivotIndex = partition(players, left, right);
    
    if (pivotIndex == k) {
        // Found the kth element, we're done
        return;
    } else if (pivotIndex > k) {
        // k is in left subarray - only recurse on left side
        quickSelect(players, left, pivotIndex - 1, k);
    } else {
        // k is in right subarray - only recurse on right side
        quickSelect(players, pivotIndex + 1, right, k);
    }
}

// Helper function: Sort using quicksort
void quickSort(std::vector<Player>& players, int left, int right) {
    if (left >= right) return;
    
    // Partition array and get pivot index
    int pivotIndex = partition(players, left, right);
    
    // Recursively sort both sides
    quickSort(players, left, pivotIndex - 1);
    quickSort(players, pivotIndex + 1, right);
}

// Main function: quickSelectRank
RankingResult quickSelectRank(std::vector<Player>& players) {
    // Start timing
    auto start = std::chrono::high_resolution_clock::now();
    
    size_t n = players.size();
    size_t topCount = std::floor(0.1 * n);
    int cutoffIndex = n - topCount;  // Index where top 10% begins
    
    // First use quickselect to place the pivot at the cutoff position
    // This partitions the array so all elements > cutoff are on the right
    quickSelect(players, 0, n - 1, cutoffIndex);
    
    // Then use quicksort to sort just the top 10%
    quickSort(players, cutoffIndex, n - 1);
    
    // Extract the top 10% (now sorted) into result vector
    std::vector<Player> topPlayers(players.begin() + cutoffIndex, players.end());
    
    // End timing and calculate elapsed time
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> elapsed = end - start;
    
    return {topPlayers, {}, elapsed.count()};
}

} // namespace Offline
```

**Learning Notes:**
- **Quickselect Efficiency**: Quickselect has an average time complexity of O(n), while sorting would require O(n log n). This is because quickselect only needs to recurse into one partition (the one containing our target), while quicksort recurses into both.

- **Hybrid Approach**: This implementation is a hybrid that uses:
  1. Quickselect to efficiently partition the array so the top 10% elements are on one side
  2. Quicksort to sort only those top 10% elements

- **Memory Usage**: The implementation uses O(log n) memory due to the recursive calls on the stack. This is still very efficient compared to approaches that would create copies of the data.

- **Pivot Selection**: This implementation uses the rightmost element as pivot. Advanced implementations might use median-of-three or randomized pivot selection to avoid worst-case scenarios.

**References:**
- [Quickselect Algorithm](https://en.wikipedia.org/wiki/Quickselect)
- [Quicksort Algorithm](https://en.wikipedia.org/wiki/Quicksort)
- [Median of Medians Algorithm](https://en.wikipedia.org/wiki/Median_of_medians) (advanced pivot selection)

## Task 2: Going Online

### Part A: "Live" Streaming (VectorPlayerStream)

**Concept: Stream Processing**

Stream processing involves handling data sequentially, one item at a time, rather than having the entire dataset available at once. This models real-world scenarios like processing a live data feed or working with datasets too large to fit in memory.

**Implementation Steps:**

1. Add private members to VectorPlayerStream class in PlayerStream.hpp:
```cpp
private:
    const std::vector<Player>& players_;  // Reference to source vector
    size_t currentIndex_;                 // Current position in the stream
```

2. Create PlayerStream.cpp file and implement VectorPlayerStream:
```cpp
#include "PlayerStream.hpp"

// Constructor: Initialize stream with reference to vector and set index to 0
VectorPlayerStream::VectorPlayerStream(const std::vector<Player>& players)
    : players_(players), currentIndex_(0) {}

// Get next player from the stream, advancing position
Player VectorPlayerStream::nextPlayer() {
    // Throw exception if trying to read past the end
    if (currentIndex_ >= players_.size()) {
        throw std::runtime_error("No more players in the stream");
    }
    
    // Return current player and advance index
    return players_[currentIndex_++];
}

// Check how many players remain in the stream
size_t VectorPlayerStream::remaining() const {
    return players_.size() - currentIndex_;
}
```

**Learning Notes:**
- **Stream Interface**: The PlayerStream abstract base class defines an interface for streaming data, providing a consistent way to access sequential data regardless of the source.

- **Exception Handling**: The implementation throws an exception when attempting to read past the end of the stream, providing clear error reporting.

- **Efficient Implementation**: Using a reference to the vector avoids copying the data, keeping the stream operation memory-efficient.

- **Iterator Pattern**: This is a simplified implementation of the Iterator design pattern, which provides a way to access elements of a collection sequentially without exposing the underlying representation.

**References:**
- [Iterator Design Pattern](https://refactoring.guru/design-patterns/iterator)
- [C++ Streams](https://en.cppreference.com/w/cpp/io/basic_istream)
- [Exception Handling in C++](https://en.cppreference.com/w/cpp/language/exceptions)

### Part B: replaceMin Implementation

**Concept: Min-Heap Maintenance**

This function implements a specialized heap operation that replaces the root of a min-heap with a new element and then restores the heap property. It's essential for maintaining a fixed-size collection of the highest-valued elements in a stream.

**Implementation Steps:**

Implement replaceMin in the Online namespace in Leaderboard.cpp:
```cpp
namespace Online {

void replaceMin(PlayerIt first, PlayerIt last, Player& target) {
    // Replace the root (minimum element) with the target
    *first = std::move(target);
    
    // Percolate down to restore heap property
    size_t size = std::distance(first, last);
    size_t current = 0;  // Root index
    size_t child;
    
    // While there's at least a left child
    while ((child = 2 * current + 1) < size) {
        // If there's a right child and it's smaller than left child
        if (child + 1 < size && (first + child)->level_ > (first + child + 1)->level_) {
            ++child;  // Use the right child
        }
        
        // If the element is already in the right position, we're done
        if ((first + current)->level_ <= (first + child)->level_) {
            break;
        }
        
        // Otherwise, swap with the smallest child and continue
        std::iter_swap(first + current, first + child);
        current = child;
    }
}

} // namespace Online
```

**Learning Notes:**
- **Percolate Down Operation**: This is a key operation for maintaining the heap property. When the root value changes, we need to "bubble down" the new value until it reaches its correct position.

- **Iterator-Based Implementation**: This function works with iterators rather than direct array indices, making it more flexible and compatible with any STL container.

- **Move Semantics**: Using `std::move` can improve performance by avoiding unnecessary copying of the Player object.

- **Binary Heap Node Indexing**: In a binary heap represented as an array:
  - For a node at index i:
  - Left child is at index 2i + 1
  - Right child is at index 2i + 2
  - Parent is at index (i-1)/2 (integer division)

**References:**
- [Binary Heap](https://en.wikipedia.org/wiki/Binary_heap)
- [C++ Iterators](https://en.cppreference.com/w/cpp/iterator)
- [Move Semantics](https://en.cppreference.com/w/cpp/language/move_constructor)

### Part C: rankIncoming Implementation

**Concept: Online Selection Algorithm**

This is the main online algorithm that processes a stream of players one at a time, maintaining a collection of the top players seen so far and recording level cutoffs at specified intervals.

**Implementation Steps:**

Implement rankIncoming in the Online namespace in Leaderboard.cpp:
```cpp
namespace Online {

RankingResult rankIncoming(PlayerStream& stream, const size_t& reporting_interval) {
    // Start timing
    auto start = std::chrono::high_resolution_clock::now();
    
    std::vector<Player> topPlayers;
    std::unordered_map<size_t, size_t> cutoffs;
    size_t processedCount = 0;
    
    // Process stream until no players remain
    while (stream.remaining() > 0) {
        Player currentPlayer = stream.nextPlayer();
        processedCount++;
        
        // Case 1: Haven't filled our heap to capacity yet
        if (topPlayers.size() < reporting_interval) {
            topPlayers.push_back(currentPlayer);
            
            // If we just completed our initial heap, make it a min-heap
            if (topPlayers.size() == reporting_interval) {
                std::make_heap(topPlayers.begin(), topPlayers.end(),
                              [](const Player& a, const Player& b) { return a.level_ > b.level_; });
                
                // Record cutoff at this milestone
                cutoffs[processedCount] = topPlayers.front().level_;
            }
        }
        // Case 2: Player level is higher than current minimum in the heap
        else if (currentPlayer.level_ > topPlayers.front().level_) {
            // Replace the minimum in the heap with this player
            replaceMin(topPlayers.begin(), topPlayers.end(), currentPlayer);
            
            // Record cutoff at reporting intervals
            if (processedCount % reporting_interval == 0) {
                cutoffs[processedCount] = topPlayers.front().level_;
            }
        }
        // Case 3: Player level is lower, but we still need to record cutoffs
        else if (processedCount % reporting_interval == 0) {
            cutoffs[processedCount] = topPlayers.front().level_;
        }
    }
    
    // Record final cutoff if not already recorded and if we processed any players
    if (processedCount > 0 && cutoffs.find(processedCount) == cutoffs.end()) {
        cutoffs[processedCount] = topPlayers.front().level_;
    }
    
    // Sort the top players for the final result (ascending order by level)
    std::sort(topPlayers.begin(), topPlayers.end(),
             [](const Player& a, const Player& b) { return a.level_ < b.level_; });
    
    // End timing and calculate elapsed time
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> elapsed = end - start;
    
    return {topPlayers, cutoffs, elapsed.count()};
}

} // namespace Online
```

**Learning Notes:**
- **Online Algorithm Characteristics**: This algorithm handles each element once, without requiring the entire dataset at once. Key features:
  1. Processes data sequentially
  2. Makes decisions immediately for each element
  3. Cannot revise earlier decisions
  4. Uses bounded memory regardless of input size

- **Fixed-Size Min-Heap**: We maintain a min-heap of size reporting_interval, where:
  - The minimum element is always at the root (front of vector)
  - New higher-level players replace the minimum
  - The heap always contains the highest-level players seen so far

- **Cutoff Recording**: The algorithm records the minimum level needed to be in the top players at specified intervals, creating a history of how the leaderboard evolved over time.

- **Time Complexity**: O(n log k) where n is the number of players in the stream and k is the reporting interval. Each of the n players takes at most O(log k) time to process.

**References:**
- [Online Algorithms](https://en.wikipedia.org/wiki/Online_algorithm)
- [Streaming Algorithms](https://www.cs.dartmouth.edu/~ac/Teach/data-streams-lecnotes.pdf)
- [Priority Queues](https://en.wikipedia.org/wiki/Priority_queue)

## Extra Credit: API Integration

**Concept: Real-Time Data Fetching**

This extends the online algorithm concept to handle real-time data from a web API, demonstrating how ranking algorithms can work with external data sources.

**Implementation Steps:**

1. Enable API in PlayerStream.hpp:
```cpp
// Uncomment for extra credit
#define API_ENABLED
```

2. Add private members to APIPlayerStream in PlayerStream.hpp:
```cpp
private:
    size_t cursor_, seed_;         // API request parameters
    size_t expected_length_;       // Total expected players
    size_t batch_size_;            // How many players to fetch per request
    std::vector<Player> current_batch_; // Currently fetched batch
    size_t batch_index_;           // Current position in batch
    size_t players_retrieved_;     // Total players retrieved so far
```

3. Implement APIPlayerStream in PlayerStream.cpp:
```cpp
#ifdef API_ENABLED

APIPlayerStream::APIPlayerStream(const size_t& expected_length, const size_t& seed, const size_t& batch_size)
    : cursor_(1), seed_(seed), expected_length_(expected_length), 
      batch_size_(batch_size), current_batch_(), batch_index_(0), players_retrieved_(0) {
    // Initialize with an empty batch
}

Player APIPlayerStream::nextPlayer() {
    // If we've exhausted current batch or have no batch yet, fetch a new one
    if (batch_index_ >= current_batch_.size()) {
        try {
            // Construct API URL with query parameters
            std::string url = SOCKET + "/api?seed=" + std::to_string(seed_) + 
                             "&cursor=" + std::to_string(cursor_) + 
                             "&batch=" + std::to_string(batch_size_);
            
            // Make API request
            cpr::Response response = cpr::Get(cpr::Url{url});
            
            // Check if request was successful
            if (response.status_code != 200) {
                throw std::runtime_error("API request failed with status code: " + 
                                        std::to_string(response.status_code));
            }
            
            // Parse JSON response
            auto json_response = nlohmann::json::parse(response.text);
            
            // Update cursor for next request
            cursor_ = json_response["cursor"].template get<size_t>();
            
            // Get levels from response
            auto levels = json_response["levels"].template get<std::vector<size_t>>();
            
            // Create Player objects from the levels
            current_batch_.clear();
            for (const auto& level : levels) {
                // Use a generic name with index for simplicity
                current_batch_.push_back(Player("Player" + std::to_string(players_retrieved_ + current_batch_.size()), level));
            }
            
            // Reset batch index
            batch_index_ = 0;
            
        } catch (const std::exception& e) {
            throw std::runtime_error(std::string("Failed to fetch new batch: ") + e.what());
        }
    }
    
    // If we still have no players after trying to fetch, we're done
    if (current_batch_.empty()) {
        throw std::runtime_error("No more players available in the stream");
    }
    
    // Return the next player and increment counters
    Player next_player = current_batch_[batch_index_++];
    players_retrieved_++;
    
    return next_player;
}

size_t APIPlayerStream::remaining() const {
    return expected_length_ - players_retrieved_;
}

#endif
```

**Learning Notes:**
- **Batch Processing**: Fetching data in batches is much more efficient than making an API call for each individual player.

- **Lazy Loading**: The implementation only fetches new data when needed, conserving resources.

- **HTTP Communication**: The cpr library simplifies making HTTP requests in C++.

- **JSON Parsing**: The nlohmann/json library provides tools for parsing and working with JSON data.

- **Error Handling**: Robust error handling is essential when working with external APIs that may fail.

- **Real-World Applications**: This pattern is common in applications like leaderboards, recommendation systems, and analytics dashboards that work with live data.

**References:**
- [C++ Requests (cpr)](https://github.com/libcpr/cpr)
- [JSON for Modern C++](https://github.com/nlohmann/json)
- [REST API Design Best Practices](https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design)
- [Pagination Patterns for APIs](https://developer.atlassian.com/server/confluence/pagination-in-the-rest-api/)

## Building and Testing

### Basic Build
```bash
make
```

### Extra Credit Build with CMake
```bash
cmake .
make
```

Or with Ninja (faster):
```bash
cmake -G Ninja -S . -B build
cd build
ninja
```

### Running the Sample Server (for Extra Credit)
```bash
pip install uv
uv venv
.\.venv\Scripts\Activate  # Or appropriate activation command for your OS
uv sync
python server.py
```

## Key Concepts & References

### 1. Algorithm Paradigms
- **Offline vs. Online Algorithms**: [Introduction to Online Algorithms](https://en.wikipedia.org/wiki/Online_algorithm)
- **Divide and Conquer**: [Divide and Conquer Algorithms](https://www.geeksforgeeks.org/divide-and-conquer-algorithm-introduction/)

### 2. Data Structures
- **Heaps**: [Binary Heap](https://en.wikipedia.org/wiki/Binary_heap)
- **Min-Heap vs. Max-Heap**: [Heap Data Structure](https://www.geeksforgeeks.org/heap-data-structure/)

### 3. Selection & Sorting
- **Quickselect**: [Quickselect Algorithm](https://en.wikipedia.org/wiki/Quickselect)
- **Quicksort**: [Quicksort Algorithm](https://en.wikipedia.org/wiki/Quicksort)
- **Heapsort**: [Heapsort Algorithm](https://en.wikipedia.org/wiki/Heapsort)

### 4. C++ Features
- **STL Algorithms**: [C++ STL Algorithms](https://en.cppreference.com/w/cpp/algorithm)
- **Iterators**: [C++ Iterators](https://en.cppreference.com/w/cpp/iterator)
- **Lambda Expressions**: [C++ Lambda Expressions](https://en.cppreference.com/w/cpp/language/lambda)
- **Move Semantics**: [Move Semantics in C++](https://en.cppreference.com/w/cpp/language/move_constructor)

### 5. Streaming & API Integration
- **Stream Processing**: [Data Stream Processing](https://en.wikipedia.org/wiki/Stream_processing)
- **HTTP Client in C++**: [C++ Requests Library](https://github.com/libcpr/cpr)
- **JSON Parsing**: [JSON for Modern C++](https://github.com/nlohmann/json)

---

This guide walks through implementing each component of the ranking algorithms project while providing educational context and references. By understanding both the practical implementation steps and the underlying concepts, you'll develop a comprehensive mastery of these important algorithms and data structures.
