#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;


/*这也能过。。。 真的是醉了
 用DFS来建表，然后暴力法查！
*/


// DFS
void buildSubstringSet(const string& s, const int begin, unordered_set<string>& sets, string& path){
    if(begin >= s.size())
        return;
    for(int cur = begin; cur < s.size(); cur++){
        path = path + s[cur];
        sets.insert(path);   //map和set里面的的push也都默认的是copy，默认的都是copy！！
        buildSubstringSet(s, cur+1, sets, path);
        path.pop_back();
    }
    
}
class Solution {
public:
    int findLUSlength(vector<string>& strs) {
        // build set_list
        vector<unordered_set<string>> set_list (strs.size());
        for(int i = 0; i < strs.size(); i++){
            string init_path = "";
            buildSubstringSet(strs[i], 0, set_list[i], init_path);
        }
        int maxlen = -1;
        //暴力查找最大独一无二子串
        for(int i = 0; i < set_list.size(); i ++){
            for (string cur_str: set_list[i]){
                bool isunique = true;
                for (int j = 0; j < set_list.size(); j++){
                    if (j != i and set_list[j].count(cur_str)){
                        isunique = false;
                        break;
                    }
                }
                if(isunique)
                    maxlen = max(int(cur_str.size()), maxlen);
            }
        }
        return maxlen;
    }
};


//int main(){
//    Solution* s = new Solution;
//    vector<string> strs = {"abc", "ab"};
//    s -> findLUSlength(strs);
//
//}
