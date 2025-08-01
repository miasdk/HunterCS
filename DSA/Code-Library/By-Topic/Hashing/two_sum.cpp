#include <vector>
#include <unordered_map>
#include <iostream>

/**
 * @brief   Two Sum Problem
 *        Given an array of integers, return indices of the two numbers such that they add up to a specific target.    
 * *      You may assume that each input would have exactly one solution, and you may not use the same element twice.
 *        You can return the answer in any order.
 * 
 * Key data structure: unordered_map
 * Key methods: find(), operator[]
 * Reference: 
 * find() : https://en.cppreference.com/w/cpp/container/unordered_map/find
 */
class Solution {
    public:
        std::vector<int> twoSum(std::vector<int>& nums, int target) {
           std::unordered_map<int, int> valueToIndex; 
    
           for (int i = 0; i < nums.size(); i++){ 
            int currentValue = nums[i]; 
            // Determine two numbers that add up to target
            int needed = target - currentValue; 
            
            // Check if needed already exists in HashTable(since the inputs do not need to be consecutive)
            if (valueToIndex.find(needed) != valueToIndex.end()){
                return { valueToIndex[needed], i};
            }
            // Add current value and its index to hash map 
            valueToIndex[currentValue] = i; 
           }
           return { }; //No Solution found 
        }
    };

