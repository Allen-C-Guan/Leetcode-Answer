#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int pointer_zero = 0;
        for(int i = 0; i < nums.size(); i++){
            if (nums[i] != 0){
                swap(nums[i], nums[pointer_zero]);
                pointer_zero ++;
            }
        }
    }
};

//int main (){
//    vector<int> nums = {0,1,0,3,12};
//    Solution* s = new Solution;
//    s -> moveZeroes(nums);
//}
