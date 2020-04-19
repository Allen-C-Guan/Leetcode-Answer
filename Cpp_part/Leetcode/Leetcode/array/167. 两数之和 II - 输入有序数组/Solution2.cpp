#include <iostream>
#include <vector>
using namespace std;
/*双指针法
 双指针法本质上是 decrease a constant的方法。 只用该方法的前提在于，可以利用当前结果，定向的缩小范围。这里是移动指针
 */
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0, right = numbers.size() - 1;
        while (left < right ){
            int cur_sum = numbers[left] + numbers[right];
            if (cur_sum == target)
                return vector<int> {left+1, right+1};
            else if (cur_sum < target)
                left ++;
            else
                right --;
        };
        return vector<int>{-1, -1};
    }
};
//
//int main(){
//    Solution* s = new Solution;
//    vector<int> input = {2, 7, 15, 11};
//    vector<int> res = s -> twoSum(input, 9);
//}
