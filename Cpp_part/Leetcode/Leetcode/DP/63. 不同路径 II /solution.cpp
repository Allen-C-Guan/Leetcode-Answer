#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int x_size = obstacleGrid.size(), y_size = obstacleGrid[0].size();
        vector<vector<long>> dp(x_size, vector<long>(y_size, 0)); //注意溢出的问题，里面的值采用long来存储。
        for(int i = 0; i < x_size; i++)
            if(obstacleGrid[i][0] == 1)
                break;
            else
                dp[i][0] = 1;
        for(int i = 0; i < y_size; i++)
            if(obstacleGrid[0][i] == 1)
                break;
            else
                dp[0][i] = 1;
        
        for(int x = 1; x < x_size; x++){
            for(int y = 1; y < y_size; y++){
                if(obstacleGrid[x][y] != 1)
                    dp[x][y] = dp[x-1][y] + dp[x][y-1];
            }
        }
        return dp[x_size-1][y_size-1];
    }
};

//int main(){
//    Solution* s = new Solution;
//    vector<vector<int>> inputs = {{1,0}};
//    s -> uniquePathsWithObstacles(inputs);
//    
//}
