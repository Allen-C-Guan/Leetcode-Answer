#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
//这种利用index的方法，最主要的点就在于你的权重必须大于所有存在的数值，不然就会导致有最小公约数。
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int weight = nums.size() + 1;
        for (int n: nums ){
            int index = n % weight;
            if (index < nums.size()){
                nums[index] = nums[index] + weight;
            }
        }
        for (int i = 0 ; i < nums.size(); i++){
            if (nums[i] < weight){
                return i;
            }
        }
        return int(nums.size());
    }
};

//int main(){
//    Solution* s = new Solution;
//    auto nums = vector<int> {1,2,3};
//    s -> missingNumber(nums);
//}

