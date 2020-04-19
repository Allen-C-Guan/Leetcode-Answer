#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int integerBreak(int n) {
        if(n < 3) return 1;
        if(n == 3) return 2;
        vector<int> dp (n+1, 1);
        for (int i = 1; i < n+1; i ++){
            for (int j = i-1; j > - 1; j --){
                dp[i] = max(dp[i], dp[j] * (i-j));
            }
        }
        return *(dp.end()-1);
    }
};



//int main(){
//    Solution* s = new Solution;
//    auto res = s->integerBreak(3);
//    cout << res << endl;
//}
