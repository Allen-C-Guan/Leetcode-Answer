#include <iostream>
#include <vector>
#include <string>

using namespace std;

/*
 这里使用的是dp方法
 dp[x][y] = dp[x-1][y-1] + 1  or dp [x][y] = max(dp[x][y-1], dp[x-1][y])
 表示 要么各退一步，然后涨一个值，要么至少选择一个退一步，挑一个大的作为当前的值。
 
 */
class Solution {
public:
    int minDistance(string word1, string word2) {
        int x_size = word1.size() + 1, y_size = word2.size() + 1;
        vector<vector<int>> dp (x_size, vector<int>(y_size, 0));
        
        for(int x = 1; x < x_size; x ++){
            for(int y = 1; y < y_size; y++){
                if(word1[x-1] == word2[y-1]){
                    dp[x][y] = dp[x-1][y-1] + 1;
                }else
                    dp[x][y] = max(dp[x-1][y-1], max(dp[x-1][y], dp[x][y-1]));
            }
        }
        return x_size + y_size - 2 - 2 * dp[x_size-1][y_size-1];
    }
};

//
//int main(){
//    Solution* s = new Solution;
//    auto res = s -> minDistance("eat", "tea");
//}
//
