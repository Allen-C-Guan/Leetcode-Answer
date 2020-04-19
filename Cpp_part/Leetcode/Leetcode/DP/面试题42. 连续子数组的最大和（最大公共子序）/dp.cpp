#include <iostream>
#include <vector>

using namespace std;
/*
dp[i]表示以i结尾的最大的和，必须要包含i
 */
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> dp = {0};
        int maxs =  nums[0];
        for(int i = 0; i < nums.size(); i ++){
            dp.push_back(max(dp[i]+nums[i], nums[i]));
            maxs = max(dp[i+1], maxs);
        }
        return maxs;
    }
};
