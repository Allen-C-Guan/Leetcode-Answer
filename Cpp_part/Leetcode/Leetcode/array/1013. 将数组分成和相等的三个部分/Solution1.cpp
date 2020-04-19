#include <iostream>
#include <vector>
#include <numeric>
using namespace std;
/*
 这题的关键点在于三等分， 只要任意截取两个部分就行了。。
 这题两个点
 1. accumulate(iterator.begin(), iterator.end(), head_value)
 2. 先相加，后判定，不然无法处理sum = 0 因此target = 0的情况。
 */

class Solution {
public:
    bool canThreePartsEqualSum(vector<int>& A) {
        int sum = 0;
        sum = accumulate(A.begin(),A.end(),0);
        if (sum%3) return false;
        
        int first = 0, len = A.size(), cur_sum = 0, target = sum/3;
        while (first < len){
            cur_sum += A[first];   //这题最尴尬的地方就是，必须先加，后判定，不然就处理不了相加和=0的情况
            first ++;
            if (cur_sum == target)
                break;
        }
        if (cur_sum != target)
            return false;
        
        int second = first;
        while (second < len-1){
            cur_sum += A[second];
            if (cur_sum == 2*target)
                return true;
            second ++;
        }
        return false;
    }
};

//
//int main(){
//    Solution* s = new Solution;
//    vector<int> A = {1,-1,1,-1};
//    cout << s -> canThreePartsEqualSum(A) << endl;
//}
