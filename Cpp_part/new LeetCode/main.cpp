#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int n_size = grid.size(), m_size = grid[0].size();
        vector<vector<int>> dp (n_size, vector<int> (m_size, 0));
        dp[0][0] = grid[0][0];
        for (int i = 1; i < n_size; i++) {
            dp[i][0] = grid[i][0] + dp[i-1][0];
        }
        for (int j = 1; j < m_size; j++) {
            dp[0][j] = grid[0][j] + dp[0][j-1];
        }
        for (int i = 1; i < n_size; i++) {
            for (int j = 1; j < m_size; j++) {
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
            }
        }
        return dp.back().back();
    }
};

int main() {
    vector<vector<int>> input = {{1,3,1}, {1,5,1},{4,2,1}};
    Solution s;
    s.minPathSum(input);



}
