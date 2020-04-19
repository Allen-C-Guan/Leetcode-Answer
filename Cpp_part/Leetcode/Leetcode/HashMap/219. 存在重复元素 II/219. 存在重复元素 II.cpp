#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> dic;
        for (int i = 0; i < nums.size(); i++){
            //如果存在 且小于等于k
            if(dic.find(nums[i]) != dic.end() and (i - dic[nums[i]]) <= k)
                return true;
            else
                dic[nums[i]] = i;
        }
        return false;
    }
};


//int main() {
//    Solution* s = new Solution;
//    vector <int> inputs = {1,2,3,4,5,6,7,7,7};
//    auto res = s -> containsNearbyDuplicate(inputs, 6);
//    cout << "this is code" << endl;
//    return 0;
//}
