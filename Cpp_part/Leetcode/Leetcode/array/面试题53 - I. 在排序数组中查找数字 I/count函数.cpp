#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/*
 <algorithm> 里的 cout的用法有点东西，和python中的cout一样。
 */
class Solution {
public:
    int search(vector<int>& nums, int target) {
        return count(nums.begin(), nums.end(), target);
    }
};
