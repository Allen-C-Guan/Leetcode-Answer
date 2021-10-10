//
// Created by Allen on 2021/10/10.
//

#ifndef C__20LEETCODE_33_SEARCH_IN_ROTATED_SORTED_ARRAY_H
#define C__20LEETCODE_33_SEARCH_IN_ROTATED_SORTED_ARRAY_H
#include <iostream>
#include <vector>
using namespace std;


class Solution {
public:
    int search(vector<int>& nums, int target) {
        int begin = 0, end = nums.size() - 1;
        while (begin <= end) {
            int mid = (begin + end) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            // 这里必须是 <=，因为当begin == mid的时候，我们依然认为是正序，因为mid收敛于begin侧
            if (nums[begin] <= nums[mid]) {
                if (nums[begin] <= target && target < nums[mid]) {
                    end = mid - 1;
                } else {
                    begin = mid + 1;
                }
            } else {
                if (nums[mid] < target && target <= nums[end]) {
                    begin = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
        }
        return -1;
    }
};


int main() {
    Solution s;
    vector<int> v = {3, 1};
    s.search(v, 1);
    return 0;
}

#endif //C__20LEETCODE_33_SEARCH_IN_ROTATED_SORTED_ARRAY_H
