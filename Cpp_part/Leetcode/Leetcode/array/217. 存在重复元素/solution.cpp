#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        if (!nums.size()) return false;
        sort(nums.begin(), nums.end(), greater<int>());
        int i = 0;
        while (i < nums.size()-1){
            if (nums[i] == nums[i+1])
                return true;
            i++;
        }
    return false;
    }
};
