#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
    public: 
        int numSquares(int n) {
            // Create a DP array to store the minimum number of perfect squares 
            std::vector<int> dp(n + 1, INT_MAX); 

            // Base case: 0 requires 0 perfect squares 
            dp[0] = 0; 
            
            //Fill the dp array from 1 to n 
            for(int i = 1; i <= n; ++i){
                //Trying all possible perfect squares less than or equal to i 
                for(int j = 1; j * j <= i; ++j){
                    //Update dp[i] to be minimum of current value and dp[i - j*j] + 1
                    dp[i] = std::min(dp[i], dp[i - j*j] + 1);
                }
            }
            
            return dp[n]; // Return the minimum number of perfect squares for n
      }
};

int main() {
    Solution solution;
    int n = 12; // Example input
    int result = solution.numSquares(n);
    std::cout << "Minimum number of perfect squares for " << n << " is: " << result << std::endl;
    return 0;
}