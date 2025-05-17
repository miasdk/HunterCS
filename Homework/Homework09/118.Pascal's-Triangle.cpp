#include <vector>
#include <iostream>
class Solution {
    public: 
        std::vector<std::vector<int>> generate(int numRows) {
            //Initialize result with the correct number of rows
            std::vector<std::vector<int>> result(numRows);

            // Fill in each row 
            for (int i = 0; i < numRows; ++i) {
                // Each row has i+1 elements 
                result[i].resize(i + 1);

                // Ensure first and last elements of each roq are always 1
                result[i][0] = 1;
                result[i][i] = 1;

                // Calculate middle elements using recurrence relation 
                for (int j = 1; j < i; ++j) {
                    result[i][j] = result[i-1][j-1] + result[i-1][j];
                }

            }
            return result;
        }
};
int main() {
    Solution solution;
    int numRows = 5;
    std::vector<std::vector<int>> triangle = solution.generate(numRows);

    // Print the triangle
    for (const auto& row : triangle) {
        for (int num : row) {
            std::cout << num << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}