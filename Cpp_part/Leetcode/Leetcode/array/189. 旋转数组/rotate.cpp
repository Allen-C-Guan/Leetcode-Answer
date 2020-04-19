#include <iostream>
#include <vector>
using namespace std;
/*
 使用c++的函数。rotate(iterator.left(), .mid(), .right())。
 就会把mid后半截放到left前面去，而且是inplace的
 */
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        ::rotate(nums.begin(), nums.end()- (k % nums.size()), nums.end());
    }
};
