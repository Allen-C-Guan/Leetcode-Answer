#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool isStraight(vector<int>& nums) {
        sort(nums.begin(),  nums.end(), less<int>());
        for(int i = 1; i < nums.size(); i++){
            if (nums[i] == nums[i-1] and nums[i] != 0){
                return false;
            }
        }
        int zeros = count(nums.begin(), nums.end(), 0), cnt = 0;
        
        for (int i = zeros+1; i < nums.size(); i++){
            if(nums[i] != nums[i-1] + 1)
                cnt += nums[i] - nums[i-1] - 1;
        }
        return cnt <= zeros;
    }
};

//int main (){
//    Solution* s = new Solution;
//    vector<int> nums {0,0,2,2,5};
//    bool res = s -> isStraight(nums);
//    printArray(nums);
//    cout << boolalpha << res << endl;
//    
//}
