#include <iostream>
#include <string>
#include <vector>

using namespace std;

/*
 这题的精髓竟然是数学知识， 可以证明，只要所有数均大于1，则必有括号加载加在第二个之后就行了
 */
class Solution {
public:
    string optimalDivision(vector<int>& nums) {
        
        if (nums.size() == 1){
            return to_string(nums[0]);
        }
        
        if (nums.size() == 2)
            return to_string(nums[0]) + "/" + to_string(nums[1]);
        
        string res = to_string(nums[0]) + "/(";
        for(int i = 1; i < nums.size(); i++){
            res += to_string(nums[i]) + "/";
        }
        
        res[res.size()-1] = ')';
        return res;
    }
};
