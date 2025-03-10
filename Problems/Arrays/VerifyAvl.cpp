#include <iostream>
#include <vector>

class Solutions {
    public: 

    //naive approach
    int removeElement(std::vector<int>& nums, int val) {
        auto it = nums.begin(); // Always intialize the iterator, using auto is a good practice
        while (it != nums.end()) {
            if (*it == val) {
                it = nums.erase(it);
            } else {
                ++it;
            }
        }
        return nums.size();
    }

    //optimized approach
    int removeElementOptimized(std::vector<int>& nums, int val){
        auto it2 = nums.begin();
        for (auto it = nums.begin(); it!=nums.end(); ++it) {
            if (*it != val) {
                *it2 = *it;
                ++it2;
            }
        }
        return it2 - nums.begin();
    }

    //even simpler
    int removeElementOptimal(std::vector<int>&nums, int val){
        auto overwriter = nums.begin(); 
        for (int x : nums){
            if (x != val){
                *overwriter = x;
                ++overwriter;
            }
        }
        return overwriter - nums.begin();
    }
};

