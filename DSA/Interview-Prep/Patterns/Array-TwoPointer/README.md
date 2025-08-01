# Array & Two-Pointer Pattern - Interview Guide

## 🎯 Pattern Recognition
**Use two-pointer technique when you need:**
- Find pairs with specific sum/difference
- Reverse or rearrange arrays
- Remove duplicates from sorted arrays
- Find subarrays with target properties
- Optimize brute force O(n²) solutions to O(n)

## 📋 Core Templates

### Basic Two-Pointer Setup
```cpp
// Opposite direction pointers
int left = 0, right = nums.size() - 1;
while (left < right) {
    // Check condition with nums[left] and nums[right]
    if (condition_met) {
        // Process result
        left++; right--;
    } else if (need_larger_sum) {
        left++;
    } else {
        right--;
    }
}

// Same direction pointers (slow-fast)
int slow = 0;
for (int fast = 0; fast < nums.size(); fast++) {
    if (condition) {
        nums[slow] = nums[fast];
        slow++;
    }
}
```

### Sliding Window Template
```cpp
int left = 0, maxLen = 0;
for (int right = 0; right < nums.size(); right++) {
    // Expand window by including nums[right]
    
    // Shrink window while condition violated
    while (window_invalid) {
        // Remove nums[left] from window
        left++;
    }
    
    // Update result with current window
    maxLen = max(maxLen, right - left + 1);
}
```

## 🔥 Must-Know Problems

### 1. Two Sum II (Sorted Array) ⭐⭐⭐
```cpp
vector<int> twoSum(vector<int>& numbers, int target) {
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
```

### 2. Remove Duplicates from Sorted Array ⭐⭐⭐
```cpp
int removeDuplicates(vector<int>& nums) {
    if (nums.empty()) return 0;
    
    int slow = 0;
    for (int fast = 1; fast < nums.size(); fast++) {
        if (nums[fast] != nums[slow]) {
            slow++;
            nums[slow] = nums[fast];
        }
    }
    return slow + 1;
}
```

### 3. Valid Palindrome ⭐⭐
```cpp
bool isPalindrome(string s) {
    int left = 0, right = s.length() - 1;
    
    while (left < right) {
        // Skip non-alphanumeric characters
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

### 4. Container With Most Water ⭐⭐⭐
```cpp
int maxArea(vector<int>& height) {
    int left = 0, right = height.size() - 1;
    int maxWater = 0;
    
    while (left < right) {
        int area = min(height[left], height[right]) * (right - left);
        maxWater = max(maxWater, area);
        
        // Move pointer with smaller height
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    return maxWater;
}
```

### 5. 3Sum ⭐⭐⭐
```cpp
vector<vector<int>> threeSum(vector<int>& nums) {
    vector<vector<int>> result;
    sort(nums.begin(), nums.end());
    
    for (int i = 0; i < nums.size() - 2; i++) {
        // Skip duplicates for first number
        if (i > 0 && nums[i] == nums[i-1]) continue;
        
        int left = i + 1, right = nums.size() - 1;
        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];
            if (sum == 0) {
                result.push_back({nums[i], nums[left], nums[right]});
                
                // Skip duplicates
                while (left < right && nums[left] == nums[left+1]) left++;
                while (left < right && nums[right] == nums[right-1]) right--;
                
                left++; right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }
    return result;
}
```

## 💡 Key Patterns

### Pattern 1: Opposite Direction Pointers
**When**: Sorted array, find pairs, palindrome check
**Template**: `left = 0, right = n-1`, move based on comparison
```cpp
while (left < right) {
    if (condition) return result;
    else if (need_increase) left++;
    else right--;
}
```

### Pattern 2: Slow-Fast Pointers
**When**: Remove elements, find cycles, duplicate removal
**Template**: `slow` for write position, `fast` for reading
```cpp
int slow = 0;
for (int fast = 0; fast < n; fast++) {
    if (keep_element) nums[slow++] = nums[fast];
}
```

### Pattern 3: Sliding Window
**When**: Subarray problems, longest/shortest with condition
**Template**: Expand right, shrink left when invalid
```cpp
int left = 0;
for (int right = 0; right < n; right++) {
    // Add nums[right] to window
    while (window_invalid) left++;
    // Update result
}
```

### Pattern 4: Fixed Distance Pointers
**When**: Compare elements at fixed distance apart
**Template**: Maintain fixed gap between pointers

## ⚡ Interview Tips

### Time/Space Complexity
- **Two-pointer**: O(n) time, O(1) space
- **Sliding window**: O(n) time, O(1) space
- **Brute force**: O(n²) time - avoid this!

### When to Use
✅ Sorted array problems  
✅ Palindrome checking  
✅ Sum problems (2Sum, 3Sum)  
✅ Subarray/substring problems  
✅ Remove duplicates/elements  

### Common Mistakes
- Forgetting to handle duplicates in 3Sum
- Wrong boundary conditions (left < right vs left <= right)
- Not skipping invalid characters in palindrome
- Moving wrong pointer in sum problems

### Optimization Strategy
1. **Identify**: Can brute force O(n²) be optimized?
2. **Sort**: Many two-pointer problems need sorted input
3. **Choose pattern**: Opposite direction vs same direction
4. **Handle edge cases**: Empty array, single element, duplicates

## 🎪 Practice Progression

### Week 1: Master These (Easy)
1. Two Sum II ⭐⭐⭐
2. Valid Palindrome ⭐⭐
3. Remove Duplicates ⭐⭐⭐
4. Merge Sorted Array ⭐⭐

### Week 2: Add These (Medium)
1. Container With Most Water ⭐⭐⭐
2. 3Sum ⭐⭐⭐
3. Remove Element ⭐⭐
4. Sort Colors ⭐⭐

### Week 3: Challenge (Medium-Hard)
1. 3Sum Closest ⭐⭐⭐
2. 4Sum ⭐⭐⭐
3. Trapping Rain Water ⭐⭐⭐
4. Longest Substring Without Repeating ⭐⭐⭐

## 📚 Related Files
- **Code Examples**: `../../../Code-Library/By-Topic/Arrays/`
- **Templates**: `../../../Code-Library/Templates/array_two_pointer_template.cpp`
- **Quick Reference**: `../../../Quick-Reference/`

## 🧠 Mental Model

### Two-Pointer Decision Tree
```
Is array sorted?
├── Yes → Use opposite direction pointers
│   ├── Sum problem → Move based on sum comparison
│   └── Palindrome → Move inward comparing values
└── No → Consider same direction or sliding window
    ├── Remove elements → Use slow-fast pattern
    └── Subarray problem → Use sliding window
```

### Common Two-Pointer Scenarios
1. **Find pair with target sum** → Opposite direction
2. **Remove duplicates** → Slow-fast  
3. **Longest valid subarray** → Sliding window
4. **Palindrome check** → Opposite direction
5. **Partition array** → Slow-fast 