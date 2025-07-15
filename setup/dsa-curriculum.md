# Comprehensive DSA Technical Interview Curriculum

This evidence-based curriculum synthesizes proven methodologies from NeetCode 150, Blind 75, FAANG company patterns, and educational best practices to create an optimal learning progression for technical interviews.

## Foundation and preparation timeline

**Target Timeline**: 3-4 months (10-15 hours/week) for comprehensive preparation  
**Minimum Viable**: 6-8 weeks intensive (20+ hours/week)  
**Maintenance**: 1-2 hours weekly after achieving proficiency

**Prerequisites**: Basic programming proficiency in chosen language (Python, Java, C++, or JavaScript)

## Phase 1: Foundation (Weeks 1-3) - 25% of Total Time

### Week 1: Arrays and Hashing (8-10 hours)
**Core Concepts**: Array manipulation, hash tables, two pointers technique

**Essential Problems** (15 problems total):
- Contains Duplicate (#217) - Easy
- Valid Anagram (#242) - Easy  
- Two Sum (#1) - Easy *[Universal FAANG favorite]*
- Group Anagrams (#49) - Medium
- Top K Frequent Elements (#347) - Medium *[Amazon favorite]*
- Product of Array Except Self (#238) - Medium
- Valid Sudoku (#36) - Medium
- Encode/Decode Strings (#271) - Medium Premium
- Longest Consecutive Sequence (#128) - Medium

**Advanced Practice**:
- Subarray Sum Equals K (#560) - Medium
- 4Sum (#18) - Medium
- Largest Rectangle in Histogram (#84) - Hard

**Time Complexity Expectations**: O(n) for most operations, O(n log n) for sorting-based solutions  
**Practice Schedule**: 2 easy + 1 medium daily

### Week 2: Two Pointers and Sliding Window (6-8 hours)
**Core Concepts**: Two pointers, sliding window technique, fast/slow pointers

**Essential Problems** (12 problems total):
- Valid Palindrome (#125) - Easy
- Two Sum II (#167) - Easy
- 3Sum (#15) - Medium *[Universal FAANG problem]*
- Container With Most Water (#11) - Medium
- Trapping Rain Water (#42) - Hard *[Google favorite]*

**Sliding Window**:
- Best Time to Buy/Sell Stock (#121) - Easy
- Longest Substring Without Repeating Characters (#3) - Medium *[Meta favorite]*
- Longest Repeating Character Replacement (#424) - Medium
- Permutation in String (#567) - Medium
- Minimum Window Substring (#76) - Hard
- Sliding Window Maximum (#239) - Hard

**Time Complexity**: O(n) for most problems  
**Focus**: Pattern recognition for pointer movement strategies

### Week 3: Stacks and Basic Recursion (6-8 hours)
**Core Concepts**: Stack operations, parentheses matching, monotonic stacks

**Essential Problems** (10 problems total):
- Valid Parentheses (#20) - Easy *[Universal problem]*
- Min Stack (#155) - Easy
- Evaluate Reverse Polish Notation (#150) - Medium *[Google favorite]*
- Generate Parentheses (#22) - Medium
- Daily Temperatures (#739) - Medium
- Car Fleet (#853) - Medium
- Largest Rectangle in Histogram (#84) - Hard

**Advanced**:
- Basic Calculator (#224) - Hard
- Serialize and Deserialize Binary Tree (#297) - Hard

**Time Complexity**: O(n) stack operations  
**Pattern Focus**: When to use stacks vs other data structures

## Phase 2: Non-Linear Structures (Weeks 4-7) - 35% of Total Time

### Week 4: Binary Search (6-8 hours)
**Core Concepts**: Binary search variations, search space optimization

**Essential Problems** (8 problems total):
- Binary Search (#704) - Easy
- Search a 2D Matrix (#74) - Medium  
- Koko Eating Bananas (#875) - Medium
- Find Minimum in Rotated Sorted Array (#153) - Medium *[Amazon favorite]*
- Search in Rotated Sorted Array (#33) - Medium *[Amazon favorite]*
- Time Based Key-Value Store (#981) - Medium
- Median of Two Sorted Arrays (#4) - Hard

**Time Complexity**: O(log n) expected for all solutions

### Week 5-6: Trees and Binary Search Trees (10-12 hours)
**Core Concepts**: Tree traversals, BST properties, tree construction

**Essential Problems** (18 problems total):

**Basic Trees**:
- Invert Binary Tree (#226) - Easy *[Universal problem]*
- Maximum Depth of Binary Tree (#104) - Easy
- Diameter of Binary Tree (#543) - Easy
- Balanced Binary Tree (#110) - Easy
- Same Tree (#100) - Easy

**Tree Traversals**:
- Binary Tree Inorder Traversal (#94) - Easy
- Binary Tree Level Order Traversal (#102) - Medium
- Binary Tree Right Side View (#199) - Medium

**Advanced Trees**:
- Subtree of Another Tree (#572) - Easy
- Lowest Common Ancestor (#235/#236) - Easy/Medium *[Meta favorite]*
- Binary Tree from Preorder/Inorder (#105) - Medium
- Validate Binary Search Tree (#98) - Medium
- Kth Smallest Element in BST (#230) - Medium

**Hard Trees**:
- Binary Tree Maximum Path Sum (#124) - Hard *[Google favorite]*
- Serialize/Deserialize Binary Tree (#297) - Hard
- Word Search II (#212) - Hard

**Time Complexity**: O(n) for most tree operations, O(log n) for balanced BST

### Week 7: Heaps and Priority Queues (6-8 hours)
**Core Concepts**: Min/max heaps, priority queue operations, k-way problems

**Essential Problems** (8 problems total):
- Kth Largest Element (#215) - Medium
- Last Stone Weight (#1046) - Easy
- K Closest Points to Origin (#973) - Medium
- Task Scheduler (#621) - Medium
- Design Twitter (#355) - Medium
- Find Median from Data Stream (#295) - Hard

**Time Complexity**: O(log n) insertions, O(1) peek operations

## Phase 3: Advanced Algorithms (Weeks 8-10) - 25% of Total Time

### Week 8: Graphs - BFS/DFS (8-10 hours)
**Core Concepts**: Graph representation, traversal algorithms, connected components

**Essential Problems** (15 problems total):

**Basic Graph Traversal**:
- Number of Islands (#200) - Medium *[Universal FAANG problem]*
- Clone Graph (#133) - Medium *[Meta favorite]*
- Max Area of Island (#695) - Medium
- Pacific Atlantic Water Flow (#417) - Medium

**Advanced Traversal**:
- Surrounded Regions (#130) - Medium
- Rotting Oranges (#994) - Medium
- Course Schedule (#207) - Medium *[Google favorite]*
- Course Schedule II (#210) - Medium
- Redundant Connection (#684) - Medium

**Complex Graphs**:
- Number of Connected Components (#323) - Medium Premium
- Graph Valid Tree (#261) - Medium Premium
- Word Ladder (#127) - Hard

**Advanced**:
- Alien Dictionary (#269) - Hard Premium *[Google favorite]*

**Time Complexity**: O(V + E) for most graph algorithms

### Week 9: Dynamic Programming Foundations (8-10 hours)
**Core Concepts**: Memoization, tabulation, optimal substructure
**Note**: Meta officially bans DP questions, focus extra here for other companies

**1D DP Problems** (12 problems total):
- Climbing Stairs (#70) - Easy
- Min Cost Climbing Stairs (#746) - Easy  
- House Robber (#198) - Easy
- House Robber II (#213) - Medium
- Longest Palindromic Substring (#5) - Medium
- Palindromic Substrings (#647) - Medium
- Decode Ways (#91) - Medium
- Coin Change (#322) - Medium *[Google favorite]*
- Maximum Product Subarray (#152) - Medium
- Word Break (#139) - Medium
- Longest Increasing Subsequence (#300) - Medium
- Partition Equal Subset Sum (#416) - Medium

**Time Complexity**: O(n) to O(n²) depending on problem structure

### Week 10: Advanced DP and Backtracking (8-10 hours)
**2D DP Problems** (8 problems total):
- Unique Paths (#62) - Medium
- Longest Common Subsequence (#1143) - Medium
- Best Time to Buy/Sell Stock with Cooldown (#309) - Medium
- Coin Change 2 (#518) - Medium
- Target Sum (#494) - Medium
- Interleaving String (#97) - Medium
- Longest Increasing Path in Matrix (#329) - Hard
- Edit Distance (#72) - Hard

**Backtracking** (7 problems total):
- Subsets (#78) - Medium
- Combination Sum (#39) - Medium
- Permutations (#46) - Medium
- Subsets II (#90) - Medium
- Combination Sum II (#40) - Medium
- Word Search (#79) - Medium
- N-Queens (#51) - Hard

## Phase 4: Integration and Mastery (Weeks 11-12) - 15% of Total Time

### Week 11: Advanced Topics and Patterns
**Greedy Algorithms** (5 problems):
- Maximum Subarray (#53) - Easy *[Universal problem]*
- Jump Game (#55) - Medium
- Jump Game II (#45) - Hard
- Gas Station (#134) - Medium
- Hand of Straights (#846) - Medium

**Advanced Data Structures**:
- Implement Trie (#208) - Medium
- Design Add and Search Words (#211) - Medium
- Word Search II (#212) - Hard
- LRU Cache (#146) - Medium *[Frequently asked]*

### Week 12: Mock Interviews and Company-Specific Practice

**Mock Interview Schedule**:
- 3-4 timed coding sessions (45 minutes each)
- Practice explaining solutions clearly
- Focus on debugging and optimization discussions

**Company-Specific Focus** (choose based on target):
- **Google**: Mathematical problems, optimal solutions
- **Meta**: Arrays/strings, system thinking
- **Amazon**: Practical problems, leadership principles integration
- **Microsoft**: Straightforward implementations

## Time Complexity Reference Guide

**Target Complexities by Problem Type**:
- Array operations: O(n) expected, O(n log n) acceptable
- Search problems: O(log n) required
- Tree operations: O(n) traversal, O(log n) BST operations  
- Graph algorithms: O(V + E) standard
- Dynamic programming: O(n) to O(n²) depending on dimensions

## Weekly Practice Structure

**Daily Schedule** (2 hours total):
- **30 minutes**: Review previous day's concepts
- **45 minutes**: Learn new topic/solve new problems
- **45 minutes**: Practice mixed problems from earlier topics

**Weekend Deep Dives** (3-4 hours):
- **1 hour**: Advanced problems from current week's topic
- **1 hour**: Mock interview simulation
- **1-2 hours**: Review and strengthen weak areas

## Progress Milestones

**Week 4**: Can solve 80% of easy problems independently  
**Week 8**: Consistently solves medium problems with occasional hints  
**Week 12**: Approaches hard problems with structured thinking, ready for interviews

**Problem Count Targets**:
- End of Month 1: 50+ problems solved
- End of Month 2: 100+ problems solved  
- End of Month 3: 150+ problems solved
- Interview-ready: 200+ problems with pattern mastery

## Success Indicators

**Technical Readiness**:
- Solves 70%+ of medium problems within 25 minutes
- Can explain time/space complexity for all solutions
- Recognizes patterns quickly across different problem types
- Debugs solutions effectively under time pressure

**Interview Readiness**:
- Communicates thought process clearly while coding
- Handles follow-up questions and optimizations
- Writes clean, readable code with good variable names
- Manages time effectively during 45-minute sessions

This curriculum synthesizes proven methodologies with evidence-based learning principles to create an optimal progression from DSA fundamentals to interview mastery. The structured timeline, progressive difficulty, and focus on high-frequency patterns ensures efficient preparation for technical interviews at top tech companies.