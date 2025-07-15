#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cassert>

/**
 * LeetCode 1: Two Sum - Complete Analysis
 * 
 * Problem: Given an array of integers nums and an integer target, 
 * return indices of the two numbers such that they add up to target.
 * 
 * Constraints:
 * - Only one valid answer exists
 * - Cannot use the same element twice
 * - Return indices in any order
 * 
 * This file demonstrates multiple approaches with complexity analysis
 * and interview communication strategies.
 */

class TwoSumSolutions {
public:
    /**
     * Approach 1: Brute Force
     * Time: O(n²), Space: O(1)
     * 
     * Interview Notes:
     * - Mention this as the naive approach
     * - Good starting point to show problem understanding
     * - Immediately suggest optimization
     */
    std::vector<int> twoSumBruteForce(std::vector<int>& nums, int target) {
        int n = nums.size();
        
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        
        return {}; // No solution found
    }
    
    /**
     * Approach 2: Hash Table (One Pass)
     * Time: O(n), Space: O(n)
     * 
     * Interview Notes:
     * - This is the expected optimal solution
     * - Explain the complement concept clearly
     * - Mention trade-off: space for time
     */
    std::vector<int> twoSumHashTable(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> complement_to_index;
        
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            
            // Check if complement exists
            auto it = complement_to_index.find(complement);
            if (it != complement_to_index.end()) {
                return {it->second, i}; // Found pair
            }
            
            // Store current number for future complements
            complement_to_index[nums[i]] = i;
        }
        
        return {}; // No solution found
    }
    
    /**
     * Approach 3: Two Pointers (requires sorting)
     * Time: O(n log n), Space: O(n) for storing indices
     * 
     * Interview Notes:
     * - Good if we only need to return values, not indices
     * - Explain why this doesn't work for original indices requirement
     * - Show alternative when indices don't matter
     */
    std::vector<int> twoSumTwoPointers(std::vector<int>& nums, int target) {
        // Create pairs of (value, original_index)
        std::vector<std::pair<int, int>> value_index_pairs;
        for (int i = 0; i < nums.size(); i++) {
            value_index_pairs.push_back({nums[i], i});
        }
        
        // Sort by values
        std::sort(value_index_pairs.begin(), value_index_pairs.end());
        
        int left = 0;
        int right = value_index_pairs.size() - 1;
        
        while (left < right) {
            int sum = value_index_pairs[left].first + value_index_pairs[right].first;
            
            if (sum == target) {
                return {value_index_pairs[left].second, value_index_pairs[right].second};
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        
        return {}; // No solution found
    }
    
    /**
     * Approach 4: Hash Table with Frequency Check
     * Time: O(n), Space: O(n)
     * 
     * Interview Notes:
     * - Handles edge case where target = 2 * element
     * - Good defensive programming practice
     */
    std::vector<int> twoSumWithFrequency(std::vector<int>& nums, int target) {
        std::unordered_map<int, std::vector<int>> value_to_indices;
        
        // Build frequency map with all indices
        for (int i = 0; i < nums.size(); i++) {
            value_to_indices[nums[i]].push_back(i);
        }
        
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            
            if (value_to_indices.count(complement)) {
                if (complement != nums[i]) {
                    // Different values
                    return {i, value_to_indices[complement][0]};
                } else if (value_to_indices[complement].size() > 1) {
                    // Same value, but need two different indices
                    return {value_to_indices[complement][0], value_to_indices[complement][1]};
                }
            }
        }
        
        return {}; // No solution found
    }
};

/**
 * Interview Communication Template
 */
class TwoSumInterview {
public:
    std::vector<int> solve(std::vector<int>& nums, int target) {
        // Step 1: Clarify requirements
        std::cout << "Let me clarify: we need to return indices of two numbers that sum to target, right?" << std::endl;
        std::cout << "Can I assume exactly one solution exists?" << std::endl;
        std::cout << "Can I use the same element twice? No, different indices required." << std::endl;
        
        // Step 2: Discuss approaches
        std::cout << "\nI can think of a few approaches:" << std::endl;
        std::cout << "1. Brute force: O(n²) time, O(1) space - check all pairs" << std::endl;
        std::cout << "2. Hash table: O(n) time, O(n) space - optimal solution" << std::endl;
        std::cout << "3. Two pointers: O(n log n) time - but loses original indices" << std::endl;
        
        // Step 3: Choose optimal approach
        std::cout << "\nI'll use the hash table approach for O(n) time complexity." << std::endl;
        std::cout << "The idea is to store complements as we iterate." << std::endl;
        
        // Step 4: Implement
        std::unordered_map<int, int> complement_map;
        
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            
            if (complement_map.find(complement) != complement_map.end()) {
                std::cout << "Found pair: nums[" << complement_map[complement] 
                         << "] + nums[" << i << "] = " << complement << " + " 
                         << nums[i] << " = " << target << std::endl;
                return {complement_map[complement], i};
            }
            
            complement_map[nums[i]] = i;
        }
        
        return {};
    }
};

/**
 * Test Cases and Validation
 */
class TwoSumTester {
private:
    TwoSumSolutions solutions;
    
    bool validateSolution(const std::vector<int>& nums, const std::vector<int>& result, int target) {
        if (result.size() != 2) return false;
        
        int i = result[0], j = result[1];
        if (i < 0 || i >= nums.size() || j < 0 || j >= nums.size()) return false;
        if (i == j) return false; // Same index used twice
        
        return nums[i] + nums[j] == target;
    }
    
public:
    void runAllTests() {
        std::cout << "=== Two Sum Test Suite ===" << std::endl;
        
        // Test Case 1: Basic case
        std::vector<int> nums1 = {2, 7, 11, 15};
        int target1 = 9;
        testCase(nums1, target1, "Basic case");
        
        // Test Case 2: Negative numbers
        std::vector<int> nums2 = {-3, 4, 3, 90};
        int target2 = 0;
        testCase(nums2, target2, "With negative numbers");
        
        // Test Case 3: Duplicates
        std::vector<int> nums3 = {3, 3};
        int target3 = 6;
        testCase(nums3, target3, "Duplicates");
        
        // Test Case 4: Larger array
        std::vector<int> nums4 = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        int target4 = 17;
        testCase(nums4, target4, "Larger array");
        
        // Test Case 5: No solution (should not happen per problem constraints)
        std::vector<int> nums5 = {1, 2, 3};
        int target5 = 10;
        testCase(nums5, target5, "No solution");
        
        std::cout << "=== All tests completed ===" << std::endl;
    }
    
    void testCase(std::vector<int> nums, int target, const std::string& description) {
        std::cout << "\nTest: " << description << std::endl;
        std::cout << "Input: nums = [";
        for (int i = 0; i < nums.size(); i++) {
            std::cout << nums[i];
            if (i < nums.size() - 1) std::cout << ", ";
        }
        std::cout << "], target = " << target << std::endl;
        
        // Test all approaches
        auto result1 = solutions.twoSumBruteForce(nums, target);
        auto result2 = solutions.twoSumHashTable(nums, target);
        auto result3 = solutions.twoSumTwoPointers(nums, target);
        
        std::cout << "Brute force: ";
        printResult(result1);
        std::cout << " Valid: " << (validateSolution(nums, result1, target) ? "✓" : "✗") << std::endl;
        
        std::cout << "Hash table: ";
        printResult(result2);
        std::cout << " Valid: " << (validateSolution(nums, result2, target) ? "✓" : "✗") << std::endl;
        
        std::cout << "Two pointers: ";
        printResult(result3);
        std::cout << " Valid: " << (validateSolution(nums, result3, target) ? "✓" : "✗") << std::endl;
    }
    
    void printResult(const std::vector<int>& result) {
        if (result.empty()) {
            std::cout << "No solution";
        } else {
            std::cout << "[" << result[0] << ", " << result[1] << "]";
        }
    }
};

/**
 * Performance Analysis
 */
void analyzePerformance() {
    std::cout << "\n=== Performance Analysis ===" << std::endl;
    std::cout << "Approach         | Time     | Space   | Notes" << std::endl;
    std::cout << "-----------------|----------|---------|------------------" << std::endl;
    std::cout << "Brute Force      | O(n²)    | O(1)    | Simple, inefficient" << std::endl;
    std::cout << "Hash Table       | O(n)     | O(n)    | Optimal for this problem" << std::endl;
    std::cout << "Two Pointers     | O(n log n)| O(n)    | Good for sorted arrays" << std::endl;
    std::cout << "Hash w/ Frequency| O(n)     | O(n)    | Handles edge cases" << std::endl;
    
    std::cout << "\nHash Table Analysis:" << std::endl;
    std::cout << "- Average case: O(1) lookup per element → O(n) total" << std::endl;
    std::cout << "- Worst case: O(n) lookup per element → O(n²) total (rare)" << std::endl;
    std::cout << "- Space: O(n) in worst case (all unique elements)" << std::endl;
    std::cout << "- Trade-off: Use extra space to achieve better time complexity" << std::endl;
}

/**
 * Interview Tips
 */
void printInterviewTips() {
    std::cout << "\n=== Interview Tips ===" << std::endl;
    std::cout << "1. Always clarify requirements first" << std::endl;
    std::cout << "2. Start with brute force, then optimize" << std::endl;
    std::cout << "3. Explain the hash table trade-off: space for time" << std::endl;
    std::cout << "4. Walk through an example step by step" << std::endl;
    std::cout << "5. Consider edge cases: duplicates, negatives, no solution" << std::endl;
    std::cout << "6. Mention that hash operations are O(1) average case" << std::endl;
    std::cout << "7. Be ready to implement without STL if asked" << std::endl;
}

// Main function for testing
int main() {
    TwoSumTester tester;
    tester.runAllTests();
    
    analyzePerformance();
    printInterviewTips();
    
    std::cout << "\n=== Interview Demo ===" << std::endl;
    TwoSumInterview interview;
    std::vector<int> demo_nums = {2, 7, 11, 15};
    int demo_target = 9;
    interview.solve(demo_nums, demo_target);
    
    return 0;
} 