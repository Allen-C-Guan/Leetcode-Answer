#include <iostream>
#include <vector>
using namespace std;
/*
 这里我们没有用in place做的
 */
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int rot = k % nums.size();
        //只是一个提前判定而已
        if (!rot)   return;
        
        vector<int> new_nums;
        new_nums.assign(nums.end()-rot, nums.end());
        for (vector<int>::iterator it = nums.begin(); it != nums.end()-rot; it++ )
            new_nums.push_back(*it);
        nums = new_nums;
    }
};


//int main (){
//    vector<int> input = {1, 2};
//    Solution* foo = new Solution;
//    foo -> rotate(input, 3);
//}
