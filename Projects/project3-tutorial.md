# Ranking Selection Algorithms: From Offline to Online Processing

This comprehensive tutorial explores various ranking selection algorithms, focusing on both offline and online approaches for selecting and sorting top performers from a dataset. These techniques are applicable to many real-world scenarios, from gaming leaderboards to data analysis pipelines.

## 1. Theoretical Foundations

### Offline vs. Online Algorithms

In algorithmic design, the terms "offline" and "online" refer to fundamentally different approaches to processing data:

**Offline Algorithms:**
- Have access to the entire input dataset at once
- Can make decisions with complete information
- Often more efficient for one-time processing
- Examples: sorting, partitioning, full-dataset analysis

**Online Algorithms:**
- Process data items one at a time, in sequence
- Must make decisions without seeing future inputs
- Maintain minimal state between processing steps
- Examples: streaming algorithms, real-time data processing

In the context of selection algorithms, offline approaches can examine the entire dataset to find the top k elements, while online approaches must maintain only the "best seen so far" as they process each new element.

### Heap Data Structures

A heap is a specialized tree-based data structure that satisfies the heap property:

- In a **max-heap**, for any node C, the value of C's parent is greater than or equal to C
- In a **min-heap**, for any node C, the value of C's parent is less than or equal to C

Key heap operations include:
- `make_heap`: Convert a range into a heap (O(n))
- `push_heap`: Add an element to a heap (O(log n))
- `pop_heap`: Remove the top element from a heap (O(log n))
- `sort_heap`: Sort elements of a heap (O(n log n))

The C++ STL provides these operations in the `<algorithm>` header, allowing heap operations on raw vectors without using the `priority_queue` container.

### Quickselect and Quicksort

**Quickselect** is an algorithm to find the kth smallest element in an unordered list. It's similar to quicksort but only recurses into one side of the partition:

1. Choose a pivot element
2. Partition elements around the pivot
3. If k equals the pivot position, return the pivot
4. If k is less than the pivot position, recurse on the left subarray
5. If k is greater than the pivot position, recurse on the right subarray

**Quicksort** is a divide-and-conquer sorting algorithm that:

1. Selects a pivot element
2. Partitions elements around the pivot
3. Recursively sorts both the left and right subarrays

Our hybrid approach will use quickselect until finding the partition point for the top 10%, then apply quicksort only to that portion.

### Streaming Data Processing

Streaming data processing involves:
- Processing data sequentially without storing the entire dataset
- Maintaining a fixed-size "state" that summarizes what's been seen
- Making decisions based on current input and maintained state
- Optimizing for memory efficiency and throughput

For ranking problems, this typically means maintaining a fixed-size collection of the "best k elements seen so far" and updating it as new elements arrive.

## 2. Core Algorithms Implementation

Let's dive into the algorithms implemented in this project:

### Heapsort with Early Stopping

This approach leverages heap operations to efficiently find and sort the top k elements:

1. Build a max-heap from all elements (O(n))
2. Pop only the top k elements (O(k log n))
3. Reverse the result to have ascending order

The key insight is that we don't need to fully sort the entire dataset—we only extract the top elements we care about.

### Hybrid Quickselect/Quicksort

This algorithm combines two approaches:

1. Use quickselect to find the partition point for the top 10% of elements
2. Once identified, use quicksort to sort just that portion
3. Return the sorted top elements

This is more efficient than sorting the entire dataset when we only need the top portion.

### Online Streaming Algorithm

The online approach processes elements one at a time:

1. Maintain a min-heap of size k (the reporting interval)
2. For each new element:
   - If heap size < k, add the element
   - If element > the minimum in heap, replace the minimum with this element
3. After processing all elements, sort the heap to get the final ranking
4. Periodically record the minimum level required to be in the top k

This approach never needs to store the entire dataset, making it suitable for streaming data.

## 3. Implementation Guide

Let's implement each component step by step.

### Heap-Based Selection Algorithm

```cpp
RankingResult heapRank(std::vector<Player>& players) {
    auto start = std::chrono::high_resolution_clock::now();
    
    // Calculate how many players represent the top 10%
    size_t topCount = std::floor(0.1 * players.size());
    
    // Create a vector to store the top players
    std::vector<Player> topPlayers;
    
    // If there are players to rank
    if (topCount > 0) {
        // Use a comparator that creates a max-heap based on player level
        auto comp = [](const Player& a, const Player& b) {
            return a.getLevel() < b.getLevel();
        };
        
        // Build a max-heap
        std::make_heap(players.begin(), players.end(), comp);
        
        // Extract the top 10% players
        for (size_t i = 0; i < topCount; ++i) {
            // Pop the maximum element to the end
            std::pop_heap(players.begin(), players.end() - i, comp);
            
            // Add it to our result (in reverse order since we're popping max elements)
            topPlayers.push_back(players[players.size() - 1 - i]);
        }
        
        // Reverse to get ascending order
        std::reverse(topPlayers.begin(), topPlayers.end());
    }
    
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    
    return RankingResult{topPlayers, {}, duration.count()};
}
```

### Optimized Quickselect/Quicksort Hybrid

For this implementation, we'll need helper functions for partitioning and quicksort:

```cpp
namespace Offline {
    // Partition function for quickselect/quicksort
    int partition(std::vector<Player>& players, int low, int high) {
        // Select the rightmost element as pivot
        int pivotLevel = players[high].getLevel();
        
        // Index of smaller element
        int i = low - 1;
        
        for (int j = low; j < high; j++) {
            // If current element is smaller than the pivot
            if (players[j].getLevel() < pivotLevel) {
                i++;
                std::swap(players[i], players[j]);
            }
        }
        
        // Place pivot in its correct position
        std::swap(players[i + 1], players[high]);
        return i + 1;
    }
    
    // Quicksort function to sort a specific range
    void quickSort(std::vector<Player>& players, int low, int high) {
        if (low < high) {
            int pi = partition(players, low, high);
            
            quickSort(players, low, pi - 1);
            quickSort(players, pi + 1, high);
        }
    }
    
    // Quickselect function to find the kth smallest element
    void quickSelect(std::vector<Player>& players, int low, int high, int k) {
        if (low < high) {
            int pi = partition(players, low, high);
            
            // If pivot is at k, we found our partition point
            if (pi == k) {
                return;
            }
            // If pivot > k, search in left subarray
            else if (pi > k) {
                quickSelect(players, low, pi - 1, k);
            }
            // If pivot < k, search in right subarray
            else {
                quickSelect(players, pi + 1, high, k);
            }
        }
    }

    RankingResult quickSelectRank(std::vector<Player>& players) {
        auto start = std::chrono::high_resolution_clock::now();
        
        // Calculate how many players represent the top 10%
        size_t topCount = std::floor(0.1 * players.size());
        std::vector<Player> topPlayers;
        
        if (topCount > 0) {
            // Find the position that separates the top 10% from the rest
            // (n - topCount) is the position of the first element in the top 10%
            int partitionPoint = players.size() - topCount;
            
            // Use quickselect to find the partition point
            quickSelect(players, 0, players.size() - 1, partitionPoint);
            
            // Now sort just the top 10% using quicksort
            quickSort(players, partitionPoint, players.size() - 1);
            
            // Copy the top 10% to the result vector
            topPlayers.assign(players.begin() + partitionPoint, players.end());
        }
        
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
        
        return RankingResult{topPlayers, {}, duration.count()};
    }
}
```

### Vector-Based Stream Implementation

```cpp
class VectorPlayerStream : public PlayerStream {
private:
    const std::vector<Player> players_;
    size_t currentIndex_;
    
public:
    // Constructor
    VectorPlayerStream(const std::vector<Player>& players) 
        : players_(players), currentIndex_(0) {}
    
    // Get the next player from the stream
    Player nextPlayer() override {
        if (currentIndex_ >= players_.size()) {
            throw std::runtime_error("No more players in the stream");
        }
        
        return players_[currentIndex_++];
    }
    
    // Return how many players are left in the stream
    size_t remaining() const override {
        return players_.size() - currentIndex_;
    }
};
```

### The replaceMin Helper Function

```cpp
void replaceMin(PlayerIt first, PlayerIt last, Player& target) {
    // Store the old minimum value
    Player temp = *first;
    
    // Replace the root with the new value
    *first = target;
    
    // Calculate the size of the heap
    size_t size = std::distance(first, last);
    
    // Percolate down to maintain the heap property
    size_t i = 0;  // Start at the root
    size_t child;
    
    while ((child = 2 * i + 1) < size) {
        // Compare left and right children, find the smaller one
        PlayerIt leftChild = first + child;
        PlayerIt rightChild = leftChild + 1;
        
        // If right child exists and is smaller than left child
        if (rightChild < last && rightChild->getLevel() < leftChild->getLevel()) {
            child++;  // Use right child
        }
        
        PlayerIt smallerChild = first + child;
        
        // If the replaced value is smaller than the smaller child, we're done
        if ((first + i)->getLevel() <= smallerChild->getLevel()) {
            break;
        }
        
        // Swap with the smaller child and continue down
        std::swap(*(first + i), *smallerChild);
        i = child;
    }
    
    // Store the original value in target (if needed for later use)
    target = temp;
}
```

### Stream-Based Ranking Implementation

```cpp
RankingResult streamRank(PlayerStream& stream, size_t reporting_interval) {
    auto start = std::chrono::high_resolution_clock::now();
    
    // Vector to store the top players
    std::vector<Player> topPlayers;
    
    // Map to track cutoff levels at reporting intervals
    std::map<size_t, size_t> cutoffs;
    
    // Count of players processed
    size_t playerCount = 0;
    
    // Process all players in the stream
    while (stream.remaining() > 0) {
        Player currentPlayer = stream.nextPlayer();
        playerCount++;
        
        // Case 1: We haven't filled our top players yet
        if (topPlayers.size() < reporting_interval) {
            topPlayers.push_back(currentPlayer);
            
            // If we just filled our heap to capacity, make it a min-heap
            if (topPlayers.size() == reporting_interval) {
                std::make_heap(topPlayers.begin(), topPlayers.end(), 
                               [](const Player& a, const Player& b) {
                                   return a.getLevel() > b.getLevel();
                               });
                               
                // Record the cutoff level at this reporting interval
                cutoffs[playerCount] = topPlayers.front().getLevel();
            }
        } 
        // Case 2: We have a full heap, check if this player should replace minimum
        else {
            // If new player is better than the minimum in our heap
            if (currentPlayer.getLevel() > topPlayers.front().getLevel()) {
                // Replace the minimum element with the new player
                replaceMin(topPlayers.begin(), topPlayers.end(), currentPlayer);
                
                // If we've reached a reporting interval, record the cutoff
                if (playerCount % reporting_interval == 0) {
                    cutoffs[playerCount] = topPlayers.front().getLevel();
                }
            }
            // Otherwise, if we've reached a reporting interval, record the existing cutoff
            else if (playerCount % reporting_interval == 0) {
                cutoffs[playerCount] = topPlayers.front().getLevel();
            }
        }
    }
    
    // Always record the final cutoff, even if not a multiple of reporting_interval
    if (topPlayers.size() == reporting_interval && 
        playerCount % reporting_interval != 0) {
        cutoffs[playerCount] = topPlayers.front().getLevel();
    }
    
    // Sort the top players by level (ascending)
    std::sort(topPlayers.begin(), topPlayers.end(), 
              [](const Player& a, const Player& b) {
                  return a.getLevel() < b.getLevel();
              });
    
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    
    return RankingResult{topPlayers, cutoffs, duration.count()};
}
```

## 4. API-Based Streaming Implementation

For the extra credit portion, here's how to implement the API-based streaming solution:

```cpp
class APIPlayerStream : public PlayerStream {
private:
    const size_t expected_length_;
    size_t cursor_;
    size_t seed_;
    const size_t batch_size_;
    size_t players_read_;
    std::vector<Player> current_batch_;
    size_t batch_index_;
    
protected:
    const std::string PORT = "5000";
    const std::string HOSTNAME = "http://127.0.0.1";
    const std::string SOCKET = HOSTNAME + ":" + PORT;
    
public:
    APIPlayerStream(const size_t& expected_length, const size_t& seed, 
                   const size_t& batch_size)
        : expected_length_(expected_length), 
          cursor_(1),  // Start at cursor 1
          seed_(seed), 
          batch_size_(batch_size),
          players_read_(0),
          current_batch_(),
          batch_index_(0) {}
    
    Player nextPlayer() override {
        // If we've read all expected players
        if (players_read_ >= expected_length_) {
            throw std::runtime_error("No more players in the stream");
        }
        
        // If we need to fetch a new batch
        if (batch_index_ >= current_batch_.size()) {
            fetchBatch();
            batch_index_ = 0;
        }
        
        // Get player from current batch
        Player player = current_batch_[batch_index_++];
        players_read_++;
        
        return player;
    }
    
    size_t remaining() const override {
        return expected_length_ - players_read_;
    }
    
private:
    void fetchBatch() {
        // Construct the API URL
        std::string url = SOCKET + "/api?seed=" + std::to_string(seed_) +
                         "&cursor=" + std::to_string(cursor_) +
                         "&batch=" + std::to_string(batch_size_);
                         
        // Make the API request
        cpr::Response response = cpr::Get(cpr::Url{url});
        
        // Check if request was successful
        if (response.status_code != 200) {
            throw std::runtime_error("API request failed: " + response.text);
        }
        
        // Parse the JSON response
        auto json_response = nlohmann::json::parse(response.text);
        
        // Extract the new cursor
        cursor_ = json_response["cursor"].template get<size_t>();
        
        // Extract player levels
        auto levels = json_response["levels"].template get<std::vector<size_t>>();
        
        // Create Player objects
        current_batch_.clear();
        for (size_t i = 0; i < levels.size(); ++i) {
            // Generate a player name (can be anything)
            std::string name = "Player" + std::to_string(players_read_ + i + 1);
            current_batch_.emplace_back(name, levels[i]);
        }
    }
};
```

## 5. Algorithm Visualization

### Heap-Based Selection Algorithm

Let's visualize the heap selection algorithm with a step-by-step example:

1. **Initial Array**: [Player("A", 5), Player("B", 9), Player("C", 1), Player("D", 7), Player("E", 3)]

2. **Build Max-Heap**:
   ```
        9(B)
       /    \
     7(D)    5(A)
    /  \
   3(E) 1(C)
   ```

3. **Extract Top 2 Elements (20%)**:
   - Pop 9(B) → Array becomes [7(D), 3(E), 5(A), 1(C), 9(B)]
   - Pop 7(D) → Array becomes [5(A), 3(E), 1(C), 7(D), 9(B)]

4. **Result (ascending)**: [7(D), 9(B)]

### Hybrid Quickselect/Quicksort

Let's visualize the quickselect/quicksort hybrid with a step-by-step example:

1. **Initial Array**: [5, 2, 9, 1, 7, 6, 3, 8, 4]

2. **Quickselect to find partition for top 30% (3 elements)**:
   - Choose pivot: 4
   - After partitioning: [2, 1, 3, **4**, 7, 6, 9, 8, 5]
   - We need position 6 for top 30%
   - Recurse on right side: [7, 6, 9, 8, 5]
   - Choose pivot: 5
   - After partitioning: [**5**, 6, 9, 8, 7]
   - Found partition point

3. **Quicksort the top 30%**: [5, 6, 7, 8, 9]

4. **Result**: [7, 8, 9]

### Online Processing with Fixed Memory

Let's visualize the online algorithm with a step-by-step example:

1. **Initial Min-Heap (size 3)**: [Empty]

2. **Stream Input**: 5, 2, 9, 1, 7, 6, 3, 8, 4

3. **Process Stream**:
   - Read 5: Heap = [5]
   - Read 2: Heap = [2, 5]
   - Read 9: Heap = [2, 5, 9]
   - Make min-heap: [2, 5, 9]
   - Read 1: 1 < 2 (min), ignore
   - Read 7: 7 > 2 (min), replace: [5, 7, 9]
   - Read 6: 6 > 5 (min), replace: [6, 7, 9]
   - Read 3: 3 < 6 (min), ignore
   - Read 8: 8 > 6 (min), replace: [7, 8, 9]
   - Read 4: 4 < 7 (min), ignore

4. **Final Top 3 (sorted)**: [7, 8, 9]

### Batch Processing in API-Based Streaming

1. **Initialize**: Expected length = 10, Batch size = 3
2. **First API Call**: /api?seed=42&cursor=1&batch=3
   - Response: { "cursor": 4, "levels": [10, 5, 8] }
   - Current batch: [Player1(10), Player2(5), Player3(8)]
3. **Process Batch**: Return players one by one
4. **Second API Call**: /api?seed=42&cursor=4&batch=3
   - Response: { "cursor": 7, "levels": [12, 3, 9] }
   - Current batch: [Player4(12), Player5(3), Player6(9)]
5. **Continue** until expected_length players processed

## 6. Complexity Analysis and Applications

### Time and Space Complexity

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|-----------------|
| HeapRank  | O(n + k log n) | O(k) additional |
| QuickSelectRank | O(n + k log k) average | O(log n) recursive |
| StreamRank | O(n log k) | O(k) |
| APIStreamRank | O(n log k) | O(k + batch_size) |

Where:
- n = number of elements
- k = size of the result set (top 10%)

### Trade-offs Between Approaches

**Offline Approaches:**
- **Advantages**: Process entire dataset once, potentially more efficient for one-time analysis
- **Disadvantages**: Require entire dataset in memory, not suitable for streaming data

**Online Approaches:**
- **Advantages**: Constant memory usage, work with streaming data, can produce incremental results
- **Disadvantages**: May be less efficient for one-time processing of fixed datasets

### Real-World Applications

These algorithms have applications beyond gaming leaderboards:

1. **Financial Systems**: Identifying top-performing assets in real-time trading
2. **Social Media**: Trending content aggregation and recommendation
3. **Anomaly Detection**: Identifying outliers in data streams
4. **Search Engines**: Top-k query processing
5. **Recommendation Systems**: Finding the most relevant items for users
6. **Load Balancing**: Distributing work to the least busy servers
7. **Sensor Networks**: Identifying significant readings from distributed sensors

### Advanced Variations

For distributed and big data systems:

1. **Distributed Top-K**: Using map-reduce paradigms to find top elements across shards
2. **Probabilistic Methods**: Approximate top-k with sketching algorithms
3. **Sliding Window Models**: Finding top-k elements in recent time windows
4. **Parallelized Implementations**: Leveraging multiple cores for faster processing
5. **Incremental Maintenance**: Efficiently updating results as data changes

## 7. Conclusion

Ranking selection algorithms are foundational techniques with wide-ranging applications. By understanding both offline approaches (like heapsort and quickselect) and online methods (like stream processing), you can choose the appropriate solution based on your specific constraints and requirements.

The key insights from this tutorial:

1. Offline algorithms like heap-based selection and quickselect are efficient for one-time processing of complete datasets
2. Online algorithms provide memory-efficient solutions for streaming data
3. Careful implementation of core operations like replaceMin can greatly improve performance
4. API-based streaming adds complexity but enables real-time processing of remote data sources

With these techniques, you can build efficient ranking systems for applications ranging from game leaderboards to large-scale data analytics platforms.
