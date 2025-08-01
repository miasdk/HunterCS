# Python Translation Examples

> **📝 Note**: This file shows how the C++ templates in this repository would translate to Python. For a complete Python version, see `../PYTHON-REPO-TEMPLATE.md`

## 🔄 C++ vs Python Template Comparison

### Hash Table Pattern

#### C++ Version
```cpp
#include <unordered_map>
#include <vector>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> map;
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (map.count(complement)) {
            return {map[complement], i};
        }
        map[nums[i]] = i;
    }
    return {};
}
```

#### Python Version
```python
def two_sum(nums, target):
    """Hash table approach - O(n) time, O(n) space"""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Alternative using dict.get()
def two_sum_alt(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if seen.get(complement) is not None:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### Tree Traversal Pattern

#### C++ Version
```cpp
#include <queue>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

vector<vector<int>> levelOrder(TreeNode* root) {
    if (!root) return {};
    
    vector<vector<int>> result;
    queue<TreeNode*> q;
    q.push(root);
    
    while (!q.empty()) {
        int levelSize = q.size();
        vector<int> currentLevel;
        
        for (int i = 0; i < levelSize; i++) {
            TreeNode* node = q.front();
            q.pop();
            currentLevel.push_back(node->val);
            
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        result.push_back(currentLevel);
    }
    return result;
}
```

#### Python Version
```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    """BFS level order traversal"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(current_level)
    
    return result

# More Pythonic recursive approach
def level_order_recursive(root):
    def dfs(node, level, result):
        if not node:
            return
        
        if level >= len(result):
            result.append([])
        
        result[level].append(node.val)
        dfs(node.left, level + 1, result)
        dfs(node.right, level + 1, result)
    
    result = []
    dfs(root, 0, result)
    return result
```

### Array Two-Pointer Pattern

#### C++ Version
```cpp
#include <vector>
#include <algorithm>
using namespace std;

vector<int> twoSumSorted(vector<int>& numbers, int target) {
    int left = 0, right = numbers.size() - 1;
    
    while (left < right) {
        int sum = numbers[left] + numbers[right];
        if (sum == target) {
            return {left + 1, right + 1}; // 1-indexed
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return {};
}

bool isPalindrome(string s) {
    int left = 0, right = s.length() - 1;
    
    while (left < right) {
        while (left < right && !isalnum(s[left])) left++;
        while (left < right && !isalnum(s[right])) right--;
        
        if (tolower(s[left]) != tolower(s[right])) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
```

#### Python Version
```python
def two_sum_sorted(numbers, target):
    """Two pointers on sorted array"""
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

def is_palindrome(s):
    """Check if string is palindrome"""
    # Method 1: Two pointers (space efficient)
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

# Method 2: Pythonic (but uses O(n) space)
def is_palindrome_pythonic(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
```

## 🔑 Key Differences Summary

### Language Features
| Feature | C++ | Python |
|---------|-----|--------|
| **Type Declaration** | `vector<int> nums` | `nums` (dynamic typing) |
| **Iteration** | `for (int i = 0; i < size; i++)` | `for i, val in enumerate(list)` |
| **Hash Table** | `unordered_map<int, int>` | `dict` |
| **Queue** | `queue<TreeNode*>` | `collections.deque` |
| **String** | `string s; s.length()` | `s = ""; len(s)` |

### Syntax Advantages
- **C++**: Explicit types, performance control, STL algorithms
- **Python**: List comprehensions, dynamic typing, readable syntax

### Interview Considerations
- **C++**: Shows systems knowledge, memory awareness
- **Python**: Faster coding, easier explanation, focus on algorithms

---

**🎯 Takeaway**: Both languages can solve the same patterns, but each has unique strengths. Choose based on the role and company culture! 