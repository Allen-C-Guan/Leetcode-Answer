//
// Created by Allen on 2021/10/10.
//

#ifndef C__20LEETCODE_34_FIND_FIRST_AND_LAST_POSITION_OF_ELEMENT_IN_SORTED_ARRAY_H
#define C__20LEETCODE_34_FIND_FIRST_AND_LAST_POSITION_OF_ELEMENT_IN_SORTED_ARRAY_H

#include <memory>
#include <vector>
#include <optional>

using namespace std;

class Solution {
public:

    /*
     * 二分法的精髓：
     * 1. 获取mid的位置，让mid靠近左边（start + end)/2
     * 2. 判定mid是否与target相等
     * 3. 强制范围缩小，至少一个单位，根据target和mid的大小，begin在mid的右侧一个，或者end在mid的左侧一个
     */
    std::optional<size_t> findTargetIndex(vector<int>& nums, int target) {
        int begin = 0, end = nums.size() - 1;
        while (begin <= end) {
            size_t mid = (begin + end) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[mid] < target) {
                begin = mid + 1;// 这里没有必要从mid开始，+1有强制指针移动的作用，否则指针在 1， 2的时候，会无法移动
            } else {
                end = mid - 1;
            }
        }
        return {};
    }
    int findEage(vector<int>& nums, int index, int step) {
        int target = nums[index];
        // 这要先探路，移动左边，
        while ((index + step) < nums.size() && (index + step) >= 0) {
            if (nums[index + step] != target) {
                break;
            } else {
                index += step;
            }
        }
        return index;
    }

    vector<int> searchRange(vector<int>& nums, int target) {
        auto index = findTargetIndex(nums, target);
        if (index == nullopt) {
            return {-1, -1};
        }
        return {findEage(nums, index.value(), -1), findEage(nums, index.value(), 1)};
    }
};
int test() {
    Solution s;
    vector<int> input = {1};
    s.searchRange(input, 1);
}

#endif //C__20LEETCODE_34_FIND_FIRST_AND_LAST_POSITION_OF_ELEMENT_IN_SORTED_ARRAY_H
