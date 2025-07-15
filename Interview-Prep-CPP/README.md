# HunterCS Interview Prep - C++

> **Master Data Structures & Algorithms with Modern C++**
> 
> *Systematic interview preparation optimized for C++ strengths: STL mastery, performance optimization, and clean code.*

## 🎯 Why C++ for Interviews?

**C++ Advantages:**
- **Performance**: Industry standard for systems, gaming, HFT
- **STL Mastery**: Demonstrates deep algorithmic understanding
- **Memory Management**: Shows low-level programming skills
- **Modern Features**: C++17/20 knowledge sets you apart

**Top Companies Using C++:** Google, Microsoft, Meta, Amazon, Bloomberg, Jane Street, Citadel

---

## 🚀 Quick Start

### New to C++ Interviews?
```bash
cd START-HERE
# Read README.md for structured learning path
```

### Pattern Practice
```bash
cd Interview-Prep/Patterns/
# Focus on one pattern at a time
```

### STL Mastery
```bash
cd Interview-Prep/STL-Mastery/
# Master containers critical for interviews
```

---

## 📁 Repository Structure

```
HunterCS-Interview-Prep-CPP/
├── 📖 START-HERE/              # Learning roadmap & getting started
├── 🎯 Interview-Prep/          # Core interview preparation
│   ├── Patterns/               # Algorithm patterns (Hash, Tree, DP)
│   ├── STL-Mastery/           # C++ STL deep dive
│   ├── Company-Prep/          # Company-specific practice
│   └── Daily-Practice/        # Practice methodology
├── 💻 Code-Library/            # Ready-to-use implementations
│   ├── Templates/             # C++ algorithm templates
│   ├── By-Topic/              # Organized by data structure
│   └── Solutions/             # Complete problem solutions
├── ⚡ Quick-Reference/         # Cheat sheets & complexity tables
├── 🛠️ Tools/                   # Practice utilities
└── 📝 Practice-Problems/       # Curated problem sets
```

## 🏆 Learning Path

### Phase 1: Foundations (Week 1-2)
1. **Time Complexity Analysis** → `Quick-Reference/big-o-cheat-sheet.md`
2. **STL Containers** → `Interview-Prep/STL-Mastery/`
3. **Basic Patterns** → `Interview-Prep/Patterns/Hash-Table/`

### Phase 2: Core Patterns (Week 3-6)
1. **Hash Tables** → Master frequency counting, two-sum variants
2. **Tree Traversal** → BFS, DFS, binary tree problems
3. **Two Pointers** → Array manipulation, string problems
4. **Dynamic Programming** → Classic problems, optimization

### Phase 3: Advanced Topics (Week 7-8)
1. **Graph Algorithms** → BFS, DFS, shortest path
2. **System Design** → C++ specific considerations
3. **Mock Interviews** → Practice under time pressure

---

## 🎯 Interview Focus Areas

### Must-Know C++ Features
```cpp
// Modern C++ (C++17/20)
auto freq = std::unordered_map<int, int>{};
for (const auto& [key, value] : freq) { /* structured binding */ }

// Range-based algorithms
std::ranges::sort(nums);
auto it = std::ranges::find(nums, target);

// Smart pointers
std::unique_ptr<TreeNode> root = std::make_unique<TreeNode>(5);
```

### Critical STL Containers
- **unordered_map/set**: O(1) operations, hash tables
- **vector**: Dynamic arrays, most versatile
- **queue/stack**: BFS/DFS, algorithm building blocks
- **priority_queue**: Heaps, greedy algorithms
- **map/set**: Ordered data, when sorting matters

### Performance Highlights
- **Memory Layout**: Vector vs list performance implications
- **Iterator Categories**: Random access vs bidirectional
- **Algorithm Complexity**: STL algorithm time guarantees
- **Custom Comparators**: Lambda functions, function objects

---

## 📊 Success Metrics

### 🎯 Beginner Goals (0-3 months experience)
- [ ] Solve 50 easy problems using STL
- [ ] Master unordered_map, vector, queue, stack
- [ ] Understand O(n), O(log n), O(1) patterns
- [ ] Complete hash table and tree traversal patterns

### 🎯 Intermediate Goals (3-12 months experience)  
- [ ] Solve 100 medium problems
- [ ] Master all STL containers and algorithms
- [ ] Implement graph algorithms (BFS, DFS, Dijkstra)
- [ ] Complete dynamic programming patterns

### 🎯 Advanced Goals (1+ years experience)
- [ ] Solve 200+ problems including hard
- [ ] Explain C++ memory model and optimization
- [ ] Design efficient data structures from scratch
- [ ] Pass interviews at top tech companies

---

## 🌟 Why This Repository?

### ✅ **Systematic Approach**
- Anti-overwhelm methodology
- Pattern-based learning (not random problems)
- Clear progression from basic to advanced

### ✅ **C++ Optimized**
- Modern C++ best practices
- STL-first solutions
- Performance considerations explained

### ✅ **Interview Focused**
- Real interview questions and patterns
- Time complexity emphasis
- Clean, readable code style

### ✅ **Hunter College Proven**
- Based on CSCI 335 curriculum
- Professor-approved explanations
- Peer-tested learning materials

---

## 🔗 Related Resources

- **Python Version**: [HunterCS-Interview-Prep-Python](../HunterCS-Interview-Prep-Python/)
- **Course Materials**: [CSCI 335 DSA Course](../HunterCS/335/)
- **Practice Platform**: LeetCode, HackerRank, CodeForces

---

## 🤝 Contributing

1. **Pattern Improvements**: Add clearer explanations or better examples
2. **Code Optimization**: More efficient C++ implementations
3. **New Problems**: Interview questions with detailed solutions
4. **STL Insights**: Advanced STL usage patterns

---

**🎯 Start your C++ interview prep journey today!** Head to `START-HERE/` for your personalized learning roadmap.

---

*Built with ❤️ for Hunter College CS students and C++ interview preparation* 