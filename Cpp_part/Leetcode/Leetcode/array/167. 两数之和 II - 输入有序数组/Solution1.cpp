#include <iostream>
#include <vector>
using namespace std;
//超时法
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> res;
        for(int i = 0; i < numbers.size(); i ++){
            res.push_back(target - numbers[i]);
        }
        for(int i = 0; i < numbers.size(); i++){
            for (int j = i+1; j < numbers.size(); j++){
                if (res[i] == numbers[j])
                    return vector<int> {i+1, j+1};
            }
        }
        return vector<int>{-1,-1};
    }
};

//int main(){
//    Solution* s = new Solution;
//    vector<int> input = {2, 7, 15, 11};
//    vector<int> res = s -> twoSum(input, 9);
//}
