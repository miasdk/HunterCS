# Comprehensive Heap Problems Collection

This collection contains original and adapted problems designed specifically to help you master heap data structures through progressive learning and practice.

## Table of Contents
1. [Foundational Heap Problems](#foundational-heap-problems)
2. [Application-Based Problems](#application-based-problems)
3. [Advanced Heap Problems](#advanced-heap-problems)
4. [Algorithmic Challenges](#algorithmic-challenges)
5. [Real-World Scenarios](#real-world-scenarios)

---

## Foundational Heap Problems

### Problem 1: Heap Implementation from Scratch

**Task**: Implement a binary max heap from scratch that supports the following operations:
- `insert(val)`: Insert a value into the heap
- `extractMax()`: Remove and return the maximum element
- `peek()`: Return the maximum element without removing it
- `heapify(array)`: Convert an array into a valid max heap

**Input/Output Example**:
```
Operations:
1. heapify([3, 1, 6, 5, 2, 4])
2. peek()
3. insert(10)
4. peek()
5. extractMax()
6. peek()

Expected Output:
1. [6, 5, 4, 3, 2, 1] (implementation detail, result may vary but must be a valid max heap)
2. 6
3. (no output)
4. 10
5. 10
6. 6
```

**Learning Focus**: Understanding the core heap operations and array representation of a heap.

---

### Problem 2: Convert Max Heap to Min Heap

**Task**: Given an array representing a max heap, convert it to a min heap with O(n) time complexity.

**Input/Output Example**:
```
Input: [9, 4, 7, 1, 2, 6, 3]
Output: [1, 2, 3, 4, 9, 6, 7] (implementation detail, result may vary but must be a valid min heap)
```

**Hint**: You can build a min heap bottom-up, starting from the last non-leaf node.

**Learning Focus**: Understanding heap property and the efficient way to construct heaps.

---

### Problem 3: Is This a Binary Heap?

**Task**: Write a function that checks if a given array represents a valid binary max heap.

**Input/Output Example**:
```
Input 1: [90, 15, 10, 7, 12, 2]
Output 1: true

Input 2: [9, 15, 10, 7, 12, 2]
Output 2: false (15 is greater than its parent 9)
```

**Learning Focus**: Understanding heap property verification and parent-child relationships in a heap.

---

### Problem 4: Find the Kth Smallest Element

**Task**: Implement a function to find the kth smallest element in an array using a heap. Try to use both max heap and min heap approaches, and compare which is more efficient.

**Input/Output Example**:
```
Input: [7, 10, 4, 3, 20, 15], k = 3
Output: 7
```

**Learning Focus**: Learning different approaches to solve selection problems using heaps.

---

## Application-Based Problems

### Problem 5: Running Median

**Task**: Design a data structure that can efficiently insert integers and find the median of all inserted values at any time.

**Input/Output Example**:
```
Operations:
1. insert(5)
2. insert(3)
3. getMedian() // Should return 4
4. insert(8)
5. getMedian() // Should return 5
6. insert(4)
7. getMedian() // Should return 4.5
```

**Hint**: Use two heaps - a max heap for the first half of the sorted data and a min heap for the second half.

**Learning Focus**: Using multiple heaps in tandem to solve complex problems.

---

### Problem 6: Task Scheduler

**Task**: Given a list of tasks represented by characters and a cooldown period 'n', find the minimum time needed to execute all tasks. The same task cannot be executed again until a cooldown period has passed.

**Input/Output Example**:
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B
```

**Learning Focus**: Using heap for greedy scheduling problems.

---

### Problem 7: Stream of Numbers

**Task**: Design a data structure that can efficiently handle a stream of numbers with the following operations:
- `add(num)`: Add a number to the stream.
- `getTop(k)`: Return the top k largest numbers seen so far.
- `getFrequent(k)`: Return the k most frequent numbers seen so far.

**Input/Output Example**:
```
Operations:
1. add(4)
2. add(1)
3. add(3)
4. add(4)
5. getTop(2) // Should return [4, 3]
6. getFrequent(1) // Should return [4]
7. add(2)
8. getTop(3) // Should return [4, 3, 2]
```

**Learning Focus**: Maintaining multiple heaps with specific properties over a stream of data.

---

### Problem 8: Merge K Sorted Files

**Task**: You have k sorted files, each containing a large number of integers. Write a function that efficiently merges these files into one sorted file.

**Input/Output Example**:
```
Input:
File 1: [1, 5, 7, 9]
File 2: [2, 4, 6, 8]
File 3: [0, 3, 10, 12]

Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
```

**Hint**: Use a min heap to efficiently track the smallest available value from each file.

**Learning Focus**: Using heap for external sorting and merge operations.

---

## Advanced Heap Problems

### Problem 9: Dynamic Median Path

**Task**: Given a binary tree, find the path from root to a leaf where the median of the values along the path is maximized.

**Input/Output Example**:
```
Input: 
        5
       / \
      3   8
     / \   \
    1   4   10
   /
  2

Output: [5, 8, 10]
Explanation: Path [5, 8, 10] has median 8, which is higher than any other path.
```

**Hint**: You'll need to track medians efficiently for each path exploration.

**Learning Focus**: Combining heap operations with tree traversal.

---

### Problem 10: Merge K Linked Lists with Constraints

**Task**: Merge k sorted linked lists with the additional constraint that lists with smaller average values should contribute more elements to the beginning of the merged list when possible.

**Input/Output Example**:
```
Input:
List 1: 1->5->9
List 2: 2->4->6
List 3: 3->7->8

Output: 1->2->3->4->5->6->7->8->9
```

**Learning Focus**: Using heaps with custom priority metrics.

---

### Problem 11: Online Percentile Tracker

**Task**: Design a data structure that can efficiently track the pth percentile of a stream of integers in real-time.

**Input/Output Example**:
```
Operations:
1. add(10)
2. add(20)
3. add(30)
4. add(40)
5. getPercentile(25) // Should return 15
6. getPercentile(50) // Should return 25
7. getPercentile(75) // Should return 35
```

**Hint**: Use two heaps and dynamically adjust them to maintain the percentile point.

**Learning Focus**: Advanced heap manipulation for statistical calculations.

---

### Problem 12: Stock Price Fluctuation System

**Task**: Design a system that tracks the price of a stock over time and can efficiently answer the following queries:
- `update(timestamp, price)`: Update the price of the stock at the given timestamp.
- `current()`: Return the latest price of the stock.
- `maximum()`: Return the maximum price recorded.
- `minimum()`: Return the minimum price recorded.

**Input/Output Example**:
```
Operations:
1. update(1, 10)
2. update(2, 5)
3. current() // Should return 5
4. maximum() // Should return 10
5. update(1, 3) // Correcting the price for timestamp 1
6. maximum() // Should return 5
7. minimum() // Should return 3
```

**Learning Focus**: Using multiple heaps to track different metrics with update capabilities.

---

## Algorithmic Challenges

### Problem 13: Skyline Problem

**Task**: A city's skyline is the outer contour formed by all the buildings when viewed from a distance. Given the locations and heights of all buildings, compute the skyline.

**Input/Output Example**:
```
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
```

**Hint**: Use a max heap to track the highest building at each point.

**Learning Focus**: Using heap in sweep line algorithms.

---

### Problem 14: Shortest Path with Obstacles

**Task**: Given a grid with obstacles (1) and empty cells (0), find the shortest path from the top-left to the bottom-right, where you can remove at most k obstacles.

**Input/Output Example**:
```
Input: 
grid = [
  [0,0,0],
  [1,1,0],
  [0,0,0],
  [0,1,1],
  [0,0,0]
], k = 1

Output: 6
```

**Hint**: Use a modified Dijkstra's algorithm with a min heap prioritizing paths by both distance and obstacles removed.

**Learning Focus**: Using heap in graph traversal algorithms with constraints.

---

### Problem 15: Hot Potato Game Simulation

**Task**: Simulate a hot potato game where n players stand in a circle. In each round, the potato passes m positions and the player holding it is eliminated. Find the last player standing.

**Input/Output Example**:
```
Input: n = 7, m = 3
Output: Player 4
```

**Hint**: Use a specialized heap structure where extraction and reinsertion follow the game's rules.

**Learning Focus**: Implementing a circular elimination algorithm using heap properties.

---

## Real-World Scenarios

### Problem 16: CPU Task Scheduler

**Task**: Implement a CPU task scheduler that schedules tasks based on their priority, burst time, and arrival time. Each task has a priority (higher value means higher priority), burst time (time needed to complete), and arrival time.

**Input/Output Example**:
```
Input:
Tasks = [
  {id: 1, priority: 2, burst: 5, arrival: 0},
  {id: 2, priority: 1, burst: 3, arrival: 1},
  {id: 3, priority: 3, burst: 2, arrival: 2}
]

Output: Execution order: 1, 3, 2
```

**Learning Focus**: Using heap for priority-based scheduling with multiple attributes.

---

### Problem 17: Dynamic Load Balancer

**Task**: Implement a load balancer that distributes incoming requests to a set of servers based on their current load and processing power.

**Input/Output Example**:
```
Operations:
1. addServer(id=1, power=2)
2. addServer(id=2, power=3)
3. assignTask(size=5) // Should assign to server 2
4. assignTask(size=2) // Should assign to server 1
5. assignTask(size=6) // Should assign to server 1
6. getServerLoads() // Should return {1: 8/2, 2: 5/3}
```

**Learning Focus**: Using heap for dynamic resource allocation.

---

### Problem 18: Ride-sharing Platform

**Task**: Design a ride-sharing platform that matches riders with nearby drivers based on distance, driver rating, and car type preference.

**Input/Output Example**:
```
Operations:
1. addRider(id=1, location=[0,0], carPref="SUV")
2. addDriver(id=101, location=[1,1], rating=4.5, carType="Sedan")
3. addDriver(id=102, location=[0,1], rating=4.2, carType="SUV")
4. matchRider(1) // Should return driver 102
```

**Hint**: Use a multi-attribute priority structure with dynamic updates.

**Learning Focus**: Applying heap for multi-criteria matching problems.

---

### Problem 19: Continuous File Backup System

**Task**: Implement a continuous backup system that identifies and backs up the most frequently modified files within a limited storage budget.

**Input/Output Example**:
```
Operations:
1. addFile("doc1.txt", size=100, modCount=5)
2. addFile("img1.jpg", size=500, modCount=1)
3. addFile("code.py", size=50, modCount=20)
4. backup(maxSize=600) // Should backup "code.py" and "doc1.txt"
```

**Learning Focus**: Using heap for resource-constrained optimization.

---

### Problem 20: Real-time Analytics Dashboard

**Task**: Design a real-time analytics dashboard that tracks the top performers, most frequent errors, and trend changes from a continuous stream of events.

**Input/Output Example**:
```
Operations:
1. logEvent("user1", "purchase", amount=100)
2. logEvent("user2", "view", item="product1")
3. logEvent("user1", "purchase", amount=200)
4. logEvent("user3", "error", code="E404")
5. getTopUsers(2) // Should return ["user1", "user2"]
6. getFrequentErrors(1) // Should return ["E404"]
```

**Learning Focus**: Using multiple heaps to track different metrics in a streaming context.

---

## Implementation Guidelines

For each problem, follow these steps:

1. Understand the problem and define the required operations clearly.
2. Choose the appropriate heap type (min/max/specialized) for the problem.
3. Implement a solution that optimizes both time and space complexity.
4. Test your solution with the provided examples and additional test cases.
5. Analyze the time and space complexity of your solution.

After implementing each solution, reflect on:
- How the heap data structure simplified the problem
- Any challenges you faced during implementation
- Alternative approaches and their trade-offs
- How the problem relates to real-world applications

These reflections will deepen your understanding and help you recognize patterns for future problems.

## Learning Progression

I recommend tackling these problems in the order presented, as they build on each other:

1. Start with the foundational problems to establish a solid understanding of heap mechanics.
2. Move to application-based problems to see how heaps solve common algorithmic challenges.
3. Progress to advanced heap problems that combine heaps with other data structures.
4. Challenge yourself with algorithmic problems that use heaps in sophisticated ways.
5. Finally, work on real-world scenarios to see how heap concepts apply in practical situations.

This structured approach will progressively build your heap mastery from basic operations to complex applications.
